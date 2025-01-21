from ics import Calendar
import math

from core.lib import (
    save_calendars
)
from core.config import host
from modules.globals import MODULE_FUNCTIONS

class UE :
    name: str = ""
    semester: int = 0
    master: str = ""
    paths: dict[str, Calendar] = {}
    def __init__(self, calendar: dict[str, Calendar], ue: str, semester: int, master: str):
        self.name = ue
        self.semester = semester
        self.master = master
        year = math.ceil(semester/2)
        key = f"{master}.{ue}"  # Génère une clé composite
        self.paths = save_calendars(MODULE_FUNCTIONS[key](calendar[ue]), f"m{year}/{master}/{ue}".lower())

    def to_json(self):
        return {
            "name": self.name,
            "year": f"M{math.ceil(self.semester/2)}",
            "semester": self.semester,
            "groups": [{
                "group": f"{name}",
                "url": f"{host}{path}"
            } for name, path in self.paths.items()]
        }

    def to_markdown(self):
        return f"## {self.name} (M{math.ceil(self.semester/2)}, S{self.semester%2})\n" + ''.join(f"### {name}\n{host}{path}\n\n" for name, path in self.paths.items())
