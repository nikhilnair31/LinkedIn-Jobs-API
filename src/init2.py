import os
import logging
from dotenv import load_dotenv
from collections import defaultdict
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from linkedin_api import Linkedin

load_dotenv()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# region Setup Firebase and Env Vars
# cred = credentials.Certificate(
#     {
#         "type": os.environ.get("FIREBASE_ADMIN_TYPE"),
#         "project_id": os.environ.get("FIREBASE_ADMIN_PROJECT_ID"),
#         "private_key_id": os.environ.get("FIREBASE_ADMIN_PRIVATE_KEY_ID"),
#         "private_key": os.environ.get("FIREBASE_ADMIN_PRIVATE_KEY").replace('\\n', '\n'),
#         "client_email": os.environ.get("FIREBASE_ADMIN_CLIENT_EMAIL"),
#         "client_id": os.environ.get("FIREBASE_ADMIN_CLIENT_ID"),
#         "auth_uri": os.environ.get("FIREBASE_ADMIN_AUTH_URI"),
#         "token_uri": os.environ.get("FIREBASE_ADMIN_TOKEN_URI"),
#         "auth_provider_x509_cert_url": os.environ.get("FIREBASE_ADMIN_AUTH_PROVIDER_X509_CERT_URL"),
#         "client_x509_cert_url": os.environ.get("FIREBASE_ADMIN_CLIENT_X509_CERT_URL")
#     }
#     {
#         "type": "service_account",
#         "project_id": "nikhil-nair",
#         "private_key_id": "2762285979e13a47f80dd54a3ede4507b5906d78",
#         "private_key": '-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHGkj4BR4pZvXz\nERGZglZF1hJfwIoslxFz2Z2Lrmw22I4wJmZV5E7dy6EpBKar6EjPa1cL0gw7gTFC\n+zZGC+JcDR42Qy2SJ0XN+KUW4//B5KPru7efuTui8F0nOnjWO4W7f0p9v/Hx3hj3\nnLZOSlUuYLQo4RFZTWWTR6EG4yIvE6e0NnoX8GjFjqnN4xzQbaGgWbC4iDL/U/YF\n+6r8VCDpFBhIIeA7hkmMOBnzN46o6dLrS9yvHKSjZwqt9Gc4fG9klUA4J9hV9a9o\nOXmXLM9EyUH5peXRfNQjEbd0Ad3LoNs8tsK1aoX3fGITdqOrVSSI2gv9tiv59Xl4\nlF0ZiDRpAgMBAAECggEATzfGm6QRpaB5ME50xbLFl8C+i8mEUIyE3abSl9584O+V\n11OX+Qm/VWEtTLA0joZ73cdUGXhn9I8JJiDkrccRt9ViVW2yJooorHSHXw21V5Sc\nofEM9OiS8VgYgEC0Dm0dXwYdAd6KqdTX80EvigPqU2sXk4JFUFZKmWhxCdf6ZGcG\ncxXIfK5Pqh5YCJS5nidOhG9Fyt0XaWc+xZbROd9TJLmGjdhEFjyEcSFeYK0F0Cbd\nWjtXya2U3Hg+yGE5HYu8rqzGjXPgHaCRexqlPPt1VmpYsS70NzMIW2PF2EGuVzqU\n2c3lGXsr6llCJgOQ0B2+ee18HXqCpUOD6kTayLIBRwKBgQDkFUbRGE29IhBkB5w0\n5nB5v3tpokFRutplZcAHghEdAIVE4im7qOklV5QTxB550LJJNvD1lNQDzFGZPkVR\nMmLeRJYeeBAUBJG/No4tawhroRUUf3DV4fn9QwbEDAEtJEh1NRSIlimDa8T+00l7\n5EJZ3BehnA4QE8pOhPfShg5QdwKBgQDfePCJwlnLrJ+i5okEF4OY0DRzKDcAiqjf\n3F/+wVnRDDG98C8SwO/3W2/fbGj/RgVJR7nQi+KMhubqMSuGVIPNJ+UzghwezV7m\nlzY4AXfDLl3OTMeTrVPx39wgzsOD7ifkyVujnShdH4dz/LKWtJYShMhJPMpJs1xY\n9tB2Htq6HwKBgBjiMV2ylxihVMR1CBfFZFQEDgTSTOoLxrP1S+QFzrQpUGDZg9AT\nd4w5Z9BYPzLvD+Ro+BTy7caUTfq4DnvzUVIKjY45bxef//6qhwxxdvO3GUOpO7g5\n9ToqS9yrqp0wLi+LYPgd2d2arl1W09eOaabAGlvpWKdsYU/7tcXkFj+1AoGAVLw0\n6OdqyRHxjgFAHu8TlRQNb0TmZiwtkIStWZnTBrNLASxbjQ7fbrmbF+qxfWn9gyXR\nTURdaM+WK2LtkAfn2hiwjfFd3EgfHexkQKQ91yJzq0/ttQ9Z7zLk8wOzmwjo05WO\nS+HBdl4ILHC6/u4GoYr7rtmAEqYR9CHSNZfJdB0CgYEAyl/euMStHDKdS6HsD6eJ\nOFgBxPpVtlmAyfO9HqH0BBLIlNWmcaHeF4dTUPqocUgIvRMdwtygXNjWqI5LCxVG\n9XTPncuVEtVV4C9BQxpymxtEMLzyXPsugiq6BGgXgnbonisleyL/JV+RZluYSd6Z\nVeR+4YdBsocwUoGNwzz56Rc=\n-----END PRIVATE KEY-----\n',
#         "client_email": "firebase-adminsdk-gamwn@nikhil-nair.iam.gserviceaccount.com",
#         "client_id": "110227509871586027379",
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-gamwn%40nikhil-nair.iam.gserviceaccount.com"
#     }
# )

cred = credentials.Certificate("cred.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nikhil-nair-default-rtdb.firebaseio.com'
})
ref = db.reference("/linkedin_data/")
api = Linkedin('nikhilnair3118@gmail.com', 'aS7Q9iAYfh/nT-;')
pushable_data_dict = defaultdict(dict)
#endregion

#region Setup other stuff
# Adding child to tore LinkedIn data only
ref = db.reference("/linkedin_data/")
# Authenticate using any Linkedin account credentials
logger.info(f'EMAIL: {os.environ["EMAIL"]} | PASS: {os.environ["PASS"]}')
api = Linkedin(os.environ["EMAIL"], os.environ["PASS"])
# Empty dict to fill up on each run
pushable_data_dict = defaultdict(dict)
#endregion

#region Main functions
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