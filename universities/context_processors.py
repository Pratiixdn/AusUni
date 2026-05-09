"""Global context processors for AusUni"""

from .models import State


def global_context(request):
    """Provide global data to all templates."""
    return {
        'all_states': State.objects.order_by('name'),
        'site_name': 'AusUni',
        'site_tagline': 'Your Complete Guide to Australian Universities',
    }
