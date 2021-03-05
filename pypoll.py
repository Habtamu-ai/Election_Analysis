#. The Data we need to retrive
#1.Total number of votes cast.
#2. A complit list of candidate who recived votes.
#3. The percentages of votes each candidates won.
#4. The toal number of votes each candidates won.
#5. The winneer of the electio based on popular votes

import csv
import os
file_to_load = os.path.join( 'c:' + os.sep, "Users","Tikuyeh","Election_Analysis","Resources","Election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
     #print(election_data)
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join('c:'+ os.sep, "Users","Tikuyeh","Election_Analysis", "analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write three counties to the file.
 txt_file.write("Counties in the Election\n_ _ _ _ _ _ _ _ _ _\nArapahoe\nDenver\nJefferson")
# Open the election results and read the file.
with open(file_to_load) as election_data:
  # Read the file object with the reader function.
    file_reader = csv.reader(election_data) 
    # Print the header row.
    headers = next(file_reader)
    print(headers)