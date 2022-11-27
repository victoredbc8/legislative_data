from models.vote_result import VoteResult


class Legislator:

    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
        self.voted_bills = []
    
    def __str__(self):
        return self.name

    def vote(self, bill:VoteResult):
        self.voted_bills.append(bill)
    
    def number_of_supported_bills(self):
        supported_bills = 0
        for vote in self.voted_bills:
            if vote.type == 1:
                supported_bills += 1
        return supported_bills

    def number_of_opposed_bills(self):
        opposed_bills = 0
        for bill in self.voted_bills:
            if bill.type == 2:
                opposed_bills += 1
        return opposed_bills
