function pasteText(inputId) {
  navigator.clipboard.readText().then(
    clipText => document.getElementById(inputId).value = clipText);
}