__author__ = 'fengjigang'
# -*- coding: utf-8 -*-
import sys
from PySide import QtCore,QtGui
from a import Ui_Form


class loadingDlg(QtGui.QDialog):
    def __init__(self,parent=None):
        super(loadingDlg, self).__init__(parent)
        self.label = QtGui.QLabel('Red', self)
        self.setFixedSize(100,100)
        self.setWindowOpacity(0.5)
        self.setWindowFlags(QtCore.Qt.Dialog|QtCore.Qt.CustomizeWindowHint)
        self.setContentsMargins(0,0,0,0)
        self.label.setContentsMargins(0,0,0,0)

        self.movie = QtGui.QMovie("loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.movie.setScaledSize(QtCore.QSize(100,100))
        #self.label.show()
    def destroyDlg(self):
        self.close ()

    def __del__(self):
        del self.label
        del self.movie

class gthread(QtCore.QThread):
    def __init__(self,parent=None):
        super(gthread, self).__init__(parent)

    def run(self):
        import time
        print "thread start"
        time.sleep(2)

class mainWin(QtGui.QWidget, Ui_Form):
    def __init__(self, parent = None):
        super(mainWin,self).__init__(parent)
        self.setupUi(self)

        self.process = gthread()
        QtCore.QObject.connect(self.process, QtCore.SIGNAL("finished()"), self.finished)
        QtCore.QObject.connect(self.pushButton,  QtCore.SIGNAL('clicked()'), self.pushButtonClicked)

        self.loading = loadingDlg(self)
    def pushButtonClicked(self):
        self.process.start()
        self.loading.exec_()
    def finished(self):
        print "finished"
        # self.loading.destroyDlg()

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    mw = mainWin()
    mw.show()
    sys.exit(app.exec_())