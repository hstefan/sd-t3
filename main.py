import sys
from gui_wrapper import Gui_Wrapper
from PyQt4 import QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = Gui_Wrapper()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
