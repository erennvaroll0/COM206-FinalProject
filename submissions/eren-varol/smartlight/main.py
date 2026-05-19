import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_design import Ui_LightBackManager

class SmartLightingManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LightBackManager()
        self.ui.setupUi(self)
        
        self.current_scene = None  
        
        self.history_stack = []    

        self.ui.label_status.setText("No active scene in the system.")

        self.ui.pushButton_activate.clicked.connect(self.activate_scene)
        self.ui.pushButton_back.clicked.connect(self.back_to_previous_scene)

        self.ui.pushButton_cinema.clicked.connect(self.set_cinema_mode)
        self.ui.pushButton_study.clicked.connect(self.set_study_mode)
        self.ui.pushButton_sleep.clicked.connect(self.set_sleep_mode)

        self.setWindowTitle("LightBack Manager")

    def display_status(self):
        if self.current_scene is None:
            self.ui.label_status.setText("No active scene in the system.")
        else:
            name = self.current_scene["name"]
            bright = self.current_scene["brightness"]
            color = self.current_scene["color"]
            self.ui.label_status.setText(
                f"💡 ACTIVE\n"
                f"Scene: {name}\n"
                f"Brightness: %{bright}\n"
                f"Color: {color}"
            )

    def push_to_stack(self, name, bright, color):
        if self.current_scene is not None:
            self.history_stack.append(self.current_scene)

        self.current_scene = {
            "name": name,
            "brightness": bright,
            "color": color
        }
        self.display_status()

    def activate_scene(self):
        name = self.ui.lineEdit_sceneName.text()
        bright = self.ui.lineEdit_brightness.text()
        color = self.ui.lineEdit_color.text()

        if not name or not bright or not color:
            self.ui.label_status.setText("⚠️ Please fill in all fields!")
            return

        self.push_to_stack(name, bright, color)

        self.ui.lineEdit_sceneName.clear()
        self.ui.lineEdit_brightness.clear()
        self.ui.lineEdit_color.clear()
        
    
    def set_cinema_mode(self):
        self.push_to_stack("Cinema Mode", "10", "Red")

    def set_study_mode(self):
        self.push_to_stack("Study Mode", "90", "White")

    def set_sleep_mode(self):
        self.push_to_stack("Sleep Mode", "5", "Yellow")

    def back_to_previous_scene(self):
        if len(self.history_stack) > 0:
            self.current_scene = self.history_stack.pop()
            self.display_status()
        else:
            self.current_scene = None
            self.display_status()
            self.ui.label_status.setText("❌ No previous scene found!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SmartLightingManager()
    window.show()
    sys.exit(app.exec())