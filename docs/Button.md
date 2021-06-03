# Button

Button an inherited class of [QPushButton](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QPushButton.html), styled using [QSS](https://doc.qt.io/qt-5/stylesheet-syntax.html) and [QVariantAnimation](https://doc.qt.io/qtforpython-5/PySide2/QtCore/QVariantAnimation.html).

<img alt="Button Example" src="../img/ButtonExample.gif" width="400"/>

## Constructors & Methods

- [Button()](#button-1)

- [setBorder()](#setborder)

- [setColors()](#setcolors)

- [setFont()](#setfont)



## Button

Create new Button object.

```python
Button(
    parent=None,
    primaryColor=(21, 21, 21, 255),
    secondaryColor=(245, 177, 66, 255),
    parentBackgroundColor=(240, 240, 240, 255),
    fontFamily='Verdana',
    fontSize=8,
    fontWeight='normal',
    borderStyle='solid',
    borderWidth=1,
    borderRadius=2,
)
```

### Parameters:

**parent** : *[QWidget](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QWidget.html) obj/[QLayout](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLayout.html) obj, optional*
- parent element

**primaryColor** : *[QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str, default=(21, 21, 21, 255)*
- normal text color and background color on hover

**secondaryColor** : *[QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str, default=(245, 177, 66, 255)*
- normal background color and the text color on hover

**parentBackgroundColor** : *[QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str, default=(240, 240, 240, 255)*
- parent element's background color used for minimize effect on click

**fontFamily** : *str, default='Verdana'*
- name of font family

**fontSize** : *int, default=8*
- font size

**fontWeight** : *str, default='normal'*
- font weight

**borderStyle** : *str, default='solid'*
- border style

**borderWidth** : *int, default=1*
- border width

**borderRadius** : *int, default=2*
- border radius

### Returns:
- *Button obj*

## setBorder

Set button border properties.

```python
setBorder(
    borderStyle=None,
    borderWidth=None,
    borderRadius=None,
)
```

### Parameters:

**borderStyle** : *str, optional*
- border style

**borderWidth** : *int, optional*
- border width

**borderRadius** : *int, optional*
- border radius

### Returns:
- *None*

## setColors

Set button colors.

```python
setColors(
    primaryColor=None,
    secondaryColor=None,
    parentBackgroundColor=None,
)
```

### Parameters:

**primaryColor** : *[QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str, optional*
- normal text color and background color on hover

**secondaryColor** : *[QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str, optional*
- normal background color and the text color on hover

**parentBackgroundColor** : *[QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str, optional*
- parent element's background color used for minimize effect on click

### Returns:
- *None*

## setFont

Set button text font properties.

```python
setFont(
    fontFamily=None,
    fontSize=None,
    fontWeight=None,
)
```

### Parameters:

**fontFamily** : *str, optional*
- name of font family

**fontSize** : *int, optional*
- font size

**fontWeight** : *str, optional*
- font weight

### Returns:
- *None*

