
# Convertendo arquivos 
```shell
pyuic5 -x nome.ui -o nome.py
```

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

# Labels (escrita dentro do window) 

```python
label = QtWidgets.QLabel(target)
label.setText('My label')
label.move(50,50)
```
# Buttons

```python
b1 = QtWidgets.QPushButton(win)
b1.setText("click me")
b1.move(100,100) # to move the button
```

