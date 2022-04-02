import sys
from time import sleep
from PyQt5 import QtWidgets,  QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QVBoxLayout, QStackedLayout, QLayoutItem, QListWidget, QInputDialog, QLineEdit, QCheckBox, QComboBox, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap, QCursor


class MainWindow(QMainWindow):
    def __init__(self,) -> None:
        super().__init__()

        fontId = QFontDatabase.addApplicationFont("fs-gravity.ttf")
        self.fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

        self.back_but = QPushButton(self)
        self.back_but.setStyleSheet('''
        QPushButton {color: white;
                    background-color: rgba(255, 255, 255, 0)
                                        }''')
        self.back_but.resize(170, 50)
        self.back_but.setFont(QFont(self.fontName, 20))
        self.back_but.setText("BACK TO MENU")
        self.back_but.move(5, 50)
        self.back_but.clicked.connect(self.main_start)
        self.back_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.back_but.hide()

        self.setFixedSize(1152, 648)
        self.setWindowTitle("TGRAMER")
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet('''
        QMainWindow {background-image: url(back.png)}
        '''
                           )

        self.main_title = QLabel(self)
        self.main_title.setText("TGRAMER")
        self.main_title.setAlignment(Qt.AlignCenter)
        self.main_title.resize(400, 90)
        self.main_title.setFont(QFont(self.fontName, 70))
        self.main_title.setStyleSheet('''
        QLabel {color: white}''')
        self.main_title.move(110, 250)
        self.main_title.hide()

        self.by_title = QLabel(self)
        self.by_title.setText("BY THE INTERNET")
        self.by_title.setAlignment(Qt.AlignCenter)
        self.by_title.resize(400, 60)
        self.by_title.setFont(QFont(self.fontName, 30))
        self.by_title.setStyleSheet('''
        QLabel {color: white}''')
        self.by_title.move(140, 340)
        self.by_title.hide()

        self.pars_but = QPushButton(self)
        self.pars_but.setText("PARSING")
        self.pars_but.resize(400, 150)
        self.pars_but.setFont(QFont(self.fontName, 60))
        self.pars_but.setStyleSheet('''
        QPushButton {background-color: #EE0823;
                    color: white;
                                        }''')

        self.pars_but.move(700, 220)
        self.pars_but.clicked.connect(self.pars_window)
        self.pars_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pars_but.hide()

        self.inv_but = QPushButton(self)
        self.inv_but.setText("INVITING")
        # self.pars_but.setAlignment(Qt.AlignCenter)
        self.inv_but.resize(400, 150)
        self.inv_but.setFont(QFont(self.fontName, 60))
        self.inv_but.setStyleSheet('''
        QPushButton {background-color: #EE0823;
                    color: white;
                                        }''')
        self.inv_but.move(700, 20)
        self.inv_but.clicked.connect(self.inv_window)
        self.inv_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.inv_but.hide()

        self.mail_but = QPushButton(self)
        self.mail_but.setText("MAILING")
        # self.pars_but.setAlignment(Qt.AlignCenter)
        self.mail_but.resize(400, 150)
        self.mail_but.setFont(QFont(self.fontName, 60))
        self.mail_but.setStyleSheet('''
        QPushButton {background-color: #EE0823;
                    color: white;
                                        }''')
        self.mail_but.move(700, 420)
        self.mail_but.clicked.connect(self.mail_window)
        self.mail_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.mail_but.hide()

        self.pointer1 = QLabel(self)
        self.pointer1.setPixmap(QPixmap("pointer.png"))
        self.pointer1.resize(QPixmap("pointer.png").size())
        self.pointer1.move(610, 460)
        self.pointer1.hide()

        self.pointer2 = QLabel(self)
        self.pointer2.setPixmap(QPixmap("pointer.png"))
        self.pointer2.resize(QPixmap("pointer.png").size())
        self.pointer2.move(610, 260)
        self.pointer2.hide()

        self.pointer3 = QLabel(self)
        self.pointer3.setPixmap(QPixmap("pointer.png"))
        self.pointer3.resize(QPixmap("pointer.png").size())
        self.pointer3.move(610, 60)
        self.pointer3.hide()

        self.log_win = QListWidget(self)
        self.log_win.setFont(QFont(self.fontName, 10))
        self.log_win.resize(400, 360)
        self.log_win.setStyleSheet('''
        QListWidget {background-color: #EE0823;
                    color: white;
                                        }''')
        self.log_win.move(700, 240)
        self.log_win.hide()

        self.log_title = QLabel(self)
        self.log_title.setFont(QFont(self.fontName, 20))
        self.log_title.resize(400, 20)
        self.log_title.setText("LOGS:")
        self.log_title.setStyleSheet('''
        QLabel {background-color: #EE0823;
                    color: white;
                    text-decoration: underline;
                                        }''')
        self.log_title.move(700, 220)
        self.log_title.hide()

        self.group_link_zone = QLineEdit(self)
        self.group_link_zone.setPlaceholderText("Ссылка на группу")
        self.group_link_zone.setFont(QFont(self.fontName, 20))
        self.group_link_zone.move(280, 120)
        self.group_link_zone.resize(300, 30)
        self.group_link_zone.hide()

        self.group_add_zone = QLineEdit(self)
        self.group_add_zone.setPlaceholderText("Сколько добавить всего")
        self.group_add_zone.setFont(QFont(self.fontName, 20))
        self.group_add_zone.move(280, 220)
        self.group_add_zone.resize(300, 30)
        self.group_add_zone.hide()

        self.group_each_zone = QLineEdit(self)
        self.group_each_zone.setPlaceholderText("Сколько c каждого аккаунта")
        self.group_each_zone.setFont(QFont(self.fontName, 20))
        self.group_each_zone.move(280, 300)
        self.group_each_zone.resize(300, 30)
        self.group_each_zone.hide()

        self.group_pausemin_zone = QLineEdit(self)
        self.group_pausemin_zone.setPlaceholderText("Мин. пауза")
        self.group_pausemin_zone.setFont(QFont(self.fontName, 20))
        self.group_pausemin_zone.move(280, 420)
        self.group_pausemin_zone.resize(150, 30)
        self.group_pausemin_zone.hide()

        self.group_pausemax_zone = QLineEdit(self)
        self.group_pausemax_zone.setPlaceholderText("Макс. пауза")
        self.group_pausemax_zone.setFont(QFont(self.fontName, 20))
        self.group_pausemax_zone.move(450, 420)
        self.group_pausemax_zone.resize(150, 30)
        self.group_pausemax_zone.hide()

        self.start_but = QPushButton(self)
        self.start_but.setText("START INVITING")
        # self.pars_but.setAlignment(Qt.AlignCenter)
        self.start_but.resize(400, 150)
        self.start_but.setFont(QFont(self.fontName, 40))
        self.start_but.setStyleSheet('''
        QPushButton {background-color: #EE0823;
                    color: white;
                                        }''')
        self.start_but.move(700, 20)
        self.start_but.clicked.connect(self.start_working)
        self.start_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.start_but.hide()

        self.check_memb = QCheckBox(self)
        self.check_memb.setChecked(True)
        self.check_memb.move(450, 220)
        self.check_memb.setStyleSheet('''
            QCheckBox {}

            QCheckBox::indicator {
            width: 30px;
            height: 30px;}
        ''')
        self.check_memb.hide()

        self.check_memb_text = QLabel(self)
        self.check_memb_text.setText("Участники")
        self.check_memb_text.setAlignment(Qt.AlignRight)
        self.check_memb_text.resize(150, 40)
        self.check_memb_text.setFont(QFont(self.fontName, 20))
        self.check_memb_text.setStyleSheet('''
        QLabel {color: white}''')
        self.check_memb_text.move(280, 215)
        self.check_memb_text.hide()

        self.check_amd = QCheckBox(self)
        self.check_amd.setChecked(True)
        self.check_amd.move(450, 280)
        self.check_amd.setStyleSheet('''
            QCheckBox {}

            QCheckBox::indicator {
            width: 30px;
            height: 30px;}
        ''')
        self.check_amd.hide()

        self.check_adm_text = QLabel(self)
        self.check_adm_text.setText("Админы")
        self.check_adm_text.setAlignment(Qt.AlignRight)
        self.check_adm_text.resize(150, 40)
        self.check_adm_text.setFont(QFont(self.fontName, 20))
        self.check_adm_text.setStyleSheet('''
        QLabel {color: white}''')
        self.check_adm_text.move(280, 275)
        self.check_adm_text.hide()

        self.check_photo = QCheckBox(self)
        self.check_photo.move(450, 340)
        self.check_photo.setStyleSheet('''
            QCheckBox {}

            QCheckBox::indicator {
            width: 30px;
            height: 30px;}
        ''')
        self.check_photo.hide()

        self.check_photo_text = QLabel(self)
        self.check_photo_text.setText("С фото профиля")
        self.check_photo_text.setAlignment(Qt.AlignRight)
        self.check_photo_text.resize(190, 40)
        self.check_photo_text.setFont(QFont(self.fontName, 20))
        self.check_photo_text.setStyleSheet('''
        QLabel {color: white}''')
        self.check_photo_text.move(240, 335)
        self.check_photo_text.hide()

        self.check_chatting = QCheckBox(self)
        self.check_chatting.move(450, 400)
        self.check_chatting.setStyleSheet('''
            QCheckBox {}

            QCheckBox::indicator {
            width: 30px;
            height: 30px;}
        ''')
        self.check_chatting.hide()

        self.check_chatting_text = QLabel(self)
        self.check_chatting_text.setText("Писали в чат")
        self.check_chatting_text.setAlignment(Qt.AlignRight)
        self.check_chatting_text.resize(190, 40)
        self.check_chatting_text.setFont(QFont(self.fontName, 20))
        self.check_chatting_text.setStyleSheet('''
        QLabel {color: white}''')
        self.check_chatting_text.move(240, 395)
        self.check_chatting_text.hide()

        self.active = QComboBox(self)
        self.active.resize(100, 30)
        self.active.setFont(QFont(self.fontName, 15))
        self.active.addItem("Все")
        self.active.addItem("Онлайн")
        self.active.addItem("Неделя")
        self.active.move(450, 460)
        self.active.hide()

        self.active_text = QLabel(self)
        self.active_text.setText("Активность")
        self.active_text.setAlignment(Qt.AlignRight)
        self.active_text.resize(190, 40)
        self.active_text.setFont(QFont(self.fontName, 20))
        self.active_text.setStyleSheet('''
        QLabel {color: white}''')
        self.active_text.move(240, 455)
        self.active_text.hide()

        self.mes_zone = QTextEdit(self)
        self.mes_zone.setStyleSheet('''QTextEdit {border: 3px solid #EE0823}''')
        self.mes_zone.setFont(QFont(self.fontName, 15))
        self.mes_zone.move(250, 120)
        self.mes_zone.resize(390, 200)
        self.mes_zone.hide()

        self.mes_title = QLabel(self)
        self.mes_title.setText("Сообщение")
        self.mes_title.resize(200, 40)
        self.mes_title.setFont(QFont(self.fontName, 20))
        self.mes_title.setStyleSheet('''
        QLabel {color: white}''')
        self.mes_title.move(250, 80)
        self.mes_title.hide()

        self.mes_total = QLineEdit(self)
        self.mes_total.setPlaceholderText("Сколько отправить всего")
        self.mes_total.setFont(QFont(self.fontName, 20))
        self.mes_total.move(250, 380)
        self.mes_total.resize(320, 30)
        self.mes_total.hide()

        self.mes_each = QLineEdit(self)
        self.mes_each.setPlaceholderText("Сколько с каждого")
        self.mes_each.setFont(QFont(self.fontName, 20))
        self.mes_each.move(250, 420)
        self.mes_each.resize(320, 30)
        self.mes_each.hide()

        self.mes_pause = QLineEdit(self)
        self.mes_pause.setPlaceholderText("Задержка")
        self.mes_pause.setFont(QFont(self.fontName, 20))
        self.mes_pause.move(250, 460)
        self.mes_pause.resize(320, 30)
        self.mes_pause.hide()

        self.main_start()

    def main_start(self):
        self.main_title.show()
        self.by_title.show()
        self.pars_but.show()
        self.inv_but.show()
        self.mail_but.show()

        self.log_win.hide()
        self.pointer1.show()
        self.pointer2.show()
        self.pointer3.show()

        self.log_title.hide()
        self.back_but.hide()

        self.group_link_zone.hide()
        self.group_add_zone.hide()
        self.group_each_zone.hide()
        self.group_pausemin_zone.hide()
        self.group_pausemax_zone.hide()
        self.start_but.hide()

        self.check_memb.hide()
        self.check_memb_text.hide()
        self.check_amd.hide()
        self.check_adm_text.hide()
        self.check_photo.hide()
        self.check_photo_text.hide()
        self.check_chatting.hide()
        self.check_chatting_text.hide()
        self.active.hide()
        self.active_text.hide()

        self.mes_zone.hide()
        self.mes_title.hide()
        self.mes_total.hide()
        self.mes_each.hide()
        self.mes_pause.hide()

    def pars_window(self):
        self.inv_but.hide()
        self.mail_but.hide()
        self.main_title.hide()
        self.by_title.hide()
        self.pointer1.hide()
        self.pointer2.hide()
        self.pointer3.hide()

        self.back_but.show()
        self.start_but.move(self.pars_but.pos())
        self.start_but.setText("START PARSING")
        self.start_but.show()

        self.group_link_zone.show()
        self.check_memb.show()
        self.check_memb_text.show()
        self.check_amd.show()
        self.check_adm_text.show()
        self.check_photo.show()
        self.check_photo_text.show()
        self.check_chatting.show()
        self.check_chatting_text.show()
        self.active.show()
        self.active_text.show()

    def inv_window(self):
        self.pars_but.hide()
        self.mail_but.hide()
        self.main_title.hide()
        self.by_title.hide()
        self.pointer1.hide()
        self.pointer2.hide()
        self.pointer3.hide()
        self.inv_but.hide()

        self.back_but.show()
        self.log_win.move(700, 240)
        self.log_win.show()
        self.log_title.move(700, 220)
        self.log_title.show()
        self.group_link_zone.show()
        self.group_add_zone.show()
        self.group_each_zone.show()
        self.group_pausemin_zone.show()
        self.group_pausemax_zone.show()

        self.start_but.move(self.inv_but.pos())
        self.start_but.setText("START INVITING")
        self.start_but.show()

    def mail_window(self):
        self.inv_but.hide()
        self.pars_but.hide()
        self.main_title.hide()
        self.by_title.hide()
        self.pointer1.hide()
        self.pointer2.hide()
        self.pointer3.hide()

        self.back_but.show()
        self.start_but.move(self.mail_but.pos())
        self.start_but.setText("START MAILING")
        self.start_but.show()

        self.mes_zone.show()
        self.mes_title.show()
        self.mes_total.show()
        self.mes_each.show()
        self.mes_pause.show()

        self.log_title.move(700, 20)
        self.log_title.show()
        self.log_win.move(700, 40)
        self.log_win.show()

    def start_working(self):
        # старт работы внешних скриптов
        # возможно перенесу в другой файл
        pass


app = QApplication(sys.argv)
mw = MainWindow()

mw.show()
sys.exit(app.exec_())
