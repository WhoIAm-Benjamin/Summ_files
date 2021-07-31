import sys
import os

from PySide2 import QtGui, QtWidgets, QtCore
import design

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
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        path = e.mimeData().urls()[0].path()[1:]
        self.table.add
        self.files.append(path)

    def sizer_complete(self):
        for i in self.files:
            self.sizer(i)

    def sizer(self, directory):
        self.size += sys.getsizeof(directory)

app = QtWidgets.QApplication()
window = MainWindow()
window.show()
sys.exit(app.exec_())
