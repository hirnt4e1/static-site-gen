import unittest

from htmlnode import HTMLNode
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('h1', 'Header Text')
        node2 = HTMLNode('h1', 'Header Text')
        self.assertEqual(node, node2)
    def test_defaults(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)
    def test_props_to_html(self):
        expected = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        actual = node.props_to_html()
        self.assertEqual(expected, actual)
    def test_props_to_html_blank(self):
        expected = ''
        node = HTMLNode(None, None, None, None)
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()