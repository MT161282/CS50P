class Jar:
    def __init__(self, capacity=12):
        if type(capacity) is not int or capacity < 0:
            raise ValueError

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "\U0001F36A" * self.size

    def deposit(self, n):
        if type(n) is not int or n < 0:
            raise ValueError

        if self.size + n > self.capacity:
            raise ValueError

        self._size += n

    def withdraw(self, n):
        if type(n) is not int or n < 0:
            raise ValueError

        if n > self.size:
            raise ValueError

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
