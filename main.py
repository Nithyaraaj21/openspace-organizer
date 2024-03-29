#import functions from src
from time import perf_counter
start_time = perf_counter()
import pandas as pd
from src.utils import Store          # Stores the results in an Excel file named "result.xlxs"
from src.table import Table          # Functions to define tbale and seat 
from src.openspace import OpenSpace  #Function to organise seating arrangement


if __name__ == "__main__":

    excel_file = "colleagues.xlsx"    # Define the path to the excel file
    data = pd.read_excel(excel_file)  # Read  data from the Excel file 
    
    
    colleagues = data.to_dict(orient="records")  # Data to dictionary
    tables = [Table(4), Table(4), Table(4), Table(4) , Table(4), Table(4)]
    openspace = OpenSpace(tables)
    openspace.organize(colleagues)
    openspace.display()
    store_instance = Store(openspace.tables)
    store_instance.store("results.xlsx")
    
print(f"\nTime spent to finish the task: {perf_counter() - start_time} seconds.")    