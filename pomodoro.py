import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLCDNumber
from PyQt5.QtCore import QTimer

class PomodoroApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro Timer")
        self.resize(300, 200)

        self.timer_duration = 25 * 60  # 25 minute
        self.break_duration = 5 * 60  # 5 minute
        self.long_break_duration = 15 * 60  # 15 minute
        self.num_pomodoros = 0
        self.current_duration = self.timer_duration
        self.timer_running = False

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.timer_display = QLCDNumber()
        self.timer_display.display(self.timer_duration // 60)
        layout.addWidget(self.timer_display)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_timer)
        layout.addWidget(self.reset_button)

        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer_display)

    def start_timer(self):
        if not self.timer_running:
            self.timer.start(1000)  # Update every second
            self.start_button.setEnabled(False)
            self.timer_running = True

    def reset_timer(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.timer_running = False
        self.current_duration = self.timer_duration
        self.timer_display.display(self.timer_duration // 60)

    def update_timer_display(self):
        self.current_duration -= 1
        if self.current_duration == 0:
            self.timer.stop()
            self.timer_running = False
            self.num_pomodoros += 1
            if self.num_pomodoros % 4 == 0:
                self.current_duration = self.long_break_duration
            else:
                self.current_duration = self.break_duration
        mins, secs = divmod(self.current_duration, 60)
        self.timer_display.display(mins)


def main():
    app = QApplication(sys.argv)
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()