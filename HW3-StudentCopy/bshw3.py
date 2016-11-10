##
# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import re
import requests
from bs4 import BeautifulSoup


print ("Import successful")
print("\n")

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")


# Part 1
findword = soup.find_all(text = re.compile('student'))
for student in findword:
    new = str(student).replace('student', 'AMAZING student')
    student.replace_with(new)


# Part 2 
for links in soup.find_all('iframe'):
	links['src'] = "/Users/JonathanBracci/Desktop/problemset3/SI206/Barcelona.jpg"

# Part 3
for image in soup.find_all('img'):
	image['src'] = "/Users/JonathanBracci/Desktop/problemset3/SI206/HW3-StudentCopy/Media/logo.png"

new_html_file = open("HW3_BS_OutPut.html", "w")
print('Creating html file ....')
print ("\n")
new_html_file.write(str(soup))
new_html_file.close()
print('Finished')