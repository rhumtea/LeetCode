class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = []
        self.stack.append(homepage)
        self.index = 0
        self.length = 1

    def visit(self, url: str) -> None:
        if self.index+1 < len(self.stack):
            self.stack[self.index+1] = url
            self.index += 1
            self.length = self.index+1
        else:
            self.stack.append(url)
            self.length += 1
            self.index += 1

    def back(self, steps: int) -> str:
        self.index = max(0, self.index - steps)
        return self.stack[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(self.length-1, self.index + steps)
        return self.stack[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)