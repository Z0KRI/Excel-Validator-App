from PySide6.QtWidgets import QApplication

class AppBase(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.set_application_style()
    
    def set_application_style(self):
        self.setStyle("Fusion")