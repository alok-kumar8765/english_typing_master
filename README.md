# Professional Typing Practice Application

A clean, modern desktop GUI application built in Python using **Tkinter**. This tool helps users evaluate and improve their typing speed (WPM), accuracy, and overall typing efficiency across multiple difficulty levels.

---

## 📋 Table of Contents
- [Features](#-features)
- [Requirements](#-requirements)
- [How to Run / Use](#-how-to-run--use)
- [Pros](#-pros)
- [Cons](#-cons)
- [Limitations](#-limitations)
- [How It Works](#-how-it-works)

---

## ⚡ Features

- **Multiple Difficulty Levels**: Choose from **Easy**, **Medium**, or **Hard** paragraphs.
- **Real-time Live Metrics**:
  - **WPM (Words Per Minute)** recalculated dynamically every 200 ms.
  - **Accuracy Percentage** based on character-by-character comparison.
  - **Elapsed Time Tracker**.
- **Auto-Completion Detection**: Automatically finishes and displays a summary banner when the typed text matches the prompt perfectly.
- **Minimalist GUI**: Clean design built with native Tkinter and TTK widgets.
- **Zero Third-Party Dependencies**: Runs directly on any standard Python installation.

---

## 🛠️ Requirements

- **Python Version**: Python 3.6 or higher.
- **Libraries**: Standard library packages only (`tkinter`, `random`, `time`).
  - No external `pip install` commands required!

> **Note for Linux Users**: If Tkinter is not pre-installed on your system, install it via your package manager:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 🚀 How to Run / Use

1. **Save the Code**: Save the script file as `typing_practice.py`.
2. **Execute the Application**:
   ```bash
   python typing_practice.py
   ```
3. **Start Practicing**:
   1. Select your preferred difficulty level (**Easy**, **Medium**, or **Hard**) from the dropdown menu.
   2. Click the **Start Test** button.
   3. Focus moves automatically to the text box — start typing the displayed paragraph!
   4. Watch your WPM, Accuracy, and Time update live.
   5. Once completed, your final score will be displayed at the bottom.
   6. Click **New Test** at any time to clear and reset the application.

---

## 👍 Pros

1. **Lightweight & Fast**: Loads instantly with minimal CPU/RAM footprint.
2. **Offline-Capable**: Completely standalone with no network requirements.
3. **No External Dependencies**: Works out-of-the-box on standard Python distributions.
4. **Clean Code Structure**: Clear modular layout making it simple to extend, modify, or add custom practice paragraphs.

---

## 👎 Cons

1. **Static Content**: Relies on a fixed set of hardcoded paragraphs in a Python dictionary.
2. **Basic Visual Feedback**: Does not highlight individual mis-typed characters (red/green highlight) inside the input box in real time.
3. **Exact Match Completion**: Test completion triggers only when the string matches the reference paragraph *exactly*, including newlines and spacing.

---

## ⚠️ Limitations

1. **No Data Persistence**: Practice history, high scores, or progress analytics are not saved when the application closes.
2. **Basic WPM Calculation**: WPM is derived from total space-separated words rather than the standard 5-character standardized word length (`(Total Characters / 5) / Minutes`).
3. **No Key-by-Key Highlighting**: Unlike web platforms (e.g., Monkeytype or TypingClub), individual characters are not colored in real time to show errors instantly.

---

## ⚙️ How It Works

1. **`start_test()`**: Retrieves a random paragraph based on the selected difficulty, clears previous inputs, captures `time.time()`, and sets `test_running = True`.
2. **`update_stats()`**: A recursive GUI loop running every 200 milliseconds via `root.after()`. It calculates current elapsed time, splits the user string to count words, and compares typed characters with the target text to calculate live accuracy.
3. **`finish_test()`**: Triggered when `typed_text == current_paragraph`. It halts the timer loop and locks in the final metrics score.