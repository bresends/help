# Classes 
> É necessário sempre criar 1 único aplicativo 

```python
app = QtWidgets.QApplication(sys.argv)
# Start the event loop.
sys.exit(app.exec_())

# Programa não passa desse ponto até o exit ser apertado
```

> Depois colocamos a classe da janela 

```python
window = QMainWindow()
window.show() # IMPORTANT!!!!! Windows are hidden by default.
```

> Dentro da Main window criamos widgets 
> Se o Widget não tiver uma classe mãe ele é considerado uma janela


# Modificando Widgets 

```python
from PyQt5.QtCore import Qt
# The `Qt` namespace has a lot of attributes to customise widgets http://doc.qt.io/qt-5/qt.html
label.setAlignment(Qt.AlignCenter)

# Set the central widget of the Window. Widget will expand to take up all the space in the window by default.
self.setCentralWidget(label)
```

# Labels (escrita dentro do window) 

```python
label = QtWidgets.QLabel(target)
label.setText('My label')
label.move(50,50)
```
# Buttons

```python
button = QtWidgets.QPushButton(win)
button.setText("click me")
button.move(100,100) # to move the button
button.clicked.connect(self.função_desejada)
```
