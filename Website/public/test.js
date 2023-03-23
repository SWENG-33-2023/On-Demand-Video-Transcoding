document.getElementById('upload-form').addEventListener('submit', function (event) {
  event.preventDefault();
  const fileInput = document.getElementById('upload');
  const file = fileInput.files[0];

  if (!file) {
    alert('Please choose a file.');
    return;
  }

  const formData = new FormData();
  formData.append('file', file);

  fetch('/upload', {
    method: 'POST',
    body: formData,
  })
    .then((res) => {
      if (res.status === 200) {
        alert('File uploaded successfully');
      } else {
        alert('Failed to upload file');
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
