#!/usr/bin/env python3
#here comes copyright
'''
Dokumentacni retezec s testama

bla bla bla

'''

class SortedList:
    def __init__(self, sequence=None):
        if sequence is None:
            self.__list = []
        else:
            self.__list = sorted(list(sequence))
    
    def __contains__(self, value):
        '''
        Vraci hodnotu True, pokud se objekt value nachazi v posloupnost nebo pokud je objekt value klicem v mapovani.
        '''
        return value in self.__list
    
    def __str__(self):
        '''
        Vrati retezovou reprezentaci objektu
        '''
        return str(self.__list)

    def __len__(self):
        '''
        Vrati pocet prvku v listu
        '''
        return len(self.__list)
    
    def __getitem__(self, index):
        '''
        Vrati hodnotu zadane indexove pozice
        '''        
        return self.__list[index]
    
    def __getindex(self, value):
        '''
        Vrati indexovou pozici zadane hodnoty, (nebo kam hodnota náleží, není-li v seznamu)
        '''
        i = 0
        while i < len(self.__list):
            if self.__list[i] >= value:
                return i
            i += 1         
        return i


    def add(self, value):
        '''
        Pripoji prvek value do seznamu podle odpovidajici serazene sequence.
        '''
        index = self.__getindex(value)
        self.__list.insert(index, value)
    
    def index(self, value):
        '''
        Vrati indexovou pozici nejlevejsiho vyskytu prvku value v seznamu nebo rezu zacatek:konec. 
        Nebo vrati vyjimku ValueError.
        '''
        return self.__list.index(value)

    def count(self, value):
        '''
        Spočítá všechny výskyty hodnoty v seznamu
        '''
        return self.__list.count(value)
    
    def pop(self, index):
        '''
        Vrati a odstrani prvek na indexove pozici v seznamu
        '''
        return self.__list.pop(index)
    
    def remove(self, value):
        '''
        Odstrani nejlevejsi vysky prvku value ze seznamu nebo vyvola vyjimku
        '''
        self.__list.remove(value)
        return value
    
    # def remove_all(self, value):
        #'''
        #Ostrani kazdy vyskyt prvku value ze seznamu
        #'''
        #count = self.__list.count(value)
        #return count
    
    @property
    def reverse(self):
        '''
        Obrati seznam na miste
        '''
        return self.__list[::-1]

    @property
    def clear(self):
        '''
        Vycisti seznam
        '''
        self.__list = []

mylist = SortedList(("the", "quick", "brown", "fox", "jumped"))
print(mylist)
mylist.add("5")
print(mylist)
