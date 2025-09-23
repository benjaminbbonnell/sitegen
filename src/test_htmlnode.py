import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_prop_to_html_false(self):
        node = HTMLNode("tag", "value", "children", {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), "href=https://www.google.com, target=_blank")

    def test_repr(self):
        node = HTMLNode("tag", "value", "children", "props")
        self.assertEqual(
            "HTMLNode(tag=tag, value=value, children=children, props=props)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()