# from flask import Flask

# app = Flask(__name__)

# def make_bold(function):
#     def wrapper_function(*args, **kwargs):
#         return f"<b>{function(*args, **kwargs)}</b>"
#     return wrapper_function

# def make_underline(function):
#     def wrapper_function(*args, **kwargs):
#         return f"<u>{function(*args, **kwargs)}</u>"
#     return wrapper_function

# def make_italic(function):
#     def wrapper_function(*args, **kwargs):
#         return f"<i>{function(*args, **kwargs)}</i>"
#     return wrapper_function

# @app.route("/<name>/<age>")
# @make_bold
# @make_italic
# @make_underline
# def hello_world(name, age):
#     return f"Hello {name}, you are {age} old!"



# @app.route("/")
# def index():
#     return '''
#         <h1 style="text-align: center">Hello World</h1>
#         <p>This is a paragraph.</p>
#         <img src="https://www.bbc.co.uk/news/in-pictures-56211135" alt="Image from BBC">
#     '''

# if __name__ == "__main__":
#     app.run(debug=True)
# # inputs = eval(input())
# # # TODO: Create the logging_decorator() function 👇



# # # TODO: Use the decorator 👇

# # def logging_decorator(function):
# #   def wraper_function(*args, **kwargs):
# #     print(f"You called {function.__name__}({args[0]},{args[1]},{args[2]})")
# #     print(f"It returned: {function(*args, **kwargs)}")
# #   return wraper_function
  
# # @logging_decorator
# # def a_function(a, b, c):
# #   return a * b * c

# # a_function(inputs[0], inputs[1], inputs[2])



from flask import Flask
from random import randint

app = Flask(__name__)

NUMBER = randint(0, 9)

def check_func(fn):
    def wrapper_func(number):
        try:
            guess = int(number)
        except ValueError:
            return '''<h1>Invalid input. Please enter a number between 0 and 9.</h1>'''

        if guess == NUMBER:
            return '''<h1>You guessed the correct number!</h1>
                      <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzM2bDFrZzZxdDN6bWhwOWU0MHRleTBiYnIyZ2t2ZzVhd3FjY3Z5ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26tknCqiJrBQG6bxC/giphy.webp"
                      alt="Number gif">'''
        elif guess < NUMBER:
            return '''<h1>Guess Higher</h1>
                      <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnhrbG53NnFnZ2l4bGs3cWk1ZmJ1bDM2YzRhZ2N2ZHEwdHZ4czNjaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iIppd7C1OmVNKwuHZB/giphy.webp"
                      alt="Guess Higher gif">'''
        else:
            return '''<h1>Guess Lower</h1>
                      <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzBsb2J1d2gybG96aHp6emNkbjB1N2Qwa3oweDZkMG12cDJieXlrYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hPPx8yk3Bmqys/giphy.webp"
                      alt="Guess Lower gif">'''
        
        return fn(number)
    return wrapper_func

@app.route("/<int:number>")
@check_func
def num(number):
    return ""

@app.route("/")
def opening():
    return '''<h1>Guess a number between 0 and 9</h1>
              <img src="https://i.giphy.com/3o7aCSPqXE5C6T8tBC.webp" alt="Number gif">'''

if __name__ == "__main__":
    app.run(debug=True)
