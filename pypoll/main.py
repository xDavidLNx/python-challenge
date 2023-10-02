import csv
import os

csvpath = os.path.join('.','resources','election_data.csv')
results_path = os.path.join('.','analysis','Election_results.txt')

#With opens file using the cvs module
with open (csvpath, encoding = 'UTF-8') as dataset:
    csv_iterable = csv.reader(dataset) # creates an iterable object from the dataset
    header = next(csv_iterable) #Separates the headers from the rest of the data, allowing to make calculations

    #Sets variables, to take in values as a cumulative value and lists respectively
    voters = []
    candidates = []
    unique_candidates = []
    votes = {}
    win_percentage = {}
    #For loop to create a dictionary when a new candidate, or vote for an existing candidate, is read.
    for row in csv_iterable:    

        voters.append(row[0]) # stores the voters id for future count
        candidates= row[2] #gets the candidate of every row in the loop
        
        #Conditional that adds a candidate to the dictionary and sums 1 vote when a candidate already exists in unique_candidates dictionary
        if candidates not in unique_candidates:
            unique_candidates.append(candidates)
            votes[candidates] = 0
        votes[candidates] += 1
    #counts the total votes using the lenght of the list created in the previous for loop       
    total_votes = len(voters)
    
    #For loop that calculates the amount of votes of a candidate relative to the voters pool and stores it in a new dictionary
    for x in votes:
        win_percentage[x] = (votes[x]/total_votes) * 100
        
    winner = max(win_percentage,key=win_percentage.get) #gets the max win percentage from the dictionary, from that it gets the paired name 
    # debugging print
    #print(f'Total votes cast: {total_votes}')
    #print(unique_candidates)
    #print(votes)
    #print(win_percentage)
    #print(winner)

    #Terminal
    print("Election results\n\n")
    print("---------------------------------------------\n\n")
    print("Total votes : %d \n\n" % total_votes)
    print("---------------------------------------------\n\n")
    
    # iterates on the votes and win_percentage dictionaries to display any candidates and information stored in said dictionaries 
    for key, value in votes.items():
        candidate_results = (f'{key}: {win_percentage[key]:.3f}% ({value:,})\n')
        print(candidate_results)
    print("\n---------------------------------------------\n")
    print("\n Winner: %s" % winner)
    
#Exports and string formats the results to a new txt file    
with open(results_path, 'w') as exportdata:
    exportdata.write("Election results\n\n")
    exportdata.write("---------------------------------------------\n\n")
    exportdata.write("Total votes : %d \n\n" % total_votes)
    exportdata.write("---------------------------------------------\n\n")
    
    # iterates on the votes and win_percentage dictionaries to display any candidates and information stored in said dictionaries 
    for key, value in votes.items():
        candidate_results = (f'{key}: {win_percentage[key]:.3f}% ({value:,})\n')
        exportdata.write(candidate_results)
    exportdata.write("\n---------------------------------------------\n")
    exportdata.write("\n Winner: %s" % winner)
    
