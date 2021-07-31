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

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_ok.clicked.connect(self.sizer_complete)
        self.reset.setDisabled(True)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        path = e.mimeData().urls()[0].path()[1:]
        self.listing.addItem(path)
        self.files.append(path)
        self.reset.setEnabled(True)

    def sizer_complete(self):
        for i in self.files:
            self.sizer(i)
        # size in B
        s = self.size
        if s >= 1024:
            # size in KB
            s = self.size = self.size / 1024
        if s >= 1024:
            # size in MB
            s = self.size = self.size / 1024
        if s >= 1024:
            # size in GB
            s = self.size = self.size / 1024
        if s >= 1024:
            # size in TB
            s = self.size = self.size / 1024
        if s >= 1024:
            # size in PB
            self.size = self.size / 1024
        total_size = TotalSize()
        total_size.show()


    def sizer(self, directory):
        self.size += sys.getsizeof(directory)

    def cleaner(self):
        self.listing.clear()


class TotalSize(QtWidgets.QDialog, design_sizer.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

    def close(self):
        window.cleaner()
        self.destroy()

app = QtWidgets.QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec_())
