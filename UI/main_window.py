from PySide6.QtWidgets import QMainWindow

from .molecules import DialogMolecule
from app.Handlers import DragDropManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.drag_drop_manager = DragDropManager()
        self.setAcceptDrops(True)
        self.setWindowTitle("Validador de archivos de Excel")
        self.setFixedSize(600, 400)
    
    #? ------- Eventos de arrastrar y soltar -------
    def dragEnterEvent(self, event):
        result = self.drag_drop_manager.handle(event.mimeData())
        if result:
            event.acceptProposedAction()
        else:
            event.ignore()
            self.invalid_excel_file_dialog()

    def dragMoveEvent(self, event):
        result = self.drag_drop_manager.handle(event.mimeData())
        if result:
            event.acceptProposedAction()
        else:
            event.ignore()
            self.invalid_excel_file_dialog()

    def invalid_excel_file_dialog(self):
        DialogMolecule.warning(
            self,
            "Archivo inválido",
            "Solo se permiten archivos de Excel (.xlsx, .xls, .xlsm).",
        ).exec()