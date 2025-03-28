# vips dzsave \
#      Sin\ logos\ ni\ leyenda.png \
#      ../sapzurro/___/static/map/tiles \
#      --tile-size 254 \
#      --overlap 0 \
#      --suffix .webp[Q=100] \
#      --layout google \
#      --centre


vips dzsave \
     Sin\ logos\ ni\ leyenda.png \
     ../sapzurro/___/static/map/tiles \
     --tile-size=256 \
     --suffix=.webp[Q=100] \
     --layout=zoomify \
     --strip

mv ../sapzurro/___/static/map/tiles/TileGroup0/* ../sapzurro/___/static/map/tiles
mv ../sapzurro/___/static/map/tiles/TileGroup1/* ../sapzurro/___/static/map/tiles
mv ../sapzurro/___/static/map/tiles/TileGroup2/* ../sapzurro/___/static/map/tiles
mv ../sapzurro/___/static/map/tiles/TileGroup3/* ../sapzurro/___/static/map/tiles

rm -rf ../sapzurro/___/static/map/tiles/TileGroup*
rm ../sapzurro/___/static/map/tiles/ImageProperties.xml
