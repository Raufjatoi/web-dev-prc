const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const resultDiv = document.getElementById('result');
const ctx = canvas.getContext('2d');

// Load the COCO-SSD model
async function loadModel() {
    const model = await cocoSsd.load();
    startVideo(model);
}

// Start the video stream
async function startVideo(model) {
    // Access the camera
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;

    video.onloadedmetadata = async () => {
        video.play();
        detectFrame(model);
    };
}

// Function to detect objects in the video frame
async function detectFrame(model) {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas

    const predictions = await model.detect(video);

    // Draw the predictions on the canvas
    predictions.forEach(prediction => {
        ctx.beginPath();
        ctx.rect(...prediction.bbox);
        ctx.lineWidth = 2;
        ctx.strokeStyle = 'red';
        ctx.fillStyle = 'red';
        ctx.stroke();
        ctx.fillText(`${prediction.class} (${Math.round(prediction.score * 100)}%)`, prediction.bbox[0], prediction.bbox[1] > 10 ? prediction.bbox[1] - 5 : 10);
    });

    requestAnimationFrame(() => detectFrame(model)); // Continue the detection loop
}

// Start the application
loadModel();
