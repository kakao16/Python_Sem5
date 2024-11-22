# Stanisław Kusiak

class Fibonacci:
    current, next = 0, 1
    index = 0
    def __init__(self, stop):
        self.stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.stop:
            self.index += 1    
            fib = self.current
            self.current, self.next = self.next, self.current + self.next
            return fib
        else:
            raise StopIteration
  
        
fibonacci = Fibonacci(10)
fibIter = iter(fibonacci)

for i in fibIter:
    print(i)
