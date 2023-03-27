// if submit button is clicked:
// - event listener is invoked.
// - user's file is uploaded to disk.
document.getElementById('upload-form').addEventListener('submit', function (event) {
    event.preventDefault();

    // "Check fileInput.files.length, in case the user clicked cancel." maybe a good idea - FionnCL
    if(!validResolution()){
      return console.log("Error: No resolution selected.")
    }

    const fileInput = document.getElementById('upload');
    const file = fileInput.files[0];

    if (!file) {
      alert('Please choose a file.');
      return;
    }
  
    // saw some code saying this is random, I don't believe it but it's random enough for now. - FionnCL
    // the below assumes that the user uploads a video that doesn't have more or less than 1 period.
    var formData = new FormData();
    formData.append('file', file);
  
    // could be a problem if it starts transcoding before its uploaded.
    // may have to wait for upload to be done.
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

      // after uploading, make api request
      var mediaName = file.name;
      var mediaScale = getResolution();
      var mediaEncoding = "libx264";
      var mediaNameOutput = mediaName;

      apiRequest(mediaName, mediaScale, mediaEncoding, mediaNameOutput);
  });

function apiRequest(mediaName, mediaScale, mediaEncoding, mediaNameOutput){
    var data = {
      "mediaName": mediaName,
      "mediaScale": mediaScale,
      "mediaEncoding": mediaEncoding,
      "mediaNameOutput": mediaNameOutput
    }
    fetch("http://127.0.0.1:4000/transcoder", {
        method: "POST",
        mode: "no-cors",
        headers: {
          "Content-Type": "application/json"
        },
        body: data
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