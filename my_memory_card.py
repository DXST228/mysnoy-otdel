# подключение библиотек
from PyQt5.QtCore import Qt
# все виджеты (элементы интерфейса) - Q + название на инглише
from PyQt5.QtWidgets import (
    QApplication, QWidget, QRadioButton, QLabel, 
    QVBoxLayout, QHBoxLayout, QMessageBox, QPushButton, QGroupBox, 
    QButtonGroup
)
from PyQt5.QtCore import Qt, QFile, QIODevice, QTextStream
from PyQt5 import QtGui
from random import randint, shuffle
from const import *
from pops import *


class MyWindow(QWidget):
    def __init__(self, title='My App', w=400, h=200):
        super().__init__()
        self.pops = Pops()
        self.setWindowTitle(title)
        self.resize(w, h)
        self.set_styles()
        self.setUI()
        


    def setUI(self):
        self.answer = QPushButton(TOORES)
        self.answer.clicked.connect(self.chek_answer)
        self.text1 = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
        x =2000
        self.grupp = QButtonGroup()        
        self.buttons=[]
        for i in range(1,5):
            x+=5
            self.button = QRadioButton(str(x))
            self.buttons.append(self.button)
            self.grupp.addButton(self.button)

        line1 = QVBoxLayout()
        line1.addWidget(self.buttons[0])
        line1.addWidget(self.buttons[1])

        line2 = QVBoxLayout()
        line2.addWidget(self.buttons[2])
        line2.addWidget(self.buttons[3])

        qlain = QHBoxLayout()
        qlain.addLayout(line1)
        qlain.addLayout(line2)

        self.qwestion = QGroupBox('Варианты ответов:')
        self.qwestion.setLayout(qlain)

        self.isright = QLabel('Прав ты или нет?')
        self.right = QLabel('Ответ будет тут!')

        reslain = QVBoxLayout()
        reslain.addWidget(self.isright)
        reslain.addWidget(self.right)

        self.result = QGroupBox('Результат теста')
        self.result.setLayout(reslain)
        self.result.hide()
        self.ask(self.pops.qs[self.pops.now])

        mainlain = QVBoxLayout()
        mainlain.addWidget(self.text1, alignment=Qt.AlignCenter)
        mainlain.addWidget(self.qwestion,alignment=Qt.AlignCenter )
        mainlain.addWidget(self.result, alignment=Qt.AlignCenter)
        mainlain.addWidget(self.answer,alignment=Qt.AlignCenter)

        
        self.setLayout(mainlain)

    def click(self):
        if self.answer.text()== TOORES:
            self.show_result()
            
        else:
            self.next_question()
    def set_styles(self, ui_filename='style.qss', icon='IHV.png'):
        stream = QFile(ui_filename)
        stream.open(QIODevice.ReadOnly)
        self.setStyleSheet(QTextStream(stream).readAll())
        self.setWindowIcon(QtGui.QIcon(icon))
    def message(self, title, text):
        window=QMessageBox()
        window.setText(text)
        window.setWindowTitle(title)
        window.exec()
    def show_result(self):
        self.answer.setText(GUESS)
        self.result.show()
        self.qwestion.hide()

    def show_question(self):
        self.answer.setText(TOORES)
        self.grupp.setExclusive(False)
        for button in self.buttons:
            button.setChecked(False)
        self.grupp.setExclusive(True)
        self.result.hide()
        self.qwestion.show()
    def ask(self, q:dict):
        self.text1.setText(q[QUESTION])
        shuffle(self.buttons)
        self.buttons[0].setText(q[RIGHT])
        self.right.setText(self.buttons[0].text())
        for i in range(3):
            self.buttons[i+1].setText(q[WRONG][i])
        self.show_question()
    def chek_answer(self):
        if len(self.pops.qs)!=1:
            if self.buttons[0].isChecked():
                self.isright.setText('True')
                self.pops.levelup()
                self.click()
            #перейди к следующему вопросу пж
            else:
                for button in self.buttons[1:]:
                    if button.isChecked():
                        self.isright.setText('False')
                        self.click()
        else:
            self.text1.setText('Тест закончен, '+ self.pops.end())
            #self.answer.hide()
            self.result.show()
            self.qwestion.hide()
            self.answer.setText(GUESS)
    def next_question(self):
        self.pops.next()
        queue = self.pops.qs[self.pops.now]
        self.ask(queue)
        #5Б отдай вопрос плз
app = QApplication([])

window = MyWindow()
window.show()
app.exec()