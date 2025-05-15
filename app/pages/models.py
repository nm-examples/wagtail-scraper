from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class StandardPage(Page):
    """A standard page model."""

    body = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
