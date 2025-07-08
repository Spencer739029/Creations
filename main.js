const speech = new SpeechSynthesisUtterance();
const voiceSelect = document.querySelector("select");
const textarea = document.querySelector("textarea");
const button = document.querySelector("button");

let voices = [];

function populateVoices() {
    voices = window.speechSynthesis.getVoices();
    voiceSelect.innerHTML = ""; // Clear existing options

    voices.forEach((voice, i) => {
        const option = document.createElement("option");
        option.value = i;
        option.textContent = `${voice.name} (${voice.lang})`;
        voiceSelect.appendChild(option);
    });

    // Set default voice
    if (voices.length > 0) {
        speech.voice = voices[0];
    }
}

window.speechSynthesis.onvoiceschanged = populateVoices;

// Handle voice selection change
voiceSelect.addEventListener("change", () => {
    const selectedIndex = parseInt(voiceSelect.value);
    if (!isNaN(selectedIndex) && voices[selectedIndex]) {
        speech.voice = voices[selectedIndex];
    }
});

// Handle button click
button.addEventListener("click", () => {
    speech.text = textarea.value.trim();
    if (speech.text) {
        window.speechSynthesis.speak(speech);
    }
});
