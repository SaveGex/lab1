
from itertools import takewhile

def printBombka(bombka: str, indexes: list[dict[str, int]]) -> func:

    def decorator(func) -> func:

        def wrapper(*args, **kwargs) -> any:

            result = func(*args, **kwargs)

            for index in indexes:

                x = index['x']

                y = index['y']

                row = result[y]

                spacesInRow = sum(
                    1 for _ in takewhile(lambda c: c == ' ', row)
                )

                result[y][x + spacesInRow] = bombka

            return result

        return wrapper

    return decorator


def triangel(start: int, end: int, space: int, christmasTree: list[list[str]] | None = None) -> list[list[str]]:

    if christmasTree is None:
        christmasTree = []

    space = space if space > 0 else 0

    if(start <= end):

        left_side = ' ' * space + '^' * start
        right_side = '^' * (start - 1) + ' ' * space

        christmasTree.append(list(left_side + right_side))

        return triangel(start + 1, end, space - 1, christmasTree)
    else:

        return christmasTree


def buildTree(bombka, indexes: list[dict[str, int]]) -> list[list[str]]:

    @printBombka(bombka, indexes)
    def draw() -> list[list[str]]:
        tempTree: list[list[str]] = []
        tempTree.extend(triangel(1, 4, 4))
        tempTree.extend(triangel(3, 5, 2))
        return tempTree

    return draw()
def printTree(arg: list[list[str]]):
    print('\n'.join(''.join(line) for line in arg))

indexes = [
    {
        'x': 1,
        'y': 2
    },
    {
        'x': 5,
        'y': 3
    },
    {
        'x': 3,
        'y': 5
    },
    {
        'x': 6,
        'y': 6
    }
]

christmasTree: list[list[str]] = buildTree('o', indexes)
christmasTree2: list[list[str]] = buildTree('*', indexes)
printTree(christmasTree)
print("_______________________")
printTree(christmasTree2)


# def print_bombkę(bombka: str):
#     print("""
#     ^
#    ^^^
#   ^{bombka}^^^
#  ^^^^^{bombka}^
#   ^^^^^
#  ^^{bombka}^^^^
# ^^^^^^{bombka}^^
#     """)

# print_bombkę('o')
# print_bombkę('*')
