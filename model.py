

class Bill:

    def __init__(self, id:int, title:str, sponsor=int):
        self.id  = id
        self.title = title
        self.sponsor = sponsor

    def __str__(self):
        return self.title


class Legislator:

    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
    
    def __str__(self):
        return self.name


class Vote:

    def __init__(self, id:int, bill:int):
        self.id = id
        self.bill = bill


class VoteResult:

    def __init__(self, id:int, legislator:int, vote:int, type:int):
        self.id = id
        self.legislator = legislator
        self.vote = vote
        self.type = type

    
        