#~/usr/bin/python
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import config

def create_connection():
    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setDatabaseName('smartnet')
    db.setHostName('127.0.0.1')
    db.setUserName('root')
    db.setPassword('Echo@1927')
    if not db.open():
        QMessageBox.critical(None, "Cannot open database",
                             "Unable to establish a database connection.\n"
                             "This example needs SQLite support. Please read the Qt SQL "
                             "driver documentation for information how to build it.\n\n"
                             "Click Cancel to exit.", QMessageBox.Cancel)
        return False
    return True

create_connection()