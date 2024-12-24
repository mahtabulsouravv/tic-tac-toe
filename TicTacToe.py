import sys
from PyQt5.QtWidgets import QApplication
from Backend.Action import TicTacToe 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())