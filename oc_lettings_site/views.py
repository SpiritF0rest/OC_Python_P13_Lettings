from django.shortcuts import render

from oc_lettings_site import logger


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus. Aliquam vitae erat
# ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """Allows you to display the home page.

    Args:
        request: HttpRequest

    Returns:
        HttpResponse whose content is filled with the result of calling with the passed arguments.
    """
    return render(request, 'index.html')


def sentry_test(request):
    """Allows you to test logs to Sentry.

    Args:
        request: HttpRequest

    Returns:
        HttpResponse whose content is filled with the result of calling with the passed arguments.
    """
    logger.info("I am a breadcrumb")
    logger.error("I am an event", extra=dict(bar=43))
    return render(request, 'sentry_test.html')
