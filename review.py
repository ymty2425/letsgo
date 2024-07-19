# Review 1
def add_to_list(value, my_list=[]):

    my_list.append(value)

    return my_list


# Review 1 fixed
# Use None as the default value for my_list, and create a new list if my_list is None.
def add_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


# Review 2
def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."


# Review 2 fixed
# Use f-string instead since in the origianl string format, the {} won't be interpreted as placeholders.
def format_greeting(name, age):
    return f"Hello, my name is {name} and I am {age} years old."


# Review 3


class Counter:
    count = 0

    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count


# Review 3 fixed
# Use an instance variable instead of a class variable to increment the count for each instance.
class Counter:
    def __init__(self):
        self.count = 1

    def get_count(self):
        return self.count


# Review 4

import threading


class SafeCounter:

    def __init__(self):

        self.count = 0

    def increment(self):

        self.count += 1


def worker(counter):

    for _ in range(1000):

        counter.increment()


counter = SafeCounter()

threads = []

for _ in range(10):

    t = threading.Thread(target=worker, args=(counter,))

    t.start()

    threads.append(t)


for t in threads:

    t.join()

# Review 4 fixed
# Add a lock to ensure that only onw thread can modify the count at a time.
import threading


class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()


# Review 5


def count_occurrences(lst):
    counts = {}

    for item in lst:
        if item in counts:
            counts[item] = +1
        else:
            counts[item] = 1

    return counts


# Review 5 fixed
# Use += instead of =+ to increment the count of each item. That's the only thing I noticed.
def count_occurrences(lst):
    counts = {}

    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts
