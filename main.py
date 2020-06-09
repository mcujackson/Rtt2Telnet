import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QWidget, QSystemTrayIcon, QMenu, QAction, QMessageBox
from PyQt5 import QtGui
import rtt2telnet_ui
import rtt2telnet_driver
import pylink
import logging
import json

#初始化log的格式
logfmt = "%(asctime)s %(filename)s %(funcName)s: %(levelname)s: %(message)s"
logdatafmt = "%Y-%m-%d %H:%M:%S"

#接口类型对照表
targetInterface = {
    "SWD": pylink.enums.JLinkInterfaces.SWD,
    "JTAG": pylink.enums.JLinkInterfaces.JTAG,
    "cJTAG": pylink.enums.JLinkInterfaces.C2,
    "FINE": pylink.enums.JLinkInterfaces.FINE
}

#负责存储芯片类型列表
chipList = []
#默认下拉框启动后默认的芯片类型列表
defalutChipName = ""


class Control():
    def __init__(self, ui, MainWindow):
        self.ui = ui
        self.MainWindow = MainWindow
        #开关按钮
        ui.switchButton.clicked.connect(self.__switchRttToTelnet)
        #隐藏到托盘按钮
        ui.hideButton.clicked.connect(self.__hide)
        #加入芯片信号型号
        ui.chipCombox.addItems(chipList)
        #设置当前默认芯片型号
        ui.chipCombox.setCurrentText(defalutChipName)
        #初始化托盘图标
        self.__trayIcon()

    def __switchRttToTelnet(self):
        """开启按钮按下后执行的函数.

        包括创建通道0、1的telnet服务器
        创建rtt转telnet服务
        已经关闭后所执行的收尾操作

        Args:
          self (Control): the ``Control`` instance
        Returns:
          None
        """
        if self.ui.switchButton.text() == "开启":
            #创建通道0对应的tcp服务器
            self.telnetObj1 = rtt2telnet_driver.TcpServer(
                '0.0.0.0', int(self.ui.channel0Port.text()), 2048)
            #创建通道1对应的tcp服务器
            self.telnetObj2 = rtt2telnet_driver.TcpServer(
                '0.0.0.0', int(self.ui.channel1Port.text()), 2048)
            #创建rtt2转telnet服务
            self.rtt2telnetController = rtt2telnet_driver.RttToTelnet(
                device=self.ui.chipCombox.currentText(),  #芯片类型
                interface=targetInterface[
                    self.ui.interfaceCombox.currentText()],  #接口类型
                speed=int(self.ui.speedCombox.currentText().replace("kHz","")),  #速度
                reset=True,  #连接后复位
                telnetObj1=self.telnetObj1,
                telnetObj2=self.telnetObj2,
            )
            if self.rtt2telnetController.isActive() == False:
                try:
                    #开始rtt转telnet服务
                    self.rtt2telnetController.start()
                except Exception as e:
                    #开启失败必须删除整个服务对象
                    del self.rtt2telnetController
                    #删除通道0对应的tcp服务器
                    self.telnetObj1.stop()
                    del self.telnetObj1
                    #删除通道1对应的tcp服务器
                    self.telnetObj2.stop()
                    del self.telnetObj2
                    logging.exception(e)
                    QMessageBox.information(self.MainWindow, "警告",
                                            "开启失败，请检查jlink是否连接上芯片或者网络端口是否被占用")
                    return
            else:
                self.telnetObj1.stop()
                del self.telnetObj1
                self.telnetObj2.stop()
                del self.telnetObj2
            self.ui.switchButton.setText("关闭")

        elif self.ui.switchButton.text() == "关闭":
            if self.rtt2telnetController.isActive() == True:
                self.rtt2telnetController.stop()
                del self.rtt2telnetController
                self.telnetObj1.stop()
                del self.telnetObj1
                self.telnetObj2.stop()
                del self.telnetObj2
            self.ui.switchButton.setText("开启")

    def __hide(self):
        """隐藏窗口.

        将窗口隐藏并作出气泡提示

        Args:
          self (Control): the ``Control`` instance
        Returns:
          None

        """
        #隐藏窗口
        self.MainWindow.hide()
        #隐藏后的气泡提示
        self.tuopan.showMessage(u"提示", '双击再次打开窗口',
                                icon=1)  #icon的值  0没有图标  1是提示  2是警告  3是错误

    def __trayIcon(self):
        """创建托盘图标.

        Args:
          self (Control): the ``Control`` instance
        Returns:
          None

        """
        #托盘
        self.tuopan = QSystemTrayIcon(self.MainWindow)  #创建托盘
        self.tuopan.setIcon(QtGui.QIcon(r'./resizeApi.png'))  #设置托盘图标
        # 弹出的信息被点击就会调用messageClicked连接的函数
        #tuopan.messageClicked.connect(self.message)

        #托盘图标被激活所执行的回调
        self.tuopan.activated.connect(self.__iconActivated)
        #设置提示信息
        self.tuopan.setToolTip(u'rtt2telnet')
        #创建托盘的右键菜单
        #tpMenu = QMenu()
        # a1 = QAction(QtGui.QIcon('exit.png'), u'关于', self.MainWindow) #添加一级菜单动作选项(关于程序)
        # a1.triggered.connect(self.about)
        # a2 = QAction(QtGui.QIcon('exit.png'), u'退出', self.MainWindow) #添加一级菜单动作选项(退出程序)
        # a2.triggered.connect(self.quit)
        # tpMenu.addAction(a1)
        # tpMenu.addAction(a2)
        #tuopan.setContextMenu(tpMenu) #把tpMenu设定为托盘的右键菜单
        self.tuopan.show()  #显示托盘

    def __iconActivated(self, reason):
        """激活托盘图标所执行的操作
        
        Args:
          self (Control): the ``Control`` instance
          reason (QSystemTrayIcon) 事件类型
        Returns:
          None
        """
        if reason == QSystemTrayIcon.DoubleClick:  #双击 显示或隐藏窗口
            self.__windowShow()
        elif reason == QSystemTrayIcon.Trigger:  # 单击无效
            pass

    #响应托盘双击，最大最小化界面
    def __windowShow(self):
        """托盘双击事件.

        Args:
          self (Control): the ``Control`` instance
        Returns:
          None

        """
        if self.MainWindow.isMinimized() or not self.MainWindow.isVisible():
            #若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
            self.MainWindow.showNormal()
            self.MainWindow.activateWindow()
        else:
            #直接隐藏
            self.MainWindow.hide()


