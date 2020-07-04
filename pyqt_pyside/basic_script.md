
# Convertendo arquivos 
```shell
pyuic5 -x nome.ui -o nome.py
pyside2-uic mainwindow.ui > ui_mainwindow.py
```
> https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html

# Programa Base

```python
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Meu título")
        self.initUI()

    def initUI(self):

        button = QPushButton("PyQt5 button", self)
        button.setToolTip("Esse é um botão de exemplo")
        button.move(100, 70)
        button.clicked.connect(self.on_click)

        label = QtWidgets.QLabel(self)
        label.setText("My label")
        label.move(50, 50)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print("PyQt5 button click")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
```

