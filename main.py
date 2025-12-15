from core import AppBase
from ui import MainWindow
import sys

def main():
    #? Llamada principal de la aplicación
    app = AppBase(sys.argv)
    
    #? Ventana principal
    m_view = MainWindow()
    
    #? Mostrar la ventana principal
    m_view.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())