from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

import sys

def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine("main.qml", app)

    app.exec()

if __name__ == "__main__":
    main()