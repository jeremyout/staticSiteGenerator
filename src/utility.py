from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected input to be of type TextNode")
    if text_node.text_type == text_type_text:
        return LeafNode(tag=None,value=text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode(tag="b", value=text_node.text)
    if  text_node.text_type == text_type_italic:
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode(tag=text_node.text_type, value=text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode(tag="img", value="",props={"src":text_node.url, "alt":text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")
