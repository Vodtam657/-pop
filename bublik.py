from PyQt5.QtWidgets import *
import database


def menu_window():
    window = QDialog()
    main_line = QDialog()
    quest_lbl = QLabel("Введіть запитання")
    right_ans_lbl = QLabel("Введіть правильну відповідь")
    quest_edit = QLineEdit()
    right_ans_edit = QLineEdit()
    add_quest_btn = QPushButton("Змінити запитання")
    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)
    main_line.addLayout(h1)
    def add_quest_funk():

        a = {

                "Запитання": "Ялуко",
                "Правильна відповідь": "apple",
                "Неправильна 1": "home",
                "Неправильна 2": "banana",
                "Неправильна 3": "orange",
            }