def loadChipList():
    """加载芯片型号列表.

    从当前目录下的chipList.json中读取列表，并填入全局
    变量chipList中

    Args:
        None
    Returns:
        None

     """
    global chipList
    global defalutChipName
    chipListFile = os.path.abspath(os.curdir)
    file = chipListFile + '/chipList.json'
    if os.path.exists(file):
        with open(file, 'r+', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                logging.exception(e)
                exit(-1)
    if "chipList" in data:
        chipList = chipList + (data["chipList"])
        print(data["chipList"])
    if "default" in data:
        defalutChipName = data["default"]


def initLog():
    """初始log日志.

    将log日志的存放位置定向到当前目录下的rttToTelnet.log中
    
    Args:
        None
    Returns:
        None

     """
    logfile = '.\\rttToTelnet.log'
    if not os.path.exists(
            logfile) or os.path.getsize(logfile) > 1 * 1024 * 1024:
        with open(logfile, 'w') as f:
            pass

    logging.basicConfig(filename = logfile, filemode = 'a', \
    format = logfmt, datefmt = logdatafmt, level = logging.INFO)


if __name__ == '__main__':
    #加载芯片型号列表
    loadChipList()
    #log日志重定向
    initLog()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = rtt2telnet_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    control = Control(ui, MainWindow)
    #设置图标
    MainWindow.setWindowIcon(QtGui.QIcon(r'./resizeApi.png'))
    MainWindow.show()
    sys.exit(app.exec_())