import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("Text A", TextType.BOLD)
        node2 = TextNode("Text B", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_equal_url(self):
        node1 = TextNode("Node", TextType.LINK, url="https://a.com")
        node2 = TextNode("Node", TextType.LINK, url="https://b.com")
        self.assertNotEqual(node1, node2)

    def test_default_url_is_none(self):
        node = TextNode("Check default URL", TextType.CODE)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
