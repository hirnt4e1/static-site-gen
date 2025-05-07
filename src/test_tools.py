import unittest

from tools import text_node_to_html_node, split_nodes_delimiter
from textnode import TextNode, TextType

class TestTools(unittest.TestCase):
    def test_split_nodes_delimiter_0(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes_expected = [
            TextNode("This is text with a ", TextType.TEXT), 
            TextNode("code block", TextType.CODE), 
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, new_nodes_expected)
    def test_split_nodes_delimiter_1(self):
        node = TextNode("*We have a shortage of* bold men", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        new_nodes_expected = [
            TextNode("We have a shortage of", TextType.BOLD), 
            TextNode(" bold men", TextType.TEXT), 
            ]
        self.assertEqual(new_nodes, new_nodes_expected)
    def test_split_nodes_delimiter_2(self):
        node = TextNode("*We have a shortage of bold men", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "*", TextType.BOLD)

if __name__ == "__main__":
    unittest.main()