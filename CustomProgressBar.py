# -*- coding: utf-8 -*-
__author__ = 'fengjigang'
import  sys
from PySide import QtCore,QtGui
class LoadingProgressBar(QtGui.QDialog):

    def __init__(self,parent = None):
        super(LoadingProgressBar, self).__init__(parent)
        self.label = QtGui.QLabel(self)
        self.resize(QtCore.QSize(100,100))
        self.setWindowOpacity(0.5)
        self.setWindowFlags(QtCore.Qt.Dialog|QtCore.Qt.CustomizeWindowHint)
        self.setContentsMargins(0,0,0,0)
        self.movie = QtGui.QMovie("loading.gif")
        self.movie.setScaledSize(QtCore.QSize(100,100))
        self.label.setMovie(self.movie)
        self.label.setContentsMargins(0,0,0,0)
        self.movie.start()
        self.center()

    def center(self):
        screen=QtGui.QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def show(self):
        '显示此dialog'
        print 'sss'
        self.exec_()

    def destory(self):
        '删除此dialog'
        self.close()

app = QtGui.QApplication(sys.argv)
bar = LoadingProgressBar()
bar.show()
sys.exit(app.exec_())

