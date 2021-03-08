ELECTION ANALYSIS README 
By Monica M. Holmes
3-8-2021

# Election_Analysis
I will use Visual Studio Code and some Python
## Project Overview
Assist a Colorado Election Board employee, Tom, with in an election audit of tabulated results for a US Congressional precinct in Colorado. I am tasked with automating and reporting:
  -Total number of votes cast.
  -Get a complete list of candidates who received votes.
  -Total number of votes for each candidate.
  -The percentage of votes for each candidate.
  -The winner of the election based on popular vote.
  
This written code may also be used to audit other congressional districts, senate districts, and local elections. 

Three primary voting methods were taken into account, 
  1. Mail-in Ballots - which were hand counted at the central office.
  2. Punch Cards - which were machine counted and tabulated.
  3. Direct Recording Electronic (DRE) counting machines - which were computer counted.
Altogether, the votes cast by these three methods were counted and together determined the Election Results.

## Resources
My data source was the election_results.csv file.
The software used was Python 3, Visual Studio Code, Jupyter, Git Bash and Git Hub.

## Summary
The analysis of the election show that:
-There were 369,711 votes cast
-The list of candidates who received votes and their corresponding number and percentage of votes were:
  Charles Casper Stockham: 23.0% (85,213)
  Diana DeGette: 73.8% (272,892)
  Raymon Anthony Doane: 3.1% (11,606)
-The winner of the election (based on popular vote) was Diana DeGette, with 272,892 votes and 73.8% of the vote.

Election Results
-------------------------
Total Votes: 369,711
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------

## Challenge Overview Advantages and Disadvantages
In summary, the advantages of automating the election analysis process using Python and Visual Studio Code is it speeds up the results, improves accuracy and allows for multiple analysis methods to be performed, enhancing the question/answer process.  It also may be copied and used elsewhere. The disadvantage of automating the election process is it is time consuming to write the code.
After getting used to using Jupyter and Visual Studio Code (VS), I found VS is good for running the entire code, where Juypter allows you to break the code up into sections. The other drawback was when using Git Bash to upload and commit my code, I often received error messages and it would not commit using that manner. 

## Challenge Summary
In summary, this data was very complex and challenging but in rewarding in the end. I definitely see the advantages of using Python code for large data sets and for situations that may utilize the application in multiple ways/methods. These are excellent tools and will further businesses now and in the future. In this instance it quickly performed election results analysis, determining the winner to be Diana DeGette.

