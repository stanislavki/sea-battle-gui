import tkinter as tk
 class BattleshipGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Морской бой")
        self.cell_size = 30
        self.field_size = 10
        self.colors = {
            0: "lightblue",
            1: "gray",
            2: "white",
            3: "orange",
            4: "red"
        }
        self.setup_main_menu()
    def setup_main_menu(self):
        """Главное меню"""
        for widget in self.window.winfo_children():
            widget.destroy()
        title = tk.Label(self.window, text="МОРСКОЙ БОЙ", font=("Arial", 24))
        title.pack(pady=20)
        btn_vs_friend = tk.Button(
            self.window,
            text="Играть с другом",
            font=("Arial", 14),
            command=self.start_vs_friend
        )
        btn_vs_friend.pack(pady=10)
        btn_vs_bot = tk.Button(
            self.window,
            text="Играть с компьютером",
            font=("Arial", 14),
            command=self.start_vs_bot
        )
        btn_vs_bot.pack(pady=10)
    def start_vs_friend(self):
        """Начать игру с другом"""
        print("Игра с другом")
    def start_vs_bot(self):
        """Начать игру с ботом"""
        print("Игра с ботом")
    def run(self):
        self.window.mainloop()
 if __name__ == "__main__":
    app = BattleshipGUI()
    app.run()


def create_field_canvas(self, parent, title, clickable=False, click_callback=None):
    """Создать канвас с игровым полем"""
    frame = tk.Frame(parent)
    label = tk.Label(frame, text=title, font=("Arial", 12))
    label.pack()
    canvas = tk.Canvas(
        frame,
        width=self.cell_size * self.field_size,
        height=self.cell_size * self.field_size
    )
    canvas.pack()

    for i in range(self.field_size + 1):
        x = i * self.cell_size
        canvas.create_line(x, 0, x, self.field_size * self.cell_size)
        canvas.create_line(0, x, self.field_size * self.cell_size, x)
    if clickable and click_callback:
        canvas.bind("<Button-1>", lambda e: self.on_field_click(e, click_callback))
    return frame, canvas


def on_field_click(self, event, callback):
    """Обработка клика по полю"""
    x = event.x // self.cell_size
    y = event.y // self.cell_size
    if 0 <= x < self.field_size and 0 <= y < self.field_size:
        callback(x, y)


def draw_field(self, canvas, field_data):
    """Отрисовать поле по данным"""
    for y in range(self.field_size):
        for x in range(self.field_size):
            cell = field_data[y][x]
            color = self.colors.get(cell, "lightblue")
            x1 = x * self.cell_size
            y1 = y * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")