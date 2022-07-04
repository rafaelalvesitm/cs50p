class Jar:
    def __init__(self, capacity=12, size=0):
        if capacity < 0:
            raise ValueError("Capacity must be positive.")
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        content = self.size + n
        if content > self.capacity:
            raise ValueError("Cannot deposit more cookies than capacity.")
        else:
            self.size = content
            print(f"Deposited {n} cookies.")

    def withdraw(self, n):
        content = self.size - n
        if content < 0:
            raise ValueError("Cannot withdraw more cookies than there are.")
        else:
            self.size = content
            print(f"Withdrew {n} cookies.")

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Capacity must be positive.")
        self._capacity = n

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, n):
        self._size = n
