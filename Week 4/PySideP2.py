"""
Carson Mehl
Cst205
6/27/2024
Lab - PySide(QT) Pt2
Summary: This code is for implementing 2 different buttons for a GUI
"""

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property

my_app = QApplication([])

class DoubleButton(QWidget):
  def __init__(self):
      super().__init__()
      vbox = QVBoxLayout()
      
      # The buttons
      my_btn = QPushButton('button 1')
      my_btn2 = QPushButton('button 2')
      
      # Checking if buttons are clicked
      self.my_lbl = QLabel('button not yet clicked')
      self.my_lbl2 = QLabel('button 2 not yet clicked')
      my_btn.clicked.connect(self.on_click)
      my_btn2.clicked.connect(self.on_click2)
      
      # Adding to layout (this matters for how you want stuff placed)
      vbox.add_widget(self.my_lbl)
      vbox.add_widget(self.my_lbl2)
      vbox.add_widget(my_btn)
      vbox.add_widget(my_btn2)
      
      # The window
      self.set_layout(vbox)
      self.resize(400, 400)
      self.show()

  # For button 1
  @Slot()
  def on_click(self):
      self.my_lbl.text = 'The first button has been clicked!'
      
  # For button 2
  @Slot()
  def on_click2(self):
      self.my_lbl2.text = 'The second button has been clicked!'
      
# create a MyWindow Object/instance
my_win = DoubleButton()

# enter the Qt main loop and start to execute the Qt code
sys.exit(my_app.exec())