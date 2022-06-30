# -*- coding: utf-8 -*-
from queue import Queue


class Request:
    """ This class represent a request to be printed"""
    def __init__(self, user: str, document: str) -> None:
        self.id_user = user
        self.name_file = document
    
    def __str__(self) -> str:
        """Returns a string with the information of a request"""
        return "User: " + self.id_user + ", \t Document: " + self.name_file


class PrinterQueue(Queue):
    """This class simulates a network printer"""

    def add_request(self, request: Request) -> None:
        """Adds a new request to be printed"""
        self.enqueue(request)

    def number_requests(self) -> int:
        """Returns the number of pending requests"""
        return len(self)

    def show_pending_requests(self) -> None:
        """Show the pending requests"""
        for r in self._items:
            print(r)

    def print_request(self) -> None:
        """process (print) the first request saved into the printer"""
        if self.is_empty():
            print('There is no work to print')
            return

        r = self.dequeue()
        print("printing:", r)

    def print_all(self):
        """process all pending requests"""
        while not self.is_empty():
            self.print_request()
  
  
if __name__ == '__main__':
    p = PrinterQueue()
    p.add_request(Request("293939", "Unit2.pdf"))
    p.add_request(Request("111", "Unit1.pdf"))
    p.add_request(Request("333", "Unit3.pdf"))

    print('showing pending requests:')
    p.show_pending_requests()
    print()

    print('print the next request:')
    p.print_request()
    print('Number of pending requests: ', p.number_requests())
    print()

    print('showing pending requests:')
    p.show_pending_requests()
    print()

    print('print the next request:')
    p.print_request()
    print()

    print('showing pending requests:')
    p.show_pending_requests()
    print()

    print('Number of pending requests: ', p.number_requests())
    print()

    p.add_request(Request('isegura', 'eda2023.pptx'))

    print('showing pending requests:')
    p.show_pending_requests()
    print()

    print('printing all:')
    p.print_all()
    print()

    print('Number of pending requests: ', p.number_requests())
    print()
