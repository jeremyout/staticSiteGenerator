from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value and self.tag not in ['img', 'br', 'hr']:
            raise ValueError("Leaf nodes require a value, except for self-closing tags")
        if self.tag is None:
            return self.value
        else:
            if self.tag in ['img', 'br', 'hr']:
                return f'<{self.tag}{self.props_to_html()}>'
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
            
    
    def __repr__(self):
        return f"LeafNode(value: {self.value}, tag: {self.tag}, props: {self.props})"