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

function acceptOfferRed() {
     location.replace('./prihvat_price_list.html');
}

function rejectOfferRed() {
    location.replace('./prihvat_price_list.html');
}

function rejectOffer(offerNum) {
    let offer = document.getElementById("ponuda/cijena-" + offerNum).remove();
}

function checkData() {
    var error = false;
    var errMsg = document.getElementsByClassName("regErrMsg")[0];

    restoreReg();

    if(document.getElementById("prijedlogNaslovPrice").value == "") {
        error = true;
        var errReq = document.createElement("span");
        errReq.innerHTML = "Mora biti upisan naslov";

        errMsg.appendChild(errReq);
    }

    if (document.getElementById("InputList").childNodes.length == 0) {
        error = true;
        var errReq = document.createElement("span");
        errReq.innerHTML = "Mora biti dan barem jedan podatak";

        errMsg.appendChild(errReq);
    }

    var nonEnterElem = false;
    var textArray = document.getElementsByClassName("text-field-class");
    var imgVidArray = document.getElementsByClassName("elem-check-selected");

    for(var i = 0; i < textArray.length; i++) {
        if(textArray[i].value == "") {
            nonEnterElem = true;
        }
    }

    for(var i = 0; i < imgVidArray.length; i++) {
        if(imgVidArray[i].value == "") {
            nonEnterElem = true;
        }
    }

    if(nonEnterElem) {
        error = true;
        var errReq = document.createElement("span");
        errReq.innerHTML = "Odabrani elementi moraju biti popunjeni";

        errMsg.appendChild(errReq);
    }

    if (error) {
        errMsg.style.marginTop = "20px";
        errMsg.style.padding = "10px";
        errMsg.style.opacity = "1";
        return false;
    }

    return true;
}

function checkPswd() {
    var error = false;
    var errMsg = document.getElementsByClassName("regErrMsg")[0];
    var regMail = new RegExp("\\s*\\S+@\\S+.\\S+");

    var pswd = document.getElementById("regPswd").value;
    var rePswd = document.getElementById("reRegPswd").value;
    var mail = document.getElementById("mail").value;
    var user = document.getElementById("user").value;

    restoreReg();

    if (pswd != rePswd) {
        error = true;
        var errPass = document.createElement("span");
        errPass.innerHTML = "Lozinke se ne podudaraju.";

        errMsg.appendChild(errPass);
        console.log("Error logged, errMsg: " + errMsg);
    }

    if (mail == "" || rePswd == "" || pswd == "" || user == "") {
        error = true;
        var errReq = document.createElement("span");
        errReq.innerHTML = "Moraju biti popunjena sva polja";

        errMsg.appendChild(errReq);
    }

    if (!regMail.test(mail)) {
        error = true;
        var errMail = document.createElement("span");
        errMail.innerHTML = "E-mail je neispravnog formata";

        errMsg.appendChild(errMail);
    }

    if (error) {
        errMsg.style.marginTop = "20px";
        errMsg.style.padding = "10px";
        errMsg.style.opacity = "1";
        return false;
    }

    return true;
}

function restoreReg() {
    var errHold = document.getElementsByClassName("regErrMsg")[0];
    errHold.style.marginTop = "0px";
    errHold.style.padding = "0px";
    errHold.style.opacity = "0";
    errHold.childNodes.forEach(c => c.remove());
    restoreRegSec(errHold);
}

function restoreRegSec(errHold) {
    errHold.childNodes.forEach(c => c.remove());
}

function updatePrice() {
    var selectedMaterialIndex = document.getElementById("materijaliChoose").value;
    var searchString = "data-";
    searchString = searchString.concat(selectedMaterialIndex);

    var selectedMaterial = document.getElementById(searchString).innerHTML;
    document.getElementById("cijena").innerHTML = selectedMaterial;
    
    console.log(selectedMaterialIndex);
    console.log(searchString);
}