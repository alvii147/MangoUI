# QSharpTools

## Overview

**QSharpTools** is a library for **PyQt5** that includes better styled widgets for sharper desktop UI development.

## SharpButton

**SharpButton** an inherited class of **QPushButton,** styled using **QSS** and **QVariantAnimation.**

### Example Use

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from QSharpTools import SharpButton

app = QApplication(sys.argv)
myWin = QMainWindow()
myWin.resize(250, 250)
myWin.move(500, 500)

myWin.sharpbutton = SharpButton(
    parent = myWin,
    primaryColor = (2, 34, 143),
    secondaryColor = "rgb(189, 208, 245)",
    borderRadius = 6
)
myWin.sharpbutton.setText("SharpButton")
myWin.sharpbutton.move(80, 100)

myWin.show()
sys.exit(app.exec_())
```

![Sharp Button Recording](img/SharpButtonRecording.gif)