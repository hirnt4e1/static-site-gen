class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        return "".join(list(map(lambda kv: f' {kv[0]}="{kv[1]}"', self.props.items())))
    def __eq__(self, value):
        if (self.tag, self.value, self.children, self.props) == (value.tag, value.value, value.children, value.props):
            return True
        return False
    def __repr__(self):
        return f"HTMLNode:({self.tag}, {self.value}, {self.children}, {self.props})"