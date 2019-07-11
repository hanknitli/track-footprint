import sys

from PyQt5.QtWidgets import QApplication

from graphics import mainwindow


def run():
    # Initialize the application
    app = QApplication(sys.argv)

    # Initialize the config files
    # TODO

    # Initialize log files
    # TODO

    # Initialize the app window
    window = mainwindow.MainWindow()
    window.show()

    # App execution
    app.exec_()
