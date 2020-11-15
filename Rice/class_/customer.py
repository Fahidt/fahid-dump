

class customer:
    def __init__(self, id, date, email):
        self.id = cid
        self.date = date
        self.email = email
    
    def customer_info(self):
        return(self.id,  self.date, self.email)
    
    def __repr__(self):
        return f"id: {self.id}, date: {self.date}, email: {self.email}"