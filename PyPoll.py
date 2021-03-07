# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete lis of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
#with open (file_to_load) as election_data:

    # To do: perform analysis.
#    print(election_data)
# Import csv and os  and add our dependencies.   
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter to zero.
total_votes = 0

# Declare a new list, candidate_options and candidate_votes.
candidate_options = []
# Declare the empty dictionary.
candidate_votes ={}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
#Print the file object.
    #print(election_data)
    # To do: read and analyze the data here.
# Read the file object with the reader function.
    #file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:

    # To do: read and analyze the data here.

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to/Increment the total_votes by 1.
        total_votes += 1
        #Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list via append 
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
        # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidates count.
        candidate_votes[candidate_name] += 1
      
        # Print the candidate vote dictionary.
    #print(candidate_votes)
 
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.#for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")
 
   

