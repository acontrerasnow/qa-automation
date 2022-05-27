import json
import requests



# #=========================================================================
# #                              QA TEST
# #=========================================================================

def Report_Discord(content):
    url = ''
    data = {
        "content": content
    }

    requests.post(url,json=data)