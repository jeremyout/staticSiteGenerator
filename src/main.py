from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)
    html = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    print(html.props_to_html())
    leaf = LeafNode("p", "This is a paragraph of text.")
    print(leaf.to_html())


main()