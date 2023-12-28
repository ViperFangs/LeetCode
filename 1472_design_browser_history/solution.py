""" 
Author: Aarya
Description: You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.
    Implement the BrowserHistory class:
        BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
        void visit(string url) Visits url from the current page. It clears up all the forward history.
        string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. 
            Return the current url after moving back in history at most steps.
        string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. 
            Return the current url after forwarding in history at most steps.
Space Complexity: O(n), the algorithm uses a doubly linked list to do the operations
Logic: The logic here is to use a doubly linked list to store the next and previous browser pages visited.
    Note: There is another solution that uses a list which is faster for some operations.
"""
# BrowserNode stores the url, next and previous values
class BrowserNode:
    def __init__(self, val = "", next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
# BrowserHistory keeps track of a pointer to navigate through the history
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