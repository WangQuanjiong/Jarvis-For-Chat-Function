
import sys
#form PyQt5.QtCore import
import PyQt5.QtCore 
from PyQt5.QtWidgets import *
#from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QListWidget,QStackedWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtCore import QSize, Qt
#QApplication.setStyleSheet()
class winBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("demo.py")
        self.statusBar().showMessage("2018")
        self.resize(800,600)
        self.main_layout = QHBoxLayout(self, spacing=0)     #窗口的整体布局
        self.main_layout.setContentsMargins(0,0,0,0)
        menu = self.menuBar()
        file_menu = menu.addMenu("file")
        edit_menu = menu.addMenu("edit")

        newfile_action = QAction('new file',self)
        file_menu.addAction(newfile_action)
        newfile_action.setStatusTip('create a new file') 

        exit_action = QAction('exit',self)
        exit_action.setStatusTip("Click to exit program")
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+F4')
        edit_menu.addAction(exit_action)
        #self.main_layout.addWidget(self.left_widget)
class LeftTabWidget(QWidget):
    '''左侧选项栏'''
    def __init__(self):
        super(LeftTabWidget, self).__init__()
        self.setObjectName('LeftTabWidget')
        self.resize(800,600)
        self.setWindowTitle('LeftTabWidget')
        
        #with open('D:/python/code/qt/test/QSS/QListWidgetQSS.qss', 'r') as f:   #导入QListWidget的qss样式
        #    self.list_style = f.read()

        self.main_layout = QHBoxLayout(self, spacing=0)     #窗口的整体布局
        self.main_layout.setContentsMargins(0,0,0,0)

        self.left_widget = QListWidget()     #左侧选项列表
        self.right_widget = QStackedWidget() #右侧
        #self.left_widget.setStyleSheet(self.list_style)
        self.left_widget.setGeometry(0,0,0,0)
        self.main_layout.addWidget(self.left_widget)
        self.main_layout.addWidget(self.right_widget)
        self.left_widget.setFixedWidth(180)
        self.right_widget.resize(620,600)
        self._setup_ui()

    def _setup_ui(self):
        '''加载界面ui'''

        self.left_widget.currentRowChanged.connect(self.right_widget.setCurrentIndex)   #list和右侧窗口的index对应绑定

        self.left_widget.setFrameShape(QListWidget.NoFrame)    #去掉边框

        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  #隐藏滚动条
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.left_widget
        list_str = ['热点分析','关键词提醒','群发助手','单项好友删除']
        #url_list = ['job_num_wordcloud.html', 'edu_need.html', 'salary_bar.html', 'edu_salary_bar.html']
        
        self.func1Page = QWidget()
        self.func2Page = QWidget()
        self.func3Page = QWidget()
        self.func4Page = QWidget()

        label1 = QLabel('热点分析')
        label2 = QLabel('关键词提醒')
        label3 = QLabel('群发助手')
        label4 = QLabel('单项好友删除')
        for i in range(4):
            self.item = QListWidgetItem(list_str[i],self.left_widget)   #左侧选项的添加
            self.item.setSizeHint(QSize(180,80))
            self.item.setTextAlignment(Qt.AlignCenter)                  #居中显示

            #self.browser = QWebView()                                   #右侧用QWebView来显示html网页
            #self.browser.setUrl(QUrl.fromLocalFile('D://python//code//vision//%s' % url_list[i]))
            #self.right_widget.addWidget(self.browser)

    
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    #win = winBox()
    #win.show()
    left = LeftTabWidget()
    left.show()
    style = open(r"D:\2018software\QssUI\StyleSheets\MetroUI.qss","r",encoding='utf-8')
    style_str = style.read()
    #style_str = style_str.decode('utf-8')
    app.setStyleSheet(style_str)

    sys.exit(app.exec_())

 