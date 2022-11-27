import csv

from models.bill import Bill
from models.legislator import Legislator
from models.vote import Vote
from models.vote_result import VoteResult


class LegislativeData:
    def __init__(self):
        self.legislators = self.extract_legislators()
        self.bills = self.extract_bills()
        self.votes = self.extract_votes()
        self.vote_results = self.extract_vote_results()

    def extract_legislators(self):
        legislators = []
        with open("./repository/legislators.csv", 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for row in csvreader:
                legislators.append(Legislator(id=int(row[0]), name=row[1]))
        return legislators

    def extract_bills(self):
        with open("./repository/bills.csv", 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            bills = []
            for row in csvreader:
                self.bills.append(Bill(id=int(row[0]), title=row[1]))

    def extract_votes(self):
        with open("./repository/votes.csv", 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            votes = []
            for row in csvreader:
                self.votes.append(Vote(id=int(row[0]), bill=int(row[1])))
        
    def extract_vote_results(self):
        with open("./repository/vote_results.csv", 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            vote_results = []
            for row in csvreader:
                self.vote_results.append(VoteResult(id=int(row[0]), legislator=int(row[1]), vote=int(row[2]), type=int(row[3])))
