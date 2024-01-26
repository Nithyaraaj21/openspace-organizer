# Define the Seat class
class Seat:

    # Initialize the attributes
    def __init__(self, free=True, seat_occupant=None):
        self._free = free # A boolean indicating if the seat is free
        self._seat_occupant = seat_occupant # A string indicating the name of the occupant

    # Define the string representation of the seat
    def __str__(self):
        if self.free:
            return "This seat is free."
        else:
            return f"This seat is occupied by {self.seat_occupant}."

    # Define the getter and setter methods for the free attribute
    @property
    def free(self):
        return self._free

    @free.setter
    def free(self, value):
        # Check if the value is a boolean
        if isinstance(value, bool):
            self._free = value
        else:
            raise TypeError("The free attribute must be a boolean.")

    # Define the getter and setter methods for the seat_occupant attribute
    @property
    def seat_occupant(self):
        return self._seat_occupant

    @seat_occupant.setter
    def seat_occupant(self, value):
        # Check if the value is a string or None
        if isinstance(value, str) or value is None:
            self._seat_occupant = value
        else:
            raise TypeError("The seat_occupant attribute must be a string or None.")

    # Set_occupant 
    def set_occupant(self, name):
        
        if self.free: # Check if the seat is free
            self.seat_occupant = name # Assign the name to the seat_occupant attribute
            self.free = False # Set the free attribute to False
            print(f"{name} has been assigned to this seat.")  # Print a confirmation message
        else:
            print(f"This seat is already occupied by {self.seat_occupant}.") # Print an error message

    # Remove_occupant 
    def remove_occupant(self):
        if not self.free: # Check if the seat is occupied
            name = self.seat_occupant # Store the name of the seat_occupant in a variable
            # Set the seat_occupant attribute to None
            self.seat_occupant = None
            # Set the free attribute to True
            self.free = True
            # Print a confirmation message
            print(f"{name} has been removed from this seat.")
            # Return the name of the removed seat_occupant
            return name
        else:
            # Print an error message
            print(f"This seat is already free.")

# Define the Table class
class Table:
    # Initialize the attributes
    def __init__(self, capacity):
        self.capacity = capacity # An integer indicating the number of seats at the table
        self.seats = [Seat() for _ in range(capacity)] # A list of Seat objects (size = capacity)

    # Define the string representation of the table
    def __str__(self):
        return f"This table has {self.capacity} seats, of which {len(self)} are occupied."

    # Define the length of the table
    def __len__(self):
        # Initialize a counter for the occupied seats
        occupied_seats = 0
        # Loop through the seats
        for seat in self.seats:
            # Check if the seat is occupied
            if not seat.free:
                # Increment the counter
                occupied_seats += 1
        # Return the number of occupied seats
        return occupied_seats

    # Has free_spot?
    def has_free_spot(self):
       
        for seat in self.seats:  # Loop through the seats
            
            if seat.free:         # Check if any seat is free
                # Return True
                return True
        # Return False if no seat is free
        return False

    # assign_seat
    def assign_seat(self, name):
        # Check if the table has a free spot
        if self.has_free_spot():
            # Loop through the seats
            for seat in self.seats:
                # Check if the seat is free
                if seat.free:
                    # Set the seat_occupant of the seat to the name
                    seat.set_occupant(name)
                    # Break the loop
                    break
        else:
            # Print an error message
            print(f"This table is full. No seat available for {name}. Please arrange a new table.")

    # no_of_seats_left
    def no_of_seats_left(self):
        # Return the difference between the capacity and the length of the table
        return self.capacity - len(self)