from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def flip_card():
    global current_card
    c.itemconfig(card_background, image=image_card_back)
    c.itemconfig(card_title, text="Italian", fill="white")
    c.itemconfig(card_word, text=current_card["Italian"], fill="white")


def set_new_card():
    global current_card
    current_card = new_card()
    print(current_card)
    c.itemconfig(card_title, text="English", fill="black")
    c.itemconfig(card_word, text=current_card["English"], fill="black")
    w.after(3000, func=flip_card)
    c.itemconfig(card_background, image=image_card_front)


def new_card():
    return random.choice(data)


def is_know():
    global current_card
    data.remove(current_card)
    data_to_save = pandas.DataFrame(data)
    data_to_save.to_csv("data/words_to_learn.csv")
    set_new_card()


try:
    data_csv = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv")
    data = original_data.to_dict(orient="records")
else:
    data = data_csv.to_dict(orient="records")

w = Tk()
w.title("Flash Cards")
w.config(padx=50, pady=50, background=BACKGROUND_COLOR)
c = Canvas(width=800, height=526, highlightthickness=0)
image_card_front = PhotoImage(file="images/card_front.png")
image_card_back = PhotoImage(file="images/card_back.png")
card_background = c.create_image(400, 263, image=image_card_front)
c.config(bg=BACKGROUND_COLOR)
c.grid(column=0, row=0, columnspan=2)

card_title = c.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
card_word = c.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

image_button_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_button_wrong, highlightthickness=0, command=set_new_card)
button_wrong.grid(column=0, row=1)

image_button_correct = PhotoImage(file="images/right.png")
button_correct = Button(image=image_button_correct, highlightthickness=0, command=is_know)
button_correct.grid(column=1, row=1)

set_new_card()

w.mainloop()
