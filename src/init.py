import os
import logging
import requests
import firebase_admin
from firebase_admin import db
from collections import defaultdict
from firebase_admin import credentials

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# region Setup Firebase and Env Vars
proxycurl_api_key = 'AKjT11L3-pcJI0lbvk5Iyw'
cred = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nikhil-nair-default-rtdb.firebaseio.com'
})
#endregion

#region Setup other stuff
ref = db.reference("/linkedin_data/")
pushable_data_dict = defaultdict(dict)
#endregion

#region Main functions
# GET my profile info for dropdowns
def get_dropdown_info():
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': 'Bearer ' + proxycurl_api_key}
    params = {
        'url': f'https://www.linkedin.com/in/nikhilnair31/',
    }
    response = requests.get(api_endpoint, params=params, headers=header_dic).json()

    pushable_data_dict['work'] = response['experiences']
    pushable_data_dict['education'] = response['education']
    pushable_data_dict['languages']  = response['languages']
    pushable_data_dict['projects'] = response['accomplishment_projects']
    pushable_data_dict['certificates'] = response['certifications']

# GET my profile posts info
def get_posts_info():
    allposts = api.get_profile_posts('nikhilnair31', 'ACoAACbXpHcBc_ApSJ1Ms1TGv8RQMT33HFfPWbs', 10)
    print(allposts)

    firstpost = allposts[0]
    pushable_data_dict['post']['postTitle'] = firstpost['content']['com.linkedin.voyager.feed.render.ArticleComponent']['title']['text']
    pushable_data_dict['post']['postURL'] = firstpost['content']['com.linkedin.voyager.feed.render.ArticleComponent']['navigationContext']['actionTarget']
    pushable_data_dict['post']['postText'] = firstpost['commentary']['text']['text']
    pushable_data_dict['post']['postLikes'] = firstpost['socialDetail']['totalSocialActivityCounts']['numLikes']
    pushable_data_dict['post']['postComments'] = firstpost['socialDetail']['totalSocialActivityCounts']['numComments']
    pushable_data_dict['post']['postViews'] = firstpost['socialDetail']['totalSocialActivityCounts']['numImpressions']
    pushable_data_dict['post']['postShares'] = firstpost['socialDetail']['totalShares']

def push_dict_to_firebase(dict):
    # ref.push().set(dict)
    ref.set(dict)
    
def print_dict(func_source, dict):
    print('\n', func_source, ':\n', dict)
#endregion

def handler(event, context): 
    try:
        get_dropdown_info()
        get_posts_info()
        push_dict_to_firebase(pushable_data_dict)
        return {
            'statusCode': 200,
            'body': 'success bish'
        }
    except Exception as e: 
        logger.error(f'logging f max: {e}\n\n')
        return {
            'statusCode': 400,
            'body': 'f max'
        }

if __name__=="__main__":
    handler(None, None)