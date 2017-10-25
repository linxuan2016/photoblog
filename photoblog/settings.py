import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "wandefu.azurewebsites.net"]


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
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'photoblog', 'static'),
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
    'ckeditor_filebrowser_filer',
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

CMS_PERMISSION = True
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



#    'content': {
#        'name' : 'Content',
#        'plugins': ['TextPlugin', 'LinkPlugin'],
#        'default_plugins':[
#            {
#                'plugin_type':'TextPlugin',
#                'values':{
#                    'body':'<p>Great websites : %(_tag_child_1)s and %(_tag_child_2)s</p>'
#                },
#                'children':[
#                    {
#                        'plugin_type':'LinkPlugin',
#                        'values':{
#                            'name':'django',
#                            'url':'https://www.djangoproject.com/'
#                        },
#                    },
#                    {
#                        'plugin_type':'LinkPlugin',
#                        'values':{
#                            'name':'django-cms',
#                            'url':'https://www.django-cms.org'
#                        },
#                    },
#                ]
#            },
#        ]
#    }
}


#TINYMCE_DEFAULT_CONFIG = {
#    'plugins': "table,spellchecker,paste,searchreplace",
#    'theme': "advanced",
#    'cleanup_on_startup': True,
#    'custom_undo_redo_levels': 10,
#}
#TINYMCE_SPELLCHECKER = True
#TINYMCE_JS_ROOT = os.path.join(STATIC_URL, "tiny_mce")
#TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js' 
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
#TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

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


MIGRATION_MODULES = {
#    'djangocms_column': 'djangocms_column.migrations_django',
#    'djangocms_flash': 'djangocms_flash.migrations_django',
#    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
#    'djangocms_inherit': 'djangocms_inherit.migrations_django',
#    'djangocms_link': 'djangocms_link.migrations_django',
#    'djangocms_style': 'djangocms_style.migrations_django',
#    'djangocms_file': 'djangocms_file.migrations_django',
#    'djangocms_picture': 'djangocms_picture.migrations_django',
#    'djangocms_teaser': 'djangocms_teaser.migrations_django',
#    'djangocms_video': 'djangocms_video.migrations_django',
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

CSRF_COOKIE_SECURE = None

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#SESSION_COOKIE_AGE = 10 * 60
