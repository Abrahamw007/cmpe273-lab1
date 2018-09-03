import requests as r
import json as j

# to create a github repo from post request
# github_url="https://github.com/abrahamwilliam"
#
# data=j.dumps({'name':'cmpe273-lab1','description':'cmpe273-lab1'})
# githubChecking=r.get(github_url,auth=('abrahamwilliam','abrahammm'))
# print(githubChecking.status_code)
# githubCreation=r.post(github_url,data,auth=('abrahamwilliam','abrahammm'))
# print(githubCreation.status_code)

for i in range(3):
    MyRequest=r.get('https://webhook.site/#/5443c001-7a4d-46e3-81a2-af671125128a')
    print(MyRequest.headers['Date'])



