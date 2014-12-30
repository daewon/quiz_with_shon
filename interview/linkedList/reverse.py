#http://cslibrary.stanford.edu/105/LinkedListProblems.pdf

class Node:
    def __init__(self, value = 0, nt = None):
        self.value = value
        self.next = nt
    def __str__(self):
        return "%s" % self.value



# return head of reversed list.
def reverse(head):
    if head == None or head.next == None: 
        return (head, head)
    
    (newHead, last) = reverse(head.next)
    head.next = None
    last.next = head
    return (newHead, head)

def reverseIter(head):
    if head == None or head.next == None: return head
    # deal with size 2
    ptr = head.next.next
    prev = head.next
    prev2 = head
    prev3 = None
    while ptr != None: 
        prev.next = prev2
        prev2.next = prev3
        prev3 = prev2
        prev2 = prev
        prev = ptr
        ptr = ptr.next

    prev.next = prev2
    prev2.next = prev3
    return prev
    
    
# prepend element at the front of list
def prepend(head, node):
    node.next = head
    return node
    
# append element at the end of list
def append(head, node):
    while head.next != None:
        head = head.next
    # now head is last node on list
    head.next = node

# sortedInsert.
def sortedInsert(head, node):
    ptr = head
    while ptr.next != None and ptr.next.value < node.value: 
        ptr = ptr.next
    node.next = ptr.next
    ptr.next = node
    
def printList(head):
    while head != None: 
        print head.value
        head = head.next


head = Node(10, None)
append(head, Node(20, None))
head = prepend(head, Node(1, None))

# printList(head)
# newNode = Node(15, None)
# sortedInsert(head, newNode)
# printList(head)
head = reverseIter(head)
printList(head)
#(head, tmp) = reverse(head)

#printList(head)



    
