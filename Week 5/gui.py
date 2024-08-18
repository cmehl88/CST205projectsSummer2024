"""
Carson Mehl
Cst205
7/3/2024
HW3 Week 4
Summary: This code is for the gui of the image search program that creates two windows.
First window is for the user to select key word and then what transformation they want.
Example keywords to try: "gardens”, “vessel”, “memorial”, “airport”, “anime”
Connected programs required to function: functions.py, image_info.py
"""

from PySide6.QtWidgets import (QWidget, QApplication,
QLabel, QPushButton, QLineEdit, QVBoxLayout,QComboBox)
from PySide6.QtCore import Qt, Slot
from image_info import image_info
from __feature__ import snake_case, true_property
from PySide6.QtGui import QPixmap
from functions import my_search, options
import sys

app = QApplication([])
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # The objects
        self.line_edit = QLineEdit()
        my_lbl = QLabel('Type a key word')
        my_lbl2 = QLabel('Select an image transformation')
        self.combo_box = QComboBox()
        self.search_btn = QPushButton('Search')
        self.combo_box.add_items(['Sepia', 'Negative', 'Grayscale', 'Thumbnail', 'None'])
        self.result_label = QLabel()

        # Add objects to the layout
        layout.add_widget(my_lbl)
        layout.add_widget(self.line_edit)
        layout.add_widget(my_lbl2)
        layout.add_widget(self.combo_box)
        layout.add_widget(self.search_btn)
        layout.add_widget(self.result_label)
        layout.set_alignment(Qt.AlignTop | Qt.AlignLeft)

        # Connectivity
        self.search_btn.clicked.connect(self.image_search)

        # Window
        self.set_layout(layout)
        self.resize(300, 150)

    @Slot()
    def image_search(self):
        # First save both the edit line and drop down box option
        search_option = self.line_edit.text
        option_index = self.combo_box.current_index

        # Put the key word in the search function
        image_id = my_search(search_option)
        if image_id:
            # Create the filepath using the image id then adding .jpg to the end
            image_filepath = f'hw3_images/{image_id}.jpg'

            # Send to functions.py for transformation choices
            options(option_index, image_filepath)
            self.the_new_window('transformed_image.jpg')
        else:
            # If the keyword isn't recognized display no_results.jpg
            self.the_new_window('hw3_images/no_results.jpg')

    # Open new window
    def the_new_window(self, image_filepath):
        self.new_win = NewWindow(image_filepath)
        self.new_win.show()

class NewWindow(QWidget):
    def __init__(self, image_filepath):
        super().__init__()
        layout = QVBoxLayout()

        # The objects
        self.result_label = QLabel()

        # Add objects to layout
        layout.add_widget(self.result_label)

        # Window and Qpixmap
        self.set_layout(layout)
        pixmap = QPixmap(image_filepath)
        self.result_label.pixmap = pixmap
        self.resize(pixmap.width(), pixmap.height())

my_win = MyWindow()
my_win.show()
sys.exit(app.exec())