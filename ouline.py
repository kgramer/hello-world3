from bs4 import BeautifulSoup
import requests
import json

def getJobList(role,location):

    url = "https://www.talent.com/jobs?k="+role+"&l="+location

    response = requests.request("GET", url)
    print('Response code: '+str(response.status_code))

    soup = BeautifulSoup(response.content, 'html.parser')
    JobDetails = soup.find_all('div', class_='card card__job')
    myArr = {}
    i = 0
    for job in JobDetails:
        jobTitle = job.find('h2', class_='card__job-title').text.strip()
        company = job.find('div', class_='card__job-empname-label').text.strip()
        description = job.find('p', class_='card__job-snippet').text.replace('\n', '').replace("'", "").strip()
        jobDetailsjson = {
            "Title": jobTitle,
            "Company": company,
            "Description": description
        }
        myArr[i] = jobDetailsjson
        i = i + 1
    return myArr





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
    print(getJobList(role,location))
    
if __name__ == '__main__':
    main()