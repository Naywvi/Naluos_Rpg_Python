from typing import Container


class Inventory:
    def __init__(self) -> None:
        self.container = []
    
    def add(self,item):
          self.container.append(item)

    def remove(self, item):
        self.container.remove(item)
        
    def get_text(self):
        text = "[INV] "
        for i in range (0,len(self.container)):
            text += self.container[i]
            if i != len(self.container)-1: text += ", "
        if text == "[INV] ": text += "Tu as rien"
        return text
    def has_already(self, item):
        for i in range (0,len(self.container)):
            if item == self.container[i]:
                return True
        return False
    
    def clear(self):
        self.container = []