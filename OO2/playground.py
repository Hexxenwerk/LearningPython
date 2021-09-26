def decorate_message(fun):
    # Nested function
    def add_welcome(site_name) -> str:
        return "Welcome to " + fun(site_name)

    # Decorator returns a function
    return add_welcome


@decorate_message
def site(site_name: str) -> str:
    return site_name


# This call is equivalent to call to
# decorate_message() with function
# site("GeeksforGeeks") as parameter
print(site("GeeksforGeeks"))
