#Import random to randomly place peoples 
import random as rd




###########################################################""
"""Define the OpenSpace
  Step 1:  Initialize the openspace attributes
  Step 2:  Calcualte total seat capacity
  Step 3:  Organize

"""
###################################################################

class OpenSpace:
    
    def __init__(self, tables):
        self.tables = tables
        self.number_of_people = 0
        self.people_without_seats = []

    def total_seats(self):
        return sum(table.capacity for table in self.tables)

    def organize(self, people):
        rd.shuffle(people)
        for table in self.tables:
            for seat in table.seats:
                if seat.free and people:
                    seat.assign_occupant(people.pop())
                    self.number_of_people += 1
        if people:
            self.people_without_seats = people

########################################################################
# Create  a display function to display the statistical informations of the open space
# Calculated Total number of peoples and number of peoples with out seat
#            

########################################################################
    def display(self):
        print("\nOpenspace info:")
        total_seats = sum(table.capacity for table in self.tables)
        total_people = self.number_of_people + len(self.people_without_seats)
        print(f"\nNumber of People in the Room: {total_people}")
        print(f"\nTotal Number of Seats in the Room: {total_seats}")

        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i} Information:")
            table.display()
#
        if self.people_without_seats:
            print("\nPeople without a seat:")
            for i, person in enumerate(self.people_without_seats, start=1):
                print(f"{i}. {person['Name']}")
            print(" All seats are filled. Please find an alternative arrangement for these peoples.")

            
