import inspect
import json

from MangoUI import Button, Canvas, Slider, TagBox

def parseParams(params):
    param_info = {}
    for param in params:
        nametype_desc = [p.strip() for p in param.split(':')]
        name_type = [p.strip().strip(')') for p in nametype_desc[0].split('(')]
        param_info[name_type[0]] = {'type': name_type[1], 'description': nametype_desc[1]}

    return param_info

def parseDocString(docstring):
    func_desc = ''
    func_params = {}
    func_returns = []

    ds = docstring.split('Returns:')
    func_returns = [ret.strip() for ret in ds[1].strip().split('\n')]

    ds = ds[0].split('Parameters:')
    func_desc = ds[0].strip()
    if len(ds) > 1:
        func_params = [param.strip() for param in ds[1].strip().split('\n')]
        func_params = parseParams(func_params)

    return func_desc, func_params, func_returns

def classSignature(class_type):
    class_members = inspect.getmembers(class_type)
    class_methods = [member for member in class_members if inspect.isfunction(member[1])]

    class_signature = {}
    class_signature['name'] = class_type.__name__
    class_signature['description'] = class_type.__doc__
    method_signatures = {}

    for method in class_methods:
        if method[1].__doc__ == None:
            continue

        method_desc, method_params, method_returns = parseDocString(method[1].__doc__)

        method_sgn = {k : {'default': str(v).lstrip(k + '='), 'type':method_params.get(k)['type'], 'description':method_params.get(k)['description']} for (k, v) in inspect.signature(method[1]).parameters.items() if method_params.get(k) != None}
        method_signatures[method[0]] = {}
        method_signatures[method[0]]['description'] = method_desc
        method_signatures[method[0]]['args'] = method_sgn
        method_signatures[method[0]]['returns'] = method_returns

    class_signature['methods'] = method_signatures

    return class_signature

def documentClass(class_type):
    class_signature = classSignature(class_type)
    class_name = class_signature['name']
    class_desc = class_signature['description']

    doc = f'# {class_name}\n\n'
    doc += f'{class_desc}\n\n'

    gifpath = f'../img/{class_name}Example.gif'
    doc += f'<img alt="{class_name} Example" src="{gifpath}" height="300"/>\n\n'

    doc += f'## Constructors & Methods\n\n'
    for (method_name, method_sgn) in class_signature['methods'].items():
        name = method_name
        link = '#' + name.lower()
        if name == '__init__':
            name = class_name
            link = '#' + name.lower() + '-1'

        doc += f'- [{name}()]({link})\n\n'

    doc += '\n\n'

    for (method_name, method_sgn) in class_signature['methods'].items():
        name = class_name if method_name == '__init__' else method_name
        desc = method_sgn['description']

        doc += f'## `{name}`()\n\n'
        doc += f'{desc}\n\n'
        doc += f'```python\n{name}('

        if len(method_sgn['args']) < 2:
            for (arg_name, arg_sgn) in method_sgn['args'].items():
                doc += arg_name
                if len(arg_sgn['default']) > 0:
                    doc += '=' + arg_sgn['default']
        else:
            doc += '\n'
            for (arg_name, arg_sgn) in method_sgn['args'].items():
                doc += '    ' + arg_name
                if len(arg_sgn['default']) > 0:
                    doc += '=' + arg_sgn['default']
                    doc += ',\n'

        doc += ')\n```\n\n'
        
        if len(method_sgn['args']) > 0:
            doc += '### Parameters:\n\n'

        for (arg_name, arg_sgn) in method_sgn['args'].items():
            arg_type = arg_sgn['type']

            arg_def = arg_sgn['default']
            if arg_def == 'None':
                arg_def = ', optional'
            elif len(arg_def) > 0:
                arg_def = ', default=' + arg_def
            doc += f'**{arg_name}** : *{arg_type}{arg_def}*\n'

            arg_desc = arg_sgn['description']
            doc += f'- {arg_desc}\n\n'

        doc += '### Returns:\n'

        first_iter = True
        for ret in method_sgn['returns']:
            if first_iter == True:
                first_iter = False
            else:
                doc += ', \n'
            doc += f'- *{ret}*'

        doc += '\n\n'

    doc = addHyperlinks(doc)

    return doc

def addHyperlinks(doc):
    links = {
        'QColor': 'https://doc.qt.io/qtforpython-5/PySide2/QtGui/QColor.html',
        'QPushButton': 'https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QPushButton.html',
        'QSS': 'https://doc.qt.io/qt-5/stylesheet-syntax.html',
        'QVariantAnimation': 'https://doc.qt.io/qtforpython-5/PySide2/QtCore/QVariantAnimation.html',
        'QLabel': 'https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLabel.html',
        'QPixmap': 'https://doc.qt.io/qtforpython/PySide6/QtGui/QPixmap.html',
        'QPainter': 'https://doc.qt.io/qtforpython-5/PySide2/QtGui/QPainter.html',
        'QStackedWidget': 'https://doc.qt.io/archives/qtforpython-5.12/PySide2/QtWidgets/QStackedWidget.html',
        'Qt.Orientation': 'https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html#PySide6.QtCore.PySide6.QtCore.Qt.Orientation',
        'QEasingCurve.Type': 'https://doc.qt.io/qtforpython/PySide6/QtCore/QEasingCurve.html#PySide6.QtCore.PySide6.QtCore.QEasingCurve.Type',
        'QLayout': 'https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLayout.html',
        'QWidget': 'https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QWidget.html',
    }

    linked_doc = doc
    md_links = {k:f'[{k}]({v})' for (k, v) in links.items()}
    for (k, v) in md_links.items():
        linked_doc = linked_doc.replace(k, v)

    return linked_doc

def createDocumentation(class_type):
    doc_content = documentClass(class_type)
    with open(class_type.__name__ + '.md', 'w+') as docfile:
        docfile.write(doc_content)

if __name__ == '__main__':
    createDocumentation(Button)
    createDocumentation(Canvas)
    createDocumentation(Slider)
    createDocumentation(TagBox)