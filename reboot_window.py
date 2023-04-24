# Прикольный код который выводит окошко предлагающее перезаупстить компуктер.
# Код коротенький но мне нравится, Видно какой есть потенциал для всяких програмулек.

import shutdown_minicode
import tkinter as tk
from tkinter import messagebox

def confirmation():
    # Создаем окно.
    root = tk.Tk()
    root.withdraw()
    # Показываем окно с подтверждением.
    result = messagebox.askyesno("Перезапуск", "Перезапустить компьютер?")
    if result:
        main.off()
    else:
        print("Действие отменено")


confirmation()