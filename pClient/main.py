from guiApp import GuiApp
from PyQt5 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = GuiApp() 
    window.show()  
    app.exec_()  
    window.saveList()

if __name__ == '__main__':  
    main()  