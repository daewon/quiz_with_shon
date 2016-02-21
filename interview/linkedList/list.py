# http://cslibrary.stanford.edu/105/LinkedListProblems.pdf


class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        
class List:
    def __init__(self, datas = []):
        self.head = None
        self.appends(datas)
        
    def show(self):
        ptr = self.head
        s = "["
        while ptr != None:
            s += str(ptr.data)
            s += ","
            ptr = ptr.next
        t = s[:-1]
        if s[-1] == "[": t = s
        print t + "]"
        
    def append(self, data):
        if self.head == None:
            # empty list
            self.head = Node(data)
        else:
            # not empty list
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            
            ptr.next = Node(data)
            
    def appends(self, datas):
        if len(datas) == 0: return 
            
        first = datas[0]
        current = self.head        
        
        while current != None and current.next != None:
            current = current.next
        
        if current == None: # empty
            current = Node(datas[0])
            self.head = current
            start = 1
        else:
            start = 0
            
        for data in datas[start:]:
            current.next = Node(data)
            current = current.next
        
            
    def prepend(self, data):
        old = self.head
        new = Node(data)
        new.next = old
        self.head = new
    
    def prepends(self, datas):
        for data in datas:
            new = Node(data)
            new.next = self.head
            self.head = new
            
    # 1. count
    def count(self):
        ptr = self.head
        count = 0
        while ptr != None:
            count += 1
            ptr = ptr.next
        return count
    
    """
        2. getNth(): 
        ex: {42, 13, 666}, 1 -> 13
        The index should be in the range [0..length-1]. If it is not, GetNth() should assert() fail (or you could implement some other error case strategy).
        tc0: 
            ls = List()
            ls.getNth(0) -> exception
            ls.getNth(1) -> exception
        tc1: 
            ls = List()
            ls.append(10)
            ls.getNth(0) -> 10
            ls.getNth(1) -> exception
            
    """
    def getNth(self, n):
        ptr = self.head 
        while ptr != None and n > 0:
            ptr = ptr.next
            n -= 1
            
        if ptr == None: raise Exception("n is our of range.")
        else:  return ptr.data
    
    """
        3. delteList():
        Write a function DeleteList() that takes a list, deallocates all of its memory and sets its
        head pointer to NULL (the empty list).
        tc0: 
            ls = List()
            ls.deleteAll()
            ls.show()  expect []
        tc1: 
            ls = List()
            ls.append(10)
            ls.show expect [10]
            ls.deleteAll()
            ls.show() expect []
    """
    def deleteList(self):
        ptr = self.head
        while ptr != None:
            old = ptr
            ptr = ptr.next
            del old
        self.head = ptr
        
    """
        4. pop()
        Pop() takes a non-empty list, deletes the head node, and returns the head node's data. 
        assert() fail if there is not a node to pop. 
    """
    def pop(self):
        ptr = self.head
        if ptr == None: raise Exception("no element to pop.")
        else:
            data = ptr.data
            self.head = ptr.next
            return data
    
    """
        5. insertNth()
        insert a new node at any index within a list. 
        tc0: 
            ls = List()
            ls.insertNth(-1, 10) expect exception
            ls.insertNth(0, 10) expect [10]
        tc1: 
            ls = List([10, 20])
            ls.prepend(30)
            
            ls.insertNth(0, 0) expect [0, 10, 20, 30]
            ls.insertNth(1, 0) expect [10, 0, 20, 30]
            ls.insertNth(2, 0) expect [10, 20, 0, 30]
            ls.insertNth(3, 0) expect [10, 20, 30, 0]
            ls.insertNth(4, 0) expect exception
            
    """
    def insertNth(self, n, data):
        ptr = self.head
        if n < 0: raise Exception("n >= 0")
        elif n == 0: self.prepend(data)
        else:
            # find position on n-1th.
            while ptr != None and n > 1: 
                n -= 1
                ptr = ptr.next
        
            if ptr == None: raise Exception("can`t insert nth")
            else:
                new = Node(data)
                new.next = ptr.next
                ptr.next = new
    
    """
        6. sortedInsert 
        given sorted list, insert node into correct sorted position in list.
        tc0: 
            ls = List([1])
            
            ls.sortedInsert(0) expect [0, 1]
            ls.sortedInsert(2) expect [1, 2]
        tc1: 
            ls = List([10, 20, 30])

            ls.sortedInsert(11) expect [10, 11, 20, 30]
            ls.sortedInsert(9) expect [9, 10, 11, 20, 30]
            ls.sortedInsert(21) expect [10, 20, 21, 30]
            ls.sortedInsert(31) expect [10, 20, 30, 31]
        tc2: 
            ls = List()
            
            ls.sortedInsert(10) expect [10]
        tc3:
            ls = List()
            
            ls.sortedInsert(10)
            ls.sortedInsert(20)
            ls.show() expect [10, 20]
    """
    def sortedInsert(self, data):
        ptr = self.head
        # empty list
        if ptr == None: self.prepend(data)
        else:
            # find smaller node. 
            prev_ptr = ptr
            while ptr != None and ptr.data < data:
                prev_ptr = ptr
                ptr = ptr.next

            if prev_ptr == ptr: 
                # head.data > data so insert new node infront of head.
                self.prepend(data)
            else:
                # insert between prev_ptr, ptr
                new = Node(data)
                new.next = prev_ptr.next
                prev_ptr.next = new
                
    """
        7. insertSort()
        Write an InsertSort() function which given a list, rearranges its nodes so they are sorted in
        increasing order. It should use SortedInsert().
        
        O(N^2), use extra memory
        tc0: 
            ls = List([])
            ls.insertSort() expect []
        tc1:
            ls = List([1,2,3])
            
            ls.insertSort() expect [1, 2, 3]
        tc2: 
            ls = List([3,2,1])
            
            ls.insertSort() expect [1, 2, 3]
            
    """
    def insertSort(self):
        ls = List()
        ptr = self.head
        while ptr != None: 
            ls.sortedInsert(ptr.data)
            ptr = ptr.next
        self.head = ls.head
    
    """
        8. Append()
        given 'a' and 'b', appends 'b' onto the end of 'a', and then sets 'b' to NULL
        ex) a: [1, 2], b: [3, 4] => appendList(a, b) = [1, 2, 3, 4] and b = []
        
        tc0: 
            a = List()
            b = List()
            b.append(10)
            a.appendList(b) expect a = [10], b = []
        tc1:
            a = List()
            a.append(10)
            b = List()
            a.appendList(b) expect a = [10], b = []
        tc2:
            a = List()
            a.append(10)
            b = List()
            b.append(20)
            a.appendList(b) expect a = [10, 20], b = []
            
    """
    def appendList(self, other):
       ptr = self.head
       if ptr == None: 
           self.head = other.head
           other.head = None
       else:
           while ptr.next != None: 
               ptr = ptr.next
           ptr.next = other.head
           other.head = None
         
    
    """
        9. frontBackSplit
        Split the nodes of the given list into front and back halves,
        and return the two lists. If the length is odd, the extra node should go in the front list.
        ex) [2, 3, 5, 7, 11] -> [2, 3, 5], [7, 11]
        
        tc0: 
            a = List()
            a.append(10)
            b = a.splitHalf() expect exception
        tc1:
            a.append(10)
            a.append(20)
            b = a.splitHalf()
            a.show() = [10], b.show() = [20]
        tc2:
            a.append(10)
            a.append(30)
            a.append(20)
            b = a.splitHalf()
            a.show() = [10, 30], b.show() = [20]
        tc3:
            a.append(10)
            a.append(40)
            a.append(30)
            a.append(20)
            b = a.splitHalf()
            a.show() = [10, 40], b.show() = [30, 20]
    """
    def splitHalf(self):
        ptr = self.head
        b = List()
        if (ptr == None or ptr.next == None):
            return b
        else:
            prev = ptr
            ptr_2 = ptr
            
            while ptr_2 != None and ptr_2.next != None: 
                prev = ptr
                ptr = ptr.next
                ptr_2 = ptr_2.next.next

            
            if ptr_2 == None: 
                # even
                b.head = ptr
                prev.next = None
            else:
                # odd
                b.head = ptr.next
                ptr.next = None
                
            return b
            
        
    """
        10. removeDuplicates
        takes a list sorted in increasing order and deletes any duplicate nodes from the list. 
        Ideally, the list should only be traversed once.
        tc0: 
            ls = List()
            ls.removeDuplicates()
            ls.show() expect []
        tc1:
            ls = List()
            ls.append(1)
            ls.removeDuplicates()
            ls.show() expect [1]
            
        tc1:
            ls = List()
            ls.append(1)
            ls.append(1)
            ls.append(2)
            ls.removeDuplicates()
            ls.show() expect [1, 2]
        
    """
    def removeDuplicates(self):    
        old = None
        prev = self.head
        ptr = self.head
        while ptr != None:
            if old == None or old != ptr.data: 
                # keep this node
                old = ptr.data
                prev = ptr
                ptr = ptr.next
            else:
                # delete this node
                tmp = ptr.next
                prev.next = ptr.next
                ptr = ptr.next
       
    """
        11. move node
         Take the node from the front of the source, and move it to
         the front of the dest.
         It is an error to call this with the source list empty.
         ex) [1, 2, 3], [1, 2, 3] => [1, 1, 2, 3], [2, 3]
         tc0: 
             a = List()
             b = List()
             b.append(10)
             a.moveNode(b)
             a.show() = [10]
             b.show() = []
         tc1:
             a = List()
             b = List()
             a.eppend(10)
             b.append(20)
             a.moveNode(b)
             a.show()
             b.show()
    """
    def moveNode(self, other):
        if other.head == None: raise Exception("can't move any from b since it is empty.")
        tmp = other.head
        other.head = other.head.next
        tmp.next = self.head
        self.head = tmp
    
    """
        12. alternatingSplit()
        Given the source list, split its nodes into two shorter lists.
        If we number the elements 0, 1, 2, ... then all the even elements
        should go in the first list, and all the odd elements in the second.
        The elements in the new lists may be in any order.
         
        ex) [a, b, a, b, a] => [a, a, a], [b, b]
        tc0: 
            a = List()
            a.append(1)
            b = a.alternatingSplit()
            a.show()    expect [1]
            b.show()    expect []
        tc1:
            a.append(1)
            a.append(2)
            b = a.alternatingSplit()
            a.show()    expect [1]
            b.show()    expect [2]
        tc2:
            a.append(1)
            a.append(2)
            a.append(3)
            b = a.alternatingSplit()
            a.show()    expect [1, 3]
            b.show()    expect [2]
            
    """
    def alternatingSplit(self):
        ptr = self.head
        if ptr == None: return List()
        else:
            b = List()
            bptr = None
            while ptr != None and ptr.next != None:
                ptr_next_next = ptr.next.next
                if bptr == None: b.head = ptr.next
                else: bptr.next = ptr.next
                
                ptr.next.next = None
                ptr.next = ptr_next_next
                ptr = ptr_next_next
            return b
    
    """
        13. ShuffleMerge()
         Merge the nodes of the two lists into a single list taking a node
         alternately from each list, and return the new list.
         ex) [1,2,3] and [7, 13, 1] -> [1, 7, 2, 13, 3, 1]
         tc0:
             a = List()
             
             a.append(1)
             b = List()
             b.append(7)
             b.append(13)
             b.append(1)
             a.shuffleMerge(b)
             a.show() expect [1, 7, 13, 1]
        tc1:
             a = List()
             a.append(1)
             a.append(2)
             a.append(3)
             b = List()
             a.shuffleMerge(b)
             a.show() expect [1, 2, 3]
                 
    """
    def shuffleMerge(self, other):
        current_a = self.head
        current_b = other.head
        
        if current_a == None: 
            self.head = other.head
            return
        if current_b == None:
            return
        
        c = List()
        c.head = Node(None)
        current_c = c.head            
        while current_a != None and current_b != None:
            next_a, next_b = current_a.next, current_b.next
            
            current_c.next = current_a
            current_c.next.next = current_b
            current_c = current_b
            
            current_a = next_a
            current_b = next_b
        
        while current_a != None:
            current_c.next = current_a
            current_c = current_c.next
            current_a = current_a.next
        
        while current_b != None:
            current_c.next = current_b
            current_c = current_c.next
            current_b = current_b.next
        
        self.head = c.head.next    
        
    def shuffleMergeInplace(self, other):
        current_a = self.head
        current_b = other.head
        if current_a == None: self.head = other.head
        elif current_b == None: pass
        else:
            prev_a = current_a
            prev_b = current_b
            while current_a != None and current_b != None:
                next_a, next_b = current_a.next, current_b.next
                prev_a = current_a
                prev_b = current_b

                current_b.next = current_a.next
                current_a.next = current_b
                current_a = next_a
                current_b = next_b

            if current_a == None:
                prev_b.next = current_b
        other.head = None

    """
        14. SortedMerge()
        Takes two lists sorted in increasing order, and
        splices their nodes together to make one big
        sorted list which is returned.
        ex) [1,2,3] and [1, 13] -> [1, 1, 2, 3, 13]

    """
    @staticmethod
    def sortedMerge(a, b):
        c = List()
        c.head = Node(None)
        current_c = c.head
        current_a, current_b = a.head, b.head
        
        while current_a != None and current_b != None:
            if current_a.data < current_b.data:
                # insert a into c
                current_c.next = current_a
                current_c = current_c.next
                current_a = current_a.next
            else:
                current_c.next = current_b
                current_c = current_c.next
                current_b = current_b.next
        
        while current_a != None:
            current_c.next = current_a
            current_c = current_c.next
            current_a = current_a.next
            
        while current_b != None:
            current_c.next = current_b
            current_c = current_c.next
            current_b = current_b.next
        
        c.head = c.head.next
        return c
       
         
    """
        15. mergeSort
        ex) [1,3,2,4] -> [1,2,3,4]
        tc0:
            a = List()
            b = List.mergeSort(a)
            b.show()    expect  []
        tc1:
            a = List([1])
            b = List.mergeSort(a)
            b.show()    expect  [1]
        tc2:
            a = List([3,1])
            b = List.mergeSort(a)
            b.show()    expect  [1,3]
        tc3:
            a = List([3, 1, 1, 2])
            b = List.mergeSort(a)
            b.show()    expect  [1,1,2,3]
    """
    @staticmethod
    def mergeSort(a):
        if a.head == None or a.head.next == None: return a
        b = a.splitHalf()
        a_sorted = List.mergeSort(a)
        b_sorted = List.mergeSort(b)
        return List.sortedMerge(a_sorted, b_sorted)
    
    """
        16. SortedIntersect()
         Compute a new sorted list that represents the intersection
         of the two given sorted lists. The new list should be made with its own memory, the original lists should not be changed
         ex) [1, 3, 4], [5,6] => [1,3,4,5,6]
         
         tc0:
             a = List([1,2])
             b = List()
             c = List.sortedIntersect(a, b)
             c.show()   expect  []
         tc1: 
             a = List([1,3])
             b = List([2,5,6])
             c = List.sortedIntersect(a, b)
             c.show()   expect  []
         tc2:
             a = List([1,2,3])
             b = List([2,3,4,5])
             c = List.sortedIntersect(a, b)
             c.show()   expect  [2,3]
    """
    @staticmethod
    def sortedIntersect(a, b):
        current_a, current_b = a.head, b.head
        
        c = List()
        c.head = Node(None)
        current_c = c.head
        
        while current_a != None and current_b != None:
            if current_a.data < current_b.data: 
                current_a = current_a.next
            elif current_a.data > current_b.data:
                current_b = current_b.next
            else: 
                current_c.next = current_a
                current_c = current_c.next
                current_a = current_a.next
                current_b = current_b.next
        c.head = c.head.next
        return c
    
    """
        17. Reverse(): Iterative
         Reverse the given linked list by changing its .next pointers and
         its head pointer. Takes a pointer (reference) to the head pointer.
         ex) [1, 2, 3, 4] -> [4,3,2,1]
    """
    def reverseIter(self):
        current = self.head
        prev = None
        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    """
        18. Reverse(): Recursive
         Recursively reverses the given linked list by changing its .next pointers and its head pointer in one pass of the list.
         ex) [1, 3, 2, 4] -> [4, 2, 3, 1]
         tc0:
             a = List()
             a.reverse()
             a.show()   expect []
         tc1:
             a = List([2])
             a.reverse()
             a.show()   expect  [2]
         tc2:
             a = List([2, 3])
             a.reverse()
             a.show()   expect  [3, 2]
         tc3:
             a = List([3, 2, 4])
             a.reverse()
             a.show()   expect  [4, 2, 3]
    """
    def reverse(self):
        self.head = List.reverseRec(self, self.head)
        
    @staticmethod
    def reverseRec(a, current):
        if current == None: # empty list
            return current
        if current.next == None: # one element list
            return current
            
        old = current.next
        tail = List.reverseRec(a, old)
        current.next = None
        old.next = current
        return tail
        
        
#   
# ls = List()
# # ls.show()
# ls.append(30)
# ls.append(20)
# ls.append(10)
# ls.show()
# # print ls.count()
# # print ls.getNth(0)
# # print ls.getNth(3)
# # ls.deleteList()
# # ls.show()
# # print ls.pop()
# # ls.insertNth(3, 1)
# ls.show()
# # ls.sortedInsert(31)
# #ls.sortedInsert(31)
# ls.insertSort()
# ls.show()
# a = List()
# a.append(10)
# b = List()
# b.append(20)
# a.appendList(b)
# a.show()
# b.show()
# a = List()
# a.append(1)
# a.append(2)
# a.append(3)
# b = List()
# b.append(1)
# # b.append(7)
# b.append(13)
#
# a.show()
# b.show()
# a.sortedMerge(b)
# a.show()
a = List([3, 2, 4])
a.reverse()
a.show()
# b = List([2,3,4,5,6])
# c = List.sortedIntersect(a, b)
# c.show()