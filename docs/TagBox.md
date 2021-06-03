# TagBox

TagBox is an inherited class of [QWidget](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QWidget.html) that handles tag lists.

<img alt="TagBox Example" src="../img/TagBoxExample.gif" width="400"/>

## Constructors & Methods

- [TagBox()](#tagbox-1)

- [addTag()](#addtag)

- [clearTags()](#cleartags)

- [getTags()](#gettags)

- [removeTag()](#removetag)



## TagBox

Create new TagBox object.

```python
TagBox(
    parent=None,
    textColor=(21, 21, 21, 255),
    backgroundColor=(245, 177, 66, 255),
    backgroundColorOnHover=(249, 205, 134, 255),
    fontFamily='Verdana',
    fontSize=10,
    fontWeight='normal',
    borderStyle='solid',
    borderColor=(21, 21, 21, 255),
    borderWidth=1,
    borderRadius=2,
)
```

### Parameters:

**parent** : *[QWidget](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QWidget.html) obj/[QLayout](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLayout.html) obj, optional*
- parent element

**textColor** : *[QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str, default=(21, 21, 21, 255)*
- tag text color

**backgroundColor** : *[QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str, default=(245, 177, 66, 255)*
- tag background color

**backgroundColorOnHover** : *[QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str, default=(249, 205, 134, 255)*
- tag background color on mouse hover

**fontFamily** : *str, default='Verdana'*
- name of font family

**fontSize** : *int, default=10*
- font size

**fontWeight** : *str, default='normal'*
- font weight

**borderStyle** : *str, default='solid'*
- tag border style

**borderColor** : *[QColor](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html) obj/RGBA tuple/RGBA 32-bit unsigned int/RGBA str/HEX str, default=(21, 21, 21, 255)*
- tag border color

**borderWidth** : *int, default=1*
- tag border width

**borderRadius** : *int, default=2*
- tag border radius

### Returns:
- *TagBox obj*

## addTag

Add new tag if it doesn't exist.

```python
addTag(tagName)
```

### Parameters:

**tagName** : *str*
- tag name

### Returns:
- *bool*

## clearTags

Clear all tags.

```python
clearTags()
```

### Returns:
- *None*

## getTags

Get list of tags.

```python
getTags()
```

### Returns:
- *list*

## removeTag

Remove tag by index.

```python
removeTag(index)
```

### Parameters:

**index** : *int*
- index position of tag to remove

### Returns:
- *None*

