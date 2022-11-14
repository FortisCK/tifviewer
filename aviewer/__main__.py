from PyQt5 import QtWidgets, QtCore
from pyqtgraph import ImageView
from tifffile import TiffFile


class Viewer(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose file', '/', "(*.tiff *.tif)")

        if not path[0]:
            return
        path = path[0]

        self.tif = TiffFile(path)

        self.widget = QtWidgets.QWidget(parent=self)
        self.vlayout = QtWidgets.QVBoxLayout(self.widget)

        iv = ImageView(parent=self)
        iv.setImage(self.tif.asarray(key=0))
        self.vlayout.addWidget(iv)

        self.setCentralWidget(self.widget)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    viewer = Viewer()
    viewer.show()

    viewer.resize(1000, 900)

    app.exec_()
