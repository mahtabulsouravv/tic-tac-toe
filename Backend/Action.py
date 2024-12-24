from Generated.TicTacToe import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

class TicTacToe(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load the design
        self.addEvents()  # Call the method to connect events

        # Define A Counter To Keep Track Of Who's Turn It Is!
        self.Counter = 0

	# This Where All Events!
    def addEvents(self):
        # Connect the Each Button With Clicker Method With Two Arguments: self,Button!!
        self.Button1.clicked.connect(lambda: self.clickerOne(self.Button1))
        self.Button2.clicked.connect(lambda: self.clickerTwo(self.Button2))
        self.Button3.clicked.connect(lambda: self.clickerThree(self.Button3))
        self.Button4.clicked.connect(lambda: self.clickerFour(self.Button4))
        self.Button5.clicked.connect(lambda: self.clickerFive(self.Button5))
        self.Button6.clicked.connect(lambda: self.clickerSix(self.Button6))
        self.Button7.clicked.connect(lambda: self.clickerSeven(self.Button7))
        self.Button8.clicked.connect(lambda: self.clickerEight(self.Button8))
        self.Button9.clicked.connect(lambda: self.clickerNine(self.Button9))
        self.startOver.clicked.connect(self.reset)

    def checkWin(self):
        # Across
        if self.Button1.text() != "" and self.Button1.text() == self.Button2.text() and self.Button1.text() == self.Button3.text():
            self.win(self.Button1,self.Button2,self.Button3)
        
        if self.Button4.text() != "" and self.Button4.text() == self.Button5.text() and self.Button4.text() == self.Button6.text():
            self.win(self.Button4,self.Button5,self.Button6)
        
        if self.Button7.text() != "" and self.Button7.text() == self.Button8.text() and self.Button7.text() == self.Button9.text():
            self.win(self.Button7,self.Button8,self.Button9)
        
        # Down
        if self.Button1.text() != "" and self.Button1.text() == self.Button4.text() and self.Button1.text() == self.Button7.text():
            self.win(self.Button1,self.Button4,self.Button7)
        
        if self.Button2.text() != "" and self.Button2.text() == self.Button5.text() and self.Button2.text() == self.Button8.text():
            self.win(self.Button2,self.Button5,self.Button8)
        
        if self.Button3.text() != "" and self.Button3.text() == self.Button6.text() and self.Button3.text() == self.Button9.text():
            self.win(self.Button3,self.Button6,self.Button9)
        
        # Diagonal
        if self.Button1.text() != "" and self.Button1.text() == self.Button5.text() and self.Button1.text() == self.Button9.text():
            self.win(self.Button1,self.Button5,self.Button9)
        
        if self.Button3.text() != "" and self.Button3.text() == self.Button5.text() and self.Button3.text() == self.Button7.text():
            self.win(self.Button3,self.Button5,self.Button7)
    
    def win(self, GridX,GridY,GridZ):
        # Add Winner Text In Display Label
        self.displayLabel.setText(f"Player {GridX.text()} Wins")
        # Disable The Board
        self.disable()
    
    def disable(self):
        ButtonList = [
            self.Button1,
            self.Button2,
            self.Button3,
            self.Button4,
            self.Button5,
            self.Button6,
            self.Button7,
            self.Button8,
            self.Button9,
        ]

        for Button in ButtonList:
            Button.setEnabled(False)

    
    def clickerOne(self, Button):
        # Check If Counter Is Odd / Even & Assign Mark
        if self.Counter % 2 == 0:
            Mark = "X"
            ButtonStyle = """
                color: rgb(134, 228, 198);  
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-top-left-radius: 20px;
            """
            self.displayLabel.setText("Player O Turn")
        else:
            Mark = "O"
            ButtonStyle = """
                color: rgb(236, 187, 67);
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-top-left-radius: 20px;
            """
            self.displayLabel.setText("Player X Turn")

        # Set Text And Style For The Button
        Button.setText(Mark)
        Button.setStyleSheet(ButtonStyle)
        Button.setEnabled(False)
        # Increment The Counter
        self.Counter += 1
         # Check If Won !
        self.checkWin()
    
    def clickerTwo(self, Button):
        if self.Counter % 2 == 0:
            Mark = "X"
            ButtonStyle = """
                color: rgb(134, 228, 198);  
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-radius:0px;
            """
            self.displayLabel.setText("Player O Turn")
        else:
            Mark = "O"
            ButtonStyle = """
                color: rgb(236, 187, 67);
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-radius:0px;
            """
            self.displayLabel.setText("Player X Turn")
        Button.setText(Mark)
        Button.setStyleSheet(ButtonStyle)
        Button.setEnabled(False)
        self.Counter += 1
        self.checkWin()
        

    def clickerThree(self, Button):
        if self.Counter % 2 == 0:
            Mark = "X"
            ButtonStyle = """
                color: rgb(134, 228, 198);  
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-top-right-radius: 20px;
            """
            self.displayLabel.setText("Player O Turn")
        else:
            Mark = "O"
            ButtonStyle = """
                color: rgb(236, 187, 67);
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-top-right-radius: 20px;
            """
            self.displayLabel.setText("Player X Turn")
        Button.setText(Mark)
        Button.setStyleSheet(ButtonStyle)
        Button.setEnabled(False)
        self.Counter += 1
        self.checkWin()
    
    def clickerFour(self, Button):
        if self.Counter % 2 == 0:
            Mark = "X"
            ButtonStyle = """
                color: rgb(134, 228, 198);  
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-radius:0px;
            """
            self.displayLabel.setText("Player O Turn")
        else:
            Mark = "O"
            ButtonStyle = """
                color: rgb(236, 187, 67);
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-radius:0px;
            """
            self.displayLabel.setText("Player X Turn")
        Button.setText(Mark)
        Button.setStyleSheet(ButtonStyle)
        Button.setEnabled(False)
        self.Counter += 1
        self.checkWin()
    
    def clickerFive(self, Button):
        if self.Counter % 2 == 0:
            Mark = "X"
            ButtonStyle = """
                color: rgb(134, 228, 198);  
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-radius:0px;
            """
            self.displayLabel.setText("Player O Turn")
        else:
            Mark = "O"
            ButtonStyle = """
                color: rgb(236, 187, 67);
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-radius:0px;
            """
            self.displayLabel.setText("Player X Turn")
        Button.setText(Mark)
        Button.setStyleSheet(ButtonStyle)
        Button.setEnabled(False)
        self.Counter += 1
        self.checkWin()
    
    def clickerSix(self, Button):
        if self.Counter % 2 == 0:
            Mark = "X"
            ButtonStyle = """
                color: rgb(134, 228, 198);  
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-radius:0px;
            """
            self.displayLabel.setText("Player O Turn")
        else:
            Mark = "O"
            ButtonStyle = """
                color: rgb(236, 187, 67);
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-radius:0px;
            """
            self.displayLabel.setText("Player X Turn")
        Button.setText(Mark)
        Button.setStyleSheet(ButtonStyle)
        Button.setEnabled(False)
        self.Counter += 1
        self.checkWin()
    
    def clickerSeven(self, Button):
        if self.Counter % 2 == 0:
            Mark = "X"
            ButtonStyle = """
                color: rgb(134, 228, 198);  
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-bottom-left-radius: 20px;
            """
            self.displayLabel.setText("Player O Turn")
        else:
            Mark = "O"
            ButtonStyle = """
                color: rgb(236, 187, 67);
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-bottom-left-radius: 20px;
            """
            self.displayLabel.setText("Player X Turn")
        Button.setText(Mark)
        Button.setStyleSheet(ButtonStyle)
        Button.setEnabled(False)
        self.Counter += 1
        self.checkWin()
    
    def clickerEight(self, Button):
        if self.Counter % 2 == 0:
            Mark = "X"
            ButtonStyle = """
                color: rgb(134, 228, 198);  
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-radius:0px;
            """
            self.displayLabel.setText("Player O Turn")
        else:
            Mark = "O"
            ButtonStyle = """
                color: rgb(236, 187, 67);
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-radius:0px;
            """
            self.displayLabel.setText("Player X Turn")
        Button.setText(Mark)
        Button.setStyleSheet(ButtonStyle)
        Button.setEnabled(False)
        self.Counter += 1
        self.checkWin()
    
    def clickerNine(self, Button):
        if self.Counter % 2 == 0:
            Mark = "X"
            ButtonStyle = """
                color: rgb(134, 228, 198);  
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-bottom-right-radius: 20px;
            """
            self.displayLabel.setText("Player O Turn")
        else:
            Mark = "O"
            ButtonStyle = """
                color: rgb(236, 187, 67);
                background-color: rgb(92, 95, 103);
                font-size: 128px; 
                font-weight: bold; 
                border-bottom-right-radius: 20px;
            """
            self.displayLabel.setText("Player X Turn")
        Button.setText(Mark)
        Button.setStyleSheet(ButtonStyle)
        Button.setEnabled(False)
        self.Counter += 1
        self.checkWin()
    
    # Start Over!
    def reset(self):
        ButtonList = [
            self.Button1,
            self.Button2,
            self.Button3,
            self.Button4,
            self.Button5,
            self.Button6,
            self.Button7,
            self.Button8,
            self.Button9,
        ]

        for Button in ButtonList:
            Button.setText("")
            Button.setEnabled(True)

        # Reset The Display Label
        self.displayLabel.setText("Player X Goes First👻")
        self.Counter = 0