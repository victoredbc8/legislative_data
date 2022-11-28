import csv

from controller import LegislativeData
from models.bill import Bill
from models.legislator import Legislator
from models.vote import Vote
from models.vote_result import VoteResult


class LegislatorsVotes(LegislativeData):
    def __init__(self):
        super().__init__()
        self.legislators_votes()
        self.bills_votes()
        self.build_legislators_csv()
        self.build_bills_csv()

    def legislators_votes(self):
        for vote in self.vote_results:
            legislator = self.get_legislator(vote.legislator)
            if legislator.id == vote.legislator:
                legislator.vote(vote)

    def bills_votes(self):
        for vote_result in self.vote_results:
            vote = self.get_vote(vote_result.vote)
            bill = self.get_bill(vote.bill)
            if vote_result.type == 1:
                bill.add_supporter_vote()
            elif vote_result.type == 2:
                bill.add_opposer_vote()
            else:
                print("invalid vote type")
    
    def get_bill(self, bill_id):
        for bill in self.bills:
            if bill.id == bill_id:
                return bill
    
    def get_vote(self, vote_id):
        for vote in self.votes:
            if vote.id == vote_id:
                return vote

    def get_legislator(self, legislator_id):
        for legislator in self.legislators:
            if legislator_id == legislator.id:
                return legislator
    
    def build_legislators_csv(self):
        header = ["id", "name", "num_supported_bills", "num_opposed_bills"]
        with open("./repository/output/legislators-support-oppose-count.csv", "w", encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerow(header)

            for legislator in self.legislators:
                row = [
                    legislator.id, 
                    legislator.name, 
                    legislator.number_of_supported_bills(), 
                    legislator.number_of_opposed_bills()
                ]
                writer.writerow(row)

    def build_bills_csv(self):
        header = ["id", "title", "supporter_count", "opposer_count", "primary_sponsor"]
        with open("./repository/output/bills.csv", "w", encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerow(header)

            for bill in self.bills:
                # TODO: not use bare except
                try:
                    primary_sponsor = self.get_legislator(bill.sponsor).name
                except:
                    primary_sponsor = " "
                row = [
                    bill.id,
                    bill.title,
                    bill.supporter_count,
                    bill.opposer_count,
                    primary_sponsor,
                ]
                writer.writerow(row)

# Run script
legislator = LegislatorsVotes()



    # print(legislators[0].number_of_supported_bills())
    # print(legislators[0].number_of_opposed_bills())

    # print(bills[0])
    # print(bills[0].opposer_count)
    # print(bills[0].supporter_count)
