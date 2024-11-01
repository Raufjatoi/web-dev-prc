// Load the MobileNet model
let model;
async function loadModel() {
    model = await mobilenet.load();
    console.log("Model loaded!");
}

loadModel();

// Handle image upload
document.getElementById('upload').addEventListener('change', async (event) => {
    const file = event.target.files[0];
    if (file) {
        const img = document.getElementById('image');
        img.src = URL.createObjectURL(file);
        img.style.display = "block";

        // Wait for the image to load before prediction
        img.onload = async () => {
            const predictions = await model.classify(img);
            displayResult(predictions);
        };
    }
});

// Display prediction results
function displayResult(predictions) {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
        <h4>Predictions:</h4>
        <ul class="list-group">
            ${predictions.map(prediction => `
                <li class="list-group-item">
                    ${prediction.className} - ${Math.round(prediction.probability * 100)}%
                </li>
            `).join('')}
        </ul>
    `;
}
