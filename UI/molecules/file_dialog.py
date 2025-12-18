from PySide6.QtWidgets import QGroupBox, QHBoxLayout, QLabel, QPushButton, QFileDialog

class FileDialogMolecule(QGroupBox):
    def __init__(self, title="Seleccionar archivo de Excel"):
        super().__init__(title)
        self.setup_ui()
        self.setup_signals()
    
    def setup_ui(self):
        self.file_layout = QHBoxLayout(self)  # Pasar self como parent

        self.file_path_label = QLabel("No file selected")
        self.file_path_label.setStyleSheet("""
            border: 1px solid #ccc; 
            padding: 5px;
            background-color: #f8f9fa;
            min-width: 200px;
        """)
        self.file_path_label.setMinimumHeight(30)
        
        self.browse_btn = QPushButton("Examinar...")
        
        # Configurar stretch para que el label ocupe espacio disponible
        self.file_layout.addWidget(self.file_path_label, 1)  # Factor de stretch = 1
        self.file_layout.addWidget(self.browse_btn)
        
        # Opcional: configurar márgenes y espaciado
        self.file_layout.setContentsMargins(10, 10, 10, 10)
        self.file_layout.setSpacing(10)
    
    def setup_signals(self):
        #? Conectar señales y slots
        self.browse_btn.clicked.connect(self.on_browse_clicked)
        
    def on_browse_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(
            parent=self,           # Ventana padre
            caption="Seleccionar archivo",  # Título
            dir=".",                        # Directorio inicial
            filter="Archivos de texto (*.xlsx);;Todos los archivos (*)"  # Filtros
        )

        if filename:
            print(f"Archivo seleccionado: {filename}")