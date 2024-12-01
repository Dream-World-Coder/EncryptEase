function pasteText(inputId) {
  navigator.clipboard.readText().then(
      clipText => document.getElementById(inputId).value = clipText);
}

// file


function pasteFile(inputId) {
  navigator.clipboard.read().then((items) => {
    items.forEach((item) => {
      const fileType = item.types.find(type => 
        type.startsWith('image/') || 
        type.startsWith('audio/') || 
        type.startsWith('video/') || 
        type === 'application/pdf' || 
        type === 'application/msword' || 
        type === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' || 
        type === 'application/vnd.ms-excel' || 
        type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
      );
      
      if (fileType) {
        item.getType(fileType).then((blob) => {
          const fileName = `pasted_file_${Date.now()}.${blob.type.split('/')[1]}`;
          const fileInput = document.getElementById(inputId);
          const dataTransfer = new DataTransfer();
          dataTransfer.items.add(new File([blob], fileName, { type: blob.type }));
          fileInput.files = dataTransfer.files;

          // Update the file name display if there is one
          const fileNameDisplay = fileInput.nextElementSibling;
          if (fileNameDisplay && fileNameDisplay.classList.contains('file-name')) {
            fileNameDisplay.textContent = fileName;
          }
        });
      } else if (item.types.includes('text/plain')) {
        item.getType('text/plain').then((blob) => {
          blob.text().then((text) => {
            const inputElement = document.getElementById(inputId);
            if (inputElement.tagName === 'INPUT' && inputElement.type === 'file') {
              // Handle file input element
              console.warn('Cannot paste text into a file input element.');
            } else {
              inputElement.value = text;
            }
          });
        });
      }
    });
  }).catch((err) => {
    console.error('Failed to read clipboard contents: ', err);
  });
}

// Add event listeners to all elements with the 'paste' class
document.querySelectorAll('.paste').forEach(span => {
  span.addEventListener('click', () => {
    const inputId = span.getAttribute('onclick').match(/'(.*?)'/)[1];
    pasteFile(inputId);
  });
});







// // Add event listeners to all buttons with the 'paste-btn' class
// document.querySelectorAll('.pst').forEach(btn => {
//   btn.addEventListener('click', () => {
//     const inputId = btn.getAttribute('data-input-id'); // Get the associated input ID
//     pasteFile(inputId);
//   });
// });

// function pasteFile(inputId) {
//   navigator.clipboard.read().then((items) => {
//     items.forEach((item) => {
//       if (item.types.includes('image/png') || item.types.includes('image/jpeg') ||
//           item.types.includes('image/gif') || item.types.includes('image/bmp') ||
//           item.types.includes('application/pdf') || item.types.includes('application/msword') ||
//           item.types.includes('application/vnd.openxmlformats-officedocument.wordprocessingml.document') ||
//           item.types.includes('application/vnd.ms-excel') || item.types.includes('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')) {

//         item.getType(item.types[0]).then((blob) => {
//           const fileName = `pasted_file_${Date.now()}.${blob.type.split('/')[1]}`;
//           const fileInput = document.getElementById(inputId);
//           const dataTransfer = new DataTransfer();
//           dataTransfer.items.add(new File([blob], fileName, { type: blob.type }));
//           fileInput.files = dataTransfer.files;

//           const fileNameDisplay = fileInput.nextElementSibling; // Assuming file name display is the next sibling
//           if (fileNameDisplay && fileNameDisplay.classList.contains('file-name')) {
//             fileNameDisplay.textContent = fileName;
//           }
//         });

//       } else if (item.types.includes('text/plain')) {
//         item.getType('text/plain').then((blob) => {
//           blob.text().then((text) => {
//             const inputElement = document.getElementById(inputId);
//             if (inputElement.tagName === 'INPUT' && inputElement.type === 'file') {
//               // Handle file input element
//               console.warn('Cannot paste text into a file input element.');
//             } else {
//               inputElement.value = text;
//             }
//           });
//         });
//       }
//     });
//   }).catch((err) => {
//     console.error('Failed to read clipboard contents: ', err);
//   });
// }
