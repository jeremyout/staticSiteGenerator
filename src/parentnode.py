from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("A tag must be supplied to a ParentNode")
        if not children:
            raise ValueError("A ParentNode must have children")
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        # Step 1: Open Tag
        open_tag = f"<{self.tag}>"
        # Prepare to hold content of all children
        children_content = ""
        # Step 2: Loop Over Children (this is the recursive step)
        for child in self.children:
            children_content += child.to_html()  # Recursively call to_html() on each child
        # Step 3: Close Tag
        close_tag = f"</{self.tag}>"
        # Combine and return
        return open_tag + children_content + close_tag