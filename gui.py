import sys
from time import sleep
from PyQt5 import QtWidgets,  QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QVBoxLayout, QStackedLayout, QLayoutItem, QListWidget, QInputDialog, QLineEdit, QCheckBox, QComboBox, QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap, QCursor


class PicClick(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        self.clicked.emit()


class MainWindow(QMainWindow):
    def __init__(self,) -> None:
        super().__init__()

        fontId = QFontDatabase.addApplicationFont("fs-gravity.ttf")
        self.fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

        self.back_but = QPushButton(self)
        self.back_but.setStyleSheet('''
        QPushButton {color: black;
                    background-color: #c7d0d9;
                    border: 1px solid rgb(144, 153, 162);
                                        }''')
        self.back_but.setFont(QFont("Arial", 15))
        self.back_but.setText("Назад")
        self.back_but.resize(150, 40)
        self.back_but.move(20, 50)
        self.back_but.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,
            blurRadius=0.0,
            color=QtGui.QColor(153, 167, 176),
            offset=QtCore.QPointF(5.0, 5.0)))

        self.back_but.clicked.connect(self.main_start)
        self.back_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.back_but.hide()

        self.setFixedSize(1152, 648)
        self.setWindowTitle("TGRAMER")

        self.setStyleSheet('''
        QMainWindow {background-color: #d9d9d9}
        '''
                           )

        self.main_title = QLabel(self)
        self.main_title.setText("TGRAMER")
        self.main_title.setAlignment(Qt.AlignCenter)
        self.main_title.resize(400, 100)
        self.main_title.setFont(QFont(self.fontName, 45))
        self.main_title.move(370, 10)
        self.main_title.hide()

        self.by_title = QLabel(self)
        self.by_title.setText("by THE INTERNET")
        self.by_title.setAlignment(Qt.AlignCenter)
        self.by_title.resize(400, 60)
        self.by_title.setFont(QFont(self.fontName, 20))
        self.by_title.move(370, 80)
        self.by_title.hide()

        self.pars_but = QPushButton(self)
        self.pars_but.setText("\n\n\n\nПарсинг")
        self.pars_but.resize(300, 300)
        self.pars_but.setFont(QFont("Arial", 21))
        self.pars_but.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,
            blurRadius=0.0,
            color=QtGui.QColor(153, 167, 176),
            offset=QtCore.QPointF(5.0, 5.0)))

        self.pars_but.setStyleSheet('''
        QPushButton {background-color: #c7d0d9;
                    color: black;
                    border: 2px solid rgb(144, 153, 162);
                    text-align: bottom;
                                        }''')

        self.pars_but.move(70, 150)
        self.pars_but.clicked.connect(self.pars_window)
        self.pars_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pars_but.hide()

        self.pars_pic = PicClick(self)
        self.pars_pic.setPixmap(QPixmap('pars.png'))
        self.pars_pic.resize(150, 150)
        self.pars_pic.move(150, 189)
        self.pars_pic.clicked.connect(self.pars_window)
        self.pars_pic.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pars_pic.hide()


        self.inv_but = QPushButton(self)
        self.inv_but.setText("\n\n\n\nИнвайтинг")
        # self.pars_but.setAlignment(Qt.AlignCenter)
        self.inv_but.resize(300, 300)
        self.inv_but.setFont(QFont("Arial", 21))
        self.inv_but.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,
            blurRadius=0.0,
            color=QtGui.QColor(153, 167, 176),
            offset=QtCore.QPointF(5.0, 5.0)))

        self.inv_but.setStyleSheet('''
        QPushButton {background-color: #c7d0d9;
                    color: black;
                    border: 2px solid rgb(144, 153, 162);
                                        }''')
        self.inv_but.move(420, 150)
        self.inv_but.clicked.connect(self.inv_window)
        self.inv_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.inv_but.hide()

        self.inv_pic = PicClick(self)
        self.inv_pic.setPixmap(QPixmap('inv.png'))
        self.inv_pic.resize(150, 150)
        self.inv_pic.move(500, 189)
        self.inv_pic.clicked.connect(self.inv_window)
        self.inv_pic.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.inv_pic.hide()

        self.mail_but = QPushButton(self)
        self.mail_but.setText("\n\n\n\nРассылка")
        self.mail_but.resize(300, 300)
        self.mail_but.setFont(QFont("Arial", 21))
        self.mail_but.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,
            blurRadius=0.0,
            color=QtGui.QColor(153, 167, 176),
            offset=QtCore.QPointF(5.0, 5.0)))

        self.mail_but.setStyleSheet('''
        QPushButton {background-color: #c7d0d9;
                    color: black;
                    border: 2px solid rgb(144, 153, 162);
                                        }''')
        self.mail_but.move(770, 150)
        self.mail_but.clicked.connect(self.mail_window)
        self.mail_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.mail_but.hide()

        self.mail_pic = PicClick(self)
        self.mail_pic.setPixmap(QPixmap('mail.png'))
        self.mail_pic.clicked.connect(self.mail_window)
        self.mail_pic.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.mail_pic.resize(150, 150)
        self.mail_pic.move(850, 189)
        self.mail_pic.hide()

        self.instr_button = QPushButton(self)
        self.instr_button.setText("Инструкция")
        self.instr_button.resize(300, 90)
        self.instr_button.setFont(QFont("Arial", 20))
        self.instr_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,
            blurRadius=0.0,
            color=QtGui.QColor(153, 167, 176),
            offset=QtCore.QPointF(5.0, 5.0)))

        self.instr_button.setStyleSheet('''
        QPushButton {background-color: #c7d0d9;
                    color: black;
                    border: 2px solid rgb(144, 153, 162);
                                        }''')

        self.instr_button.move(20, 525)
        # self.instr_button.clicked.connect()
        self.instr_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.instr_button.hide()

        self.channel_text = QLabel(self)
        self.channel_text.setText("Канал Telegram:")
        self.channel_text.setAlignment(Qt.AlignCenter)
        self.channel_text.resize(400, 60)
        self.channel_text.setFont(QFont("Arial", 18))
        self.channel_text.move(750, 525)
        self.channel_text.hide()

        self.channel_link = QLabel(self)
        self.channel_link.setText('<a href="https://t.me/the_internetgroup">@the_internetgroup</a>')
        self.channel_link.setOpenExternalLinks(True)
        self.channel_link.setAlignment(Qt.AlignCenter)
        self.channel_link.resize(400, 60)
        self.channel_link.setFont(QFont("Arial", 18))
        self.channel_link.move(750, 565)
        self.channel_link.hide()

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

        self.group_link_text = QLabel(self)
        self.group_link_text.setText("Ссылка на группу")
        self.group_link_text.resize(400, 40)
        self.group_link_text.setAlignment(Qt.AlignCenter)
        self.group_link_text.setFont(QFont("Arial", 15))
        self.group_link_text.move(370, 130)
        self.group_link_text.hide()

        self.group_link_zone = QLineEdit(self)
        self.group_link_zone.setFont(QFont("Arial", 15))
        self.group_link_zone.move(370, 175)
        self.group_link_zone.setStyleSheet('''
        QLineEdit {border: 4px solid rgb(144, 153, 162);
                                        }''')
        self.group_link_zone.resize(400, 30)
        self.group_link_zone.hide()

        self.group_add_text = QLabel(self)
        self.group_add_text.setText("Сколько добавить всего")
        self.group_add_text.resize(400, 40)
        self.group_add_text.setAlignment(Qt.AlignCenter)
        self.group_add_text.setFont(QFont("Arial", 15))
        self.group_add_text.move(120, 220)
        self.group_add_text.hide()

        self.group_add_zone = QLineEdit(self)
        self.group_add_zone.setFont(QFont("Arial", 15))
        self.group_add_zone.move(180, 265)
        self.group_add_zone.setStyleSheet('''
        QLineEdit {border: 4px solid rgb(144, 153, 162);
                                        }''')
        self.group_add_zone.resize(400, 30)
        self.group_add_zone.hide()

        self.group_each_text = QLabel(self)
        self.group_each_text.setText("Сколько добавить c каждого аккаунта")
        self.group_each_text.resize(450, 40)
        self.group_each_text.setAlignment(Qt.AlignCenter)
        self.group_each_text.setFont(QFont("Arial", 15))
        self.group_each_text.move(175, 310)
        self.group_each_text.hide()

        self.group_each_zone = QLineEdit(self)
        self.group_each_zone.setFont(QFont("Arial", 15))
        self.group_each_zone.move(180, 355)
        self.group_each_zone.setStyleSheet('''
        QLineEdit {border: 4px solid rgb(144, 153, 162);
                                        }''')
        self.group_each_zone.resize(400, 30)
        self.group_each_zone.hide()

        self.group_pausemin_text = QLabel(self)
        self.group_pausemin_text.setText("Мин. пауза")
        self.group_pausemin_text.resize(450, 40)
        self.group_pausemin_text.setAlignment(Qt.AlignCenter)
        self.group_pausemin_text.setFont(QFont("Arial", 15))
        self.group_pausemin_text.move(25, 400)
        self.group_pausemin_text.hide()

        self.group_pausemin_zone = QLineEdit(self)
        self.group_pausemin_zone.setFont(QFont("Arial", 15))
        self.group_pausemin_zone.move(180, 445)
        self.group_pausemin_zone.setStyleSheet('''
        QLineEdit {border: 4px solid rgb(144, 153, 162);
                                        }''')
        self.group_pausemin_zone.resize(150, 30)
        self.group_pausemin_zone.hide()

        self.group_pausemax_zone = QLineEdit(self)
        self.group_pausemax_zone.setPlaceholderText("Макс. пауза")
        self.group_pausemax_zone.setFont(QFont(self.fontName, 20))
        self.group_pausemax_zone.move(450, 420)
        self.group_pausemax_zone.resize(150, 30)
        self.group_pausemax_zone.hide()

        self.start_but = QPushButton(self)
        self.start_but.setText("Запуск")
        self.start_but.resize(200, 60)
        self.start_but.setFont(QFont("Arial", 20))
        self.start_but.setStyleSheet('''
        QPushButton {background-color: #c7d0d9;
                    color: black;
                    border: 2px solid rgb(144, 153, 162);
                                        }''')
        self.start_but.move(470, 500)
        self.start_but.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,
            blurRadius=0.0,
            color=QtGui.QColor(153, 167, 176),
            offset=QtCore.QPointF(5.0, 5.0)))

        self.start_but.clicked.connect(lambda: self.start_working("inv"))
        self.start_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.start_but.hide()

        self.check_memb = QCheckBox(self)
        self.check_memb.setChecked(True)
        self.check_memb.move(510, 240)
        self.check_memb.resize(28, 27)
        self.check_memb.setStyleSheet('''
            QCheckBox {border: 4px solid rgb(144, 153, 162);
                                        }

            QCheckBox::indicator {
            width: 20px;
            height: 20px;}
        ''')
        self.check_memb.hide()

        self.check_memb_text = QLabel(self)
        self.check_memb_text.setText("Участники")
        self.check_memb_text.resize(150, 40)
        self.check_memb_text.setFont(QFont("Arial", 15))
        self.check_memb_text.move(370, 230)
        self.check_memb_text.hide()

        self.check_amd = QCheckBox(self)
        self.check_amd.setChecked(True)
        self.check_amd.move(510, 290)
        self.check_amd.resize(28, 27)
        self.check_amd.setStyleSheet('''
            QCheckBox {border: 4px solid rgb(144, 153, 162);
                                        }

            QCheckBox::indicator {
            width: 20px;
            height: 20px;}
        ''')
        self.check_amd.hide()

        self.check_adm_text = QLabel(self)
        self.check_adm_text.setText("Админы")
        self.check_adm_text.resize(150, 40)
        self.check_adm_text.setFont(QFont("Arial", 15))
        self.check_adm_text.move(370, 280)
        self.check_adm_text.hide()

        self.check_photo = QCheckBox(self)
        self.check_photo.move(780, 240)
        self.check_photo.resize(28, 27)
        self.check_photo.setStyleSheet('''
            QCheckBox {border: 4px solid rgb(144, 153, 162);
                                        }

            QCheckBox::indicator {
            width: 20px;
            height: 20px;}
        ''')
        self.check_photo.hide()

        self.check_photo_text = QLabel(self)
        self.check_photo_text.setText("С фото профиля")
        self.check_photo_text.resize(210, 40)
        self.check_photo_text.setFont(QFont("Arial", 15))
        self.check_photo_text.move(560, 230)
        self.check_photo_text.hide()

        self.check_chatting = QCheckBox(self)
        self.check_chatting.move(780, 290)
        self.check_chatting.resize(28, 27)
        self.check_chatting.setStyleSheet('''
            QCheckBox {border: 4px solid rgb(144, 153, 162);
                                        }

            QCheckBox::indicator {
            width: 20px;
            height: 20px;}
        ''')
        self.check_chatting.hide()

        self.check_chatting_text = QLabel(self)
        self.check_chatting_text.setText("Писали в чат")
        self.check_chatting_text.resize(190, 40)
        self.check_chatting_text.setFont(QFont("Arial", 15))
        self.check_chatting_text.move(560, 280)
        self.check_chatting_text.hide()

        self.active = QComboBox(self)
        self.active.resize(140, 30)
        self.active.setFont(QFont("Arial", 10))
        self.active.setStyleSheet('''
        QComboBox {border: 4px solid rgb(144, 153, 162);
                                        };
        ''')
        self.active.addItem("Все")
        self.active.addItem("Онлайн")
        self.active.addItem("Сутки")
        self.active.addItem("3 дня")
        self.active.addItem("Неделя")
        self.active.addItem("Месяц")
        self.active.move(500, 400)
        self.active.hide()

        self.active_text = QLabel(self)
        self.active_text.setText("Активность")
        self.active_text.setAlignment(Qt.AlignCenter)
        self.active_text.resize(400, 30)
        self.active_text.setFont(QFont("Arial", 15))
        self.active_text.move(370, 350)
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

        self.wind_title = QLabel(self)
        self.wind_title.setText("Парсинг")
        self.wind_title.setAlignment(Qt.AlignCenter)
        self.wind_title.resize(400, 60)
        self.wind_title.setFont(QFont("Arial", 25))
        self.wind_title.move(370, 50)
        self.wind_title.hide()

        self.main_start()

    def main_start(self):
        self.main_title.show()
        self.by_title.show()
        self.pars_but.show()
        self.pars_pic.show()
        self.inv_but.show()
        self.inv_pic.show()
        self.mail_but.show()
        self.mail_pic.show()
        self.instr_button.show()
        self.channel_text.show()
        self.channel_link.show()

        self.start_but.hide()
        self.back_but.hide()
        self.wind_title.hide()
        self.group_link_text.hide()
        self.group_link_zone.hide()
        self.check_memb_text.hide()
        self.check_memb.hide()
        self.check_amd.hide()
        self.check_adm_text.hide()
        self.check_photo.hide()
        self.check_photo_text.hide()
        self.check_chatting_text.hide()
        self.check_chatting.hide()
        self.active.hide()
        self.active_text.hide()

        self.group_add_zone.hide()
        self.group_add_text.hide()
        self.group_each_text.hide()
        self.group_each_zone.hide()
        self.group_pausemin_text.hide()
        self.group_pausemin_zone.hide()
        '''

        self.log_win.hide()
        self.pointer1.show()
        self.pointer2.show()
        self.pointer3.show()

        self.log_title.hide()

        self.group_link_zone.hide()
        self.group_add_zone.hide()
        self.group_each_zone.hide()
        self.group_pausemin_zone.hide()
        self.group_pausemax_zone.hide()

        self.check_memb.hide()
        
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
        '''

    def pars_window(self):
        self.pars_but.hide()
        self.pars_pic.hide()
        self.inv_but.hide()
        self.inv_pic.hide()
        self.mail_but.hide()
        self.mail_pic.hide()
        self.main_title.hide()
        self.by_title.hide()
        self.instr_button.hide()
        self.channel_text.hide()
        self.channel_link.hide()

        self.back_but.show()
        self.start_but.clicked.disconnect()
        self.start_but.clicked.connect(lambda: self.start_working("pars"))
        self.start_but.show()

        self.wind_title.setText("Парсинг")
        self.wind_title.show()

        self.group_link_text.move(370, 130)
        self.group_link_text.show()

        self.group_link_zone.move(370, 175)
        self.group_link_zone.show()

        self.check_memb_text.show()
        self.check_memb.show()
        self.check_amd.show()
        self.check_adm_text.show()
        self.check_photo.show()
        self.check_photo_text.show()
        self.check_chatting_text.show()
        self.check_chatting.show()
        self.active.show()
        self.active_text.show()

        '''
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
        '''

    def inv_window(self):
        self.pars_but.hide()
        self.pars_pic.hide()
        self.inv_but.hide()
        self.inv_pic.hide()
        self.mail_but.hide()
        self.mail_pic.hide()
        self.main_title.hide()
        self.by_title.hide()
        self.instr_button.hide()
        self.channel_text.hide()
        self.channel_link.hide()

        self.back_but.show()
        self.start_but.clicked.disconnect()
        self.start_but.clicked.connect(lambda: self.start_working("inv"))
        self.start_but.show()

        self.wind_title.setText("Инвайтинг")
        self.wind_title.show()

        self.group_link_text.move(80, 130)
        self.group_link_text.show()

        self.group_link_zone.move(180, 175)
        self.group_link_zone.show()

        self.group_add_text.show()
        self.group_add_zone.show()
        self.group_each_text.show()
        self.group_each_zone.show()
        self.group_pausemin_text.show()
        self.group_pausemin_zone.show()

        '''
        self.log_win.move(700, 240)
        self.log_win.show()
        self.log_title.move(700, 220)
        self.log_title.show()
        self.group_link_zone.show()
        self.group_add_zone.show()
        self.group_each_zone.show()
        self.group_pausemin_zone.show()
        self.group_pausemax_zone.show()
        '''

    def mail_window(self):
        self.pars_but.hide()
        self.pars_pic.hide()
        self.inv_but.hide()
        self.inv_pic.hide()
        self.mail_but.hide()
        self.mail_pic.hide()
        self.main_title.hide()
        self.by_title.hide()
        self.instr_button.hide()
        self.channel_text.hide()
        self.channel_link.hide()

        self.back_but.show()
        self.start_but.clicked.disconnect()
        self.start_but.clicked.connect(lambda: self.start_working("mail"))
        self.start_but.show()

        '''
        self.mes_zone.show()
        self.mes_title.show()
        self.mes_total.show()
        self.mes_each.show()
        self.mes_pause.show()

        self.log_title.move(700, 20)
        self.log_title.show()
        self.log_win.move(700, 40)
        self.log_win.show()
        '''

    def start_working(self, param):
        print(param)


app = QApplication(sys.argv)
mw = MainWindow()

mw.show()
sys.exit(app.exec_())
