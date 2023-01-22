# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_form import Ui_MainWindow
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel
import sqlite3

conn = sqlite3.connect('rapid.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE if not exists todo_list(serial_no  INTEGER, factors TEXT, type TEXT)
          ''')
conn.commit()
conn.close()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        ui = loader.load("form.ui", self)

        # ACCESSING QT OBJECTS FROM UI
        self.spinBox = ui.spinBox
        self.tableWidget = ui.tableWidget
        self.spinBox_2 = ui.spinBox_2
        self.tableWidget_2 = ui.tableWidget_2
        self.tableWidget_4 = ui.tableWidget_4
#        self.grab_all()
        self.dim_4()
        self.dim_5()
        self.dim_6()
        self.dim_7()
        self.dim_8()
        self.dim_9()
        self.dim_10()
        self.dim_11()
        self.dim_12()
        self.dim_13()
        self.dim_14()


        ui.pushButton.clicked.connect(self.createProject)
        ui.spinBox.valueChanged.connect(self.spinUp)
        ui.spinBox_2.valueChanged.connect(self.levelsData)
        ui.pushButton_10.clicked.connect(self.save_it)
        ui.show()
        # SHOW MAIN WINDOW

    def createProject(self):
        print('buttonPress')
        dialog = QFileDialog(self)
        dialog.getOpenFileName()

    def dim_3(self):
        nodes = []
        for k in [0, 1]:
            if k == 0:
                for j in [0, 1]:
                    if j == 0:
                        for i in [0, 1]:
                            nodes.append([i, j, k])
                    else:
                        for i in [1, 0]:
                            nodes.append([i, j, k])

            else:

                for i in [0, 1]:
                    if i == 0:
                        for j in [1, 0]:
                            nodes.append([i, j, k])
                    else:
                        for j in [0, 1]:
                            nodes.append([i, j, k])
                table_row = 0
                for record in nodes:
                    self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                    self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                    self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                    table_row += 1

    def dim_4(self):
        self.nodes = []
        for l in [0, 1]:
            if l == 0:
                for k in [0, 1]:
                    if k == 0:
                        for j in [0, 1]:
                            if j == 0:
                                for i in [0, 1]:
                                    self.nodes.append([i, j, k, l])
                            else:
                                for i in [1, 0]:
                                    self.nodes.append([i, j, k, l])

                else:

                    for i in [0, 1]:
                        if i == 0:
                            for j in [1, 0]:
                                self.nodes.append([i, j, k, l])
                        else:
                            for j in [0, 1]:
                                self.nodes.append([i, j, k, l])

            else:
                for j in [1, 0]:
                    if j == 1:
                        for k in [1, 0]:
                            if k== 1:
                                for i in [1, 0]:
                                    self.nodes.append([i, j, k, l])
                            else:
                                for i in [0, 1]:
                                    self.nodes.append([i, j, k, l])
                    else:
                        for i in [1, 0]:
                            if i== 1:
                                for k in [0, 1]:
                                    self.nodes.append([i, j, k, l])
                            else:
                                for k in [1, 0]:
                                    self.nodes.append([i, j, k, l])







    def dim_5(self):
        nodes_d = self.nodes
        print(nodes_d)
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_5 = [*first_set, *second_set]


    def dim_6(self):
        nodes_d = self.nodes_5
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes_5
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_6 = [*first_set, *second_set]

    def dim_7(self):
        nodes_d = self.nodes_6
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes_6
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_7 = [*first_set, *second_set]

    def dim_8(self):
        nodes_d = self.nodes_7
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes_7
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_8 = [*first_set, *second_set]

    def dim_9(self):
        nodes_d = self.nodes_8
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes_8
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_9 = [*first_set, *second_set]

    ###### 10D
    def dim_10(self):
        nodes_d = self.nodes_9
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes_9
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_10 = [*first_set, *second_set]

    ###### 11D
    def dim_11(self):
        nodes_d = self.nodes_10
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes_10
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_11 = [*first_set, *second_set]


    ###### 12D
    def dim_12(self):
        nodes_d = self.nodes_11
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes_11
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_12 = [*first_set, *second_set]

    ###### 13D
    def dim_13(self):
        nodes_d = self.nodes_12
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes_12
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_13 = [*first_set, *second_set]


    ###### 14D
    def dim_14(self):
        nodes_d = self.nodes_13
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes_13
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_14 = [*first_set, *second_set]


    ###### 15D
    def dim_15(self):
        nodes_d = self.nodes_14
        [nodes_d[n].extend([0]) for n in range(len(nodes_d))]
        first_set = nodes_d

        nodes_d = self.nodes_14
        [nodes_d[n].extend([1]) for n in range(len(nodes_d))]
        second_set = nodes_d

        self.nodes_15 = [*first_set, *second_set]

    def save_it(self):
        conn = sqlite3.connect('rapid.db')
        c = conn.cursor()
        c.execute('DELETE FROM todo_list;',)
        items = {}

        for index in range(self.tableWidget.rowCount()):
            items.update({
                "serial_no": self.tableWidget.item(index, 0),
                "factors": self.tableWidget.item(index, 1),
                "type": self.tableWidget.item(index, 2)
            })

            c.execute("INSERT INTO todo_list (serial_no, factors, type) VALUES (:serial_no, :factors, :type)",
                {
                    'serial_no': items.get('serial_no').text(),
                    'factors': items.get('factors').text(),
                    'type': items.get('type').text()
                }
            )

        conn.commit()
        conn.close()

        if self.spinBox.value() == 2:
            nodes = []
            for j in [0, 1]:
                if j == 0:
                    for i in [0, 1]:
                        nodes.append([i, j])
                else:
                    for i in [1, 0]:
                        nodes.append([i, j])

            table_row = 0
            for record in nodes:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                #self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                table_row += 1

        elif self.spinBox.value() == 3:
            self.dim_3()

        elif self.spinBox.value() == 4:
            self.dim_4()
            table_row = 0
            for record in self.nodes:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                table_row += 1
                
        elif self.spinBox.value() == 5:
            self.dim_5()
            table_row = 0
            for record in self.nodes_5:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                table_row += 1

        elif self.spinBox.value() == 6:
            self.dim_6()
            table_row = 0
            for record in self.nodes_6:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget_4.setItem(table_row, 5, QTableWidgetItem(str(record[5])))
                table_row += 1

        elif self.spinBox.value() == 7:
            self.dim_7()
            table_row = 0
            for record in self.nodes_7:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget_4.setItem(table_row, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget_4.setItem(table_row, 6, QTableWidgetItem(str(record[6])))
                table_row += 1

        elif self.spinBox.value() == 8:
            self.dim_8()
            table_row = 0
            for record in self.nodes_8:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget_4.setItem(table_row, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget_4.setItem(table_row, 6, QTableWidgetItem(str(record[6])))
                self.tableWidget_4.setItem(table_row, 7, QTableWidgetItem(str(record[7])))
                table_row += 1

        elif self.spinBox.value() == 9:
            self.dim_9()
            table_row = 0
            for record in self.nodes_9:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget_4.setItem(table_row, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget_4.setItem(table_row, 6, QTableWidgetItem(str(record[6])))
                self.tableWidget_4.setItem(table_row, 7, QTableWidgetItem(str(record[7])))
                self.tableWidget_4.setItem(table_row, 8, QTableWidgetItem(str(record[8])))
                table_row += 1

        elif self.spinBox.value() == 10:
            self.dim_10()
            table_row = 0
            for record in self.nodes_10:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget_4.setItem(table_row, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget_4.setItem(table_row, 6, QTableWidgetItem(str(record[6])))
                self.tableWidget_4.setItem(table_row, 7, QTableWidgetItem(str(record[7])))
                self.tableWidget_4.setItem(table_row, 8, QTableWidgetItem(str(record[8])))
                self.tableWidget_4.setItem(table_row, 9, QTableWidgetItem(str(record[9])))
                table_row += 1

        elif self.spinBox.value() == 11:
            self.dim_11()
            table_row = 0
            for record in self.nodes_11:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget_4.setItem(table_row, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget_4.setItem(table_row, 6, QTableWidgetItem(str(record[6])))
                self.tableWidget_4.setItem(table_row, 7, QTableWidgetItem(str(record[7])))
                self.tableWidget_4.setItem(table_row, 8, QTableWidgetItem(str(record[8])))
                self.tableWidget_4.setItem(table_row, 9, QTableWidgetItem(str(record[9])))
                self.tableWidget_4.setItem(table_row, 10, QTableWidgetItem(str(record[10])))
                table_row += 1

        elif self.spinBox.value() == 12:
            self.dim_12()
            table_row = 0
            for record in self.nodes_12:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget_4.setItem(table_row, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget_4.setItem(table_row, 6, QTableWidgetItem(str(record[6])))
                self.tableWidget_4.setItem(table_row, 7, QTableWidgetItem(str(record[7])))
                self.tableWidget_4.setItem(table_row, 8, QTableWidgetItem(str(record[8])))
                self.tableWidget_4.setItem(table_row, 9, QTableWidgetItem(str(record[9])))
                self.tableWidget_4.setItem(table_row, 10, QTableWidgetItem(str(record[10])))
                self.tableWidget_4.setItem(table_row, 11, QTableWidgetItem(str(record[11])))
                table_row += 1

        elif self.spinBox.value() == 13:
            self.dim_13()
            table_row = 0
            for record in self.nodes_13:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget_4.setItem(table_row, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget_4.setItem(table_row, 6, QTableWidgetItem(str(record[6])))
                self.tableWidget_4.setItem(table_row, 7, QTableWidgetItem(str(record[7])))
                self.tableWidget_4.setItem(table_row, 8, QTableWidgetItem(str(record[8])))
                self.tableWidget_4.setItem(table_row, 9, QTableWidgetItem(str(record[9])))
                self.tableWidget_4.setItem(table_row, 10, QTableWidgetItem(str(record[10])))
                self.tableWidget_4.setItem(table_row, 11, QTableWidgetItem(str(record[11])))
                self.tableWidget_4.setItem(table_row, 12, QTableWidgetItem(str(record[12])))
                table_row += 1

        elif self.spinBox.value() == 14:
            self.dim_14()
            table_row = 0
            for record in self.nodes_14:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget_4.setItem(table_row, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget_4.setItem(table_row, 6, QTableWidgetItem(str(record[6])))
                self.tableWidget_4.setItem(table_row, 7, QTableWidgetItem(str(record[7])))
                self.tableWidget_4.setItem(table_row, 8, QTableWidgetItem(str(record[8])))
                self.tableWidget_4.setItem(table_row, 9, QTableWidgetItem(str(record[9])))
                self.tableWidget_4.setItem(table_row, 10, QTableWidgetItem(str(record[10])))
                self.tableWidget_4.setItem(table_row, 11, QTableWidgetItem(str(record[11])))
                self.tableWidget_4.setItem(table_row, 12, QTableWidgetItem(str(record[12])))
                self.tableWidget_4.setItem(table_row, 13, QTableWidgetItem(str(record[13])))
                table_row += 1

        elif self.spinBox.value() == 15:
            self.dim_15()
            table_row = 0
            for record in self.nodes_15:
                self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
                self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
                self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
                self.tableWidget_4.setItem(table_row, 3, QTableWidgetItem(str(record[3])))
                self.tableWidget_4.setItem(table_row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget_4.setItem(table_row, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget_4.setItem(table_row, 6, QTableWidgetItem(str(record[6])))
                self.tableWidget_4.setItem(table_row, 7, QTableWidgetItem(str(record[7])))
                self.tableWidget_4.setItem(table_row, 8, QTableWidgetItem(str(record[8])))
                self.tableWidget_4.setItem(table_row, 9, QTableWidgetItem(str(record[9])))
                self.tableWidget_4.setItem(table_row, 10, QTableWidgetItem(str(record[10])))
                self.tableWidget_4.setItem(table_row, 11, QTableWidgetItem(str(record[11])))
                self.tableWidget_4.setItem(table_row, 12, QTableWidgetItem(str(record[12])))
                self.tableWidget_4.setItem(table_row, 13, QTableWidgetItem(str(record[13])))
                self.tableWidget_4.setItem(table_row, 14, QTableWidgetItem(str(record[14])))
                table_row += 1

        else:
            print("ERROR")


    def grab_all(self):
        conn = sqlite3.connect('rapid.db')
        c = conn.cursor()
        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()
        conn.commit()
        conn.close()

        table_row = 0
        for record in records:
            self.tableWidget_4.setItem(table_row, 0, QTableWidgetItem(str(record[0])))
            #self.tableWidget_4.setItem(table_row, 1, QTableWidgetItem(str(record[1])))
            #self.tableWidget_4.setItem(table_row, 2, QTableWidgetItem(str(record[2])))
            table_row += 1

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


