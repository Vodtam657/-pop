from PyQt5.QtWidgets import *

import database


def menu_window():
    window = QDialog()
    main_line = QDialog()
    quest_lbl = QLabel("Введіть запитання")
    right_ans_lbl = QLabel("Введіть правильну відповідь")
    WW2 = QLabel("Неправильна відповіть")
    WWW2_edit = QLineEdit()
    WW1 = QLabel("Неправильна відповідь")
    WWW1_edit = QLineEdit()
    WW3 = QLabel("Неправильна відповідь")
    WWW3_edit = QLineEdit()
    quest_edit = QLineEdit()
    right_ans_edit = QLineEdit()
    add_quest_btn = QPushButton("Добавити запитання")

    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_edit)
    main_line.addLayout(h1)

    h2 = QHBoxLayout()
    h2.addWidget(right_ans_lbl)
    h2.addWidget(right_ans_edit)
    main_line.addLayout(h2)

    h3 = QHBoxLayout()
    h3.addWidget(WW2)
    h3.addWidget(WWW2_edit)
    main_line.addLayout(h3)

    h4 = QHBoxLayout()
    h4.addWidget(WW3)
    h4.addWidget(WWW3_edit)
    main_line.addLayout(h4)

    h5 = QHBoxLayout()
    h5.addWidget(WW1)
    h5.addWidget(WWW1_edit)
    main_line.addLayout(h5)





    def add_quest_func():
        a = {
            "Запитання": quest_edit.text(),
            "Правильна відповідь": "",
            "Неправильна відповідь": "",
            "Неправильна 1": "",
            "Неправильна 2": "",
            "Неправильна 3": "",
            }
        database.questions.append(a)
    main_line.addWidget(add_quest_btn)
    add_quest_btn.clicked.connect(add_quest_func)
    window.setLayout(main_line)
    window.exec()