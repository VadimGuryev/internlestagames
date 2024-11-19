"""
Сравнение:
Первый способ сложнее, но подходит для большего окнтроля над тем, как данные записываются и читаются, и работает быстрее
Второй способ проще было реализовать и использование deque делает все автоматически


"""
from collections import deque


class CircularBufferDeque:
    def __init__(self, size):
        self.buffer = deque(maxlen=size)

    def addelem(self, value):
        self.buffer.append(value)

    def getelem(self):
        if self.is_empty():
            raise IndexError("Буфер пуст")
        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def __str__(self):
        return f"Buffer: {list(self.buffer)}"


buffer2 = CircularBufferDeque(3)
buffer2.addelem(1)
buffer2.addelem(2)
buffer2.addelem(3)
print(buffer2)
buffer2.addelem(4)  # Переписывает старый элемент
print(buffer2)
print("Dequeued:", buffer2.getelem())
print(buffer2)