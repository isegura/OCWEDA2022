# -*- coding: utf-8 -*-
"""
Created on Sat May 29 14:18:09 2021

@author: SECRETARIA
"""

from dlist import DList
from dlist import DNode

class DList2(DList):
    
    def quicksortDL(self):
        self._quicksortDL(0,self.size-1)   #los parámetros son las distancias al principio y final de la lista
        
    def _quicksortDL(self,left,right):
        
        i=left
        j=right
        m=(i+j)//2
        
        #first  será el primer elemento del intervalo a ordenar
        first=self.head
        for n in range(i):
            first=first.next
        #print(first.elem)    
        #mid  será el elemento pivote del intervalo a ordenar
        mid=self.head
        
        for r in range(m):
            mid=mid.next
            
           
        x=mid.elem #x es el valor del elemento pivote
        #last será el último elemento del intervalo a ordenar
        #print(mid.elem)

        last=self.head   
        for s in range(j):
            last=last.next
                
        while i<=j:
            while first.elem<x:
                first=first.next
                i+=1
                   
            while last.elem>x:
                last=last.prev
                j-=1
                   
            if i<=j:
   
                temp=first.elem
                first.elem=last.elem
                last.elem=temp
                first=first.next
                i+=1
                last=last.prev
                j-=1
 
        if left<j:
            self._quicksortDL(left,j)
        if   i<right:
            self._quicksortDL(i,right)
        
import random                
L=DList2()

for i in range(16):
    L.addLast(random.randint(0,100))
   

print(L)

L.quicksortDL()

print(L)      
print(L.head.elem,L.tail.elem,L.size)            