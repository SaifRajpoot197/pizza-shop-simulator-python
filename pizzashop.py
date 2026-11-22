import tkinter as tk

money = 10000
pizzas = 0

window = tk.Tk()
window.title("Pizza Shop")
window.geometry("800x600")

label = tk.Label(window, text="Money: 10000", font=("Arial", 30))
label.pack(pady=20)

label2 = tk.Label(window, text="Pizzas Bought: 0", font=("Arial", 20))
label2.pack(pady=20)

def buy_small():
    global money, pizzas
    if money >= 500:
        money -= 500
        pizzas += 1
        label.config(text="Money: " + str(money))
        label2.config(text="Pizzas Bought: " + str(pizzas))
    else:
        label2.config(text="Not Enough Money!")

def buy_large():
    global money, pizzas
    if money >= 1200:
        money -= 1200
        pizzas += 1
        label.config(text="Money: " + str(money))
        label2.config(text="Pizzas Bought: " + str(pizzas))
    else:
        label2.config(text="Not Enough Money!")

def earn_money():
    global money
    money += 2000
    label.config(text="Money: " + str(money))

button = tk.Button(window, text="Buy Small Pizza - 500", command=buy_small, font=("Arial", 15))
button.pack(pady=10)

button2 = tk.Button(window, text="Buy Large Pizza - 1200", command=buy_large, font=("Arial", 15))
button2.pack(pady=10)

button3 = tk.Button(window, text="Earn Money +2000", command=earn_money, font=("Arial", 15))
button3.pack(pady=10)

window.mainloop()