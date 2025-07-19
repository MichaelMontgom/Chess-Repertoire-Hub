import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import QFont



class ChessMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess Repertoire Hub - Dashboard")
        self.setStyleSheet("""
            QMainWindow {
                background: #12151B;
            }
            QWidget {
                font-family: 'Segoe UI', Arial, sans-serif;
            }
        """)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create layout
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
       
        
        # Initial setup
        self.resize(1200, 800)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Chess Repertoire Hub")
    app.setApplicationVersion("0.1")
    
    # Set global font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    try:
        # Create main window
        window = ChessMainWindow()
        
        # Show main window
        window.show()
        window.activateWindow()
        window.raise_()
        print(f"Window shown - size: {window.size()}, position: {window.pos()}")
        
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Error starting application: {e}")
        import traceback
        traceback.print_exc()