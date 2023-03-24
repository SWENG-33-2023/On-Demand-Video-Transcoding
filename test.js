// if submit button is clicked:
// - event listener is invoked.
// - user's file is uploaded to disk.
document.getElementById('upload-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    // BELOW WORKS, JUST DOESN'T RETURN ERROR I THINK - FIONN
    if(!validResolution()){
      return console.log("Error: No resolution selected.")
    }

    const fileInput = document.getElementById('upload');
    const file = fileInput.files[0];

    if (!file) {
      alert('Please choose a file.');
      return;
    }
  
    const formData = new FormData();
    formData.append('file', file);
  
    // could be a problem if it starts transcoding before its uploaded.
    // may have to wait for upload to be done.
    await fetch('/upload', {
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

      // after uploading, make api request
      var mediaName = file.name;
      var mediaScale = getResolution();
      var mediaEncoding = "libx264";
      var mediaNameOutput = mediaName;

      apiRequest(mediaName, mediaScale, mediaEncoding, mediaNameOutput);
  });

async function apiRequest(mediaName, mediaScale, mediaEncoding, mediaNameOutput){
    var data = {
      "mediaName": mediaName,
      "mediaScale": mediaScale,
      "mediaEncoding": mediaEncoding,
      "mediaNameOutput": mediaNameOutput
    }
    await fetch("https://127.0.0.1:4000/transcoder", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data),
    })
    // .then((res) => res.json().then((data) => {
    //     console.log(data);
    // })).catch((error) => {
    //     console.error("Error:", error);
    // });
}

function validResolution(){
  var dropdownMenu = document.getElementById("res").value;
  if(dropdownMenu == "select"){
    return false;
  }
  return true;
}

function getResolution(){
  var resolution = document.getElementById("res").value;
  switch(resolution){
    case "sd":
      return "640:480"
    case "hd":
      return "1280:720"
    case "fhd":
      return "1920:1080"
  }
}