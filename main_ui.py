import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import data_processing
from constants import ErrorMessages, UIConstants

cur_tarot_array = data_processing.shuffle()
result_scrollbar_created = False


class TarotApp:
    def __init__(self, root):
        self.root = root
        self.root.title(UIConstants.ROOT_TITLE)

        # 获取屏幕的宽度和高度
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = UIConstants.ROOT_INIT_WIN_WIDTH
        window_height = UIConstants.ROOT_INIT_WIN_HEIGHT

        # 计算窗口放置在屏幕中央的坐标
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.paned_window = tk.PanedWindow(root, orient=tk.VERTICAL)
        self.paned_window.pack(expand=True, fill='both')

        # 设置窗口的geometry
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 设置窗口的最小尺寸
        root.minsize(width=450, height=100)
        # root.maxsize(width=450, height=100)

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Create canvas and frame for showing result
        self.result_canvas = tk.Canvas(self.paned_window)
        self.result_canvas.pack(side=tk.LEFT, expand=True, fill='both')

        self.result_frame = tk.Frame(self.result_canvas)
        self.result_canvas.create_window((0, 0), window=self.result_frame, anchor=tk.NW)

    def create_widgets(self):
        original_window = tk.PanedWindow(self.paned_window, orient=tk.VERTICAL)
        original_window.pack(expand=True, fill='both')

        frame = tk.Frame(original_window)
        frame.pack(side=tk.TOP)

        question_label = tk.Label(frame, text=UIConstants.QUESTION)
        question_label.pack()

        self.question_entry = tk.Entry(frame)
        self.question_entry.pack()

        shuffle_button = tk.Button(frame, text=UIConstants.SHUFFLE, command=self.shuffle)
        shuffle_button.pack(side=tk.LEFT, padx=10, pady=10)

        pick_cards_button = tk.Button(frame, text=UIConstants.PICK_CARDS, command=self.pick_cards)
        pick_cards_button.pack(side=tk.LEFT, padx=10, pady=10)

    def shuffle(self):
        # Get shuffle cards data
        global cur_tarot_array
        cur_tarot_array = data_processing.shuffle()

        # Shuffle UI
        shuffle_finish_win = tk.Toplevel()
        shuffle_finish_win.title(UIConstants.SHUFFLE_RESULT)
        shuffle_finish_win.geometry(f"{UIConstants.SHUFFLE_FINISH_WIN_WIDTH}x{UIConstants.SHUFFLE_FINISH_WIN_HEIGHT}")
        shuffle_finish_win.wait_visibility()
        tk.Message(shuffle_finish_win, text=UIConstants.SHUFFLING_COMPLETE, padx=5, pady=50).pack()

        x = root.winfo_x() + root.winfo_width()//2-shuffle_finish_win.winfo_width()//2
        y = root.winfo_y() + root.winfo_height()//2 - shuffle_finish_win.winfo_height()//2
        shuffle_finish_win.geometry("+%d+%d" % (x, y))

        shuffle_finish_win.after(500, shuffle_finish_win.destroy)

    def pick_cards(self):
        # question
        try:
            question = data_processing.get_question(self.question_entry.get())
        except ValueError as e:
            messagebox.showwarning("Question Value Error", str(e))
            return

        # Number of cards in the spread
        while True:
            try:
                spread_len = data_processing.get_valid_spread_len(tk.simpledialog.askstring("Cards Needed", UIConstants.CARDS_NEED))
                break
            except ValueError as e:
                pass
                print(e)
                messagebox.showerror("Cards Needed Value Error", str(e))
            except TypeError:
                return

        # each card index
        cards_value = []
        while len(cards_value) < spread_len:
            i = len(cards_value) + 1
            try:
                value = data_processing.get_unique_card_value(tk.simpledialog.askstring(', '.join(map(str, [card[0] for card in cards_value])),
                                                                               UIConstants.CARDS_VALUE.format(data_processing.ordinal(i), spread_len, i, spread_len)), cards_value)
                cards_value.append(value)
            except ValueError as e:
                pass
                print(e)
                messagebox.showerror("Card Index Value Error", str(e))
            except TypeError:
                return

        # Result generate
        global result_scrollbar_created
        if not result_scrollbar_created:
            result_scrollbar_created = True
            result_scrollbar = tk.Scrollbar(self.paned_window, orient=tk.VERTICAL, command=self.result_canvas.yview)
            result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.result_canvas.configure(yscrollcommand=result_scrollbar.set)
            root.geometry(f"{UIConstants.ROOT_INIT_WIN_WIDTH}x{UIConstants.ROOT_ADJUSTED_WIN_HEIGHT}")

        new_result_frame = tk.Frame(self.result_frame)
        new_result_frame.pack()

        tk.Label(new_result_frame, text=f"\n{UIConstants.QUESTION} {question}").pack()
        tk.Label(new_result_frame, text=f"{UIConstants.NUMBER_OF_CARDS} {spread_len}").pack()

        # Each card value
        for i, value in enumerate(cards_value, start=1):
            card_text = f"The {data_processing.ordinal(i)} card(第{i}张牌) : {value[1]}"
            tk.Label(new_result_frame, text=card_text).pack()

        new_result_frame.update_idletasks()
        self.result_canvas.config(scrollregion=self.result_canvas.bbox("all"))
        self.result_canvas.update_idletasks()

        # 清空Question区域
        self.question_entry.delete(0, 'end')
        question = ""

    def on_closing(self):
        if messagebox.askokcancel("Quit", UIConstants.QUIT):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TarotApp(root)
    root.mainloop()
