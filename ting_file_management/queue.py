class Queue:
    def __init__(self):
        self.__data = []

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        return self.__data.pop(0)

    def search(self, index):
        if index not in range(0, len(self.__data)):
            raise IndexError
        return self.__data[index]
