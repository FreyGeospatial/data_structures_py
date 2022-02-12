# linked list does not have index
# traditional list is contained contiguously in memory,
# whereas linked lists are not necessarily contained contiguously
# in memory


# linked lists are similar to nested dictionaries
head = {
            "value": 11,
            "next": {
                "value": 3,
                "next": {
                    "value": 23,
                    "next": {
                        "value": 7,
                        "next": None
                        }
                    }
                }
        
        }

print(head['next']['next']['value'])


# class LinkedList:
#     def __init__(self, value): # create a new node
#     def append(self, value): # create new node and add to end of list
#     def prepend(self, value): # create new node and add to beginning of list
#     def insert(self, index, value): # create new node and insert at an index


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value): # create a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
my_linked_list = LinkedList(4)

print(my_linked_list.head.value)