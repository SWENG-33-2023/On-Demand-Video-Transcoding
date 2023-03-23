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
  




function apiRequest(mediaName, mediaScale, mediaEncoding, mediaNameOutput){
    data = {
        "mediaName": mediaName,
        "mediaScale": mediaScale,
        "mediaEncoding": mediaEncoding,
        "mediaNameOutput": mediaNameOutput,
    }
    fetch("https://127.0.0.1:4000/transcoder", {
        method:"POST",
        header: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    }).then((res) => res.json().then((data) => {
        console.log(data);
    })).catch((error) => {
        console.error("Error:", error);
    });
}


