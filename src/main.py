from textnode import TextNode
from htmlnode import HTMLNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)
    html = HTMLNode(None,None,None,{"href": "https://www.google.com", "target": "_blank"})
    print(html.props_to_html())


main()