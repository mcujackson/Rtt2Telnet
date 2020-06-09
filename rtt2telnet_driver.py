import pylink
import time
import threading
import logging
from socket import *
MAX_CONNECT_NUM = 2048  #最大监听数量


class TcpServer():
    def __init__(self, hostAddr, port, bufferSize):

        """初始对象

        Args:
          self (TcpServer): the ``TcpServer`` instance
          hostAddr (str):主机地址
          port(int):端口号
          bufferSize(int):一次读取的缓冲带下

        Returns:
          None
        """

        #主机地址
        self.hostAddr = hostAddr
        #绑定的端口
        self.port = port
        #一次性所读数据数量
        self.bufferSize = bufferSize

        self.tcpSocket = socket(AF_INET, SOCK_STREAM)
        self.tcpSocket.bind((hostAddr, port))
        self.tcpSocket.listen(MAX_CONNECT_NUM)

        self.currentTcpClientSocket = None

        #开启处理线程
        self.acceptTaskSwitch = True
        self.acceptThread = threading.Thread(target=self.__acceptTask,
                                             daemon=True,
                                             args=[self.tcpSocket])
        self.acceptThread.start()

    def __del__(self):
        """删除对象

        Args:
          self (TcpServer): the ``TcpServer`` instance

        Returns:
          None
        """
        #在删除对象的时候，需将所创建的其他对象删除干净
        if self.currentTcpClientSocket != None:
            self.currentTcpClientSocket.close()
        self.tcpSocket.close()
        self.acceptTaskSwitch = False
        self.acceptThread.join()

    def stop(self):
        """结束telnet处理线程

        Args:
          self (TcpServer): the ``TcpServer`` instance

        Returns:
          None
        """
        self.acceptTaskSwitch = False
        self.tcpSocket.close()
        self.acceptThread.join()

    def __acceptTask(self, tcpSocket):

        """telnet监听结果处理过程

        主要实现在另外一个链接发起后，断开当前链接，只保持一个链接供用户的操作

        Args:
          self (TcpServer): the ``TcpServer`` instance
          tcpSocket(socket):套接字对象
        Returns:
          None
        """

        while self.acceptTaskSwitch == True:
            try:
                #持续监听
                tcpClientSocket, addr = tcpSocket.accept()
                print("连接:", addr)

                #更新新的socket，在另外一个链接发起连接时，会关闭现有的链接
                if self.currentTcpClientSocket == None:
                    self.currentTcpClientSocket = tcpClientSocket
                else:
                    #关闭上一个socket
                    self.currentTcpClientSocket.close()
                    self.currentTcpClientSocket = tcpClientSocket

            except Exception as e:
                logging.error(e, exc_info=True)
                print(e)

    def write(self, data):

        """telnet服务器发送数据给客户端

        主要实现在另外一个链接发起后，断开当前链接，只保持一个链接供用户的操作

        Args:
          self (TcpServer): the ``TcpServer`` instance
          tcpSocket(socket):套接字对象
          
        Returns:
          None
        """
        if self.currentTcpClientSocket != None:
            self.currentTcpClientSocket.send(data)

    def read(self):
        try:
            if self.currentTcpClientSocket == None:
                time.sleep(1)  #如果还没建立起链接，则返回none
                return None
            data = self.currentTcpClientSocket.recv(self.bufferSize)
            if not data:
                return None
            return data
        except Exception as e:  #链接在阻塞读的时候被结束,会以异常的方式通知
            print(e)
            self.currentTcpClientSocket = None
            return None


