function apiRequest(mediaName, mediaScale, mediaEncoding, mediaNameOutput){
    const data = {
        "mediaName": mediaName,
        "mediaScale": mediaScale,
        "mediaEncoding": mediaEncoding,
        "mediaNameOutput": mediaNameOutput,
    }

    fetch("https://127.0.0.1:4000/transcoder", {
        method:"POST",
        header: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        body: JSON.stringify(data),
    }).then((res) => {
        console.log(res);
    }).catch((error) => {
        console.error("Error:", error);
    });
} 

const button = document.getElementById("myButton");

document.getElementById("upload-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const fileInput = document.getElementById("upload");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please choose a file.");
        return;
    }

    // Prepare FormData to send the file
    const formData = new FormData();
    formData.append("file", file);

    // vvv could be a problem for videos vvv
    const img = new Image();

    img.src = URL.createObjectURL(file);
    console.log(img.src)

    document.getElementById("image").src = img.src;

    img.src.download = img.src.replace(/^.*[\\\/]/, '');

    //localStorage.setItem("TESTING", img.src);
});