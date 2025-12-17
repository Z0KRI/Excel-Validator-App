from PySide6.QtCore import QMimeData
from typing import Optional

class _DragAndDropSingleton(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(_DragAndDropSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance
    
class DragDropManager(metaclass=_DragAndDropSingleton):
    def __init__(self, allowed_extensions: Optional[set[str]] = None):
        self.files = []
        self.__allowed_extensions = allowed_extensions

    def handle(self, mime: QMimeData) -> bool:
        if not mime.hasUrls():
            return False

        files = [url.toLocalFile() for url in mime.urls()]

        for path in files:
            if self.__allowed_extensions:
                if not any(path.lower().endswith(ext) for ext in self.__allowed_extensions):
                    return False
        self.files = files
        return True
