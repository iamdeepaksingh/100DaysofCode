
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"You called {func.__name__}{args}")
        result = func(args[0], args[1], args[2])
        print(f"It returned: {result}")
        func(*args)
    return wrapper()


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)

new_user = User("Deepak")
new_user.is_logged_in = True
create_blog_post(new_user)