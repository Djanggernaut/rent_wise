from django.conf import settings


def get_google_api(resquest):
    return {"GOOGLE_API_KEY": settings.GOOGLE_API_KEY}
