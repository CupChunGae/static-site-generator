from textnode import *

def main():
    example = TextNode("This is some anchor", TextType.LINK, "https://www.boot.dev")
    print(example.__repr__())

main()