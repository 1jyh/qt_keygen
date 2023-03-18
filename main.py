import sys,os, xiaoyu, json
from PyQt5.QtWidgets import QAbstractItemView, QApplication, QMessageBox, QMainWindow, QListView, QWidget
from PyQt5.QtCore import pyqtSignal, QCoreApplication, QThread, Qt
from Ui_register import Ui_MainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from concurrent.futures import ThreadPoolExecutor
from project import main


class Runthread(QThread, main):
    _signal = pyqtSignal(list)
    _call_html = pyqtSignal(str)

    def __init__(self, l, mark):
        super(Runthread, self).__init__()
        self.l = l
        self.mark = mark

    def __del__(self):

        pass

    def run(self):
        if self.mark == 'jm_login':
            self.jm_login()
        if self.mark == 'start':
            self.register()

    def jm_login(self):
        username, password = self.l
        money = '失败'
        if username and password:
            my = xiaoyu.miyun()
            global token
            # token = my.login(username, password)
            token = 'error'
            if token:
                self._signal.emit(56)
                with open('info.ini', 'w+') as fp:
                    try:
                        info = json.loads(fp.read())
                    except Exception:
                        info = {}
                        info['miyun'] = username + '----' + password + '----' + token
                        fp.write(json.dumps(info))

    def register(self):
        # 多线程入口
        # list :线程数,任务数,project_id,邀请码
        hint='Reverse engineer,'
        works, tasks = self.l[:2]
        self._call_html.emit('<font color="blue" size="3">start--> works: {}  tasks: {}</font>'.format(works, tasks))
        works = int(works)
        tasks = int(tasks)
        invest = self.l[-1]
        if works == 1 and tasks <= works:
            for i in range(tasks):
                main.parent(self, invest, i)
        elif tasks <= works:
            with ThreadPoolExecutor(max_workers=works) as t:
                for x in range(tasks):
                    t.submit(main.parent, self, invest, x)
        self._call_html.emit('<font color="red" size="3">end--></font>')



class Run_MainWindow(Ui_MainWindow, QMainWindow, QListView, QWidget):
    def __init__(self):
        super(Run_MainWindow, self).__init__()
        self.setupUi(self)
        try:
            with open("info.ini", 'r') as fp:
                info = json.loads(fp.read())
            global token
            jm_info = info['miyun'].split('----')
            token = jm_info[2]
            self.lineEdit.setText(jm_info[0])  # 接码账号
            self.lineEdit_2.setText(jm_info[1])  # 接码密码
            del jm_info
        except Exception:
            pass
        self.lineEdit_3.setText('RWK6IF')  # 邀请码
        self.lineEdit_4.setText('52814')  # 接码id
        self.lineEdit_5.setText('1')  # 线程数
        self.lineEdit_6.setText('1')  # 任务数
        self.lineEdit_7.setText('lVZ0D7PW/jmaODyoeSS/mw==')

        self.pushButton.clicked.connect(self.jm_login)
        self.pushButton_2.clicked.connect(self.task_start)  # run

        self.model = QStandardItemModel(7, 4)
        self.model.setHorizontalHeaderLabels(['phone', 'pwd', 'pay_pwd', 'log'])
        self.tableView.horizontalHeader().setStretchLastSection(True)  # 列表铺满
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止编辑
        self.tableView.setModel(self.model)  # 实例化表格

        self.model_2 = QStandardItemModel(7, 4)
        self.model_2.setHorizontalHeaderLabels(['name', 'cardId', 'xx', 'xxx'])
        self.tableView_2.horizontalHeader().setStretchLastSection(True)
        self.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_2.setModel(self.model_2)

        self.setAcceptDrops(True)
        # self.setDragDropMode(QAbstractItemView.DragDrop)
        # self.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.call_html('<font color="red" size="3">hello,第一次写，见谅,只需填邀请码,start即可<br/>https://d.ajgg52.com</font>')

    # 拖动时执行:判断文件是否存在
    def dragEnterEvent(self, evn):
        evn.accept() if evn.mimeData().hasUrls() else evn.ignore()

    # 拖动导入，拖动后执行的操作
    def dropEvent(self, evn):
        path = evn.mimeData().text().replace('file:///', '', 1)
        with open(path, 'r') as fp:
            content = fp.readlines()
        try:
            for i in range(len(content)):
                for j in range(2):
                    s = content[i].replace('\n', '').split('----')[j]
                    if len(s) <= 1:
                        raise Exception('失败')
                    self.model_2.setItem(i, j, QStandardItem(str()))
        except Exception:
            QMessageBox.critical(self, '确认', '导入失败,请检查文本')

    def jm_login(self):
        self.thread = Runthread([self.lineEdit.text(), self.lineEdit_2.text()], 'jm_login')
        self.thread._signal.connect(self.call_money)
        self.thread.start()

    def task_start(self):
        # key验证,本地AES
        conf = [self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_4.text(), self.lineEdit_3.text()]
        if not '' in conf:
            self.thread = Runthread(conf, 'start')
            self.thread._signal.connect(self.call_log)
            self.thread._call_html.connect(self.call_html)
            self.thread.start()

    def call_money(self, money):
        self.label_3.setText(money)

    def call_log(self, i):
        if len(i) == 5:
            for j, item in zip(range(4), i[:-1]):
                self.model.setItem(i[-1], j, QStandardItem(str(item)))

    def call_html(self, html):
        self.textEdit.append(html)


if __name__ == '__main__':

    # 将自建模块所在的路径添加到sys.path中
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_dir, ""))

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    MainWindow = Run_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
