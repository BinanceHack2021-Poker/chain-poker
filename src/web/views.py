# todo: views should be rewritten to API for reactApp as frontend
import logging

from django.views.generic import TemplateView, DetailView

from web.models import Game

logger = logging.getLogger(__name__)


class IndexView(DetailView):
    template_name = 'web/index.html'
    context_object_name = 'game'
    model = Game
    slug_field = 'secure_identity'


class JoinOrCreateView(TemplateView):
    template_name = 'web/join_or_create.html'
