from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class LoginApp(CMSApp):
    app_name = "django_login"
    name = "Login"
    urls = ["django_login.urls"]


apphook_pool.register(LoginApp)
