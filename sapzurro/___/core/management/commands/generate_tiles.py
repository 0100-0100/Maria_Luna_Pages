import subprocess
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Generate map tiles from base image using libvips"

    def add_arguments(self, parser):
        parser.add_argument('--input', type=str, default='core/Sin logos ni leyenda.png', help='Input image path')
        parser.add_argument('--output', type=str, default='static/map/tiles', help='Output tile directory')
        parser.add_argument('--tile-size', type=int, default=96, help='Tile size in pixels')

    def handle(self, *args, **options):
        input_image = options['input']
        output_dir = options['output']
        tile_size = options['tile_size']

        script_path = "core/generate_tiles_libvips.sh"

        self.stdout.write(f"Running tile generation script at: {script_path}")
        try:
            subprocess.run([
                "bash", script_path,
                input_image,
                output_dir,
                str(tile_size)
            ], check=True)
            self.stdout.write(self.style.SUCCESS("✅ Tiles generated successfully."))
        except subprocess.CalledProcessError as e:
            self.stderr.write(self.style.ERROR(f"❌ Tile generation failed: {e}"))
