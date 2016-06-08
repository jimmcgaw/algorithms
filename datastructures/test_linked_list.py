from linked_list import LinkedList, LinkedListItem

import unittest

class LinkedListItemTest(unittest.TestCase):
    def setUp(self):
        self.first_value = "Abominable"
        self.next_value = "Snowman"

    def test_item_value_no_next(self):
        self.linked_list_item = LinkedListItem(self.first_value)
        self.assertEqual(str(self.linked_list_item), self.first_value)
        self.assertEqual(self.linked_list_item.next(), None)

    def test_item_with_next(self):
        self.next_linked_list_item = LinkedListItem(self.next_value)
        self.linked_list_item = LinkedListItem(self.first_value, next_node=self.next_linked_list_item)
        self.assertEqual(self.linked_list_item.next(), str(self.next_linked_list_item))


if __name__ == '__main__':
    unittest.main()
