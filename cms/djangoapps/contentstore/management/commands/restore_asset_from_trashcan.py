from django.core.management.base import BaseCommand, CommandError

from xmodule.contentstore.utils import restore_asset_from_trashcan


class Command(BaseCommand):
    help = '''Restore a deleted asset from the trashcan back to it's original course'''

    def add_arguments(self, parser):
        parser.add_argument('location')

    def handle(self, *args, **options):
        restore_asset_from_trashcan(options['location'])
