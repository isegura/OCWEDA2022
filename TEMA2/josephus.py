# -*- coding: utf-8 -*-
# author: isegura
from queue import Queue
import random


def josephus(num_soldiers: int, k: int) -> int:
    """gets num and k, where num is the number of soldiers, and k is the count of each step.
    It returns the position of the surviving soldier.
    If num or k are not valid, the function will return -1 """

    # First, we check that num and k have valid values
    if not isinstance(num_soldiers, int) or num_soldiers < 2:
        print(num_soldiers, ' is a wrong number of soldiers')
        return -1
    if not isinstance(k, int) or k < 1:
        print(k, ' is a wrong K')
        return -1

    q = Queue()   # we create a queue to save the soldiers
    for i in range(1, num_soldiers + 1):
        q.enqueue(i)  # each soldier is identified with a number from 1 to num

    while len(q) > 1:   # while there are more than one soldiers in the circle
        count = 1
        # we will skip k-1 soldiers
        while count < k:
            q.enqueue(q.dequeue())    # we remove the soldier, but we enqueue it at the end of the queue
            count = count+1

        # now, we have to kill the k-th soldier;
        killed = q.dequeue()
        # please, comment this line if you do not need to know the sequence in which the soldiers are killed
        print(str(killed) + ' was killed')

    # Here, the queue still has one solider, who is the survivor
    return q.front()


if __name__ == '__main__':
    num, k_value = 41, 3
    survivor = josephus(num, k_value)
    print('Surviving soldier for {} soldiers with k:{} is {}'.format(num, k_value, survivor))
    print()

    num, k_value = 0, 3
    survivor = josephus(num, k_value)
    print('Surviving soldier for {} soldiers with k:{} is {}'.format(num, k_value, survivor))
    print()

    num, k_value = 41, 0
    survivor = josephus(num, k_value)
    print('Surviving soldier for {} soldiers with k:{} is {}'.format(num, k_value, survivor))
    print()

    for _ in range(5):
        num = random.randint(1, 50)
        k_value = random. randint(1, 10)
        survivor = josephus(num, k_value)
        print('Surviving soldier for {} soldiers with k:{} is {}'.format(num, k_value, survivor))
        print()

    num, k_value = 25, 50
    survivor = josephus(num, k_value)
    print('Surviving soldier for {} soldiers with k:{} is {}'.format(num, k_value, survivor))
    print()
