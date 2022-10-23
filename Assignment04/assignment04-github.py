#lab 05
from hashlib import new
from github import Github
from config import config as cfg
import requests
import json

# storing key in Config file
apikey = cfg["githubkey"]
g = Github(apikey)

# get the repo our text file is stored in
repo = g.get_repo("conor-mccaffrey/dataRepWK05")

# get the contents of the file
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# print out the contents of the file, keeping this as a sanity check
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)


# make our changes to the file, i.e replacing Andrew with Conor, using simple string replace method
str = contentOfFile
newContents = contentOfFile.replace('Andrew', 'Conor')
#print(newContents)

# add to gitHub
gitHubResponse=repo.update_file(fileInfo.path,"replace all instances of the word Andrew with Conor",
newContents,fileInfo.sha)
print (gitHubResponse)