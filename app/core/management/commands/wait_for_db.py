"""Django command to w8 for db to be ready"""
import time
from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    """Django command to w8 for db"""

    def handle(self,*args,**options):
        """Entrypoing for command"""
        self.stdout.write('Waiting for db...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except:
                self.stdout.write('db is unavailleble waiting 1 sec...')
                time.sleep(1)
                
        self.stdout.write(self.style.SUCCESS('DataBase abailable !'))
        