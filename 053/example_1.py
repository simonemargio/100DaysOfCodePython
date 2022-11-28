from time import sleep


def decorator(function):
    def delay_func():
        sleep(2)
        function()

    return delay_func


@decorator
def hello():
    print("HELLO")


hello()