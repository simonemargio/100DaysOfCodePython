from flask import Flask
import random

app = Flask(__name__)

RANDOM_NUBER = random.randint(0, 9)
GIF_RANDOM_NUMBER = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
GIF_FOUND = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
GIF_LOW = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
GIF_HIGH = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"


@app.route('/')
def index():
    return '<h1>Guess a number between 0 and 9</h1>' \
           f'<br><img src="{GIF_RANDOM_NUMBER}">'


@app.route('/<int:number>')
def guess_number(number):
    if number == RANDOM_NUBER:
        return '<h1 style="color:green;">You found me!</h1>' \
               f'<br><img src="{GIF_FOUND}">'
    elif number < RANDOM_NUBER:
        return '<h1 style="color:red;">Too low!</h1>' \
               f'<br><img src="{GIF_LOW}">'
    else:
        return '<h1 style="color:red;">Too high!</h1>' \
               f'<br><img src="{GIF_HIGH}">'


if __name__ == "__main__":
    print(RANDOM_NUBER)
    app.run(debug=True)
