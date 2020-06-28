"""
https://stackabuse.com/linked-lists-in-detail-with-python-examples-single-linked-lists/#singlelinkedlist
"""


class Node:
    def __init__(self, data):
        """
        Node: contain data and ref to nex Node
        when init node => we not know about next node, so ref is None
        """
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        """
        When init LinkedList, start node is None because we has empty linked list
        """
        self.start_node: Node = None

    def traverse_list(self):
        if self.start_node is None:
            print("Empty linked list")
            return
        else:
            node: Node = self.start_node
            while node is not None:
                print(node.item, " ")
                node = node.ref

    def insert_at_start(self, data: Node):
        data.ref = self.start_node
        self.start_node = data


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_start(Node(1))
    linked_list.insert_at_start(Node(2))
    linked_list.insert_at_start(Node(3))
    linked_list.insert_at_start(Node(4))
    linked_list.insert_at_start(Node(5))
    linked_list.insert_at_start(Node(6))
    linked_list.insert_at_start(Node(7))
    linked_list.insert_at_start(Node(8))
    linked_list.insert_at_start(Node(9))

    linked_list.traverse_list()
