# -*- coding:utf-8 -*-

"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to umap/settings/local.py. It should not be checked into
your code repository.

"""


from umap.settings.base import *   # pylint: disable=W0614,W0401
import environ
import dj_database_url

# Initialise environment variables
env = environ.Env(
    UMAP_DEMO_SITE=(bool, False),
    UMAP_ALLOW_ANONYMOUS=(bool, False),
    UMAP_READONLY=(bool, False),
    UMAP_EXCLUDE_DEFAULT_MAPS=(bool, False)

)
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY',default='test')
INTERNAL_IPS = ('127.0.0.1', )
ALLOWED_HOSTS = ['*', ]

DEBUG = False

ADMINS = (
    (env('ADMIN_NAME',default='test'), env('ADMIN_EMAIL',default='test')),
)
MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, default='postgis://postgres:example@localhost/postgres')
}

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

LANGUAGE_CODE = 'tr'

# Set to False if login into django account should not be possible. You can
# administer accounts in the admin interface.
ENABLE_ACCOUNT_LOGIN = True

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.bitbucket.BitbucketOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.openstreetmap.OpenStreetMapOAuth',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_GITHUB_KEY = env('SOCIAL_AUTH_GITHUB_KEY',default='xxx')
SOCIAL_AUTH_GITHUB_SECRET = env('SOCIAL_AUTH_GITHUB_SECRET',default='xxx')
SOCIAL_AUTH_BITBUCKET_KEY = env('SOCIAL_AUTH_BITBUCKET_KEY',default='xxx')
SOCIAL_AUTH_BITBUCKET_SECRET = env('SOCIAL_AUTH_BITBUCKET_SECRET',default='xxx')
# We need email to associate with other Oauth providers
SOCIAL_AUTH_GITHUB_SCOPE = ["user:email", ]
SOCIAL_AUTH_TWITTER_KEY = env('SOCIAL_AUTH_TWITTER_KEY',default='xxx')
SOCIAL_AUTH_TWITTER_SECRET = env('SOCIAL_AUTH_TWITTER_SECRET',default='xxx')
SOCIAL_AUTH_OPENSTREETMAP_KEY = env('SOCIAL_AUTH_OPENSTREETMAP_KEY',default='xxx')
SOCIAL_AUTH_OPENSTREETMAP_SECRET = env('SOCIAL_AUTH_OPENSTREETMAP_SECRET',default='xxx')
MIDDLEWARE += (
    'social_django.middleware.SocialAuthExceptionMiddleware',
)
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_BACKEND_ERROR_URL = "/"

# If you want to add a playgroud map, add its primary key
# UMAP_DEMO_PK = 204
# If you want to add a showcase map on the home page, add its primary key
# UMAP_SHOWCASE_PK = 1156
# Add a baner to warn people this instance is not production ready.
UMAP_DEMO_SITE = env('UMAP_DEMO_SITE')

# Whether to allow non authenticated people to create maps.
UMAP_ALLOW_ANONYMOUS = env('UMAP_ALLOW_ANONYMOUS')

# This setting will exclude empty maps (in fact, it will exclude all maps where
# the default center has not been updated)
UMAP_EXCLUDE_DEFAULT_MAPS = env('UMAP_EXCLUDE_DEFAULT_MAPS')

# How many maps should be showcased on the main page resp. on the user page
UMAP_MAPS_PER_PAGE = 5
# How many maps should be showcased on the user page, if owner
UMAP_MAPS_PER_PAGE_OWNER = 10

SITE_URL = env("SITE_URL",default="http://localhost:8019")
SHORT_SITE_URL = env("SHORT_SITE_URL",default="http://s.hort")

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#     }
# }

# POSTGIS_VERSION = (2, 1, 0)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# You need to unable accent extension before using UMAP_USE_UNACCENT
# python manage.py dbshell
# CREATE EXTENSION unaccent;
UMAP_USE_UNACCENT = False

# Put the site in readonly mode (useful for migration or any maintenance)
UMAP_READONLY = env('UMAP_READONLY')


# For static deployment
STATIC_ROOT = env('STATIC_ROOT')

# For users' statics (geojson mainly)
MEDIA_ROOT = env('MEDIA_ROOT')

# Default map location for new maps (akyaka)
LEAFLET_LONGITUDE = 28.3323
LEAFLET_LATITUDE = 37.1414
LEAFLET_ZOOM = 12

# Number of old version to keep per datalayer.
UMAP_KEEP_VERSIONS = 10
