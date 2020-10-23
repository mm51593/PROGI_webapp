function checkUpload() {
    var img = document.getElementById("imgLabel");
    var vid = document.getElementById("vidLabel");
    
    if(document.getElementById("upload-img").value != "") {
        img.style.backgroundColor = "lawngreen";
    } else {
        img.style.backgroundColor = "#ff5500"
    }
    
    if(document.getElementById("upload-vid").value != "") {
        vid.style.backgroundColor = "lawngreen";
    } else {
        vid.style.backgroundColor = "#ff5500"
    }
}

function checkData() {
    if(document.getElementById("upload-vid").value == "" && document.getElementById("upload-img").value == "" && document.getElementById("opisPrice").value == "") {
        return false;
    }
  return true;
}