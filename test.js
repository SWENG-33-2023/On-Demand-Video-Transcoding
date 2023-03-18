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