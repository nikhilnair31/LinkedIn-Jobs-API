import os
from dotenv import load_dotenv
from collections import defaultdict
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from linkedin_api import Linkedin

load_dotenv()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Setup stuff
cred = {
  "type": "service_account",
  "project_id": "nikhil-nair",
  "private_key_id": os.environ["FIREBASE_ADMIN_PRIVATE_KEY_ID"],
  "private_key": os.environ["FIREBASE_ADMIN_PRIVATE_KEY"].replace(r'\n', '\n'),
  "client_email": os.environ["FIREBASE_ADMIN_CLIENT_EMAIL"],
  "client_id": os.environ["FIREBASE_ADMIN_CLIENT_ID"],
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.environ["FIREBASE_ADMIN_CLIENT_X509_CERT_URL"]
}
cred = credentials.Certificate(cred)
firebase_admin = firebase_admin.initialize_app(cred, {'databaseURL': os.environ["FIREBASE_DATABASE_URL"]})

# Adding child to tore LinkedIn data only
ref = db.reference("/linkedin_data/")
# Authenticate using any Linkedin account credentials
api = Linkedin(os.environ["EMAIL"], os.environ["PASS"])
# Empty dict to fill up on each run
pushable_data_dict = defaultdict(dict)

# GET my profile info for dropdowns
def get_dropdown_info():
    profile = api.get_profile('nikhilnair31')
    print(profile)
    pushable_data_dict['work'] = profile['experience']
    pushable_data_dict['education'] = profile['education']
    pushable_data_dict['languages']  = profile['languages']

    if "projects" in profile:
        profileprojects = profile['projects']
        updatedprofileprojects = []
        for eachproj in profileprojects:
            if "members" in eachproj:
                del eachproj['members']
            if "occupation" in eachproj:
                del eachproj['occupation']
            updatedprofileprojects.append(eachproj)
        pushable_data_dict['projects'] = updatedprofileprojects
    
    if "certifications" in profile:
        profilecertificates = profile['certifications']
        updatedprofilecertificates = []
        for eachcert in profilecertificates:
            if "company" in eachcert:
                del eachcert['company']
            if "companyUrn" in eachcert:
                del eachcert['companyUrn']
            if "displaySource" in eachcert:
                del eachcert['displaySource']
            if "licenseNumber" in eachcert:
                del eachcert['licenseNumber']
            updatedprofilecertificates.append(eachcert)
        pushable_data_dict['certificates'] = updatedprofilecertificates

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