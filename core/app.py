from PySide6.QtWidgets import QApplication
from app.Handlers import DragDropManager

class AppBase(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.set_application_style()
        self.setup()
    
    def set_application_style(self):
        self.setStyle("Fusion")
    
    def setup(self):
        DragDropManager(
            allowed_extensions = {".xlsx", ".xls", ".xlsm"}
        )