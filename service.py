from controller import LegislativeData
from models.bill import Bill
from models.legislator import Legislator
from models.vote import Vote
from models.vote_result import VoteResult


class LegislatorsVotes(LegislativeData):
    def __init__(self):
        self.legislators_votes()
        self.bills_votes()

    def legislators_votes(self):
        for vote in vote_results:
            legislator = self.get_legislator()
            if legislator.id == vote.legislator:
                legislator.vote(vote)

    def bills_votes(self):
        for vote_result in vote_results:
            vote = self.get_vote(vote_result.vote_id)
            bill = self.get_bill(vote.bill)
            if vote_result.type == 1:
                bill.add_supporter_vote()
            if vote_result.type == 2:
                bill.add_opposer_vote()
        print(self.bills)
    
    def get_bill(self, bill_id):
        for bill in self.bills:
            if bill.id == bill_id:
                return bill
    
    def get_vote(self, vote_id):
        for vote in self.votes:
            if vote.id == vote_id:
                return vote

    def get_legislator(self, legislator_id):
        for legislator in legislators:
            if legislator_id == legislator.id:
                return legislator

    # print(legislators[0].number_of_supported_bills())
    # print(legislators[0].number_of_opposed_bills())

    # print(bills[0])
    # print(bills[0].opposer_count)
    # print(bills[0].supporter_count)
