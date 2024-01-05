import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import main

cur_tarot_array = []


class TarotApp:
    def __init__(self, root):
        global cur_tarot_array
        cur_tarot_array = main.shuffle(cur_tarot_array)
        self.root = root
        self.root.title("Tarot Divination")

        # 获取屏幕的宽度和高度
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # 设置窗口的宽度和高度
        window_width = 450
        window_height = 300

        # 计算窗口放置在屏幕中央的坐标
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.paned_window = tk.PanedWindow(root, orient=tk.VERTICAL)
        self.paned_window.pack(expand=True, fill='both')

        # 设置窗口的geometry
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        # self.root.geometry("")

        # 设置窗口的最小尺寸
        root.minsize(width=450, height=130)

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # 创建一个Canvas用于显示卡牌结果
        self.result_canvas = tk.Canvas(self.paned_window)
        self.result_canvas.pack(side=tk.LEFT, expand=True, fill='both')

        # 创建一个滚动条
        self.result_scrollbar = tk.Scrollbar(self.paned_window, orient=tk.VERTICAL, command=self.result_canvas.yview)
        self.result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # 将Canvas的yview与滚动条关联
        self.result_canvas.configure(yscrollcommand=self.result_scrollbar.set)

        # 创建一个Frame，用于放置卡牌结果
        self.result_frame = tk.Frame(self.result_canvas)
        self.result_canvas.create_window((0, 0), window=self.result_frame, anchor=tk.NW)

    def create_widgets(self):
        original_window = tk.PanedWindow(self.paned_window, orient=tk.VERTICAL)
        original_window.pack(expand=True, fill='both')

        frame = tk.Frame(original_window)
        frame.pack(side=tk.TOP)

        question_label = tk.Label(frame, text="Question(问题):")
        question_label.pack()

        self.question_entry = tk.Entry(frame)
        self.question_entry.pack()

        shuffle_button = tk.Button(frame, text="Shuffle (洗牌)", command=self.shuffle)
        shuffle_button.pack(side=tk.LEFT, padx=10, pady=10)

        pick_cards_button = tk.Button(frame, text="Pick Cards (抽牌)", command=self.pick_cards)
        pick_cards_button.pack(side=tk.LEFT, padx=10, pady=10)

    def shuffle(self):
        global cur_tarot_array
        cur_tarot_array = main.shuffle(cur_tarot_array)
        shuffle_finish_win = tk.Toplevel()
        shuffle_finish_win.title("Shuffle Result")
        shuffle_finish_win.geometry("200x40")
        shuffle_finish_win.wait_visibility()
        tk.Message(shuffle_finish_win, text="Shuffling complete.(洗牌结束)", padx=5, pady=50).pack()

        x = root.winfo_x() + root.winfo_width()//2-shuffle_finish_win.winfo_width()//2
        y = root.winfo_y() + root.winfo_height()//2 - shuffle_finish_win.winfo_height()//2
        shuffle_finish_win.geometry("+%d+%d" % (x, y))

        shuffle_finish_win.after(500, shuffle_finish_win.destroy)

    def pick_cards(self):
        # question
        try:
            question = main.get_question(self.question_entry.get())
        except ValueError as e:
            messagebox.showwarning("Error", str(e))
            return

        # Number of cards in the spread
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
        indices = []
        while len(indices) < spread_len:
            i = len(indices) + 1
            try:
                index = main.get_unique_card_indices(tk.simpledialog.askstring(f"{', '.join(map(str, indices))}",
                                                                               f"The {main.ordinal(i)} card. {spread_len} cards totally (第{i}张卡。共{spread_len}张牌):"),
                                                     indices)
                indices.append(index)
            except ValueError as e:
                pass
                messagebox.showerror("Error", str(e))

        # each card value
        cards_values = [cur_tarot_array[index - 1] for index in indices]

        # result generate
        new_result_frame = tk.Frame(self.result_frame)
        new_result_frame.pack()

        # 添加你的标签和其他控件到Frame中
        tk.Label(new_result_frame, text=f"\nQuestion(问题): {question}").pack()
        tk.Label(new_result_frame, text=f"Number of cards in the spread(牌阵牌数): {spread_len}").pack()

        for i, value in enumerate(cards_values, start=1):
            card_text = f"The {main.ordinal(i)} card(第{i}张牌) : {main.interpret_orientation(value)}"
            tk.Label(new_result_frame, text=card_text).pack()

        # 更新Canvas的大小
        new_result_frame.update_idletasks()

        # 配置Canvas的滚动区域
        self.result_canvas.config(scrollregion=self.result_canvas.bbox("all"))

        # 打开滚动区域的更新
        self.result_canvas.update_idletasks()

        self.question_entry.delete(0, 'end')
        question = ""

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?(是否退出？)"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TarotApp(root)
    root.mainloop()
