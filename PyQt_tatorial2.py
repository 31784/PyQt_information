import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    """The main window for my application"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        #create stacked layout
        self.create_initial_layout()
        #create the two layouts we need
        self.stacked_layout = QStackedLayout()
        self.create_initial_layout()
        self.create_hello_layout()
        #set initial layout
        self.stacked_layout.setCurrentIndex(0)
        #set the central widget to the stacked layout
        self.widget = QWidget()
        self.widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.widget)

    def create_initial_layout(self):
        self.text_box = QLineEdit()
        self.button = QPushButton("Submit")

        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.button)       

        self.initial_widget = QWidget()
        self.initial_widget.setLayout(self.layout)
        #add to stacked layout
        self.stacked_layout.addWidget(self.initial_widget)

    def create_hello_layout(self):
        self.text_box = QLineEdit()
        self.back_button = QPushButton("Back")

        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.back_button)       

        self.hello_widget = QWidget()
        self.hello_widget.setLayout(self.layout)
        
        self.stacked_layout.addWidget(self.hello_widget)

    def display_name(self):
        name = self.text_box.text()
        self.text_box.setText("Hello {0}".format(name))

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
