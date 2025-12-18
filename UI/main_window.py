from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from .molecules import DialogMolecule, FileDialogMolecule

from app.Handlers import DragDropManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()
        self.setupUi()

    def setup(self):
        self.drag_drop_manager = DragDropManager()
        self.setAcceptDrops(True)
        self.setWindowTitle("Validador de archivos de Excel")
        self.setFixedSize(600, 400)
        
        #? Layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
    
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

    def setupUi(self):
        self.main_layout.addWidget(FileDialogMolecule())