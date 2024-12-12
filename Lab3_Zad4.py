# Stanisław Kusiak

from collections import deque, defaultdict

class AhoCorasic:
    def __init__(self):
        self.num_nodes = 1
        self.edges = [{}]
        self.fail = [-1]
        self.output = [set()]
    
    def add_word(self, word, index):
        current_node = 0
        for char in word:
            if char not in self.edges[current_node]:
                self.edges[current_node][char] = self.num_nodes
                self.edges.append({})
                self.fail.append(-1)
                self.output.append(set())
                self.num_nodes += 1

            current_node = self.edges[current_node][char]

        self.output[current_node].add(index)

    def build(self):
        queue = deque()

        for char, next_node in self.edges[0].items():
            self.fail[next_node] = 0
            queue.append(next_node)

        while queue:
            current_node = queue.popleft()

            for char, next_node in self.edges[current_node].items():
                fail_node = self.fail[current_node]
                while fail_node != -1 and char not in self.edges[fail_node]:
                    fail_node = self.fail[fail_node]

                if fail_node == -1:
                    self.fail[next_node] = 0
                else:
                    self.fail[next_node] = self.edges[fail_node][char]
                    self.output[next_node].update(self.output[self.fail[next_node]])

                queue.append(next_node)

    def search(self, text):
        current_node = 0
        results = defaultdict(list)

        for i, char in enumerate(text):
            while current_node != -1 and char not in self.edges[current_node]:
                current_node = self.fail[current_node]
            
            if current_node == -1:
                current_node = 0
                continue

            current_node = self.edges[current_node][char]
            
            for word_index in self.output[current_node]:
                results[word_index].append(i)

        return results 


ac_test = AhoCorasic()
words = ["he", "she", "sheep", "eepy"]

for i, word in enumerate(words):
    ac_test.add_word(word, i)

ac_test.build()

text = "sheepy"

results = ac_test.search(text)

for word, position in results.items():
    print(f"Word: {words[word]}, Position: {position}")
