const w = 8192;
const h = 5851;

const facebookIcon = document.getElementById('facebook-icon-svg');
const instagramIcon = document.getElementById('instagram-icon-svg');
const mailIcon = document.getElementById('mail-icon-svg');
const websiteIcon = document.getElementById('website-icon-svg');
const whatsappIcon = document.getElementById('whatsapp-icon-svg');

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
  zoomSnap: 0.5
}).setView([-32, 32], 1.5);

L.control.zoom({ position: 'bottomleft' }).addTo(map);
let southWest = map.unproject([0, h], map.getMaxZoom());
let northEast = map.unproject([w, 0], map.getMaxZoom());
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
const MARKER_SIZE = 64;
fetch('/api/locations/')
  .then(response => response.json())
  .then(data => {
    data.forEach(
      location => {
        const marker = L.marker(
          [location.y, location.x],
          {
            draggable: DRAGABLE_MAP_MARKERS,
            icon: L.icon({
              iconUrl: location.icon_url ? location.icon_url : '/static/images/question-sign.webp',
              iconSize: [scaleMarkerSize(map.getZoom()), scaleMarkerSize(map.getZoom())],
              className: 'map-marker-0'
            })
          }
        ).addTo(map);

        const socialLinks = [];

        if (location.phone) {
          socialLinks.push(`
            <h2>
              ${whatsappIcon.outerHTML}
              <a target="_blank" href="https://wa.me/${location.phone.replace('+', '')}?text=Hola%2C%20%5CnVengo%20desde%20mapasapzurro.co%20y%20queria%20saber%20mas%20acerca%20de%20ustedes">${location.phone}</a>
            </h2>
          `);
        }

        if (location.instagram_link) {
          const instagramHandle = location.instagram_link.split('/').pop();
          socialLinks.push(`
           <h2>
             ${instagramIcon.outerHTML}
             <a target="_blank" href="${location.instagram_link}">@${instagramHandle}</a>
           </h2>
          `);
        }

        if (location.facebook_link) {
          const facebookHandle = location.facebook_link.split('/').pop();
          socialLinks.push(`
            <h2>
              ${facebookIcon.outerHTML}
              <a target="_blank" href="${location.facebook_link}">@${facebookHandle}</a>
            </h2>
          `);
        }

        if (location.website_link) {
          socialLinks.push(`
            <h2>
              ${websiteIcon.outerHTML}
              <a target="_blank" href="${location.website_link}">${location.website_link}</a>
            </h2>
          `);
        }

        if (location.email) {
          socialLinks.push(`
            <h2>
              ${mailIcon.outerHTML}
              <a target="_blank" href="mailto:${location.email}">${location.email}</a>
            </h2>
          `);
        }

        marker.bindPopup(`
          <div class="marker-info-container">
            <img class="marker-info-logo" height="128px" width="128px" alt="${location.name}" src="${marker.getIcon().options.iconUrl}"/>
            <h3>${location.name}</h3>
            <p>${location.description}</p>
            <div>
              ${socialLinks.join('')}
            </div>
          </div>
        `);
        markers.push({ locationId: location.id, name: location.name, marker: marker });
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
  logo.style.width = MARKER_SIZE + 'px';
  logo.style.height = MARKER_SIZE + 'px';
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

const ZOOM_MIN = 0;
const ZOOM_MAX = 4;
const MIN_MARKER_SIZE = 8;
const MAX_MARKER_SIZE = 64;

function scaleMarkerSize(zoom) {
  const scale = (zoom - ZOOM_MIN) / (ZOOM_MAX - ZOOM_MIN);
  return MIN_MARKER_SIZE + scale * (MAX_MARKER_SIZE - MIN_MARKER_SIZE);
}

function updateMarkerSizes() {
  const zoom = map.getZoom();
  const size = scaleMarkerSize(zoom);
  markers.forEach(({ marker, locationId, name }) => {
    const icon = marker.getIcon();
    const newIcon = L.icon({
      ...icon.options,
      iconSize: [size, size],
    });
    marker.setIcon(newIcon);
  });
}

map.on('zoom', updateMarkerSizes);
