from functools import wraps
from time import sleep

class LinkedList():
    def __init__(self, values=None):
        self.head = None
        if values:
            for value in reversed(values):
                self.insert(value)

    @property
    def __str__(self):
        txt = ''
        for value in self:
            txt += f'{{ {value} }} ->'
        return txt + 'None'

    def __iter__(self):
        def generate_values():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return generate_values()

    def __len__(self):
        return len(list(iter(self)))

    def __eq__(self, other):
        return list(self) == list(other)

    def __getitem__(self, index):
        if index < 0:
            raise IndexError
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError

    def insert(self, value):
        self.head = Node(value, self.head)


class Node():
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


# Starting Wrappers


def pause(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(1)
        return func(*args, **kwargs)

    return wrapper


def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return orig_val + '!!!'

    return wrapper


@pause
@emphasize
def hey_world():
    return('hey world')

print(hey_world())