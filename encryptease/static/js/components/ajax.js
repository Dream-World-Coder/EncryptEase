function displayMessage(message, type = "info") {
    const messageElement = document.createElement("div");
    messageElement.classList.add("temporary-message", type);
    messageElement.textContent = message;
    document.body.appendChild(messageElement);
    setTimeout(() => {
        messageElement.remove();
    }, 3000);
}

function showLoader() {
    document.getElementById("loader").style.display = "flex";
}
function hideLoader() {
    document.getElementById("loader").style.display = "none";
}

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("form").forEach((form) => {
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            showLoader();

            const formData = new FormData(form);
            const url = form.action;
            const method = form.method;

            fetch(url, {
                method: method,
                body: formData,
            })
                .then((response) => {
                    if (response.ok) {
                        // Check if the response is a file download
                        const contentDisposition = response.headers.get(
                            "Content-Disposition",
                        );
                        if (
                            contentDisposition &&
                            contentDisposition.indexOf("attachment") !== -1
                        ) {
                            return response.blob();
                        }
                        // text
                        else {
                            return response.json();
                        }
                    } else {
                        return response.json().then((data) => {
                            throw new Error(data.error || "Unknown error");
                        });
                    }
                })
                .then((data) => {
                    // Handle file download
                    if (data instanceof Blob) {
                        const url = window.URL.createObjectURL(data);
                        const a = document.createElement("a");
                        a.style.display = "none";
                        a.href = url;
                        a.download =
                            form.querySelector(
                                'input[type="file"]',
                            ).files[0].name;
                        document.body.appendChild(a);
                        a.click();
                        window.URL.revokeObjectURL(url);
                        console.log("File Processed Successfully!");
                    }
                    // Handle JSON response
                    else {
                        if (data.error) {
                            displayMessage(data.error);
                        } else {
                            if (data.generatedKey) {
                                displayMessage(
                                    "Key Generated Successfully!",
                                    "success",
                                );
                                document.querySelector(
                                    ".key-display",
                                ).textContent = data.generatedKey;
                            } else if (data.encrypted_msg) {
                                displayMessage(
                                    "Message Encrypted Successfully!",
                                    "success",
                                );
                                document.querySelector(
                                    ".encrypted-msg-display",
                                ).textContent = data.encrypted_msg;
                            } else if (data.decrypted_msg) {
                                displayMessage(
                                    "Message Decrypted Successfully!",
                                    "success",
                                );
                                document.querySelector(
                                    ".decrypted-msg-display",
                                ).textContent = data.decrypted_msg;
                            } else if (data.encrypted_file) {
                                displayMessage(
                                    "File Encrypted Successfully!",
                                    "success",
                                );
                            } else if (data.decrypted_file) {
                                displayMessage(
                                    "File Decrypted Successfully!",
                                    "success",
                                );
                            }
                        }
                    }
                })
                .catch((error) => {
                    displayMessage(error.message, "error");
                    console.error("Error:", error);
                })
                .finally(() => {
                    hideLoader();
                });
        });
    });
});
