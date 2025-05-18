function copyToClipboard(index) {
    // there is  a data-index in each copy button.
    // and each copy button copies the data of the results-div of that index
    // i wasnot that good with forEach back then, so i have given different ids matching the index to each results div

    var resultDiv = document.querySelector(`#resultDiv${index}`);
    var resultText = resultDiv.innerText;

    // Create a temporary input element
    var tempInput = document.createElement("input");
    tempInput.value = resultText;
    document.body.appendChild(tempInput);

    // Select the text in the temporary input element
    tempInput.select();
    tempInput.setSelectionRange(0, 99999); // For mobile devices

    // Copy the text inside the temporary input element
    document.execCommand("copy");

    // Remove the temporary input element
    document.body.removeChild(tempInput);

    // Alert the user that the password has been copied
    // displayMessage(`Copied to clipboard: ${resultText}`, "success");
}

// Attach click event listeners to each copy button
var copyBtns = document.querySelectorAll(".copy-btn");
copyBtns.forEach(function (btn, index) {
    btn.addEventListener("click", function () {
        copyToClipboard(index);
        btn.innerText = "copied!";
        setTimeout(() => {
            btn.innerText = "copy";
        }, 2000);
    });
});
