"""Module storing the load."""
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings

from core.models import Photo, Carousel

from os.path import expanduser
import numpy as np
import pandas as pd

G = '\033[92m'
RE = '\033[0m'


class Command(BaseCommand):
    """Custom python management command for updating the map Locations."""

    help = """
    Create Locations from the provided .csv file:
    Usage:
        python3 manage.py load_map_location_from_csv --path PATH_TO_FILE
    """

    def add_arguments(self, parser):
        """Adding arguments to the command."""
        parser.add_argument(
            "--path", type=str, default="./Lugares_Imperdibles.csv"
        )

    def handle(self, *args, **kwargs):
        """Create Carousel for "Lugares Imperdibles" based on the .csv file."""
        carousel, _ = Carousel.objects.get_or_create(
            name='Lugares Imperdibles',
            defaults={
                'show_description': True
            }
        )

        file_path = kwargs["path"]

        df = pd.read_csv(file_path)
        df = df.replace(np.nan, None)

        skipped_columns = ['id', 'carousels', 'added', 'should_know_sections']
        photos_path = expanduser(
            settings.BASE_DIR / 'lugares_imperdibles'
        ) + '/'

        for index, row in df.iterrows():
            row_value_dict = {}
            for model_column in Photo._meta.get_fields():
                if model_column.name not in skipped_columns:
                    row_value_dict.update(
                        {f'{model_column.name}': row[model_column.name]}
                    )

            with open(photos_path + row_value_dict["image"], "rb") as f:
                row_value_dict["image"] = File(f)
                photo_instance, _ = Photo.objects.get_or_create(
                    name=row_value_dict['name'],
                    defaults=row_value_dict
                )
            carousel.images.add(photo_instance)
            print(f'Saved {G}{photo_instance}{RE}!')

        return self.stdout.write(self.style.SUCCESS(
            f'Successfully stored {len(df)} Photos for "Lugares Imperdibles" '
            f'carousel from {file_path}'
        ))
