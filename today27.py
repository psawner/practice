class node:
    def __init__(self, val):
        self.data = val
        self.next = None

def get(head):
    if head == None:
        return
    
    while head:
        print(head.data,end='->')
        head = head.next

a = [1,2,3,4,5,6]
head = node(a[0])
temp = head

for i in range(1,len(a)):
    new_node = node(a[i])
    temp.next = new_node
    temp = temp.next

get(head)