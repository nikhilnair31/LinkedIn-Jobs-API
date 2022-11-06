# from dotenv import load_dotenv
# import os

# load_dotenv()
# print(os.environ["email"])

import json

data = json.load(open('src\cred.json'))

f = open(".env1", "x")

for key, value in data.items():
    f.write(f"{key.upper()}={value}\n")


# EMAIL='nikhilnair3118@gmail.com'
# PASS='aS7Q9iAYfh/nT-;'

# FIREBASE_DATABASE_URL='https://nikhil-nair-default-rtdb.firebaseio.com'

# FIREBASE_ADMIN_PRIVATE_KEY_ID='2762285979e13a47f80dd54a3ede4507b5906d78'
# FIREBASE_ADMIN_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHGkj4BR4pZvXz\nERGZglZF1hJfwIoslxFz2Z2Lrmw22I4wJmZV5E7dy6EpBKar6EjPa1cL0gw7gTFC\n+zZGC+JcDR42Qy2SJ0XN+KUW4//B5KPru7efuTui8F0nOnjWO4W7f0p9v/Hx3hj3\nnLZOSlUuYLQo4RFZTWWTR6EG4yIvE6e0NnoX8GjFjqnN4xzQbaGgWbC4iDL/U/YF\n+6r8VCDpFBhIIeA7hkmMOBnzN46o6dLrS9yvHKSjZwqt9Gc4fG9klUA4J9hV9a9o\nOXmXLM9EyUH5peXRfNQjEbd0Ad3LoNs8tsK1aoX3fGITdqOrVSSI2gv9tiv59Xl4\nlF0ZiDRpAgMBAAECggEATzfGm6QRpaB5ME50xbLFl8C+i8mEUIyE3abSl9584O+V\n11OX+Qm/VWEtTLA0joZ73cdUGXhn9I8JJiDkrccRt9ViVW2yJooorHSHXw21V5Sc\nofEM9OiS8VgYgEC0Dm0dXwYdAd6KqdTX80EvigPqU2sXk4JFUFZKmWhxCdf6ZGcG\ncxXIfK5Pqh5YCJS5nidOhG9Fyt0XaWc+xZbROd9TJLmGjdhEFjyEcSFeYK0F0Cbd\nWjtXya2U3Hg+yGE5HYu8rqzGjXPgHaCRexqlPPt1VmpYsS70NzMIW2PF2EGuVzqU\n2c3lGXsr6llCJgOQ0B2+ee18HXqCpUOD6kTayLIBRwKBgQDkFUbRGE29IhBkB5w0\n5nB5v3tpokFRutplZcAHghEdAIVE4im7qOklV5QTxB550LJJNvD1lNQDzFGZPkVR\nMmLeRJYeeBAUBJG/No4tawhroRUUf3DV4fn9QwbEDAEtJEh1NRSIlimDa8T+00l7\n5EJZ3BehnA4QE8pOhPfShg5QdwKBgQDfePCJwlnLrJ+i5okEF4OY0DRzKDcAiqjf\n3F/+wVnRDDG98C8SwO/3W2/fbGj/RgVJR7nQi+KMhubqMSuGVIPNJ+UzghwezV7m\nlzY4AXfDLl3OTMeTrVPx39wgzsOD7ifkyVujnShdH4dz/LKWtJYShMhJPMpJs1xY\n9tB2Htq6HwKBgBjiMV2ylxihVMR1CBfFZFQEDgTSTOoLxrP1S+QFzrQpUGDZg9AT\nd4w5Z9BYPzLvD+Ro+BTy7caUTfq4DnvzUVIKjY45bxef//6qhwxxdvO3GUOpO7g5\n9ToqS9yrqp0wLi+LYPgd2d2arl1W09eOaabAGlvpWKdsYU/7tcXkFj+1AoGAVLw0\n6OdqyRHxjgFAHu8TlRQNb0TmZiwtkIStWZnTBrNLASxbjQ7fbrmbF+qxfWn9gyXR\nTURdaM+WK2LtkAfn2hiwjfFd3EgfHexkQKQ91yJzq0/ttQ9Z7zLk8wOzmwjo05WO\nS+HBdl4ILHC6/u4GoYr7rtmAEqYR9CHSNZfJdB0CgYEAyl/euMStHDKdS6HsD6eJ\nOFgBxPpVtlmAyfO9HqH0BBLIlNWmcaHeF4dTUPqocUgIvRMdwtygXNjWqI5LCxVG\n9XTPncuVEtVV4C9BQxpymxtEMLzyXPsugiq6BGgXgnbonisleyL/JV+RZluYSd6Z\nVeR+4YdBsocwUoGNwzz56Rc=\n-----END PRIVATE KEY-----\n"
# FIREBASE_ADMIN_CLIENT_EMAIL='firebase-adminsdk-gamwn@nikhil-nair.iam.gserviceaccount.com'
# FIREBASE_ADMIN_CLIENT_ID='110227509871586027379'
# FIREBASE_ADMIN_CLIENT_X509_CERT_URL="https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-gamwn%40nikhil-nair.iam.gserviceaccount.com"