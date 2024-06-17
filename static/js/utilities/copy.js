function copyToClipboard(index) {
  // Get the result text from the specified result div
  var resultDiv = document.querySelector(`#resultDiv${index}`);
  var resultText = resultDiv.innerText.replace("result: ", "");

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
  alert("Password copied to clipboard: " + resultText);
}

// Attach click event listeners to each copy button
var copyBtns = document.querySelectorAll(".copy-btn");
copyBtns.forEach(function (btn, index) {
  btn.addEventListener("click", function () {
      copyToClipboard(index);
  });
});