# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1264, 644)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(20, 20))
        self.pushButton_3.setMaximumSize(QSize(114, 87))
        self.pushButton_3.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u"../1111/IMAGES/image 21.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(20, 20))
        self.pushButton.setMaximumSize(QSize(84, 62))
        self.pushButton.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u"../1111/IMAGES/Vector (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(20, 20))
        self.pushButton_4.setMaximumSize(QSize(84, 62))
        self.pushButton_4.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u"../1111/IMAGES/Vector (4).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(20, 20))
        self.pushButton_2.setMaximumSize(QSize(160, 62))
        self.pushButton_2.setStyleSheet(u"border:none;")
        icon3 = QIcon()
        icon3.addFile(u"../1111/IMAGES/3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_19 = QPushButton(self.frame_5)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(20, 20))
        self.pushButton_19.setMaximumSize(QSize(148, 62))
        self.pushButton_19.setStyleSheet(u"border:none;")
        icon4 = QIcon()
        icon4.addFile(u"../1111/IMAGES/Group.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_19.setIcon(icon4)
        self.pushButton_19.setIconSize(QSize(31, 31))

        self.horizontalLayout_2.addWidget(self.pushButton_19)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(20, 20))
        self.pushButton_5.setMaximumSize(QSize(148, 62))
        self.pushButton_5.setStyleSheet(u"border:none;")
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(31, 31))

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.horizontalLayout.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"border:none;")
        icon5 = QIcon()
        icon5.addFile(u"../1111/IMAGES/icons8-subtract-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u"../1111/IMAGES/icons8-maximize-button-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u"../1111/IMAGES/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.pushButton_8)


        self.horizontalLayout.addWidget(self.frame_6, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(40, 0))
        self.frame_7.setMaximumSize(QSize(348, 16777215))
        self.frame_7.setStyleSheet(u"background-color: rgb(149, 149, 149);\n"
"border: none;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 20))
        self.frame_16.setMaximumSize(QSize(16777215, 30))
        self.frame_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_16)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_18)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_18)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setStyleSheet(u"border:none;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_13)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(12, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_13)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon8 = QIcon()
        icon8.addFile(u"../1111/IMAGES/image 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon8)

        self.verticalLayout_5.addWidget(self.pushButton_9)


        self.verticalLayout_4.addWidget(self.frame_13, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.frame_12)


        self.verticalLayout_7.addWidget(self.frame_18, 0, Qt.AlignVCenter)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_17)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 14, -1, -1)
        self.tabWidget = QTabWidget(self.frame_17)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.Levels = QWidget()
        self.Levels.setObjectName(u"Levels")
        self.verticalLayout_8 = QVBoxLayout(self.Levels)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_15 = QFrame(self.Levels)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 20))
        self.frame_19.setMaximumSize(QSize(16777215, 29))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_21)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_21)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)

        self.verticalLayout_12.addWidget(self.label)


        self.horizontalLayout_5.addWidget(self.frame_21, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_22)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.spinBox = QSpinBox(self.frame_22)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(15)

        self.verticalLayout_13.addWidget(self.spinBox)


        self.horizontalLayout_5.addWidget(self.frame_22, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tableWidget = QTableWidget(self.frame_20)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 20))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet(u"border: 1px solid;")
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(2)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(92)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_14.addWidget(self.tableWidget)

        self.frame_48 = QFrame(self.frame_20)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_49)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_49)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"background-color: rgb(78, 208, 94);\n"
