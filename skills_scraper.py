#Import libraries
from linkedin_api import Linkedin
import csv
from csv import reader
import time
import random

#Set username and password
username = input('Enter username :')
password = input('Enter password : ')
api = Linkedin(username,password)

#Open CSV output file
file = open('skills.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Skills'])

list_of_skills = []
user_count = 0

#Get skills from all ids in usersId.csv
with open('usersId.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    next(csv_reader)
    for row in csv_reader:
        print('Scraping User : ', user_count)
        skills = api.get_profile_skills(row[0])
        for skill in skills:
            list_of_skills.append(skill['name'])
        user_count += 1
        time.sleep(random.randint(1, 3))

#Write to CSV
for i in range(len(list_of_skills)):
    writer.writerow([list_of_skills[i]])

print("File successfully created !")

file.close()
read_obj.close()

