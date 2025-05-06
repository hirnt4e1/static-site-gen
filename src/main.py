from textnode import TextType, TextNode

def main():
    dummy = TextNode("This is text", TextType.BOLD, "http://localhost:8888")
    print(dummy)

main()