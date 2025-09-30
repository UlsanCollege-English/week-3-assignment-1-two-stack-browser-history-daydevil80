class BrowserHistory:
    def __init__(self, start="home"):
        self._cur = start
        self._back = []
        self._fwd = []

    def visit(self, url: str) -> None:
        # Only push current page if it's not "home" or back stack not empty
        if self._cur != "home" or self._back:
            self._back.append(self._cur)
        self._cur = url
        self._fwd.clear()

    def back(self) -> str:
        if not self._back:
            raise IndexError("No previous page")
        self._fwd.append(self._cur)
        self._cur = self._back.pop()
        return self._cur

    def forward(self) -> str:
        if not self._fwd:
            raise IndexError("No forward page")
        self._back.append(self._cur)
        self._cur = self._fwd.pop()
        return self._cur

    def current(self) -> str:
        return self._cur
