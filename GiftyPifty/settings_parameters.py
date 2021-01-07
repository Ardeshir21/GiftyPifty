from django.urls import reverse_lazy


# allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'username'
LOGIN_REDIRECT_URL = reverse_lazy('baseApp:index')
ACCOUNT_EMAIL_VERIFICATION = 'optional'

# ACCOUNT_FORMS = {'signup': 'apps.accountApp.forms.CustomSignupForm'}

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
