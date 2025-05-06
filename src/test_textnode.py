import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_text_uneq(self):
        node = TextNode("This has text A", TextType.ITALIC)
        node2 = TextNode("This has text B", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_type_uneq(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node, node2)
    def test_url_default(self):
        node = TextNode("This is a text node", TextType.LINK)
        self.assertIsNone(node.url)
    def test_url_other(self):
        node = TextNode("This is a text node", TextType.LINK, 'http://localhost:8888')
        self.assertIsNotNone(node.url)


if __name__ == "__main__":
    unittest.main()