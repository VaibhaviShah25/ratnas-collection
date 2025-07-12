
const map = L.map('map').setView([20.5937, 78.9629], 5);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);


function updateTimeDate() {
  const now = new Date();
  document.getElementById('time').textContent = now.toLocaleTimeString();
  document.getElementById('date').textContent = now.toLocaleDateString();
}
setInterval(updateTimeDate, 1000);

  // Image capture logic
  document.getElementById('capture-image').addEventListener('click', () => {
    document.getElementById('photo').click(); // triggers camera input
  });

  document.getElementById('photo').addEventListener('change', () => {
    const count = document.getElementById('photo').files.length;
    document.getElementById('image-count').textContent = `${count} Image${count !== 1 ? 's' : ''}`;
  });


// Audio recording
let mediaRecorder;
let audioChunks = [];

const startBtn = document.getElementById('start-rec');
const stopBtn = document.getElementById('stop-rec');
const voiceList = document.getElementById('voice-list');
const audioInput = document.getElementById('audio');

startBtn.addEventListener('click', async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  mediaRecorder = new MediaRecorder(stream);
  audioChunks = [];

  mediaRecorder.ondataavailable = e => {
    audioChunks.push(e.data);
  };

  mediaRecorder.onstop = () => {
    const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
    const audioUrl = URL.createObjectURL(audioBlob);
    const audioEl = document.createElement('audio');
    audioEl.controls = true;
    audioEl.src = audioUrl;
    const li = document.createElement('li');
    li.appendChild(audioEl);
    voiceList.appendChild(li);

    // Convert blob to File and set in input
    const file = new File([audioBlob], 'recording.mp3', { type: 'audio/mp3' });

    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    audioInput.files = dataTransfer.files;
  };

  mediaRecorder.start();
  startBtn.disabled = true;
  stopBtn.disabled = false;
});

stopBtn.addEventListener('click', () => {
  mediaRecorder.stop();
  startBtn.disabled = false;
  stopBtn.disabled = true;
})

document.querySelector('form').addEventListener('submit', (e) => {
  const lat = document.getElementById('latitude').value;
  const lon = document.getElementById('longitude').value;
  const loc = document.getElementById('location_name').value;

  if (!lat || !lon || !loc) {
    e.preventDefault();
    alert("Location not ready yet. Please wait a few seconds.");
  }
});

  let locationReady = false;

  function updateLocation(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;

    // Set lat/lon
    document.getElementById('latitude').value = lat;
    document.getElementById('longitude').value = lon;
    document.getElementById('location').textContent = ` ${lat}, ${lon}`;
    // Reverse geocoding
    fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
      .then(res => res.json())
      .then(data => {
        document.getElementById('location_name').value = data.display_name;
        locationReady = true;
        console.log("Location set!");
      })
      .catch(err => {
        console.error("Reverse geocoding failed:", err);
      });
  }

  function handleError(error) {
    console.error("Geolocation error:", error);
    alert("Unable to fetch location. Please allow location access.");
  }

  window.onload = function () {
    navigator.geolocation.getCurrentPosition(updateLocation, handleError);
  };

  document.getElementById('locationForm').addEventListener('submit', function (e) {
    if (!locationReady) {
      e.preventDefault();
      alert("Please wait, fetching your location...");
    }
  });
