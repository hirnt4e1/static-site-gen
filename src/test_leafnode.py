import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode, text_node_to_html_node

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode('p', 'Header Text')
        node2 = LeafNode('p', 'Header Text')
        self.assertEqual(node, node2)
    def test_to_html(self):
        expected = '<h1>Header Text</h1>'
        node = LeafNode('h1', 'Header Text')
        actual = node.to_html()
        self.assertEqual(expected, actual)
    def test_to_html_with_props(self):
        expected = '<a href="https://www.google.com">Click me!</a>'
        node = LeafNode('a', "Click me!", {'href': 'https://www.google.com'})
        actual = node.to_html()
        self.assertEqual(expected, actual)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()