# import json
# import boto3

import requests
import argparse
import json
import random

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--token", help="OAuth token from GitHub", required=True)
parser.add_argument("-n", "--number", help="Number of repos to create", required=False)
parser.add_argument("-host", "--host", help="GitHub Enterprise Host", required=True)
args = parser.parse_args()

authToken = args.token
num_of_repos = args.number
hostname = args.host

url = 'https://' + hostname + '/rest/api/latest'

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "Bearer " + authToken
}

if num_of_repos is None:
    num_of_repos = 10

num_of_projects = 3

def create_projects(key):
    query = url + '/project'
    res = requests.post(query, headers = headers, data=json.dumps({"name" : "Project Example" , "key" : key }))
    print(res)
    return res

def create_repos(projectkey, repo_name, slug) :
    query = url + '/projects/' + projectkey + '/repos'
    res = requests.post(query, headers = headers, data=json.dumps(  { "name": repo_name,
  "scmId": "git",
  "slug": slug },))
    print(res.json())
    return res.json()

for n in range(1, int(num_of_projects) + 1):
    project = "PROJ" + str(n)
    #create_projects(project)

for n in range(1, int(num_of_repos) + 1):
    repository = 'demo-repo-' + str(n)
    projectkey = "PROJ" + str(random.randint(1, int(num_of_projects)))
    print("Creating repo: " + repository + " in project: " + projectkey)
    create_repos(projectkey, repository)
