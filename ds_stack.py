class Stack(list):

    def extend(self, iterable):
        pass

    def push(self, elem):
        self.append(elem)

    def remove(self,value):
        pass

    def insert(self, index, value):
        pass

    def empty(self):
        if not len(self):
            return True
        return False

    def clear(self):
        pass

    def top(self):
        return self[-1]








