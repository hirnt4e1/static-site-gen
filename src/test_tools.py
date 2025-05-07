import unittest

from tools import *
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
    def test_extract_markdown_images_0(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_links_0(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://google.com)"
        )
        self.assertListEqual([("link", "https://google.com")], matches)
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_images_2(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) desu!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" desu!", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_links_2(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png) desu!",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" desu!", TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()