'''
Returns the element in a single-linked-list that is (which) elements
from the end of the list. (Elements) is a linked list as an argument.

'''



def question5(elements,which):

    class Element(object):
        def __init__(self, value):
            self.value = value
            self.next = None

    class LinkedList(object):
        def __init__(self, head=None):
            self.head = head

        def append(self, new_element):
            current = self.head
            if self.head:
                while current.next:
                    current = current.next
                current.next = new_element
            else:
                self.head = new_element

    myList = LinkedList()
    for item in elements:
        myList.append(Element(str(item)))
        
    leading = myList.head
    target  = myList.head
    for nodez in range(0,which):
        leading = leading.next
    while leading.next is not None:
        leading = leading.next
        target  = target.next
    return target.value
        
question5([4,2,3,25],2)
question5([0,258,1,45,46,456,78,34,5645 ** 50],1)
question5([34535,'f',3,2885,456,456,7,5675,345435,'hi',456456,767,6743534535,5667,68798,9785,4545,65565,434,35,445],3)


    class Element(object):
        def __init__(self, value):
            self.value = value
            self.next = None

    class LinkedList(object):
        def __init__(self, head=None):
            self.head = head

        def append(self, new_element):
            current = self.head
            if self.head:
                while current.next:
                    current = current.next
                current.next = new_element
            else:
                self.head = new_element

        def get_position(self, position):
            counter = 1
            current = self.head
            if position < 1:
                return None
            while current and counter <= position:
                if counter == position:
                    return current
                current = current.next
                counter += 1
            return None

        def printPosFromLast(self,n):
            main_to = self.head
            ref_to  = self.head

            count = 0
            if(self.head is not None):
                while(count < n):
                    if(ref_to is None):
                        print "You have gone too far! %s is past the beginning" %(n)
                        return
                    ref_to = ref_to.next
                    count += 1

            while(ref_to is not None):
                main_to = main_to.next
                ref_to = ref_to.next

            print "Element number %s from last is %s " %(n, main_to.value)
            
			
    myList = LinkedList()
    for item in elements:
        myList.append(Element(str(item)))
		
	leading = self.head
	target  = self.head
	for nodez in which:
		leading.next
	while leading is not None:
		leading.next
		target.next
	return target.value
		
	
    try:
        return myList.printPosFromLast(which)
    except:
        print "Check your second argument"
        
question5([4,2,3,25],0)
# 2
question5([0,258,3,45 ** 55],1)
# 34
question5([34535,'f',3,2885],3)
# 65565