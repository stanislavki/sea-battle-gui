import tkinter as tk
 class BattleshipGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Морской бой")
        # Размеры
        self.cell_size = 30
        self.field_size = 10
        # Цвета
        self.colors = {
            0: "lightblue",   # Пустая клетка
            1: "gray",        # Корабль
            2: "white",       # Промах
            3: "orange",      # Попадание
            4: "red"          # Уничтожен
        }
        self.setup_main_menu()
    def setup_main_menu(self):
        """Главное меню"""
        # Очищаем окно
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
        print("Игра с другом")  # Заглушка
    def start_vs_bot(self):
        """Начать игру с ботом"""
        print("Игра с ботом")  # Заглушка
    def run(self):
        self.window.mainloop()
 if __name__ == "__main__":
    app = BattleshipGUI()
    app.run()