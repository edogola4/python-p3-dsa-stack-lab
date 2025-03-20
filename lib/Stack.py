class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        return len(self.items) == 0
        pass

    def push(self, item):
        if self.limit is not None and len(self.items) >= self.limit:
            return
        self.items.append(item)
        pass

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()
        pass

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)
        pass

    def full(self):
        if self.limit is not None and len(self.items) >= self.limit:
            return True
        return False
        pass

    def search(self, target):
        try:
            return self.items[::-1].index(target)
        except ValueError:
            return -1
        pass
