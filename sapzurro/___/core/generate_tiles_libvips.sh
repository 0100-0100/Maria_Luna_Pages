#!/bin/bash

# Default values
INPUT_IMAGE=${1:-"core/Sin logos ni leyenda.png"}
OUTPUT_DIR=${2:-"static/map/tiles"}
#TILE_SIZE=${3:-96}
TILE_SIZE=8051
echo "Generating tiles for: $INPUT_IMAGE"
echo "Output directory: $OUTPUT_DIR"
echo "Tile size: $TILE_SIZE"

# Clean previous output
rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# Generate DeepZoom tiles using vips
vips dzsave "$INPUT_IMAGE" "$OUTPUT_DIR" \
  --tile-size=$TILE_SIZE \
  --overlap=0 \
  --suffix=".webp[Q=100]" \
  --depth=onetile \
  --layout=dz \
  --centre \
  --strip
