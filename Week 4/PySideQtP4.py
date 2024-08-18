"""
Carson Mehl
Cst205
6/28/2024
Lab - PySide(QT) Pt3 (THIS IS FOR TASK 3)!!! 
Summary: Program is user chooses a color from the drop down box and then that color pops up
in another window with the background of that window being the chosen color.
"""
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QComboBox)
from PySide6.QtCore import Slot, Qt
from __feature__ import snake_case, true_property
app = QApplication([])
my_list = ['red', 'green', 'blue']

class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    
    # Objects
    self.color_list = QComboBox()
    self.color_list.add_items(my_list)
    btn = QPushButton('Click here for colored background!')
    
    # Add to the layout
    vbox = QVBoxLayout()
    vbox.add_widget(self.color_list)
    vbox.add_widget(btn)
    
    # connectivity and window sizes
    self.set_layout(vbox)
    btn.clicked.connect(self.open_win)
    self.resize(200, 200)

  # Modified slot to get an index number i
  @Slot() 
  def open_win(self):
    i = self.color_list.current_index
    self.new_win = NewWindow(i)
    self.new_win.show()

class NewWindow(QWidget):
  def __init__(self, number):
    super().__init__()
    
    # The if else that changes what the background color is depending on index number
    if number == 0:
        self.window_title = 'Background'
        self.palette = Qt.red
    elif number == 1:
        self.window_title = 'Background'
        self.palette = Qt.green
    elif number == 2:
        self.window_title = 'Background'
        self.palette = Qt.blue
        
    self.layout = QVBoxLayout()
    self.set_layout(self.layout)

main = MyWindow()
main.show()
sys.exit(app.exec())