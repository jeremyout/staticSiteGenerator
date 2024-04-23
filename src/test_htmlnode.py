import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlNode_props_to_html_anchor(self):
        html = HTMLNode(props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(html.props_to_html(), ' href="https://www.example.com" target="_blank"')

    def test_htmlNode_props_to_html_multipleTypes(self):
        html = HTMLNode(props={"class": "btn btn-primary", "data-toggle": "modal", "aria-expanded": "false"})
        self.assertEqual(html.props_to_html(), ' class="btn btn-primary" data-toggle="modal" aria-expanded="false"')

    def test_htmlNode_props_to_html_styleAndEvent(self):
        html = HTMLNode(props={"style": "color: red; font-size: 14px;", "onclick": "alert('Hello, World!')"})
        self.assertEqual(html.props_to_html(), ' style="color: red; font-size: 14px;" onclick="alert(\'Hello, World!\')"')

    def test_htmlNode_props_to_html_empty(self):
        html = HTMLNode(props={})
        self.assertEqual(html.props_to_html(), '')

    def test_htmlNode_props_to_html_specialChars(self):
        html = HTMLNode(props={"title": "Example's \"Special\" Characters & Symbols"})
        self.assertEqual(html.props_to_html(), ' title="Example\'s \"Special\" Characters & Symbols"')

    def test_htmlNode_repr(self):
        html = HTMLNode(tag="p", value="This is a test paragraph", props={"href": "https://www.example.com", "target": "_blank"})
        self.assertEqual(html.__repr__(), 
                         "HTMLNode(tag: p, value: This is a test paragraph, children: None, props: {'href': 'https://www.example.com', 'target': '_blank'})")


if __name__ == "__main__":
    unittest.main()