class RttToTelnet():
    def __init__(self,
                 device,
                 telnetObj1,
                 telnetObj2,
                 interface=pylink.enums.JLinkInterfaces.SWD,
                 speed=12000,
                 reset=True):
        # 目标芯片名字
        self.device = device
        # 调试口
        self._interface = interface
        # 连接速率
        self._speed = speed
        # 复位标志
        self._reset = reset

        # segger rtt上下通道缓存大小
        self.upbufferSize = 8 * 1024
        self.downbufferSize = 8 * 1024

        # 两个telnet服务器操作引用
        self.telnetObj1 = telnetObj1
        self.telnetObj2 = telnetObj2
        # 线程
        self.rtt2telnet = None
        self.telnet2rtt = None
        self.rtt2telnet2 = None
        self.telnet2rtt2 = None

        #线程开关
        self.threadSwitch = False

        try:
            self.jlink = pylink.JLink()
        except:
            logging.error('Find jlink dll failed', exc_info=True)
            raise

    def rttToTelnet(self):

        while self.threadSwitch == True:
            try:
                rtt_recv = self.jlink.rtt_read(0, self.upbufferSize)
            except:
                raise Exception("Jlink rtt read error")

            if len(rtt_recv) == 0:
                continue
            try:
                self.telnetObj1.write(bytes(rtt_recv))
            except:
                raise Exception("Telnet write error")

    def telnetToRtt(self):

        while self.threadSwitch == True:
            data = self.telnetObj1.read()
            if data == None or len(data) == 0:
                continue

            #过滤掉telnet连接成功发过来的握手信号
            if data == b'\xff\xfd\x03\xff\xfb\x18':
                continue

            try:
                #如果mcu的SEGGER_RTT并没有开启指定通道，则千万不可调用rtt_write函数
                #若通道0开启，SizeOfBuffer缓冲区大小不应为0
                desc = self.jlink.rtt_get_buf_descriptor(0, True)
                if desc.SizeOfBuffer == 0:
                    continue
            except Exception as e:

                print(e)
                logging.error(e, exc_info=True)

            # 将读出的数据写入到rtt
            write_index = 0

            #确保所有字节数据全部写入
            while write_index < len(data):
                try:
                    bytes_written = self.jlink.rtt_write(0, data[write_index:])
                except:
                    raise Exception("Jlink rtt write error")

                write_index = write_index + bytes_written

    def rttToTelnet2(self):
        while self.threadSwitch == True:
            try:
                rtt_recv = self.jlink.rtt_read(1, self.upbufferSize)
            except:
                raise Exception("Jlink rtt read error")

            if len(rtt_recv) == 0:
                continue
            try:
                self.telnetObj2.write(bytes(rtt_recv))
            except:
                raise Exception("Telnet write error")

    def telnetToRtt2(self):
        while self.threadSwitch == True:

            data = self.telnetObj2.read()
            if data == None or len(data) == 0:
                continue

            if data == b'\xff\xfd\x03\xff\xfb\x18':
                continue

            try:
                desc = self.jlink.rtt_get_buf_descriptor(1, True)
                if desc.SizeOfBuffer == 0:
                    continue
            except Exception as e:
                print(e)
                logging.error(e, exc_info=True)

            write_index = 0
            while write_index < len(data):
                try:
                    bytes_written = self.jlink.rtt_write(1, data[write_index:])
                except:
                    raise Exception("Jlink rtt write error")

                write_index = write_index + bytes_written

    def start(self):
        try:
            if self.jlink.connected() == False:
                # 加载jlinkARM.dll
                self.jlink.open()
                # 设置连接速率
                if self.jlink.set_speed(self._speed) == False:
                    logging.error('Set speed failed', exc_info=True)
                    raise
                if self.jlink.set_tif(self._interface) == False:
                    logging.error('Set interface failed', exc_info=True)
                    raise

                try:
                    # 连接目标芯片
                    self.jlink.connect(self.device)
                    # 启动RTT，对于RTT的任何操作都需要在RTT启动后进行
                    self.jlink.rtt_start()

                    if self._reset == True:
                        # 复位一下目标芯片，复位后不要停止芯片，保证后续操作的稳定性
                        self.jlink.reset(halt=False)

                except Exception as e:
                    logging.error('Connect target failed', exc_info=True)
                    raise

        except pylink.errors.JLinkException as errors:
            logging.error('Open jlink failed', exc_info=True)
            raise

        #开启通道0的处理线程
        self.threadSwitch = True
        self.rtt2telnet = threading.Thread(target=self.rttToTelnet,
                                           daemon=True)
        self.telnet2rtt = threading.Thread(target=self.telnetToRtt,
                                           daemon=True)
        self.rtt2telnet.start()
        self.telnet2rtt.start()

        #开启通道1的处理线程
        self.rtt2telnet2 = threading.Thread(target=self.rttToTelnet2,
                                            daemon=True)
        self.telnet2rtt2 = threading.Thread(target=self.telnetToRtt2,
                                            daemon=True)
        self.rtt2telnet2.start()
        self.telnet2rtt2.start()


    def stop(self):

        #需先将socket关闭,使telnet服务在读阻塞中退出
        if self.telnetObj1.currentTcpClientSocket:
            self.telnetObj1.currentTcpClientSocket.close()

        if self.telnetObj2.currentTcpClientSocket:
            self.telnetObj2.currentTcpClientSocket.close()

        #关闭通道0和通道1的处理线程
        self.threadSwitch = False
        # 等待线程结束
        if self.rtt2telnet.is_alive():
            self.rtt2telnet.join()

        if self.telnet2rtt.is_alive():
            self.telnet2rtt.join()

        # 等待线程结束
        if self.rtt2telnet2.is_alive():
            self.rtt2telnet2.join()

        if self.telnet2rtt2.is_alive():
            self.telnet2rtt2.join()

        try:
            if self.jlink.connected() == True:
                # 使用完后停止RTT
                self.jlink.rtt_stop()
                # 释放之前加载的jlinkARM.dll
                self.jlink.close()

        except pylink.errors.JLinkException:
            logging.error('Disconnect target failed', exc_info=True)
            pass

    def __del__(self):
        self.jlink.close()
        #在下次的对象创建之前必须先删除本对象，毕竟设备只有一个
        del self.jlink

    def isActive(self):
        return self.threadSwitch

