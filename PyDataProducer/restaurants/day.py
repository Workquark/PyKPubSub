class Day:
    opens_at: str
    closes_at: str
    is_closed: bool

    def __init__(self, opens_at: str, closes_at: str, is_closed: bool) -> None:
        self.opens_at = opens_at
        self.closes_at = closes_at
        self.is_closed = is_closed
