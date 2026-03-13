from typing import Literal


class HealthService:
    def get_status(self) -> Literal["ok"]:
        return "ok"
