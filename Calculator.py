import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic


form_class = uic.loadUiType("Calculator.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)   
        
        self.btn_Math_Expression.clicked.connect(self.btn_clicked)
        self.btn_Graph.clicked.connect(self.btn_clicked)
        self.btn_Save.clicked.connect(self.btn_clicked)
        self.btn_Rad.clicked.connect(self.btn_clicked)
        self.btn_Deg.clicked.connect(self.btn_clicked)
        self.btn_Inv.clicked.connect(self.btn_clicked)
        self.btn_Ce.clicked.connect(self.btn_clicked)
        self.btn_Left_Brack.clicked.connect(self.btn_clicked)
        self.btn_Right_Brack.clicked.connect(self.btn_clicked)
        self.btn_Multipulication.clicked.connect(self.btn_clicked)
        self.btn_Sin.clicked.connect(self.btn_clicked)
        self.btn_Cos.clicked.connect(self.btn_clicked)
        self.btn_Tan.clicked.connect(self.btn_clicked)
        self.btn_7.clicked.connect(self.btn_clicked)
        self.btn_8.clicked.connect(self.btn_clicked)
        self.btn_9.clicked.connect(self.btn_clicked)
        self.btn_Div.clicked.connect(self.btn_clicked)
        self.btn_Factorial.clicked.connect(self.btn_clicked)
        self.btn_Ln.clicked.connect(self.btn_clicked)
        self.btn_Pi.clicked.connect(self.btn_clicked)
        self.btn_4.clicked.connect(self.btn_clicked)
        self.btn_5.clicked.connect(self.btn_clicked)
        self.btn_6.clicked.connect(self.btn_clicked)
        self.btn_Minus.clicked.connect(self.btn_clicked)
        self.btn_Log.clicked.connect(self.btn_clicked)
        self.btn_exponent.clicked.connect(self.btn_clicked)
        self.btn_Square_Loot.clicked.connect(self.btn_clicked)
        self.btn_1.clicked.connect(self.btn_clicked)
        self.btn_2.clicked.connect(self.btn_clicked)
        self.btn_3.clicked.connect(self.btn_clicked)
        self.btn_Plus.clicked.connect(self.btn_clicked)
        self.btn_Ans.clicked.connect(self.btn_clicked)
        self.btn_EXP.clicked.connect(self.btn_clicked)
        self.btn_Power.clicked.connect(self.btn_clicked)
        self.btn_Dec.clicked.connect(self.btn_clicked)
        self.btn_0.clicked.connect(self.btn_clicked)
        self.btn_Del.clicked.connect(self.btn_clicked)
        self.btn_Eq.clicked.connect(self.btn_clicked)
    
        self.tv_Display.setEnabled(False)
        self.text_value = ""
        
    def btn_clicked(self):
        btn_eq = self.sender().text()
        if btn_eq == 'CE':
            print("clear")
            self.tv_Display.setText("0")
            self.tv_Display.setAlignment(Qt.AlignRight)
            self.text_value = ""
        elif btn_eq == '=':
            print("=")
            try:
                resultValue = eval(self.text_value.lstrip("0"))
                self.tv_Display.setText(str(resultValue))
                self.tv_Display.setAlignment(Qt.AlignRight)
            except:
                self.tv_Display.setText("error")
                self.tv_Display.setAlignment(Qt.AlignRight)
        else:
            if btn_eq == 'x':
                btn_eq = '*'
            self.text_value = self.text_value + btn_eq
            print(self.text_value)
            self.tv_Display.setText(self.text_value)
            self.tv_Display.setAlignment(Qt.AlignRight)
            
    

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    