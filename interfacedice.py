import tkinter as tk
import random
win = tk.Tk()
win.title("HELLO THERE!")
win.minsize(500, 400)

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

def ClickDice():
    try:
        num_of_dice = int(entry.get())
        dice = [random.randint(1, 6) for _ in range(num_of_dice)]  # the result here is the random.randint(1, 6) for thr number of dice
        total = sum(dice)
        
        result_text.set("")
        for line in range(5):
            result_text.set(result_text.get() + "".join(dice_art[die][line] + " " for die in dice) + "\n")
        result_text.set(result_text.get() + f"\nTotal: {total}")

    except ValueError:
        result_text.set("Not a valid number")
        
entry = tk.Entry(win)
entry.pack()

btndice = tk.Button(win, text="ClickDice", command=ClickDice)
btndice.pack()

result_text = tk.StringVar()
result_label = tk.Label(win, textvariable=result_text, font=("Courier", 12))
result_label.pack()


win.mainloop()