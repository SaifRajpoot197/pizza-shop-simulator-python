import tkinter as tk

money = 10000
pizzas = 0

window = tk.Tk()
window.title("Pizza Shop")
window.geometry("800x600")
window.config(bg="#FFD700") 

label = tk.Label(window, text="🍕 PIZZA SHOP 🍕", font=("Arial", 35, "bold"), bg="#FFD700", fg="red")
label.pack(pady=20)

label_money = tk.Label(window, text="Money: 10000", font=("Arial", 25, "bold"), bg="white")
label_money.pack(pady=10)

label2 = tk.Label(window, text="Pizzas Bought: 0", font=("Arial", 20), bg="#FFD700")
label2.pack(pady=10)

def buy_small():
    global money, pizzas
    if money >= 500:
        money -= 500
        pizzas += 1
        label_money.config(text="Money: " + str(money))
        label2.config(text="Pizzas Bought: " + str(pizzas))
    else:
        label2.config(text="Not Enough Money!")

def buy_large():
    global money, pizzas
    if money >= 1200:
        money -= 1200
        pizzas += 1
        label_money.config(text="Money: " + str(money))
        label2.config(text="Pizzas Bought: " + str(pizzas))
    else:
        label2.config(text="Not Enough Money!")

def earn_money():
    global money
    money += 2000
    label_money.config(text="Money: " + str(money))

tk.Button(window, text="Buy Small Pizza - 500", command=buy_small, font=("Arial", 15, "bold"), bg="orange", fg="white").pack(pady=10)
tk.Button(window, text="Buy Large Pizza - 1200", command=buy_large, font=("Arial", 15, "bold"), bg="green", fg="white").pack(pady=10)
tk.Button(window, text="Earn Money +2000", command=earn_money, font=("Arial", 15, "bold"), bg="blue", fg="white").pack(pady=10)

window.mainloop()