# Define the Seat class
class Seat:
    def __init__(self, free=True, seat_occupant=None):
        self.free = free
        self.seat_occupant = seat_occupant

    def assign_occupant(self, person):
        if self.free:
            self.seat_occupant = person
            self.free = False
  
class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self):
        return any(seat.free for seat in self.seats)

    def assign_seat(self, person):
        if self.has_free_spot():
            for seat in self.seats:
                if seat.free:
                    seat.assign_occupant(person)
                    break
        else:
            print(f"This table is full. No seat available for {person['Name']}.")

    def num_of_seats_left(self):
        return sum(seat.free for seat in self.seats)

    def display(self):
        print(f"Table Capacity: {self.capacity}")
        for i, seat in enumerate(self.seats, start=1):
            status = "Occupied" if not seat.free else "Free"
            print(f"Seat {i}: {status} - Occupant: {seat.seat_occupant['Name']}")

    

            