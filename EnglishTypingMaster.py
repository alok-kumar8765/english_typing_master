import tkinter as tk
from tkinter import ttk
import random
import time


# --------------------------------------------------
# PRACTICE PARAGRAPHS
# --------------------------------------------------

paragraphs = {
    "Easy": [
        """Learning to type quickly and accurately is a useful skill.
Regular practice can help you become more comfortable with the keyboard.
Start slowly, focus on accuracy, and gradually increase your typing speed.
With consistent practice, typing will become easier and more natural.""",

        """Every skill becomes better with practice.
Typing is no different. Try to keep your fingers close to the correct
keys and avoid looking at the keyboard too often.
Accuracy is more important than speed when you are learning."""
    ],

    "Medium": [
        """Technology has changed the way people communicate, learn, and work.
Computers are now used in almost every profession, and being able to type
quickly can save a significant amount of time. A good typing speed allows
you to focus more on your ideas instead of thinking about which key to press.""",

        """Programming is a skill that requires patience, logical thinking,
and regular practice. When learning a programming language, it is normal
to make mistakes. The important thing is to understand those mistakes and
use them as opportunities to improve. Small improvements every day can
eventually lead to excellent results."""
    ],

    "Hard": [
        """Developing professional typing skills requires more than simply
typing as fast as possible. A skilled typist maintains a consistent rhythm,
keeps errors to a minimum, and remains comfortable during long periods of
work. Accuracy becomes especially important when writing programming code,
technical documentation, business reports, or other professional material.""",

        """Modern software development involves reading documentation,
writing code, reviewing existing programs, communicating with teammates,
and solving complex problems. Although typing speed is only one part of
software development, being able to express ideas quickly through a keyboard
can make everyday programming tasks significantly more efficient."""
    ]
}


# --------------------------------------------------
# GLOBAL VARIABLES
# --------------------------------------------------

current_paragraph = ""
start_time = None
test_running = False
total_typed = 0
correct_typed = 0


# --------------------------------------------------
# MAIN WINDOW
# --------------------------------------------------

root = tk.Tk()
root.title("Professional Typing Practice")
root.geometry("1000x700")
root.configure(bg="#f4f6f8")


# --------------------------------------------------
# TITLE
# --------------------------------------------------

title = tk.Label(
    root,
    text="Typing Practice",
    font=("Arial", 28, "bold"),
    bg="#f4f6f8",
    fg="#222222"
)

title.pack(pady=(25, 5))


subtitle = tk.Label(
    root,
    text="Improve your speed, accuracy and typing confidence",
    font=("Arial", 12),
    bg="#f4f6f8",
    fg="#666666"
)

subtitle.pack(pady=(0, 20))


# --------------------------------------------------
# TOP INFORMATION BAR
# --------------------------------------------------

info_frame = tk.Frame(root, bg="#ffffff")
info_frame.pack(fill="x", padx=40, pady=10)


wpm_label = tk.Label(
    info_frame,
    text="WPM: 0",
    font=("Arial", 14, "bold"),
    bg="#ffffff"
)

wpm_label.pack(side="left", padx=25, pady=15)


accuracy_label = tk.Label(
    info_frame,
    text="Accuracy: 100%",
    font=("Arial", 14, "bold"),
    bg="#ffffff"
)

accuracy_label.pack(side="left", padx=25)


timer_label = tk.Label(
    info_frame,
    text="Time: 0s",
    font=("Arial", 14, "bold"),
    bg="#ffffff"
)

timer_label.pack(side="right", padx=25)


# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

settings_frame = tk.Frame(root, bg="#f4f6f8")
settings_frame.pack(pady=10)


tk.Label(
    settings_frame,
    text="Difficulty:",
    font=("Arial", 12),
    bg="#f4f6f8"
).pack(side="left", padx=5)


difficulty = ttk.Combobox(
    settings_frame,
    values=["Easy", "Medium", "Hard"],
    state="readonly",
    width=12
)

difficulty.set("Medium")
difficulty.pack(side="left", padx=10)


# --------------------------------------------------
# PARAGRAPH DISPLAY
# --------------------------------------------------

paragraph_frame = tk.Frame(
    root,
    bg="#ffffff",
    highlightbackground="#dddddd",
    highlightthickness=1
)

paragraph_frame.pack(
    fill="both",
    expand=False,
    padx=40,
    pady=15
)


