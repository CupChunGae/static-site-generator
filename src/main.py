print("hello world")

from textnode import *
def main():
    example = TextNode("This is some anchor", "link", "https://www.boot.dev")
    return example.__repr__

main()