from .models import AppSetting

def get_logo(request):
    logo_setting = AppSetting.objects.first()

    if logo_setting:
        logo_html = logo_setting.image_tag()  # Call the image_tag method on the instance
    else:
        logo_html = None  # Or set to a default value if no logo setting is found

    data = {
        'logo_html': logo_html
    }

    return data