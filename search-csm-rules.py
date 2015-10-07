import json
import cpapi

apiCon = 0

def create_api_connection():

    from config import clientid, clientsecret

    global apiCon
    apiCon = cpapi.CPAPI()

    apiCon.key_id = clientid
    apiCon.secret = clientsecret

    resp = apiCon.authenticateClient()

def getPolicyName(policy_id):
    data, authError = apiCon.doGetCSMPolicyDetails(policy_id)
    policy_deets = data['policy']
    return policy_deets['name']

def getCSM(rulestring):
    data, authError = apiCon.doGetIssuesCSM()
    issue = data['issues']
    for issues in issue:
        if rulestring in issues['rule_key']:
            policy_name = getPolicyName(issues['policy_id'])
            print  "Match:\tRule ID:\t%s\n\tRule Name:\t%s\n\tPolicy ID:\t%s\n\tPolicy Name:\t%s\n\n " % (issues['rule_key'], issues['name'], issues['policy_id'], policy_name)

# MAIN

create_api_connection()

rulestring = raw_input("Enter a search string for your rule:  ")

getCSM(rulestring)

