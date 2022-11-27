import csv
from model import Legislator, Bill, Vote, VoteResult

class SerializerData:
    def __init__(self):
        self.supported_bills = 0

    with open("./repository/legislators.csv", 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        legislators = []
        for row in csvreader:
            legislators.append(Legislator(id=row[0], name=row[1]))
        print(legislators)

    with open("./repository/bills.csv", 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        bills = []
        for row in csvreader:
            bills.append(Bill(id=row[0], title=row[1]))
        print(bills)

    with open("./repository/votes.csv", 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        votes = []
        for row in csvreader:
            votes.append(Vote(id=row[0], bill=row[1]))
        print(votes)
        
    with open("./repository/vote_results.csv", 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        vote_results = []
        for row in csvreader:
            vote_results.append(VoteResult(id=row[0], legislator=row[1], vote=row[2], type=row[3]))
        print(vote_results)