# 💡 SmartLight - LightBack Manager

SmartLight is a specialized desktop utility designed for precise home lighting management. The core mission of the system is to optimize room ambiance—preventing suboptimal lighting and excessive energy usage—to maintain an ideal visual and task-oriented environment.

The application streamlines the control process for smart residential lighting by integrating customizable custom scenes with standardized environmental preset modes. It aims to reduce manual adjustment overhead and enhance user workflow through a data-driven, user-centric Qt interface.

---

## 🚀 Key Functionalities

- **Scene Activation:** Automated environment configuration based on custom Scene Name, Brightness level, and Color values.
- **Preset Shortcuts:** Instant, single-click application of standard scene configurations (Cinema, Study, and Sleep modes).
- **Safety & History Tracking:** To ensure an intuitive experience, the system implements stack memory logic. If a user needs to rollback an accidental change, the "Back" action seamlessly reverts to the exact previous lighting configuration.

---

## ⚙️ How It Works (Algorithmic Logic)

The system operates based on software engineering stack architecture principles through the following logical steps:

1. **Input:** The user provides a Scene Name, Brightness level (%), and Color via the control panel fields, or triggers a direct preset button.
2. **Processing:**
   - **Pre-push Check:** If an active scene already exists in the system, it is shifted onto the history stack.
   - **Stack Push:** The new parameters are packed into a state structure and set as the current active scene.
3. **Validation:** If the history stack is empty during a rollback operation, the system gracefully handles the null state, updates the interface, and notifies the user that no deeper history exists.
4. **Output:** The real-time status display reflects the active lighting parameters synchronously with multi-line formatted precision.

---

## 🛠️ Installation & Setup

Follow these steps to run the project locally:

### Requirements

* Python 3.x (Standard for macOS/Windows)
* PySide6 Framework
* Android Studio, VS Code or any Terminal wrapper

### Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/erennvaroll0/COM206-FinalProject.git
    cd COM206-FinalProject
    ```
2. **Install dependencies:**
    ```bash
    pip install PySide6
    ```
3. **Run the application:**
    ```bash
    python3 submissions/eren-varol/smartlight/main.py
    ```

---

## 📂 Project Structure

```text
COM206-FinalProject/
├── submissions/
│   └── eren-varol/
│       └── smartlight/
│           ├── __pycache__/            # Compiled bytecode directory
│           ├── env/                    # Virtual Environment (ignored by git)
│           ├── .gitignore              # Git ignore file
│           ├── main.py                 # Main application logic
│           ├── README.md               # App local documentation
│           ├── requirements.txt        # Project dependencies
│           ├── ui_design.py            # Compiled Python UI file
│           └── ui_design.ui            # Qt Designer UI file
└── README.md                           # Main repository documentation (this file)                        # Main repository documentation (this file)
