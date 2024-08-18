"""
Carson Mehl
Cst205
6/28/2024
Lab - PySide(QT) Pt3
Summary: This code is for changing the background color, Nested layouts (going both vertical and horizontal in this example).
"""

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QComboBox)
from PySide6.QtCore import Slot, Qt
from __feature__ import snake_case, true_property

# Task 1 -------------------------------
my_qt_app = QApplication([])

class ColorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = 'Background'
        self.palette = Qt.blue
        
        # Task 2 ------------------------
        h_layout = QHBoxLayout()
        b1 = QPushButton("A")
        b2 = QPushButton("B")

        h_layout.add_widget(b1)
        h_layout.add_widget(b2)

        v_layout = QVBoxLayout()
        b4 = QPushButton("D")
        b5 = QPushButton("E")

        v_layout.add_widget(b4)
        v_layout.add_widget(b5)

        main_layout = QHBoxLayout()

        main_layout.add_layout(v_layout)
        main_layout.add_layout(h_layout) # I swapped around 41 and 42 so in the window they are reversed with vertcal going first.
        self.set_layout(main_layout)

my_window = ColorWindow()
my_window.show()
sys.exit(my_qt_app.exec())