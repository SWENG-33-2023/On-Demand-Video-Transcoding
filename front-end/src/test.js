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
    
    // the below assumes that the user uploads a video that doesn't have more or less than 1 period.
    // the random generation may not work for two files made in the same milisecond due to Date.now().
    var fileType = (fileInput.files[0].name).toString().split(".");
    var tempId = Date.now().toString(36) + Math.random().toString(36);
    var id = "";

    for(var i = 0; i < tempId.length; i++){
      var character = tempId.charAt(i);
      if(character != "."){
        id = id + character;
      }
    }

    var fileName =  id + "." + fileType[1];
    var formData = new FormData();
    formData.append('file', file, fileName);
  
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
  });

function transcode(){
  const filePath=path.join(directoryPath,fileName);
  var mediaName = "test.mkv";
  var mediaScale = getResolution();
  var mediaEncoding = "libx264";
  var mediaNameOutput = mediaName;

  apiRequest(mediaName, mediaScale, mediaEncoding, mediaNameOutput);
}

// document.getElementById('transcode-form').addEventListener('submit', function (event) {
//   // after uploading, make api request
//   // FOR FRONT END-PPL: "fileName" SHOULD BE GOTTEN BY CHOOSING A VIDEO, AND GETTING IT'S NAME
//   // LEAVE THE OUTPUTNAME = to MEDIANAME
//   var mediaName = "test.mkv";
//   var mediaScale = getResolution();
//   var mediaEncoding = "libx264";
//   var mediaNameOutput = mediaName;

//   apiRequest(mediaName, mediaScale, mediaEncoding, mediaNameOutput);
// });

function apiRequest(mediaName, mediaScale, mediaEncoding, mediaNameOutput){
    var data = {
      "mediaName": mediaName,
      "mediaScale": mediaScale,
      "mediaEncoding": mediaEncoding,
      "mediaNameOutput": mediaNameOutput
    }
    fetch("http://127.0.0.1:4000/transcoder", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });
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