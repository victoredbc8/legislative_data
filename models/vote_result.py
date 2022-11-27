class VoteResult:

    def __init__(self, id:int, legislator:int, vote:int, type:int):
        self.id = id
        self.legislator = legislator
        self.vote = vote
        self.type = type

        
    def __str__(self):
        return f"{self.legislator} voted {self.type}"
        


