import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets, uic, QtGui
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is AyoubBot, you can just call me chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well, and you ?", "i am great !, and you ?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]

    ],
    [
        r"(.*)created(.*)",
        ["Bih Ayoub created me using Python's NLTK library ","It's a secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Caen, France',]
    ],
    [
        r"(.*)raining (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of video games like league of legends",]
    ],
    [
        r"what role you play in (lol|league of legends)?(.*)",
        ["adc"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['Give me another question, I cannot understand what you were saying']
    ],
]


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('mainwindow.ui', self) # Load the .ui file
        self.button = self.findChild(QtWidgets.QPushButton, '_send')
        self.input = self.findChild(QtWidgets.QLineEdit, '_message')
        self.messages = self.findChild(QtWidgets.QListView, '_messages')
        self.quit = self.findChild(QtWidgets.QAction, '_quit_action')

        self.model = QtGui.QStandardItemModel()
        self.messages.setModel(self.model)
        self.chat = Chat(pairs, reflections)

        self.button.clicked.connect(self.printButtonPressed)
        self.quit.triggered.connect(self.shutprocess)
        self.show() # Show the GUI

    def printButtonPressed(self):
        # This is executed when the button is presseds
        first_item = QtGui.QStandardItem("Me : "+self.input.text())
        self.model.appendRow(first_item)
        second_item = QtGui.QStandardItem("Chatbot : "+self.chat.respond(self.input.text()))
        self.model.appendRow(second_item)


    def shutprocess(self):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
        else:
            pass
