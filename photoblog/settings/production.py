import os
gettext = lambda s: s
"""
Django settings for photoblog project.

Generated by 'django-admin startproject' using Django 1.8.18.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "mimiland.lisa.fan@gmail.com"
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'Linxuan FAN <linxuan.fan@email.com>'

#ADMINS = {
 #   ('Linxuan', 'linxuan.fan@email.com'),
#}
#MANAGERS = ADMINS



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in productionEBUG = False
DEBUG = True
ALLOWED_HOSTS = ['wandefu-photoblog.herokuapp.com', '0.0.0.0']


# Application definition





ROOT_URLCONF = 'photoblog.urls'



WSGI_APPLICATION = 'photoblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'live-static', 'media-root')
STATIC_ROOT = os.path.join(BASE_DIR, 'live-static', 'static-root')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'photoblog', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
                'blog.context_processors.blog_home',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'djangocms_ckeditor_filer.middleware.ThumbnailMiddleware',
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django_comments',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_ckeditor_filer',
    'djangocms_text_ckeditor',
    'filer',
    'mptt',
    'easy_thumbnails',
    'polymorphic',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_column',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_googlemap',
    'djangocms_video',
    'djangocms_flash',
    'reset_migrations',
    'photoblog',
    'photoblog_plugins',
    'blog',
    'django_login',
    'gallery',
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'hide_untranslated': False,
            'redirect_on_fallback': True,
            'code': 'en',
            'public': True,
            'name': gettext('en'),
        },
    ],
    'default': {
        'hide_untranslated': False,
        'redirect_on_fallback': True,
        'public': True,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('home.html', 'Home'),
    ('galary.html', 'Galary'),
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
)

CMS_PERMISSIONS = True
CMS_ENABLE_UPDATE_CHECK = False
CMS_UPDATE_CHECK_TYPE = ('patch')

CMS_PLACEHOLDER_CONF = {
    'my_picture': {
        'name': "My Pictures",
	'plugins': ['My_Pictures_Plugin'],
	'limits': {
	    'global': 1
	}
    },
    'last_activities': {
        'name': "Last Activities",
	'plugins': ['Image_Link_Plugin'],
	'limits': {
	    'global': 6
	}
    },
    'footer': {
        'name': "Footer",
	'plugins': ['Footer_Plugin'],
    },
    'galary_upload': {
        'name': "Galary Upload",
	'plugins': ['Galary_Plugin'],
    },
    'club_info': {
        'name': "Club Info",
	'plugins': ['Carousel_Plugin'],
    },
}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_SETTINGS = {
  'toolbar_HTMLField': [
    ['Undo', 'Redo'],
    ['ShowBlocks'],
    ['Format', 'Styles'],
    ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
    ['Maximize', ''],
    '/',
    ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
    ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
    ['Link', 'Unlink'],
    ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table', 'Filer Image'],
    ['Source']
  ],
     'extraPlugins': 'filerimage',
     'removePlugins': 'image',
}

import dj_database_url
DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
#DATABASES['default']['CONN_MAX_AGE'] = 500

MIGRATION_MODULES = {
}


THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # important! place right before django.contrib.staticfiles.finders.AppDirectoriesFinder
    #'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

FILER_DEBUG = True

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CSRF_COOKIE_SECURE = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_COOKIE_AGE = 10 * 60

CORS_REPLACE_HTTPS_REFERER     = True
HOST_SCHEME                    = "http://"
SECURE_PROXY_SSL_HEADE         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT            = True
SESSION_COOKIE_SECURE          = True
SECURE_HSTS_SECONDS            = 1000000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY              = True
CSRF_COOKIE_HTTPONLY           = True
X_FRAME_OPTIONS                = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF    = True
SECURE_BROWSER_XSS_FILTER      = True
