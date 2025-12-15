from PySide6.QtWidgets import QMessageBox

class DialogMolecule:
    @staticmethod
    def warning(parent, title: str, message: str, buttons=QMessageBox.Ok) -> QMessageBox:
        dialog = QMessageBox(parent)
        dialog.setIcon(QMessageBox.Warning)
        dialog.setWindowTitle(title)
        dialog.setText(message)
        dialog.setStandardButtons(buttons)
        return dialog