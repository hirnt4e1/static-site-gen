from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("missing tag")
        if self.children == None:
            raise ValueError("missing children")
        prefix = f'<{self.tag}{self.props_to_html()}>'
        suffix = f'</{self.tag}>'
        html_string = '' + prefix
        for child in self.children:
            html_string += child.to_html()
        html_string += suffix
        return html_string
