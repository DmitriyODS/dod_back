from dataclasses import dataclass


@dataclass
class Statistics:
    count_all: int = 0
    count_mk_1: int = 0
    count_mk_2: int = 0

    def to_dict(self):
        return {
            'count_all': self.count_all,
            'count_mk_1': self.count_mk_1,
            'count_mk_2': self.count_mk_2,
        }