"color:rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border-radius: 5px;")

        self.verticalLayout_39.addWidget(self.pushButton_10, 0, Qt.AlignLeft)


        self.horizontalLayout_12.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_48)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_50)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.pushButton_20 = QPushButton(self.frame_50)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setStyleSheet(u"background-color: rgb(78, 208, 94);\n"
"color:rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border-radius: 5px;")

        self.verticalLayout_40.addWidget(self.pushButton_20, 0, Qt.AlignRight)


        self.horizontalLayout_12.addWidget(self.frame_50)


        self.verticalLayout_14.addWidget(self.frame_48)


        self.verticalLayout_10.addWidget(self.frame_20)


        self.verticalLayout_8.addWidget(self.frame_15)

        self.tabWidget.addTab(self.Levels, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_18 = QVBoxLayout(self.tab_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_23 = QFrame(self.tab_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_23)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 20))
        self.frame_24.setMaximumSize(QSize(16777215, 29))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_25)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_25)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_15.addWidget(self.label_2)


        self.horizontalLayout_6.addWidget(self.frame_25, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_26)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.spinBox_2 = QSpinBox(self.frame_26)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimum(1)

        self.verticalLayout_16.addWidget(self.spinBox_2)


        self.horizontalLayout_6.addWidget(self.frame_26, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.frame_24)

        self.frame_27 = QFrame(self.frame_23)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_27)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.tableWidget_2 = QTableWidget(self.frame_27)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        if (self.tableWidget_2.rowCount() < 2):
            self.tableWidget_2.setRowCount(2)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem21)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(0, 20))
        self.tableWidget_2.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_2.setStyleSheet(u"border: 1px solid;")
        self.tableWidget_2.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(92)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_17.addWidget(self.tableWidget_2)

        self.frame_51 = QFrame(self.frame_27)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_52)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.frame_52)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"background-color: rgb(78, 208, 94);\n"
"color:rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border-radius: 5px;")

        self.verticalLayout_41.addWidget(self.pushButton_11, 0, Qt.AlignLeft)


        self.horizontalLayout_13.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_51)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_53)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.pushButton_21 = QPushButton(self.frame_53)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setStyleSheet(u"background-color: rgb(78, 208, 94);\n"
"color:rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border-radius: 5px;")

        self.verticalLayout_42.addWidget(self.pushButton_21, 0, Qt.AlignRight)


        self.horizontalLayout_13.addWidget(self.frame_53)


        self.verticalLayout_17.addWidget(self.frame_51)


        self.verticalLayout_11.addWidget(self.frame_27)


        self.verticalLayout_18.addWidget(self.frame_23)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_24.addWidget(self.tabWidget)


        self.verticalLayout_6.addWidget(self.frame_17)


        self.verticalLayout_3.addWidget(self.frame_11)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(40, 0))
        self.frame_8.setMaximumSize(QSize(820, 16777215))
        self.frame_8.setStyleSheet(u"background-color: rgb(149, 149, 149);\n"
"border: none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 20))
        self.frame_10.setMaximumSize(QSize(16777215, 20))
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_10)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_10)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(12, 0, 12, 0)
        self.frame_29 = QFrame(self.widget)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_29)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.pushButton_12 = QPushButton(self.frame_29)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon9 = QIcon()
        icon9.addFile(u"../1111/IMAGES/image 2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon9)

        self.verticalLayout_21.addWidget(self.pushButton_12)


        self.horizontalLayout_7.addWidget(self.frame_29, 0, Qt.AlignLeft)

        self.frame_30 = QFrame(self.widget)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_30)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3, 0, Qt.AlignRight)

        self.comboBox = QComboBox(self.frame_30)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(220, 220, 220);")

        self.horizontalLayout_8.addWidget(self.comboBox)


        self.horizontalLayout_7.addWidget(self.frame_30)


        self.verticalLayout_20.addWidget(self.widget, 0, Qt.AlignVCenter)


        self.verticalLayout_19.addWidget(self.frame_10)

        self.frame_28 = QFrame(self.frame_8)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 40))
        self.frame_28.setMaximumSize(QSize(16777215, 16777215))
        self.frame_28.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_28)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_28)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(12, 1, 12, 0)
        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_33)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_33)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_23.addWidget(self.label_4)


        self.horizontalLayout_9.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_31)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_34)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border:  1px solid;")

        self.horizontalLayout_10.addWidget(self.lineEdit)

        self.pushButton_13 = QPushButton(self.frame_34)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"background-color: rgb(78, 208, 94);\n"
