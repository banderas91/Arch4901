from dataclasses import dataclass, field
from decimal import Decimal  
from datetime import datetime
from typing import List

@dataclass
class Ticket:

    id: int  
    departure_zone: int   
    arrival_zone: int
    route_number: int 
    departure_time: datetime
    arrival_time: datetime
    buyer_id: int
    is_used: bool = False
    price: Decimal = Decimal(0)
    place: str = ""

    def mark_as_used(self):
        self.is_used = True

    def get_info(self):
        return f"Ticket {self.id} from {self.departure_zone} to {self.arrival_zone}. Departure: {self.departure_time}"
        
@dataclass        
class User:

    id: int
    name: str
    login: str  
    password_hash_code: int
    account_id: int
    tickets: List[Ticket] = field(default_factory=list)

    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)

    def get_unused_tickets(self):
        return [t for t in self.tickets if t.is_used == False]
      
@dataclass
class Account:

    user_account_id: int
    balance: Decimal = Decimal(0)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
        
ticket = Ticket(
    id=1,
    departure_zone=2,
    arrival_zone=3,
    route_number=123,
    departure_time=datetime(2023,11,12,10,0),
    arrival_time=datetime(2023,11,12,12,0), 
    buyer_id=12345    
)

print(ticket.get_info())

user = User(
    id=1,
    name="John Doe",
    login="john",
    password_hash_code=12345,
    account_id=100  
)

user.add_ticket(ticket)
print(user.get_unused_tickets())

ticket.mark_as_used()

account = Account(user_account_id=1)
account.deposit(100) 
account.withdraw(50)
print(account.balance)