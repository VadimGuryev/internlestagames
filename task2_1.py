"""
Для решения данной задачи, пришлось немного воспользоваться гуглом и документацией, тк на практике FIFO не нужно было.
Первый пример тут второй и вывод в task2_2

"""


class CircularBufferList:
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def addelem(self, value):
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.size
        if self.head == self.tail:
            self.tail = (self.tail + 1) % self.size

    def getelem(self):
        if self.is_empty():
            raise IndexError("Буфер пуст")
        value = self.buffer[self.tail]
        self.tail = (self.tail + 1) % self.size
        return value

    def is_empty(self):
        return self.head == self.tail

    def __str__(self):
        return f"Buffer: {self.buffer}"


buffer1 = CircularBufferList(3)
buffer1.addelem(1)
buffer1.addelem(2)
buffer1.addelem(3)
print(buffer1)
buffer1.addelem(4)  # Переписывает старый элемент
print(buffer1)
print("Dequeued:", buffer1.getelem())
print(buffer1)

