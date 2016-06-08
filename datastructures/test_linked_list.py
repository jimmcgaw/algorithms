from linked_list import LinkedList, LinkedListItem

import unittest

class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.words = "Hello Linked Lists".split(' ')
        self.words = list(reversed(self.words))  # reverse sentence world order

    def populate_linked_list(self):
        for item in self.words:
            self.linked_list.insert(item)
        self.assertEqual(len(self.linked_list), len(self.words))

    def test_search_item_in_list(self):
        self.populate_linked_list()
        word_to_find = self.words[0]
        self.assertEqual(str(self.linked_list.search(word_to_find)), str(LinkedListItem(word_to_find)))

    def test_search_item_not_in_list(self):
        self.populate_linked_list()
        self.assertEqual(self.linked_list.search("BadWord"), None)

    def test_next_empty_list(self):
        self.assertEqual(self.linked_list.next(), None)

    def test_next(self):
        self.populate_linked_list()
        self.assertEqual(str(self.linked_list.next()), self.words[-1])
        self.assertEqual(str(self.linked_list.next()), self.words[-2])
        self.assertEqual(str(self.linked_list.next()), self.words[-3])
        self.assertEqual(self.linked_list.next(), None)






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
