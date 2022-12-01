import sys
import math
import re
from graph import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic


form_class = uic.loadUiType("Calculator.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)   
        
        self.btn_Memory_Set.clicked.connect(self.btn_clicked)
        self.btn_Memory_Get.clicked.connect(self.btn_clicked)
        self.btn_Graph.clicked.connect(self.btn_clicked)
        self.btn_Rad.clicked.connect(self.btn_clicked)
        self.btn_Deg.clicked.connect(self.btn_clicked)
        self.btn_Grad.clicked.connect(self.btn_clicked)
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
        self.btn_Pi.clicked.connect(self.btn_clicked)
        self.btn_Pow.clicked.connect(self.btn_clicked)
        self.btn_4.clicked.connect(self.btn_clicked)
        self.btn_5.clicked.connect(self.btn_clicked)
        self.btn_6.clicked.connect(self.btn_clicked)
        self.btn_Minus.clicked.connect(self.btn_clicked)
        self.btn_Log10.clicked.connect(self.btn_clicked)
        self.btn_Log2.clicked.connect(self.btn_clicked)
        self.btn_Ln.clicked.connect(self.btn_clicked)
        self.btn_1.clicked.connect(self.btn_clicked)
        self.btn_2.clicked.connect(self.btn_clicked)
        self.btn_3.clicked.connect(self.btn_clicked)
        self.btn_Plus.clicked.connect(self.btn_clicked)
        self.btn_Ans.clicked.connect(self.btn_clicked)
        self.btn_EXP.clicked.connect(self.btn_clicked)
        self.btn_Square_Root.clicked.connect(self.btn_clicked)
        self.btn_Dec.clicked.connect(self.btn_clicked)
        self.btn_0.clicked.connect(self.btn_clicked)
        self.btn_Del.clicked.connect(self.btn_clicked)
        self.btn_Eq.clicked.connect(self.btn_clicked)
        self.tv_Display.setEnabled(False)

        self.funcOperator = ['Rad','Deg','Grad','Sin','Cos','Tan','Log10','Log2','Ln','Exp']
        self.text_value = ""        # 주 계산식
        self.memory_value = ""      # 메모리 식
        self.last_result = 0.0     # ANS용 버퍼
        
    def btn_clicked(self):         
        btn_input = self.sender().text()
        self.check_input(btn_input)                   # 인풋값 검사.

    def check_input(self, btn_input) :                # 조작, 연산 순서대로
        if(not self.isFunc(btn_input)) :       
            self.isOper(btn_input)             

    def isFunc(self, btn_input) :                   
        if btn_input == '메모리':
            print("Set Buffer")
            self.memory_value=self.text_value
            return 1
        elif btn_input == '불러오기':
            print("Get Buffer")
            self.text_value=self.memory_value
            self.tv_Display.setText(self.text_value)
            self.tv_Display.setAlignment(Qt.AlignRight)
            return 1
        elif btn_input == '그래프':
            print("show Graph")
            self.graph = Graph()
            self.graph.exec()
            return 1
        elif btn_input == 'CE':
            print("Clear")
            self.tv_Display.setText("0")
            self.tv_Display.setAlignment(Qt.AlignRight)
            self.text_value = ""
            return 1
        elif btn_input == 'Ans':
            print("Get Last Answer")
            self.text_value=str(self.last_result)
            self.tv_Display.setText(str(self.text_value))
            self.tv_Display.setAlignment(Qt.AlignRight)
            return 1
        elif btn_input == '<-':
            print("Delete")
            self.text_value=self.text_value[:-1]
            self.tv_Display.setText(str(self.text_value))
            self.tv_Display.setAlignment(Qt.AlignRight)
            return 1
        elif btn_input == '=':
            print("Equation")
            try:
                print(self.text_value)
                self.replaceExpression()                           # 수식 변환
                print(self.text_value)
                resultValue = eval(self.text_value.lstrip("0"))
                self.tv_Display.setText(format(resultValue, ".3f"))
                self.tv_Display.setAlignment(Qt.AlignRight)
                self.last_result = resultValue
                self.tv_Display.setAlignment(Qt.AlignRight)
                self.text_value = ""
            except:
                self.tv_Display.setText("error")
                self.tv_Display.setAlignment(Qt.AlignRight)
                self.text_value = ""
            return 1
        else :                                      
            return 0
            
    def isOper(self, btn_input) :    
        if btn_input in self.funcOperator :
            print(btn_input)
            btn_input = btn_input + '('
        if btn_input == 'x!' :
            print('factorial')
            btn_input = 'Factorial('
        if btn_input == 'x' :
            print('multi')
            btn_input = '*'
        if btn_input == '÷' :
            print('div')
            btn_input = '/'
        if btn_input == 'X^Y' :
            print('Power')
            btn_input = '**'
        if btn_input == '√' :
            print('Root')
            btn_input = 'SquareRoot('
        self.text_value = self.text_value + btn_input
        self.tv_Display.setText(self.text_value)
        self.tv_Display.setAlignment(Qt.AlignRight)

    def replaceExpression(self):
        self.text_value = re.sub('Rad','math.radians',self.text_value)
        self.text_value = re.sub('Deg','math.degrees',self.text_value)
        self.text_value = re.sub('Grad','9 / 10 * math.radians',self.text_value)
        self.text_value = re.sub('Sin','math.sin',self.text_value)
        self.text_value = re.sub('Cos','math.cos',self.text_value)
        self.text_value = re.sub('Tan','math.tan',self.text_value)
        self.text_value = re.sub('Factorial','math.factorial',self.text_value)
        self.text_value = re.sub('π','math.pi',self.text_value)
        self.text_value = re.sub('Log10','math.log10',self.text_value)
        self.text_value = re.sub('Log2','math.log2',self.text_value)
        self.text_value = re.sub('Ln','math.log',self.text_value)
        self.text_value = re.sub('Exp','math.exp',self.text_value)
        self.text_value = re.sub('SquareRoot','math.sqrt', self.text_value)

            
    

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    