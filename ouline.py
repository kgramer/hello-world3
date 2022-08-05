from bs4 import BeautifulSoup
import requests
import json

#function to get job list from url f'https://www.talent.com/jobs?k={role}&l={location}'
def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    print("Enter role you want to search")
    role = input()
    print("Enter location you want to search")
    location = input()
    print("Chosen role: "+role+". Chosen location: "+location)
    print("Searching...")
    # getJobList(role,location)
    
if __name__ == '__main__':
    main()