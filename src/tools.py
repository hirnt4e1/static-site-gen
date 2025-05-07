import re
from htmlnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD:
            return LeafNode('b', text_node.text, None)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text, None)
        case TextType.CODE:
            return LeafNode('code', text_node.text, None)
        case TextType.LINK:
            return LeafNode('a', text_node.text, {'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
        case _:
            raise Exception("invalid text type")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        split_count = len(split_text)
        if split_count % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(split_count):
            if split_text[i] == '':
                continue
            if i % 2 == 1:
                new_nodes.append(TextNode(split_text[i], text_type))
            else:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        markdown_images = extract_markdown_images(old_node.text)
        if len(markdown_images) == 0:
            new_nodes.append(old_node)
            continue
        node_parts = []
        leftover_text = old_node.text
        for markdown_image in markdown_images:
            markdown_image_text = f"![{markdown_image[0]}]({markdown_image[1]})"
            first_part, leftover_text = leftover_text.split(markdown_image_text, 1)
            node_parts.extend([first_part, (markdown_image[0], markdown_image[1])])
        node_parts.append(leftover_text)
        for i in range(len(node_parts)):
            if node_parts[i] == '':
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(node_parts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(node_parts[i][0], TextType.IMAGE, node_parts[i][1]))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        markdown_links = extract_markdown_links(old_node.text)
        if len(markdown_links) == 0:
            new_nodes.append(old_node)
            continue
        node_parts = []
        leftover_text = old_node.text
        for markdown_link in markdown_links:
            markdown_link_text = f"[{markdown_link[0]}]({markdown_link[1]})"
            first_part, leftover_text = leftover_text.split(markdown_link_text, 1)
            node_parts.extend([first_part, (markdown_link[0], markdown_link[1])])
        node_parts.append(leftover_text)
        for i in range(len(node_parts)):
            if node_parts[i] == '':
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(node_parts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(node_parts[i][0], TextType.LINK, node_parts[i][1]))
    return new_nodes

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    split_delimiters = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]
    for i in range(len(split_delimiters)):
        new_nodes = split_nodes_delimiter(new_nodes.copy(), *split_delimiters[i])
    new_nodes = split_nodes_image(new_nodes.copy())
    new_nodes = split_nodes_link(new_nodes.copy())
    return new_nodes