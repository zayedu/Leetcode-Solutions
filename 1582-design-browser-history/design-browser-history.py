class BrowserHistory:

    def __init__(self, homepage: str):
        self.backwards = [ ]
        self.forwards = [ ]
        self.homepage = homepage
        self.site = homepage

    def visit(self, url: str) -> None:
        self.forwards = [ ]
        self.backwards.append(self.site)
        self.site = url

    def back(self, steps: int) -> str:
        count = 0

        while count < steps:
            if len(self.backwards) < 1:
                return self.homepage
            self.forwards.append(self.site)
            
            self.site = self.backwards.pop()
            count+=1

        return self.site

        

    def forward(self, steps: int) -> str:
        count = 0

        while count < steps:
            if len(self.forwards) < 1:
                return self.site
            self.backwards.append(self.site)
            
            self.site = self.forwards.pop()
            count += 1

        return self.site

        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)