# Stanisław Kusiak

class Tree:
    def __init__(self, value = "root", branch = None):
        self.value = value
        self.branch = []

        if branch is not None:
            for i in branch:
                self.branch.append(Tree(i))

    def str(self, depth = 0):
        temp = str(self.value)
        temp += "\n"
        depth += 1
        for child in self.branch:
            for n in range(0, depth):
                temp += "   "
            
            temp += child.str(depth)

        return temp

    def __str__(self):
        temp = self.str()
        return temp
    
    def add_branch(self, child):
        self.branch.append(Tree(child))

# Testing __str__ method
oak = Tree("root", ["0", "1"])
oak.add_branch("2")
oak.branch[0].add_branch("00")
oak.branch[0].add_branch("01")
oak.branch[0].add_branch("02")

oak.branch[1].add_branch("10")
oak.branch[1].add_branch("11")
oak.branch[1].branch[0].add_branch("100")
print(oak)

