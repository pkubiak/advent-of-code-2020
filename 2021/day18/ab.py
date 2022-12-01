from copy import deepcopy


class Node:
    left: 'Node'
    right: 'Node'
    value: int

    @staticmethod
    def load(expr):
        if isinstance(expr, int):
            return Node(value=expr)
        assert isinstance(expr, list) and len(expr) == 2
    
        return Node(left=Node.load(expr[0]), right=Node.load(expr[1]))

    def save(self):
        if self.is_leaf:
            return self.value
        return [self.left.save(), self.right.save()]

    @property
    def is_leaf(self):
        return self.left is None

    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

    @property
    def magnitude(self):
        if self.is_leaf:
            return self.value
        return 3 * self.left.magnitude + 2 * self.right.magnitude

    def _split(self) -> bool:
        def visit(node):
            if node.is_leaf:
                if node.value >= 10:
                    node.left = Node(value=(node.value//2))
                    node.right = Node(value=(node.value+1)//2) 
                    node.value = None
                    raise StopIteration
            else:
                visit(node.left)
                visit(node.right)

        try:
            visit(self)
            return False
        except StopIteration:
            return True


    def _explode(self) -> bool:
        right_value = None
        last_leaf = None

        def visit(node, depth):
            nonlocal right_value, last_leaf

            if node.is_leaf: 
                if right_value is not None:
                    node.value += right_value
                    raise StopIteration
                last_leaf = node
            elif depth == 4 and right_value is None:
                assert node.left.is_leaf and node.right.is_leaf
                if last_leaf:
                    last_leaf.value += node.left.value
                right_value = node.right.value

                # Change node to Leaf
                node.value = 0
                node.left = node.right = None
            else:
                visit(node.left, depth + 1)
                visit(node.right, depth + 1)

        try:
            visit(self, 0)
        except  StopIteration:
            pass
        return right_value is not None

    def reduce(self):
        while self._explode() or self._split():
            pass

    def __add__(self, other):
        assert isinstance(other, Node)
        node = Node(left=deepcopy(self), right=deepcopy(other))
        node.reduce()
        return node


def load_numbers(path):
    with open(path) as file:
        return [eval(line) for line in file.read().split("\n")]


def part_a(numbers):
    result = Node.load(numbers[0])

    for number in numbers[1:]:
        result = result + Node.load(number)
    return result.magnitude


def part_b(numbers):
    numbers = [Node.load(x) for x in numbers]
    
    best = 0
    for a in numbers:
        for b in numbers:
            if a is not b:
                best = max(best, (a+b).magnitude)
    return best


if __name__ == "__main__":
    numbers = load_numbers("input.txt")

    print("a:", part_a(numbers))
    print("b:", part_b(numbers))