paragraph_label = tk.Label(
    paragraph_frame,
    text="Click Start Test to begin",
    font=("Arial", 16),
    bg="#ffffff",
    fg="#333333",
    wraplength=850,
    justify="left",
    anchor="w"
)

paragraph_label.pack(
    fill="both",
    padx=25,
    pady=25
)


# --------------------------------------------------
# TEXT ENTRY
# --------------------------------------------------

entry = tk.Text(
    root,
    height=7,
    font=("Consolas", 15),
    wrap="word",
    padx=15,
    pady=15
)

entry.pack(
    fill="x",
    padx=40,
    pady=10
)


# --------------------------------------------------
# RESULT
# --------------------------------------------------

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#f4f6f8",
    fg="#333333"
)

result_label.pack(pady=10)


# --------------------------------------------------
# FUNCTIONS
# --------------------------------------------------

def start_test():
    global current_paragraph
    global start_time
    global test_running
    global total_typed
    global correct_typed

    selected_level = difficulty.get()

    current_paragraph = random.choice(
        paragraphs[selected_level]
    )

    paragraph_label.config(
        text=current_paragraph
    )

    entry.delete("1.0", tk.END)

    result_label.config(text="")

    total_typed = 0
    correct_typed = 0

    start_time = time.time()
    test_running = True

    entry.focus_set()

    update_stats()


def update_stats():
    global test_running

    if not test_running:
        return

    typed_text = entry.get("1.0", tk.END).rstrip("\n")

    elapsed = time.time() - start_time

    if elapsed <= 0:
        elapsed = 0.01

    # Words typed
    words = len(typed_text.split())

    # WPM
    wpm = int((words / elapsed) * 60)

    # Accuracy
    if len(typed_text) > 0:

        correct = 0

        for i in range(
            min(len(typed_text), len(current_paragraph))
        ):
            if typed_text[i] == current_paragraph[i]:
                correct += 1

        accuracy = int(
            (correct / len(typed_text)) * 100
        )

    else:
        accuracy = 100

    wpm_label.config(
        text=f"WPM: {wpm}"
    )

    accuracy_label.config(
        text=f"Accuracy: {accuracy}%"
    )

    timer_label.config(
        text=f"Time: {int(elapsed)}s"
    )

    # Check if paragraph completed
    if typed_text == current_paragraph:

        finish_test()

    else:

        root.after(
            200,
            update_stats
        )


def finish_test():

    global test_running

    test_running = False

    typed_text = entry.get(
        "1.0",
        tk.END
    ).rstrip("\n")

    elapsed = time.time() - start_time

    words = len(typed_text.split())

    if elapsed > 0:
        wpm = int(
            (words / elapsed) * 60
        )
    else:
        wpm = 0

    correct = 0

    for i in range(
        min(
            len(typed_text),
            len(current_paragraph)
        )
    ):

        if typed_text[i] == current_paragraph[i]:
            correct += 1

    if len(typed_text) > 0:

        accuracy = int(
            (correct / len(typed_text)) * 100
        )

    else:
        accuracy = 0

    result_label.config(
        text=(
            f"Test Complete!   "
            f"WPM: {wpm}   |   "
            f"Accuracy: {accuracy}%   |   "
            f"Time: {int(elapsed)} seconds"
        )
    )


def reset_test():

    global test_running

    test_running = False

    entry.delete(
        "1.0",
        tk.END
    )

    paragraph_label.config(
        text="Click Start Test to begin"
    )

    wpm_label.config(
        text="WPM: 0"
    )

    accuracy_label.config(
        text="Accuracy: 100%"
    )

    timer_label.config(
        text="Time: 0s"
    )

    result_label.config(
        text=""
    )


# --------------------------------------------------
# BUTTONS
# --------------------------------------------------

button_frame = tk.Frame(
    root,
    bg="#f4f6f8"
)

button_frame.pack(pady=10)


start_button = tk.Button(
    button_frame,
    text="Start Test",
    font=("Arial", 13, "bold"),
    bg="#2563eb",
    fg="white",
    padx=25,
    pady=10,
    command=start_test
)

start_button.pack(
    side="left",
    padx=10
)


reset_button = tk.Button(
    button_frame,
    text="New Test",
    font=("Arial", 13),
    padx=25,
    pady=10,
    command=reset_test
)

reset_button.pack(
    side="left",
    padx=10
)


# --------------------------------------------------
# START APPLICATION
# --------------------------------------------------

root.mainloop()
