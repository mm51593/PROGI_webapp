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
        document.getElementById("tekstLabel").innerHTML = "Tekst :   <span style='color: red;'>Trebate dati barem jedno od teksta, slike ili videa</span>";
        return false;
    }
  return true;
}

function checkPswd() {
    var pswd = document.getElementById("regPswd").value;
    var rePswd = document.getElementById("reRegPswd").value;

    if(pswd != rePswd) {
        document.getElementById("lozReg").innerHTML = "Lozinka :  <span style='color: red;'>Lozinke se ne podudaraju</span>";
        return false;
    }

    return true;
}

function restoreReg() {
    document.getElementById("lozReg").innerHTML = "Lozinka : ";
}

function updatePrice() {
    document.getElementById("cijena").innerHTML = Math.floor(Math.random() * Math.floor(200));
}