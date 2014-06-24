import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    """The main window for my application"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        #create stacked layout
        self.stacked_layout = QStackedLayout()
        #create the two layouts we need
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
        self.submit_button = QPushButton("Submit")

        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.submit_button)       

        self.initial_widget = QWidget()
        self.initial_widget.setLayout(self.layout)
        #add to stacked layout
        self.stacked_layout.addWidget(self.initial_widget)

        #connection
        self.submit_button.clicked.connect(self.switch_to_hello_layout)

    def create_hello_layout(self):
        self.label = QLabel()
        self.back_button = QPushButton("Back")

        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.back_button)       

        self.hello_widget = QWidget()
        self.hello_widget.setLayout(self.layout)
        
        self.stacked_layout.addWidget(self.hello_widget)

        self.back_button.clicked.connect(self.switch_to_initial_layout)        

    def switch_to_hello_layout(self):
        self.stacked_layout.setCurrentIndex(1)
        name = self.text_box.text()
        if name == "":
            self.label.setText("Please go back and enter in your name")
        else:
            self.label.setText("Hello {0}".format(name))

    def switch_to_initial_layout(self):
        self.stacked_layout.setCurrentIndex(0)
        self.text_box.clear()


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
