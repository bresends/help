# Programa Base

```python

class MyWindow(QMainWindow):
    def __init__(self):
	  super(MyWindow,self).__init__()
	  self.initUI()

    def button_clicked(self):
        print("clicked")

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
```

# Labels (escrita dentro do window) 
```python
label = QtWidgets.QLabel(target)
label.setText('My label')
label.move(50,50)
```
