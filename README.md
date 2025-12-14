🕒 PyQt5 Digital Clock (Transparent Circular UI)

📌 Project Description

This is a custom digital clock application developed using Python and PyQt5. I created this project to practice GUI development and custom window styling. The clock displays the current system time in real-time with a transparent circular interface, glowing borders, and a custom digital font.
The window is frameless, draggable, and designed to look like a modern desktop widget.

✨ Features

Real-time digital clock (HH:MM:SS AM/PM)

Transparent background using Qt.WA_TranslucentBackground

Circular UI drawn with QPainter

Glowing green border effect

Frameless window (no title bar)

Draggable window using mouse events

Custom digital font support

Smooth time update using QTimer


🛠️ Technologies Used

Python 3

PyQt5

QTimer for time updates

QPainter for custom drawing

QFontDatabase for loading custom fonts


🧠 How It Works

I used QTimer to update the time every second.
The system time is fetched using QTime.currentTime().
I removed the default window border using Qt.FramelessWindowHint.
The circular background and border are drawn inside paintEvent() using QPainter.
Mouse events (mousePressEvent, mouseMoveEvent, mouseReleaseEvent) allow the window to be dragged anywhere on the screen.
A custom digital font is loaded using QFontDatabase.


📂 Project Structure
DigitalClock/
│
├── clockTimer.py
├── DS-DIGIB.TTF
└── README.md

▶️ How to Run the Project


Make sure Python is installed

Install PyQt5:

pip install PyQt5


Update the font path in the code:

QFontDatabase.addApplicationFont("path/to/DS-DIGIB.TTF")


Run the application:

python digital_clock.py

📸 UI Preview

Circular transparent clock

Neon green digital text

Smooth glowing border

Minimal modern design

🎯 Purpose of This Project

I developed this project to:

Improve my PyQt5 GUI skills

Learn custom painting with QPainter

Understand event handling and window movement

Create a reusable desktop widget

👤 Author

Suminda Lakshan

Computer Science Student

Python | PyQt5 | GUI Development


📜 License

This project is open-source and free to use for learning and personal projects.
