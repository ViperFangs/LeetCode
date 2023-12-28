class BrowserNode:
    def __init__(self, val = "", next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = BrowserNode(homepage)

    def visit(self, url: str) -> None:
        new_node = BrowserNode(url, None, self.current)
        self.current.next = new_node
        self.current = self.current.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev is not None:
            steps -= 1
            self.current = self.current.prev

        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next is not None:
            steps -= 1
            self.current = self.current.next

        return self.current.val     

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)