import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Waiting for database.....")) 
        is_db_up= False 
        while is_db_up is False:
            try:
                self.check(databases=['default'])
                is_db_up = True 
            except(OperationalError,Psycopg2Error):
                self.stdout.write(self.style.WARNING("Database Not Ready Yet Waiting 1 Second."))    
                time.sleep(1)            
        self.stdout.write( self.style.SUCCESS('Database Ready'))    

