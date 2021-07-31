import sys
import os

from PySide2 import QtGui, QtWidgets, QtCore
import design
import design_sizer

# def main():
#     # path = os.getcwd()
#     path = input('YYYYYYYYYYYYYYYYYYYYYY\n').replace('/', '\\')
#     print('YYYYYYYYYYYYYYYYYYYYYY')
#     files = input().replace('.', '')
#     files = files.split(',')
#     k = -1
#     for i in files:
#         k += 1
#         if i[0] == ' ':
#             files[k] = i.replace(' ', '')
#     walk(path, files)

class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):

    files = []
    size = 0

    mode = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_ok.clicked.connect(self.sizer_complete)
        self.reset.setDisabled(True)
        self.button_ok.setDisabled(True)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        path = e.mimeData().urls()[0].path()[1:]
        self.listing.addItem(path)
        self.files.append(path.replace('/', '\\'))
        self.button_ok.setEnabled(True)
        self.reset.setEnabled(True)

    def sizer_complete(self):
        for i in self.files:
            self.sizer(i)
        # size in B
        s = self.size
        if s >= 1024:
            # size in KB
            s = self.size = self.size / 1024
            self.mode = 1
        if s >= 1024:
            # size in MB
            s = self.size = self.size / 1024
            self.mode = 2
        if s >= 1024:
            # size in GB
            s = self.size = self.size / 1024
            self.mode = 3
        if s >= 1024:
            # size in TB
            s = self.size = self.size / 1024
            self.mode = 4
        if s >= 1024:
            # size in PB
            self.size = self.size / 1024
            self.mode = 5
        total_size.show()
        total_size.settings_text()

    def walker(self, directory):
        files = os.listdir(directory)
        for i in files:
            path = os.path.join(directory, i)
            if os.path.isfile(path):
                self.sizer(i)
            else:
                self.walker(path)

    def sizer(self, directory):
        if os.path.isdir(directory):
            self.walker(directory)
        # здесь косяк №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
        self.size += os.path.getsize(directory)

    def cleaner(self):
        self.listing.clear()


class TotalSize(QtWidgets.QDialog, design_sizer.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

    def settings_text(self):
        m = window.mode
        text = ''
        if m == 0:
            text = str(window.size) + ' B'
        elif m == 1:
            text = str(window.size) + ' KB'
        elif m == 2:
            text = str(window.size) + ' MB'
        elif m == 3:
            text = str(window.size) + ' GB'
        elif m == 4:
            text = str(window.size) + ' TB'
        elif m == 5:
            text = str(window.size) + ' PB'
        self.total_size.setText(text)

    def close(self):
        window.cleaner()
        self.destroy()

app = QtWidgets.QApplication()
window = MainWindow()
window.show()
total_size = TotalSize()
sys.exit(app.exec_())
