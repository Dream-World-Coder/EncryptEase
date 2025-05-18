function dragEnter(event) {
    event.preventDefault();
    event.target.classList.add("hover");
}

function dragOver(event) {
    event.preventDefault();
    event.target.classList.add("hover");
}

function dragLeave(event) {
    event.target.classList.remove("hover");
}

function drop(event) {
    event.preventDefault();
    event.target.classList.remove("hover");

    // Get the files that were dropped
    const files = event.dataTransfer.files;

    // Process the dropped files
    for (let file of files) {
        console.log("Dropped file:", file.name);
    }
}
