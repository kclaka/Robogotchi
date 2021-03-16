def tagged(func):
    def wrapper(str):
        return "<title>" + func(str) + "</title>"

    return wrapper


@tagged
def from_input(inp):
    string = inp.strip()
    return string



