document.addEventListener("DOMContentLoaded", function() {
    let textElement = document.getElementById("animated-text");
    let words = ["Hi LEO DAS", "H.I.T"];
    let currentWordIndex = 0;
    let currentLetterIndex = 0;
    let deleting = false;

    function typeEffect() {
        let currentWord = words[currentWordIndex];

        if (!deleting) {
            textElement.textContent = currentWord.slice(0, currentLetterIndex + 1);
            currentLetterIndex++;

            if (currentLetterIndex === currentWord.length) {
                if (currentWordIndex === words.length - 1) {
                    return; // Stop animation after "H.I.T"
                }
                setTimeout(() => {
                    deleting = true;
                },600); // Pause for 2 seconds before deleting
            }
        } else {
            textElement.textContent = currentWord.slice(0, currentLetterIndex - 1);
            currentLetterIndex--;

            if (currentLetterIndex === 0) {
                deleting = false;
                currentWordIndex++;
            }
        }

        let speed = 300; // 1 second per letter
        setTimeout(typeEffect, speed);
    }

    typeEffect();
});
