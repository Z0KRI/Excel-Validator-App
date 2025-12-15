from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QMimeData

from .molecules import DialogMolecule

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setAcceptDrops(True)
        self.setWindowTitle("Validador de archivos de Excel")
        self.setFixedSize(600, 400)
    
    #? ------- Eventos de arrastrar y soltar -------
    def dragEnterEvent(self, event):
        self.__validation_type(event)
    
    def dragMoveEvent(self, event):
        self.__validation_type(event)
    
    def dropEvent(self, event):
        urls = event.mimeData().urls()
        file_paths = [url.toLocalFile() for url in urls]
        print(file_paths)
    
    #? ------- Validación de tipos aceptados -------
    def __validation_type(self, event):
        if event.mimeData().hasUrls() and self._all_are_excel(event.mimeData()):
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
    
    #? --- Helper para validar extensiones Excel ---
    def _all_are_excel(self, mime: QMimeData):
        #TODO: Pasar esto a una configuración externa
        excel_ext = {".xlsx", ".xls", ".xlsm"}
        for url in mime.urls():
            path = url.toLocalFile().lower()
            if not any(path.endswith(ext) for ext in excel_ext):
                return False
        return True