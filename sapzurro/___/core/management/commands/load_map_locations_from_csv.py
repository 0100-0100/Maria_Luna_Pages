from django.core.management.base import BaseCommand
from map.models import Location
from core.models import Photo

import pandas as pd
import numpy as np

G = '\033[92m'
Re = '\033[0m'


class Command(BaseCommand):
    """
    Creates a custom command for updating the map Location records.
    """

    help = "Create Locations from the provided .csv file:\nUsage: python3 manage.py load_map_location_from_csv --path PATH_TO_FILE"

    def add_arguments(self, parser):
        """
        This function is responsible for adding arguments to the command
        """
        parser.add_argument("--path", type=str, default="./Locations.csv")

    def handle(self, *args, **kwargs):
        """
        Create Locations based on the .csv file provided.
        """
        Location.objects.all().delete()
        # photo = Photo.objects.all()[0]

        df = pd.read_csv('./Locations.csv')
        df = df.replace(np.nan, None)

        for index, row in df.iterrows():
            row_value_dict = {}

            for model_column in Location._meta.get_fields():
                if model_column.name == 'icon':
                    continue
                if model_column.name != 'id':
                    row_value_dict.update({f'{model_column.name}': row[model_column.name]})

            location_instance = Location(**row_value_dict)
            # location_instance.map_location_marker.set([photo])
            print(f'Saved {G}{location_instance}{Re}!')

            location_instance.save()

        return self.stdout.write(
                self.style.SUCCESS(f'Successfully stored {len(df)} locations from Locations.csv')
            )
