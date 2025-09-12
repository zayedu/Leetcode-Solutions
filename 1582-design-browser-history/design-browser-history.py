class BrowserHistory:

    def __init__(self, homepage: str):

        self.homepage = homepage
        self.current_site = homepage
        self.previous_sites = [ ]
        self.forward_sites = [ ]

    def visit(self, url: str) -> None:
        self.previous_sites.append(self.current_site)
        self.current_site = url
        self.forward_sites = [ ]

    def back(self, steps: int) -> str:

        for step in range(steps):
            
            if not self.previous_sites:
                break

            self.forward_sites.append(self.current_site)
            self.current_site = self.previous_sites.pop()

        return self.current_site

    def forward(self, steps: int) -> str:

        for step in range(steps):
            
            if not self.forward_sites:
                break

            self.previous_sites.append(self.current_site)
            self.current_site = self.forward_sites.pop()

        return self.current_site
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)