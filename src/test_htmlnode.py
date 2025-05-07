import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()