"color:rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border-radius:5px")

        self.horizontalLayout_10.addWidget(self.pushButton_13)


        self.horizontalLayout_9.addWidget(self.frame_34)


        self.verticalLayout_22.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_28)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_32)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_32)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_39)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(12, 0, 0, 4)
        self.pushButton_15 = QPushButton(self.frame_39)
        self.pushButton_15.setObjectName(u"pushButton_15")
        icon10 = QIcon()
        icon10.addFile(u"../1111/IMAGES/image 4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon10)

        self.verticalLayout_30.addWidget(self.pushButton_15, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_29.addWidget(self.frame_39, 0, Qt.AlignBottom)


        self.verticalLayout_22.addWidget(self.frame_32)


        self.verticalLayout_19.addWidget(self.frame_28)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 40))
        self.frame_14.setMaximumSize(QSize(16777215, 324))
        self.frame_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_14)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.tableWidget_3 = QTableWidget(self.frame_14)
        if (self.tableWidget_3.columnCount() < 3):
            self.tableWidget_3.setColumnCount(3)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        if (self.tableWidget_3.rowCount() < 4):
            self.tableWidget_3.setRowCount(4)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem29)
        icon11 = QIcon()
        icon11.addFile(u"../1111/IMAGES/icons8-close-window-50.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setIcon(icon11);
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setIcon(icon11);
        self.tableWidget_3.setItem(1, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setIcon(icon11);
        self.tableWidget_3.setItem(2, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setIcon(icon6);
        self.tableWidget_3.setItem(3, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 2, __qtablewidgetitem40)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMinimumSize(QSize(0, 40))
        self.tableWidget_3.setMaximumSize(QSize(16777215, 125))
        self.tableWidget_3.setStyleSheet(u"border: 1px solid;")
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(172)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)

        self.verticalLayout_31.addWidget(self.tableWidget_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_3)

        self.pushButton_16 = QPushButton(self.frame_14)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"background-color: rgb(78, 208, 94);\n"
"color:rgb(255, 255, 255);\n"
"padding: 5px;\n"
"border-radius:5px")

        self.verticalLayout_31.addWidget(self.pushButton_16, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.frame_14)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(40, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setStyleSheet(u"background-color: rgb(149, 149, 149);\n"
"border: none;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_9)
        self.verticalLayout_25.setSpacing(2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_9)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 20))
        self.frame_35.setMaximumSize(QSize(16777215, 20))
        self.frame_35.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_35)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(12, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_38)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.frame_38)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon12 = QIcon()
        icon12.addFile(u"../1111/IMAGES/image 7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon12)

        self.verticalLayout_28.addWidget(self.pushButton_14)


        self.verticalLayout_27.addWidget(self.frame_38, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_26.addWidget(self.frame_37)


        self.verticalLayout_25.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_9)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_36)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 280))
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setSpacing(1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_40 = QFrame(self.frame_3)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(40, 0))
        self.frame_40.setMaximumSize(QSize(1169, 16777215))
        self.frame_40.setStyleSheet(u"background-color: rgb(149, 149, 149);\n"
"border: none;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_40)
        self.verticalLayout_32.setSpacing(2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_40)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 20))
        self.frame_42.setMaximumSize(QSize(16777215, 20))
        self.frame_42.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_42)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_44)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(12, 0, 0, 0)
        self.pushButton_17 = QPushButton(self.frame_44)
        self.pushButton_17.setObjectName(u"pushButton_17")
        icon13 = QIcon()
        icon13.addFile(u"../1111/IMAGES/icons8-health-data-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon13)

        self.verticalLayout_34.addWidget(self.pushButton_17)


        self.verticalLayout_33.addWidget(self.frame_44, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_32.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_40)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_43)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.tableWidget_4 = QTableWidget(self.frame_43)
        if (self.tableWidget_4.columnCount() < 9):
            self.tableWidget_4.setColumnCount(9)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setBackground(QColor(0, 0, 0));
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem49)
        if (self.tableWidget_4.rowCount() < 11):
            self.tableWidget_4.setRowCount(11)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(4, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(5, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(6, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(7, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(8, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(9, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(10, __qtablewidgetitem60)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setStyleSheet(u"border:1px solid;\n"
"background-color: rgb(192, 192, 192);")
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_38.addWidget(self.tableWidget_4)


        self.verticalLayout_32.addWidget(self.frame_43)


        self.horizontalLayout_11.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_3)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"background-color: rgb(149, 149, 149);\n"
"border: none;")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_41)
        self.verticalLayout_35.setSpacing(2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.frame_41)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 20))
        self.frame_45.setMaximumSize(QSize(16777215, 20))
        self.frame_45.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_45)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_45)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_47)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(12, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.frame_47)
        self.pushButton_18.setObjectName(u"pushButton_18")
        icon14 = QIcon()
        icon14.addFile(u"../1111/IMAGES/error.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon14)

        self.verticalLayout_37.addWidget(self.pushButton_18)


        self.verticalLayout_36.addWidget(self.frame_47, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_35.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_41)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)

        self.verticalLayout_35.addWidget(self.frame_46)


        self.horizontalLayout_11.addWidget(self.frame_41)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Twidy", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Data Preparation", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Post Processing", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Parametric Models", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Setup of Factors", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"S/N", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Factors", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Type", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"T @ vent1", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Steady", None));
        ___qtablewidgetitem6 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem7 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"T @ door1", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Fluctuating", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Design Models", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Levels), QCoreApplication.translate("MainWindow", u"Factors", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Setup of Levels", None))
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"S/N", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Factors", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Levels", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem12 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem13 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"T @ vent1", None));
        ___qtablewidgetitem14 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem15 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem16 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"T @ door1", None));
        ___qtablewidgetitem17 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"2", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Design Models", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Levels", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"CAE Simulation Data Sets", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Simulation Package", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Simulation Working Directory", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"CAE Parameters", None))
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem21 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem23 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem24 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"4", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem25 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Pressure", None));
        ___qtablewidgetitem26 = self.tableWidget_3.item(0, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"View", None));
        ___qtablewidgetitem27 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Velocity Magnitude", None));
        ___qtablewidgetitem28 = self.tableWidget_3.item(1, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"View", None));
        ___qtablewidgetitem29 = self.tableWidget_3.item(2, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Total Temperature", None));
        ___qtablewidgetitem30 = self.tableWidget_3.item(2, 2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"View", None));
        ___qtablewidgetitem31 = self.tableWidget_3.item(3, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Turbulent Kinetic Energy", None));
        ___qtablewidgetitem32 = self.tableWidget_3.item(3, 2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"View", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Reconstruct", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Model Data Sets", None))
        ___qtablewidgetitem33 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"C1", None));
        ___qtablewidgetitem34 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"C2", None));
        ___qtablewidgetitem35 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"C3", None));
        ___qtablewidgetitem36 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"C4", None));
        ___qtablewidgetitem37 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"C5", None));
        ___qtablewidgetitem38 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"C6", None));
        ___qtablewidgetitem39 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"C7", None));
        ___qtablewidgetitem40 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"C8", None));
        ___qtablewidgetitem41 = self.tableWidget_4.horizontalHeaderItem(8)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"C10", None));
        ___qtablewidgetitem42 = self.tableWidget_4.verticalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem43 = self.tableWidget_4.verticalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem44 = self.tableWidget_4.verticalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem45 = self.tableWidget_4.verticalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem46 = self.tableWidget_4.verticalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem47 = self.tableWidget_4.verticalHeaderItem(5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem48 = self.tableWidget_4.verticalHeaderItem(6)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem49 = self.tableWidget_4.verticalHeaderItem(7)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem50 = self.tableWidget_4.verticalHeaderItem(8)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem51 = self.tableWidget_4.verticalHeaderItem(9)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem52 = self.tableWidget_4.verticalHeaderItem(10)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"12", None));
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Warnings and Errors", None))
    # retranslateUi

