const w = 8192;
const h = 5851;

function toggleLegend() {
  legend.classList.toggle('visible');
  legendButton.innerText = legendButton.innerText === 'Show Legend' ? 'Hide Legend' : 'Show Legend';
}
const legend = document.getElementById('legend');
const legendButton = document.getElementById('legend-toggle');
legendButton.addEventListener('click', toggleLegend);

const map = L.map('map', {
  crs: L.CRS.Simple,
  minZoom: 0,
  maxZoom: 4,
  zoomControl: false,
  attributionControl: false,
  zoomSnap: 0.01
 }).setView([-32, 32], 0);

L.control.zoom({ position: 'bottomleft' }).addTo(map);
let southWest = map.unproject([0, h - 90], map.getMaxZoom());
let northEast = map.unproject([w - 128, 0], map.getMaxZoom());
let bounds = L.latLngBounds(southWest, northEast);
map.setMaxBounds(bounds);

L.tileLayer('/static/map/tiles/{z}/{x}_{y}.webp', {
  tileSize: 96,
  minZoom: 0,
  maxZoom: 4,
  zoomOffset: 3,
  center: [-32, 32],
  noWrap: true,
  tms: false,
  bounds: bounds,
  unloadInvisibleTiles: false,
  updateWhenIdle: false,
  keepBuffer: 10000
}).addTo(map);

const markers = [];
fetch('/api/locations/')
  .then(response => response.json())
  .then(data => {
    data.forEach(
      location => {
        const marker = L.marker(
          [location.y, location.x],
          {
            icon: L.icon({
              iconUrl: location.icon_url ? location.icon_url : '/static/images/question-sign.webp',
              iconSize: [32, 32],
              className: 'map-marker-0'
            })
          }
        ).addTo(map);
        marker.bindPopup("<b>" + location.name + "</b>");
        markers.push({ name: location.name, marker: marker });
        const li = getMarkerLegendTemplate(location, marker);
        document.getElementById('legend-list').appendChild(li);
    });
  });

function getMarkerLegendTemplate(location, marker) {
  const li = document.createElement('li');
  const contentDiv = document.createElement('div');
  const nameH4 = document.createElement('h4');
  nameH4.innerText = location.name;
  nameH4.style.color = '#000';

  const logoDiv = document.createElement('div');
  const logo = document.createElement('img');
  logo.style.width = '32px';
  logo.style.height = '32px';
  logo.src = location.icon_url ? location.icon_url : '/static/images/question-sign.webp';
  logo.classList.add('map-marker-0');
  logoDiv.appendChild(logo);

  contentDiv.appendChild(logoDiv);
  contentDiv.appendChild(nameH4);
  li.appendChild(contentDiv);

  li.addEventListener('click', () => {
    toggleLegend();
    map.setView([location.y, location.x], 7);
    marker.openPopup();
  });
  return li;
}
