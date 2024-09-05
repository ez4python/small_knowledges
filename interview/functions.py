"""
--- decorators
"""
import inspect
import traceback


def name_of_decorator(func):
    def inner(*args, **kwargs):
        print(f'Before {func.__name__}')
        print(f'Function name: {inspect.currentframe().f_code.co_name}')  # get self(function).__name__
        result = func(*args, **kwargs)
        print('After')
        return result

    return inner


# 1-function: What does this code do? Hint: this code belongs to this theme
@name_of_decorator
def add_element(new: list[str] | str, src: list | None = None) -> list:
    stack = traceback.extract_stack()[-1].filename  # full filepath
    print(f'filename: {stack}')
    if src is None:
        src = []
    if isinstance(new, list):
        src.extend(new)
    else:
        src.append(new)
    return src


if __name__ == "__main__":
    value1 = add_element("test")
    print(value1)
    value2 = add_element(["test2", "test3"])
    print(value2)
    value3 = add_element("test4", value2)
    print(value3)
