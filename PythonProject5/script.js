// Wait for the DOM content to fully load before running the script
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("colorForm");
    const colorInput = document.getElementById("colorInput");
    const headerText = document.getElementById("headerText");

    // Listen for the form submit event
    form.addEventListener("submit", function (event) {
        // Prevent the default form submission behavior (page reload)
        event.preventDefault();

        // Get the value from the text field and trim any extra whitespace
        const userColor = colorInput.value.trim();

        // Change the text color of the header to the user's input
        if (userColor !== "") {
            headerText.style.color = userColor;
        }
    });
});