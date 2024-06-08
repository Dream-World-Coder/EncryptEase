// copy

    function copyToClipboard() {
      // Get the result text from the results div
      var resultDiv = document.querySelectorAll(".generated-password");
      var resultText = resultDiv.innerText.replace("result: ", "");
      var copyBtns = document.querySelectorAll(".copy-btn");

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
