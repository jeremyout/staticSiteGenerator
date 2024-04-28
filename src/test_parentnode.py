import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parentNode_eq(self):
        node = ParentNode(
                            "p",
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text"),
                            ],
                        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parentNode_nested_eq(self):
        section_node = ParentNode(
                                    "div",
                                    [
                                        LeafNode("h1", "Section Header"),
                                        ParentNode(
                                            "ul",
                                            [
                                                LeafNode("li", "List item 1"),
                                                LeafNode("li", "List item 2"),
                                            ]
                                        ),
                                    ]
                                )

        top_level_node = ParentNode(
                                    "div",
                                    [
                                        LeafNode("p", "This is a paragraph in the top-level div."),
                                        section_node,
                                    ]
                                    )
        
        expected_html = "<div><p>This is a paragraph in the top-level div.</p><div><h1>Section Header</h1><ul><li>List item 1</li><li>List item 2</li></ul></div></div>"
        self.assertEqual(top_level_node.to_html(), expected_html)

    def test_parentNode_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(
                None,  # This simulates not providing a tag.
                [LeafNode("p", "Sample text")]
            )
        
    def test_parentNode_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(
                "div",
                []  # This simulates providing an empty list of children.
            )

    def test_parentNode_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parentNode_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

