def triangel(start: int, end: int, space: int):
    space = space if space > 0 else 0
    if(start <= end):
        print(' ' * space, '^' * start, sep='', end='')
        print('^' * (start - 1), ' ' * space, sep='')
        triangel(start + 1, end, space - 1)
    else:
        return

def buildTree():
    triangel(1, 4, 4)
    triangel(3, 5, 2)
    print(' '*2, '###')

buildTree()

# print("""
#      ^
#     ^^^
#    ^^^^^
#   ^^^^^^^
#    ^^^^^
#   ^^^^^^^
#  ^^^^^^^^^
#     ###
# """)

