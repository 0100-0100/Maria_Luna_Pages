#!/bin/bash

# Default values
INPUT_IMAGE=${1:-"core/Sin logos ni leyenda.png"}
OUTPUT_DIR=${2:-"static/map/tiles"}
TILE_SIZE=${3:-96}
MIN_ZOOM=4
MAX_ZOOM=7

# Derived zoom depth from MIN_ZOOM to MAX_ZOOM
DEPTH=$((MAX_ZOOM - MIN_ZOOM))

echo "Generating tiles for: $INPUT_IMAGE"
echo "Output directory: $OUTPUT_DIR"
echo "Tile size: $TILE_SIZE"
echo "Zoom levels: $MIN_ZOOM to $MAX_ZOOM"

# Temporary directory
TEMP_DIR="$OUTPUT_DIR/tmp"

# Clean previous output
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# Generate DeepZoom tiles using vips
vips dzsave "$INPUT_IMAGE" "$TEMP_DIR" \
  --tile-size=$TILE_SIZE \
  --overlap=0 \
  --suffix=".webp[Q=90]" \
  --depth=one \
  --layout=dz \
  --centre

# Reformat tiles to match Leaflet's expected format: {z}-{x}-{y}.webp
for (( z=0; z<=DEPTH; z++ )); do
  leaflet_z=$((z + MIN_ZOOM))
  mkdir -p "$OUTPUT_DIR/$leaflet_z"

  find "$TEMP_DIR_files/$z" -type f -name '*.webp' | while read file; do
    filename=$(basename "$file")
    y="${filename%.*}"
    x_dir=$(dirname "$file")
    x=$(basename "$x_dir")

    # Final tile name
    tile_filename="${leaflet_z}-${x}-${y}.webp"
    cp "$file" "$OUTPUT_DIR/$tile_filename"
  done
done

# Cleanup temporary files
rm -rf "$TEMP_DIR.dzi" "$TEMP_DIR_files"

echo "✅ Tiles generated successfully."
