import twint
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Geaux Scrape!'
        width = 400
        height = 640
        self.setFixedSize(width, height)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
    
        self.searchLabel = QLabel('Search', self)
        self.searchLabel.move(20, 10)
        self.searchBox = QLineEdit(self)
        self.searchBox.move(20, 40)
        self.searchBox.resize(350,40)
        
        self.usernameLabel = QLabel('Username', self)
        self.usernameLabel.move(20, 90)
        self.usernameBox = QLineEdit(self)
        self.usernameBox.move(20, 120)
        self.usernameBox.resize(350,40)
        
        self.emailLabel = QLabel('Email', self)
        self.emailLabel.move(20, 170)
        self.emailBox = QLineEdit(self)
        self.emailBox.move(20, 200)
        self.emailBox.resize(350,40)
        
        self.locationLabel = QLabel('Near City', self)
        self.locationLabel.move(20, 250)
        self.locationBox = QLineEdit(self)
        self.locationBox.move(20, 280)
        self.locationBox.resize(350,40)
        
        self.fromLabel = QLabel('From Date', self)
        self.fromLabel.move(20, 330)
        self.fromBox = QLineEdit(self)
        self.fromBox.move(20, 360)
        self.fromBox.resize(350,40)
        
        self.toLabel = QLabel('To Date', self)
        self.toLabel.move(20, 410)
        self.toBox = QLineEdit(self)
        self.toBox.move(20, 440)
        self.toBox.resize(350,40)
        
        self.limitLabel = QLabel('Limit Results', self)
        self.limitLabel.move(20, 490)
        self.limitBox = QLineEdit(self)
        self.limitBox.move(20, 520)
        self.limitBox.resize(350,40)
        
        # Create a button in the window
        self.button = QPushButton('Submit', self)
        self.button.resize(360, 40)
        self.button.move(15,580)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        
        c = twint.Config()
        c.Search = self.searchBox.text()
        c.Near = self.locationBox.text()
        c.Username = self.usernameBox.text()
        # c.Email = self.emailBox.text()
        # if (self.usernameBox.text == ''):
        #     c.Username == ''
        # elif (self.usernameBox.text != ''):
        #     c.Username == self.usernameBox.text()
            
        # if (self.emailBox.text() == ''):
        #     c.Email == ""
        # else:
        #     c.Email == self.emailBox.text()
        c.Pandas = True
        # c.Limit = self.limitBox.text()
        if (self.limitBox.text is None):
            c.Limit == 1000
        else: 
            c.Limit == self.limitBox.text()
        
        c.Output = c.Search + '.csv'
        c.Lang = 'en'
        # c.Near = 'lafayette'
        twint.run.Search(c)
        QMessageBox.question(self, 'Message', "You searched: " + c.Search, QMessageBox.Ok, QMessageBox.Ok)
        self.searchBox.setText("")
        self.locationBox.setText("")
        self.fromBox.setText("")
        self.toBox.setText("")
        self.limitBox.setText("")
        self.usernameBox.setText("")
        self.emailBox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


# c = twint.Config()
# c.Limit = 20
# c.Search = 'test'



# twint.run.Search(c)
