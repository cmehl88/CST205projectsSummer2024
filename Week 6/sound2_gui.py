"""
Carson Mehl
Cst205
7/21/2024
Lab - Digital Audio Pt2
Summary: Recives the .wav file and using pyside6
and QDial this changes the duration of notes.
"""

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QDial)
from PySide6.QtCore import Slot
from __feature__ import snake_case, true_property
from sound2 import generate_chord  # Import the function from sound2.py

class AudioApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.dial = QDial()
        self.dial.set_minimum(1)
        self.dial.set_maximum(10)
        self.dial.set_value(4)  # Default value (seconds)
        self.dial.value_changed.connect(self.update_audio)

        self.label = QLabel('Duration: 4 seconds')
        
        self.generate_button = QPushButton('Generate Chord')
        self.generate_button.clicked.connect(self.generate_chord)

        layout = QVBoxLayout()
        layout.add_widget(self.dial)
        layout.add_widget(self.label)
        layout.add_widget(self.generate_button)

        self.set_layout(layout)
    
    @Slot()
    def update_audio(self):
        duration = self.dial.value()
        self.label.set_text(f'Duration: {duration} seconds')

    @Slot()
    def generate_chord(self):
        duration = self.dial.value()
        generate_chord(duration)

app = QApplication(sys.argv)
my_win = AudioApp()
my_win.show()
sys.exit(app.exec())