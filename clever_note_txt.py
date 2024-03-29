# Переменные
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# Окно
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Помощник решения логических задач')
main_win.resize(750, 750)

notes_win = QWidget()
# Лейауты
main_layout = QHBoxLayout()  # Основной
layout1 = QVBoxLayout()  # Левый
layout2 = QVBoxLayout()  # Правый
layout3 = QHBoxLayout()  # Правый верх
layout4 = QHBoxLayout()  # Правый низ


# Информация
def createnote():
    note_name, result = QInputDialog.getText(notes_win, 'Добавить задачи', 'Название задачи:')
    if result == True:
        text3show.addItem(note_name)
    data[note_name] = {"текст": ""}
    with open("notes.txt", "w", encoding='utf-8') as file:
        file.write(str(data))


def savenote():
    global text
    if selectednotes != 0:
        text = writetext.toPlainText()
        data[selectednotes] = {"текст": text}
        if text3show.selectedItems():
            with open("notes.txt", "w", encoding='utf-8') as file:
                file.write(str(data))


def show():
    global selectednotes
    global text
    text4show.clear()
    selectednotes = text3show.selectedItems()[0].text()
    text = data[selectednotes]['текст']
    writetext.setText(data[selectednotes]['текст'])


def deletenote():
    global selectednotes
    if selectednotes != 0:
        text3show.clear()
        writetext.clear()
        text4show.clear()
        data.pop(selectednotes)
        with open("notes.txt", "w", encoding='utf-8') as file:
            file.write(str(data))
        for cc in data:
            text3show.addItem(cc)
        selectednotes = 0


# Строчка - True, стоблик - False
def add_to(table, row_or_column):
    if row_or_column:
        table.insertRow(table.rowCount())
    else:
        table.insertColumn(table.columnCount())


note_name = 0
result = False
add = 0
selectednotes = 0
search = 0
# Обьекты
writetext = QTextEdit()
text3show = QListWidget()
text4show = QTableWidget()
text4show.setRowCount(4)
text4show.setColumnCount(4)

text1 = 'Список задач'
text1show = QLabel(text1)
text2 = 'Решение'
text2show = QLabel(text2)
textbutton1 = 'Создать задачу'
button1 = QPushButton(textbutton1)
textbutton2 = 'Удалить задачу'
button2 = QPushButton(textbutton2)
textbutton3 = 'Сохранить задачу'
button3 = QPushButton(textbutton3)
textbutton4 = 'Добавить столбик'
button4 = QPushButton(textbutton4)
button4.clicked.connect(lambda: add_to(text4show, False))
textbutton5 = 'Добавить строчку'
button5 = QPushButton(textbutton5)
button5.clicked.connect(lambda: add_to(text4show, True))



# Лейауты
layout1.addWidget(writetext)

layout2.addWidget(text1show)
layout2.addWidget(text3show)
layout3.addWidget(button1)
layout3.addWidget(button2)
layout2.addLayout(layout3)
layout2.addWidget(button3)

layout2.addWidget(text2show)
layout2.addWidget(text4show)
layout4.addWidget(button4)
layout4.addWidget(button5)
layout2.addLayout(layout4)

main_layout.addLayout(layout1)
main_layout.addLayout(layout2)

with open("notes.txt", "r", encoding='utf-8') as file:
    data1 = file.read()
    data = eval(data1)
    for cc in data:
        text3show.addItem(cc)

button1.clicked.connect(createnote)
text3show.itemClicked.connect(show)
button3.clicked.connect(savenote)
button2.clicked.connect(deletenote)

# Запуск
main_win.setLayout(main_layout)
main_win.showMaximized()

app.exec_()
