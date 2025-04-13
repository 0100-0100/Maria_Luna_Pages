const w = 8192;
const h = 5851;

const map = L.map('map', {
  crs: L.CRS.Simple,
  minZoom: 2,
  maxZoom: 5,
  zoomControl: false,
  attributionControl: false
}).setView([0, 0], 0);

L.control.zoom({ position: 'bottomleft' }).addTo(map);
const southWest = map.unproject([0, h], map.getMaxZoom());
northEast = map.unproject([w, 0], map.getMaxZoom());
const bounds = L.latLngBounds(southWest, northEast);

L.tileLayer('/static/map/tiles/{z}-{x}-{y}.webp', {
  tileSize: 256,
  minZoom: 2,
  maxZoom: 5,
  zoomOffset: 0,
  center: [0, 0],
  noWrap: true,
  tms: false,
  bounds: bounds
}).addTo(map);
map.setMaxBounds(bounds);
// Fetch locations dynamically
const markers = [];
fetch('/api/locations/')
  .then(response => response.json())
  .then(data => {
    data.forEach(loc => {
      const marker = L.marker(
        [loc.y, loc.x],
        {
          icon: L.icon({
            iconUrl: loc.icon,
            iconSize: [64, 64],
            className: 'map-marker-0',
          })
        }
      ).addTo(map);
      marker.bindPopup("<b>" + loc.name + "</b>");

      markers.push({ name: location.name, marker: marker });

      const li = document.createElement('li');
      li.textContent = loc.name;
      li.addEventListener('click', () => {
        debugger;
        map.panTo(marker.getLatLng(), { animate: true });
        marker.openPopup();
      });
      document.getElementById('legend-list').appendChild(li);
    });
  });

document.getElementById('legend-toggle').addEventListener('click', (e) => {
  const legend = document.getElementById('legend');
  legend.classList.toggle('visible');
  e.target.innerText = e.target.innerText === 'Show Legend' ? 'Hide Legend' : 'Show Legend';
  legend.style.display = (legend.style.display === 'none' || legend.style.display === '') ? 'block' : 'none';
});
