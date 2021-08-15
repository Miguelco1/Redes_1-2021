# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'redes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#https://realpython.com/python-sockets/

from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import sys
import re
from datetime import datetime
import socket
import sys
import time
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.log_text=""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 594)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(690, 160, 81, 20))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(690, 190, 81, 20))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(690, 220, 81, 20))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(690, 250, 81, 20))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(690, 280, 81, 20))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(690, 310, 81, 20))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(25, 140, 651, 331))
        self.textBrowser.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.textBrowser.setObjectName("textBrowser")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 500, 651, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(690, 500, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 21, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 15, 55, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 10, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(680, 140, 171, 261))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_8.setGeometry(QtCore.QRect(10, 230, 81, 20))
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_7.setGeometry(QtCore.QRect(10, 200, 81, 20))
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 400, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 10, 221, 31))
        self.textBrowser_2.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(340, 10, 151, 31))
        self.textBrowser_3.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 55, 31))
        self.label_3.setObjectName("label_3")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(50, 50, 221, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.groupBox.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.checkbox_aux=[]
        self.checkbox_aux.append(self.checkBox)
        self.checkbox_aux.append(self.checkBox_2)
        self.checkbox_aux.append(self.checkBox_3)
        self.checkbox_aux.append(self.checkBox_4)
        self.checkbox_aux.append(self.checkBox_5)
        self.checkbox_aux.append(self.checkBox_6)
        self.checkbox_aux.append(self.checkBox_7)
        self.checkbox_aux.append(self.checkBox_8)
        self.textBrowser.raise_()
        self.plainTextEdit.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser_3.raise_()
        self.label_3.raise_()
        self.plainTextEdit_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 859, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuClient = QtWidgets.QMenu(self.menuBar)
        self.menuClient.setObjectName("menuClient")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuClient.menuAction())
        self.retranslateUi(MainWindow)  
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.sendMsg)
        self.pushButton_2.clicked.connect(self.connect_to_server)
        self.checkBox.stateChanged.connect(self.checkBoxChangedAction)
        self.pushButton_3.clicked.connect(self.check_all)
        self.dis_checkboxes()
        self.pushButton.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.names_online=[]
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "IP"))
        self.label_2.setText(_translate("MainWindow", "PORT"))
        self.pushButton_2.setText(_translate("MainWindow", "CONNECT"))
        self.groupBox.setTitle(_translate("MainWindow", "ONLINE"))
        self.pushButton_3.setText(_translate("MainWindow", "Todos"))
        self.label_3.setText(_translate("MainWindow", "Nick"))
        self.menuClient.setTitle(_translate("MainWindow", "Client"))


    def sendMsg(self):
        msg_send=bytearray(self.plainTextEdit.toPlainText(),'utf-8')
        self.plainTextEdit.clear()
        self.check_dest()
        opcode=[2,self.dest] 
        array=bytearray(opcode)
        msg_send=array+msg_send
        self.sock.sendall(msg_send)

    def check_all(self):
        if (self.pushButton_3.text() == "Todos"):
            for aux in self.checkbox_aux:         
                if (aux.isEnabled()):
                    aux.setChecked(True)
            self.pushButton_3.setText("Nenhum")
        elif (self.pushButton_3.text() == "Nenhum"):
            for aux in self.checkbox_aux:         
                if (aux.isEnabled()):
                    aux.setChecked(False)
            self.pushButton_3.setText("Todos")

    def connect_to_server(self):
        if (self.pushButton_2.text() == "CONNECT"):
            if (self.plainTextEdit_2.toPlainText()==''):
                self.textBrowser.setText("Por favor escolher nome de usuario antes de logar")
                return
 
            self.pushButton.setEnabled(True)
            self.pushButton_3.setEnabled(True)

            self.server_address = ('127.0.0.1', 5015)
            print('connecting to {} port {}'.format(*self.server_address))
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.server_address)
            self.nick_name=self.plainTextEdit_2.toPlainText()
            opcode=[1] 
            array=bytearray(opcode)
            msg_send=array+bytearray(self.nick_name,'utf-8')
            self.sock.sendall(msg_send)

            self.worker=Worker()
            self.worker.set_sock(self.sock)
            self.worker.start()
            self.worker.update_data.connect(self.evt_update_data)
            ip_add,port=self.sock.getsockname()
            self.textBrowser_2.setText(ip_add)
            self.textBrowser_3.setText(str(port))
            self.pushButton_2.setText("DISCONNECT")
        else:
            self.pushButton.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.worker.set_connect(0)
            msg="STATUS ---> Desconectado"
            self.log_text=self.log_text+"\n"+msg
            self.textBrowser.setText(self.log_text)
            self.sock.close()
            self.textBrowser_2.setText("")
            self.textBrowser_3.setText("")
            self.plainTextEdit_2.setReadOnly(False)
            self.dis_checkboxes()
            self.pushButton_2.setText("CONNECT")

    def evt_update_data(self,val):
        data_aux=val.split(bytes([0]))
        for data in data_aux:
            if data==b"":
                continue
            opcode=data[0]
            if opcode==1:
                self.update_name(int(data[1]))


            if opcode==2:                            
                decode_data=data[1:].decode("utf-8", "ignore")
                self.log_text=self.log_text+"\n"+decode_data
                self.textBrowser.setText(self.log_text)

            if opcode==3:  
                self.names_online=[]                          
                decode_data=data[1:].split()
                for i in range(0,len(decode_data),2):
                    count=int.from_bytes(decode_data[i],"big")
                    onlines={"name":decode_data[i+1].decode("utf-8", "ignore"),"count":count}
                    if(decode_data[i+1].decode("utf-8"))==self.nick_name:   
                        self.count_number=count
                    self.names_online.append(onlines)
                    self.update_checkboxes()

            if opcode==4:                            
                decode_data=data[1:].split()
                count=int.from_bytes(decode_data[0],"big")
                onlines={"name":decode_data[1].decode("utf-8", "ignore"),"count":count}
                self.names_online.append(onlines)
                self.update_checkboxes()


            if opcode==5:                            
                self.pushButton.setEnabled(False)
                self.pushButton_3.setEnabled(False)
                self.worker.set_connect(0)
                msg="STATUS ---> Desconectado"
                self.log_text=self.log_text+"\n"+msg
                self.textBrowser.setText(self.log_text)
                self.sock.close()
                self.textBrowser_2.setText("")
                self.textBrowser_3.setText("")
                self.plainTextEdit_2.setReadOnly(False)
                self.dis_checkboxes()
                self.pushButton_2.setText("CONNECT")

    def update_name(self,val):
        if val==1:
            msg="STATUS ---> Erro de conexao usario invalido ou indisponivel"
            self.log_text=self.log_text+"\n"+msg
            self.textBrowser.setText(self.log_text)

            self.worker.set_connect(0)
            self.sock.close()
            self.pushButton_2.setText("CONNECT")
        else:
            self.plainTextEdit_2.setReadOnly(True)
            msg="STATUS ---> Conectado com Sucesso"
            self.log_text=self.log_text+"\n"+msg
            self.textBrowser.setText(self.log_text)


    def dis_checkboxes(self):
        for aux in self.checkbox_aux:         
            aux.setChecked(False)
            aux.setEnabled(False)
            aux.setHidden(True)

    def check_dest(self):
        self.dest=self.count_number
        for aux in self.checkbox_aux:         
            if (aux.isEnabled()):
                if(aux.isChecked()):
                    sender= next((item for item in self.names_online if item["name"] == aux.text()), False)
                    self.dest=self.dest+sender.get("count")



    def update_checkboxes(self):
        i=0
        for aux in self.checkbox_aux:         
            try:
                if(self.names_online[i].get("name")==self.nick_name):
                    i=i+1
                aux.setEnabled(True)
                aux.setHidden(False)
                aux.setText(self.names_online[i].get("name"))
                i=i+1
            except:
                aux.setChecked(False)
                aux.setEnabled(False)
                aux.setHidden(True)

    def checkBoxChangedAction(self, state):
        #self.pushButton.setHidden(True)
        if (QtCore.Qt.Checked == state):
            pass
        else:
            pass

class Worker(QThread):
    update_data = QtCore.pyqtSignal(bytes)
    def set_sock(self,sock):
       self.s=sock
    def set_connect(self,connect):
       self.connected=connect

    def run(self):
        self.connected=1
        while True:
            try:            
                if self.connected==1:
                    try:
                        data = self.s.recv(2048)

                    except:
                        data=-1
                        
                    if(data==-1):
                        self.s.close()
                        break
                    elif data:
                        #Transforma a mensagem de binario para string
                        try:
                            self.update_data.emit(data)

                        except:
                            if (data==-1):
                                break
                            print("Mensagem com Formato invalido recebida")
                            break
                        



                    
            except:
                pass 
            else:
                pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())