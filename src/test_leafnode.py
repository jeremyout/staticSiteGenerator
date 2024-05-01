import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafNode_pTag(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), '<p>This is a paragraph of text.</p>')

    def test_leafNode_aTag(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leafNode_imgTag(self):
        leaf = LeafNode("img", "", {"src": "https://www.google.com", "alt": "Some alt text"})
        self.assertEqual(leaf.to_html(), '<img src="https://www.google.com" alt="Some alt text">')


    def test_leafNode_noTag(self):
        leaf = LeafNode(tag=None, value="Plain old text")
        self.assertEqual(leaf.to_html(), 'Plain old text')

    def test_leafNode_repr(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.__repr__(), 
                         "LeafNode(value: This is a paragraph of text., tag: p, props: None)")
        


if __name__ == "__main__":
    unittest.main()
