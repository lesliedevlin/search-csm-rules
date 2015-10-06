import json
import cpapi

apiCon = 0

def create_api_connection():
    clientid     = 'e7479203'
    clientsecret = '1a3663e39969e0bc696a0ab6f13c0231' 

    global apiCon
    apiCon = cpapi.CPAPI()

    apiCon.key_id = clientid
    apiCon.secret = clientsecret

    resp = apiCon.authenticateClient()


def getCSM(rulestring):
    data, authError = apiCon.doGetIssuesCSM()
    issue = data['issues']
    for issues in issue:
        if rulestring in issues['rule_key']:
            print  "Match: Rule ID: %s\n\tRule Name: %s\n Policy ID: %s\n\n " % (issues['rule_key'], issues['name'], issues['policy_id'])

# MAIN

create_api_connection()

rulestring = 'IPv6'
#rulestring = raw_input("Enter a search string for your rule:  ")

getCSM(rulestring)

