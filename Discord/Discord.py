import json
import requests



# #=========================================================================
# #                              QA TEST
# #=========================================================================

def Report_Discord(content):
    url = 'https://discord.com/api/webhooks/939009660848054333/beLjectYQLrei21WdnMdxtaPemzKXniGgT8pk0VhGOU9s12tDixXBNK7j54PHUEnSsFQ'
    data = {
        "content": content
    }

    requests.post(url,json=data)