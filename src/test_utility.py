import unittest

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
from utility import (
    text_node_to_html_node,
    split_nodes_delimiter
    )

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

    def test_utility_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        print(new_nodes)
    def test_utility_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )
    def test_utility_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )
    def test_utility_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )
    def test_utility_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )
    def test_utility_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )