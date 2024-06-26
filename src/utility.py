import re

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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i,section in enumerate(sections):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches