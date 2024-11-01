const startButton = document.getElementById('start-recording');
const stopButton = document.getElementById('stop-recording');
const resultDiv = document.getElementById('result');

let recognition;
let isRecording = false;

// Initialize Speech Recognition
function initSpeechRecognition() {
    recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        resultDiv.innerText = `You said: ${transcript}`;
        speakResponse(transcript);
    };

    recognition.onerror = (event) => {
        console.error('Error occurred in recognition: ' + event.error);
        alert('Sorry, there was an error with the voice recognition.');
    };
}

// Speak the response in a cloned manner
function speakResponse(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.voice = speechSynthesis.getVoices().find(voice => voice.name === 'Google US English');
    speechSynthesis.speak(utterance);
}

// Start recording
startButton.addEventListener('click', () => {
    if (!isRecording) {
        isRecording = true;
        startButton.style.display = 'none';
        stopButton.style.display = 'inline-block';
        resultDiv.innerText = 'Listening...';
        recognition.start();
    }
});

// Stop recording
stopButton.addEventListener('click', () => {
    if (isRecording) {
        isRecording = false;
        startButton.style.display = 'inline-block';
        stopButton.style.display = 'none';
        recognition.stop();
    }
});

// Initialize Speech Recognition on load
window.onload = initSpeechRecognition;
