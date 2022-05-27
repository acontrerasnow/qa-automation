import requests
import json
import os
import slack


def web_hook_url(Scenario,step,msg):
     web_hook_url = 'https://hooks.slack.com/services/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'
     Part  = 'qa'
     slack_msg = {"text": Part+'\n'+"```"+'Scenario: '+Scenario+'\n'+'step:' +step+'\n'+msg+"```"}
     msn_to_slack = requests.post(web_hook_url, data=json.dumps(slack_msg))
     return msn_to_slack



#web_hook_url('scenario','step','msg')



