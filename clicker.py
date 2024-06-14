import tkinter as tk
import threading
import keyboard
import time
import mouse

class AutoClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Автокликер")
        self.root.geometry("300x200")
        self.work = False
        self.click_speed = 0.1  # Начальная скорость кликов (в секундах)

        # Создание и настройка виджетов
        tk.Label(root, text="Нажмите 'ё' чтобы начать/остановить автокликер", font=("Arial", 12)).pack(pady=10)
        self.status_label = tk.Label(root, text="Статус: Остановлен", font=("Arial", 12))
        self.status_label.pack(pady=10)

        tk.Label(root, text="Скорость кликов (кликов в секунду):", font=("Arial", 12)).pack(pady=10)
        self.speed_scale = tk.Scale(root, from_=1, to=100, orient="horizontal", command=self.update_speed)
        self.speed_scale.set(10)  # Установка начального значения
        self.speed_scale.pack(pady=10)

        tk.Button(root, text="Начать", command=self.start_clicker, font=("Arial", 12), bg="green", fg="white").pack(pady=10)
        tk.Button(root, text="Остановить", command=self.stop_clicker, font=("Arial", 12), bg="red", fg="white").pack(pady=10)

        keyboard.add_hotkey('ё', self.toggle_clicker)

    def toggle_clicker(self):
        self.work = not self.work
        self.update_status()

    def start_clicker(self):
        self.work = True
        self.update_status()
        threading.Thread(target=self.click_loop, daemon=True).start()

    def stop_clicker(self):
        self.work = False
        self.update_status()

    def update_status(self):
        self.status_label.config(text=f"Статус: {'Работает' if self.work else 'Остановлен'}")

    def update_speed(self, value):
        self.click_speed = 1 / int(value)

    def click_loop(self):
        while True:
            if self.work:
                mouse.click(button='left')
                time.sleep(self.click_speed)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClicker(root)
    root.mainloop()
