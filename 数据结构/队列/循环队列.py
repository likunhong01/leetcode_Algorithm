#coding=utf-8
#Version:python3.7.0
#Tools:Pycharm 2019
# Author:LIKUNHONG
__date__ = ''
__author__ = 'lkh'


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.length = k
        self.arr = [None]*k
        self.head = 0
        self.tail = 0


    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % self.length
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.arr[self.head] = None
        self.head = (self.head + 1) % self.length
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.arr[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.arr[(self.tail + self.length - 1) % self.length] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == self.tail and self.arr[self.head] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.head == self.tail and self.arr[self.head]

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(8)
param_1 = obj.enQueue(3)
param_2 = obj.enQueue(9)
param_3 = obj.enQueue(5)
param_4 = obj.enQueue(0)

obj.deQueue()
obj.deQueue()

print(obj.Rear())
print('---')
print(obj.tail)
print(obj.head)
print(obj.arr)

param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()
# print(param_3)
# print(param_4)
# print(param_5)
# print(param_6)