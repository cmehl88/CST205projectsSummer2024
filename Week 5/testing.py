   class NewWindow(QWidget):
    def __init__(self, img_path, i):
        super().__init__()
   
   label = QLabel()
   
     self.layout = QVBoxLayout()
        self.layout.add_widget(label)
        
            # set layout and size
        self.set_layout(self.layout)
        self.resize(500,500)