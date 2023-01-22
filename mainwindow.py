# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_form import Ui_MainWindow
from PySide6.QtSql import QSqlDatabase
import sys
from PySide6.QtUiTools import QUiLoader

#QSqlDatabase.addDatabase(
#   driver, connectionName=QSqlDatabase.defaultConnection
#)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        ui = loader.load("form.ui", self)

        #DATABASWE CONNECTION
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("contacts.sqlite")
        # Open the connection
        con.open()

        # ACCESSING QT OBJECTS FROM UI
        self.spinBox = ui.spinBox
        self.tableWidget = ui.tableWidget
        self.spinBox_2 = ui.spinBox_2
        self.tableWidget_2 = ui.tableWidget_2


        ui.pushButton.clicked.connect(self.createProject)
        ui.spinBox.valueChanged.connect(self.spinUp)
        ui.spinBox_2.valueChanged.connect(self.levelsData)
        ui.show()
        # SHOW MAIN WINDOW

    def createProject(self):
        print('buttonPress')
        dialog = QFileDialog(self)
        dialog.getOpenFileName()

    ####FOR THE FACTORS
    def spinUp(self):
        self.tableWidget.insertRow(self.spinBox.value())
        add_one = int(self.spinBox.value()) + 1
        self.tableWidget.setItem(self.spinBox.value(), 0, QTableWidgetItem(str(add_one)))
        self.tableWidget.setItem(self.spinBox.value(), 1, QTableWidgetItem("Factor" + " " + str(add_one)))
        self.tableWidget.setItem(self.spinBox.value(), 2, QTableWidgetItem("Steady"))

    ####FOR THE LEVELS
    def levelsData(self):
        #min_num = 2
        #max_num = 10
        #default_num = 2
        #user_input = user_input >= min_num or user_input <= max_num (default : {default_num})
        self.tableWidget_2.insertRow(self.spinBox_2.value())
        add_one = int(self.spinBox_2.value()) + 1
        self.tableWidget_2.setItem(self.spinBox_2.value(), 0, QTableWidgetItem(str(add_one)))
        self.tableWidget_2.setItem(self.spinBox_2.value(), 1, QTableWidgetItem("Factor" + " " + str(add_one)))
        self.tableWidget_2.setItem(self.spinBox_2.value(), 2, QTableWidgetItem(str(2)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    app.exec()


