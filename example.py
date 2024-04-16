import time

def time_profiler(func):
    def inner(*args, **kwargs):
        t_start = time.process_time_ns()
        result = func(*args, **kwargs)
        t_end = time.process_time_ns()
        print(f"{(t_end - t_start)/10E9} seconds")
        return result
    return inner

@time_profiler
def measure_me(n):
    total = 0
    for i in range(n):
        total += i * i

    return total

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"{self.name} by {self.author}"


if __name__ == "__main__":
    measure_me(10_000_000)
    print(Book(name = 'A book', author = 'me'))