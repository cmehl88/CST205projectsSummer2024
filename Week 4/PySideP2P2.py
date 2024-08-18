"""
Carson Mehl
Cst205
6/27/2024
Lab - PySide(QT) Pt2 (This is for task 2 of 2)
Summary: This code is for creating a drop list and display information for a GUI
"""
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QComboBox)
from PySide6.QtCore import Slot, Qt
from __feature__ import snake_case, true_property

my_app = QApplication([])

# The List with colors (I know very creative colors) (the options for the drop box)
my_list = ["Pick a color", "blue", "red", "green"]

class DropList(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # The two lines for the list
        self.my_color_box = QComboBox()
        self.my_color_box.add_items(my_list)

        # Objects
        label1 = QLabel('CST 205 Color Exchange!')
        self.label2 = QLabel('RGB:                 Hex:')

        # Add objects to layout and make it so they aren't floating out in the middle
        layout.add_widget(label1)
        layout.add_widget(self.my_color_box)
        layout.add_widget(self.label2)

        # This will make the layout to the top left of the window
        layout.set_alignment(Qt.AlignTop | Qt.AlignLeft)

        self.my_color_box.currentIndexChanged.connect(self.update_RGB_HEX)

        # Window
        self.set_layout(layout)
        self.resize(300, 300)
        self.show()

    @Slot()
    def update_RGB_HEX(self):
        # Based on what option is chosen change what label 2 says!
        my_index = self.my_color_box.current_index
        if my_index == 0:
            self.label2.text = 'RGB:                     Hex:'
        elif my_index == 1:
            self.label2.text = 'RGB: (0,0,255)           Hex:#0000ff'
        elif my_index == 2:
            self.label2.text = 'RGB: (255,0,0)           Hex:#ff0000'
        elif my_index == 3:
            self.label2.text = 'RGB: (0,255,0)           Hex:#00ff00'
     
# create a MyWindow Object/instance
my_win = DropList()

# enter the Qt main loop and start to execute the Qt code
sys.exit(my_app.exec())