import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import main

cur_tarot_array = []


def get_unique_card_indices(spread_len):
    indices = []
    while len(indices) < spread_len:
        i = len(indices) + 1
        try:
            index = int(tk.simpledialog.askstring(f"Choose Card {i}", f"The {main.ordinal(i)} card. {spread_len} cards totally (第{i}张牌。共{spread_len}张牌):"))
            print(index)
            if 1 <= index <= 78 and index not in indices:
                indices.append(index)
            else:
                raise ValueError()
        except ValueError:
            pass
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer (无效输入。请输入正确的数字)。")
    return indices


def shuffle():
    global cur_tarot_array
    cur_tarot_array = main.shuffle(cur_tarot_array)
    messagebox.showinfo("Shuffle Result", "Shuffling complete.(洗牌结束)")


class TarotApp:
    def __init__(self, root):
        global cur_tarot_array
        cur_tarot_array = main.shuffle(cur_tarot_array)
        self.root = root
        self.root.title("Tarot Divination")

        self.paned_window = tk.PanedWindow(root, orient=tk.VERTICAL)
        self.paned_window.pack(expand=True, fill='both')

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        question_label = tk.Label(self.root, text="Question(问题):")
        question_label.pack()

        self.question_entry = tk.Entry(self.root)
        self.question_entry.pack()

        shuffle_button = tk.Button(self.root, text="Shuffle (洗牌)", command=shuffle)
        shuffle_button.pack()

        pick_cards_button = tk.Button(self.root, text="Pick Cards (抽牌)", command=self.pick_cards)
        pick_cards_button.pack()

    def pick_cards(self):
        # question
        question = self.question_entry.get()
        if not question:
            messagebox.showwarning("Warning", "Please enter a question before picking cards.")
            return

        # card number
        while True:
            try:
                spread_len = main.get_valid_spread_len(tk.simpledialog.askstring("Cards Needed", "Please enter the "
                                                                                                "number of cards "
                                                                                                "needed for the "
                                                                                                "spread (请输入牌阵所需牌数):"))
                break
            except ValueError as e:
                pass
                print(e)
                messagebox.showerror("Error", str(e))

        # each card index
        indices = get_unique_card_indices(spread_len)

        # each card value
        cards_values = [cur_tarot_array[index - 1] for index in indices]

        result_window = tk.PanedWindow(self.paned_window, orient=tk.VERTICAL)
        result_window.pack(expand=True, fill='both')

        tk.Label(result_window, text=f"Question(问题): {question}").pack()
        tk.Label(result_window, text=f"Number of cards in the spread(牌阵牌数): {spread_len}").pack()

        for i, value in enumerate(cards_values, start=1):
            print(f"The {main.ordinal(i)} card(第{i}张牌) : {value} {main.interpret_orientation(value)}")
            card_label = tk.Label(result_window,
                                  text=f"The {main.ordinal(i)} card(第{i}张牌) : {main.interpret_orientation(value)}")
            card_label.pack()

        self.question_entry.delete(0, 'end')
        question = ""

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?(是否退出？)"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TarotApp(root)
    root.mainloop()
