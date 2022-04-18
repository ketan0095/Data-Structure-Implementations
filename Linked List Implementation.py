# -------------------------
# Create Node
# -------------------------

from cgi import print_environ_usage
from tracemalloc import start

# ------------------------
# Create Node Object
# ------------------------
class Node:
    def __init__(self, data) -> None:
        self.data = data  # save the data in array space
        self.ptr_to_next = None  # used to save the location for the next Node


# -------------------------
# Create Linked List
# -------------------------
class LinkedList:
    def __init__(self) -> None:
        self.head = None  # used to create starting point of LinkedList

    # -------------------------------------
    # Traverse through Linked list : O(n)
    # -------------------------------------
    def traverse_list(self):
        start_ = self.head  # assign the starting point
        while start_ != None:  # traverse untill pointer is exhausted
            print("Eelement :", start_.data)
            start_ = start_.ptr_to_next  # change pointer after traversing
        return start_

    # -------------------------------------
    # Traverse to specified index, index strat from 0
    # -------------------------------------
    def traverse_to_index(self, index):  # get index from user
        start_ = self.head  # assign the starting point
        user_req = index
        counter = 0
        while start_ != None:  # traverse untill pointer is exhausted
            if counter == user_req:
                return start_
            start_ = (
                start_.ptr_to_next
            )  # if it is not the required index yet then change pointer after traversing
            counter += 1  # increment counter

    # ------------------------------------
    # Append to specified Index
    # ------------------------------------
    def append_to_index(self, index, new_node):  # get index from user
        start_ = self.head  # assign the starting point
        user_req = index
        counter = 0
        while start_ != None:  # traverse untill pointer is exhausted
            if counter == user_req - 1:  # traverse till index-1 element
                old_next_node = start_.ptr_to_next
                start_.ptr_to_next = new_node
                new_node.ptr_to_next = old_next_node
                return counter
            start_ = (
                start_.ptr_to_next
            )  # if it is not the required index yet then change pointer after traversing
            counter += 1  # increment counter

    # -------------------------------------
    # Append to last index
    # -------------------------------------
    def append_to_last_index(self, new_node):
        start_ = self.head
        while start_ != None:
            if start_.ptr_to_next == None:
                # Last Node
                start_.ptr_to_next = new_node
                return start_
            start_ = start_.ptr_to_next

    # --------------------------------------
    # Delete head node
    # --------------------------------------
    def delete_head(self):
        start_ = self.head
        self.head = start_.ptr_to_next
        return self.head

    # ---------------------------------------
    # Delete at specific index
    # ---------------------------------------
    def delete_at_index(self, index):
        start_ = self.head
        counter = 0
        while start_ != None:
            if counter == index - 1:
                next_ = start_.ptr_to_next
                start_.ptr_to_next = next_.ptr_to_next
                return start_
            start_ = start_.ptr_to_next
            counter += 1

    # ----------------------------------------
    # Delete Last Node
    # ----------------------------------------
    def delete_last(self):
        start_ = self.head
        stop = True
        while stop:
            if start_.ptr_to_next == None:
                prev.ptr_to_next = None  # Make previous node to last node node
                return prev
            prev = start_
            start_ = start_.ptr_to_next


####################################
# ---------------------------------
#       Create Linked List
# ---------------------------------
####################################

# ------------------------
# Initialize the Linked List
# ------------------------
L_list = LinkedList()  # createa object of list

# ---------------------------
# Create Head Node
# ---------------------------
L_list.head = Node(100)  # this is the head location for linked list

# ---------------------------
# Append 2nd node to head node
# ---------------------------
second_node = Node(200)  # second node instance
L_list.head.ptr_to_next = second_node  # save pointer of 2nd node in first node


# ---------------------------
# Append 3rd node to 2nd node
# ---------------------------
third_node = Node(300)  # second node instance
second_node.ptr_to_next = third_node  # save pointer of 3rd node in 2nd node


####################################
# ---------------------------------
#       Access Linked List
# ---------------------------------
####################################

# -------------------------------------
# Traverse through Linked list : O(n)
# -------------------------------------
print("Traverse through Linked list")
print(L_list.traverse_list())


# ---------------------------------------------------------
# Traverse thorugh Linked list till desired index is found
# ---------------------------------------------------------
print()
print("Traverse thorugh Linked list till desired index is found")
print(L_list.traverse_to_index(2).data)


# --------------------------------
# Append Node at head node
# --------------------------------
print()
print("Append Node at head node")
OLD_HEAD_POINTER = L_list.head  # GET OLD head pointer
L_list.head = Node(1000)  # assign new node as head

# append new head to old head
L_list.head.ptr_to_next = OLD_HEAD_POINTER
L_list.traverse_list()

# ---------------------------------------
# Append Node at specified index
# ---------------------------------------
print()
print("Append Node at specified index")
new_node_to_append = Node(300000)
L_list.append_to_index(2, new_node_to_append)
L_list.traverse_list()


# ----------------------------------------
# Append Node at Last Node
# ----------------------------------------
print()
print("Append Node at Last Node")
new_node_to_append = Node(1000000)
L_list.append_to_last_index(new_node_to_append)
L_list.traverse_list()


####################################
# ---------------------------------
#    Delete Node in  Linked List
# ---------------------------------
####################################

# ---------------------------------------
# Delete Head Node
# ---------------------------------------
print()
print("Delete Head Node")
L_list.delete_head()
L_list.traverse_list()


# ---------------------------------------
# Delete node at specific index
# ---------------------------------------
index_ = 1
print()
print("Delete node at specific index")
L_list.delete_at_index(index_)
L_list.traverse_list()


# ---------------------------------------
# Delete node at Last
# ---------------------------------------
print()
print("Delete node at Last")
L_list.delete_last()
L_list.traverse_list()
