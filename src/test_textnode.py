import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_textNode_eq(self):
        node = TextNode("This is a text node", "text")
        node2 = TextNode("This is a text node", "text")
        self.assertEqual(node, node2)

    def test_textNode_eq_false(self):
        node = TextNode("This is a text node", "text")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_textNode_eq_false2(self):
        node = TextNode("This is a text node", "text")
        node2 = TextNode("This is a text node2", "text")
        self.assertNotEqual(node, node2)

    def test_textNode_eq_url(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", "italic", "https://www.boot.dev"
        )
        self.assertEqual(node, node2)
    def test_textNode_eq_url_false(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", "italic", "https://www.boot2.dev"
        )
        self.assertNotEqual(node,node2)
    def test_textNode_repr(self):
        node = TextNode("This is a test node", "italic", "www.testrepr.com")
        self.assertEqual(node.__repr__(), "TextNode(This is a test node, italic, www.testrepr.com)" )


if __name__ == "__main__":
    unittest.main()
