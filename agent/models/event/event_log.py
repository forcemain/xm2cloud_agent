#! -*- coding: utf-8 -*-


from agent.models import BaseModel


class EventLog(BaseModel):
    def to_dict(self):
        pass

    def is_valid(self):
        return True
