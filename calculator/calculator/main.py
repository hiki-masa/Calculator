import tkinter as tk
import calculator as calc

def main():
    win = tk.Tk()
    app = calc.CALCULATOR(master = win)
    app.mainloop()

if __name__ == "__main__":
    main()