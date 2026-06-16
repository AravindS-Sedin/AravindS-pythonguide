# Browser History Navigator
#
# Uses:
# 1. Back Stack
# 2. Forward Stack
# 3. History Queue (deque)
#
# Features:
# - Visit URL
# - Back
# - Forward
# - Show History
# - Search History

from collections import deque


class Browser:

    def __init__(self):

        self.back_stack = []

        self.forward_stack = []

        self.history_log = deque()

    def current_page(self):

        if not self.back_stack:
            return None

        return self.back_stack[-1]

    def visit(self, url):

        self.back_stack.append(url)

        self.forward_stack.clear()

        self.history_log.append(url)

        print(f"Visited: {url}")

    def back(self):

        if len(self.back_stack) <= 1:
            print("Nothing to go back to")
            return

        page = self.back_stack.pop()

        self.forward_stack.append(page)

        current = self.back_stack[-1]

        self.history_log.append(current)

        print(f"Now at: {current}")

    def forward(self):

        if not self.forward_stack:
            print("Nothing to go forward to")
            return

        page = self.forward_stack.pop()

        self.back_stack.append(page)

        self.history_log.append(page)

        print(f"Now at: {page}")

    def show_history(self):

        print("\nHistory:")

        print(" → ".join(self.history_log))

        print(f"Current: {self.current_page()}")

    def search_history(self, keyword):

        results = []

        for url in self.history_log:

            if keyword.lower() in url.lower():
                results.append(url)

        return results

  
def main():
    browser = Browser()

    browser.visit("google.com")
    browser.visit("youtube.com")
    browser.visit("github.com")

    browser.back()
    browser.back()

    browser.forward()

    browser.visit("stackoverflow.com")

    browser.show_history()


main()