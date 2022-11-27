class Bill:

    def __init__(self, id:int, title:str, sponsor=int):
        self.id  = id
        self.title = title
        self.sponsor = sponsor
        self.supporter_count = 0
        self.opposer_count = 0

    def __str__(self):
        return self.title

    def add_supporter_vote(self):
        self.supporter_count += 1
        return self.title

    def add_opposer_vote(self):
        self.opposer_count += 1
