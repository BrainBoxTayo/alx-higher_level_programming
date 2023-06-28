#!/usr/bin/python3
"""Implementation of a singly linked list"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter function for data"""
        return (self.__data)

    @property
    def next_node(self):
        """getter function for the next node"""
        return (self.__next_node)

    @data.setter
    def data(self, value):
        """setter function for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """setter function for next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """insert the nodes in a sorted manner"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value <= self.__head.data:
            # If the value is less than or equal to the head's data,
            # insert the new node at the beginning
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Find the appropriate position to insert the new node
            current = self.__head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __repr__(self):
        """defines how we print a linked list"""
        node = self.__head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return '\n'.join(nodes)
