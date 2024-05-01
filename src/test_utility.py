import unittest

from textnode import TextNode

from leafnode import LeafNode
from utility import text_node_to_html_node

class TestParentNode(unittest.TestCase):
    def test_utility_textToHtmlNode_text(self):
        textnode = TextNode("This is a plain text node", "text")
        self.assertEqual(text_node_to_html_node(textnode).to_html(),'This is a plain text node')
    def test_utility_textToHtmlNode_bold(self):
        textnode = TextNode("This is a bold node", "bold")
        self.assertEqual(text_node_to_html_node(textnode).to_html(),'<b>This is a bold node</b>')
    def test_utility_textToHtmlNode_italics(self):
        textnode = TextNode("This is an italic node", "italic")
        self.assertEqual(text_node_to_html_node(textnode).to_html(),'<i>This is an italic node</i>')
    def test_utility_textToHtmlNode_code(self):
        textnode = TextNode("This is a code node", "code")
        self.assertEqual(text_node_to_html_node(textnode).to_html(),'<code>This is a code node</code>')
    def test_utility_textToHtmlNode_aTag(self):
        textnode = TextNode("This is an anchor node", "link","https://www.google.com")
        self.assertEqual(text_node_to_html_node(textnode).to_html(), '<a href="https://www.google.com">This is an anchor node</a>')
    def test_utility_textToHtmlNode_image(self):
        textnode = TextNode("This is an image node", "image","https://www.images.google.com")
        self.assertEqual(text_node_to_html_node(textnode).to_html(),'<img src="https://www.images.google.com" alt="This is an image node">')