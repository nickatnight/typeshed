class Renderer:
    buf: str
    last_out: str
    def render(self, ast): ...
    def lit(self, s) -> None: ...
    def cr(self) -> None: ...
    def out(self, s) -> None: ...