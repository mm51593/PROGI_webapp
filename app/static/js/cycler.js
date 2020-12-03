var stringField = ["elem-arrow-l", "elem-arrow-r"];
var elemMax, videoNode, sourceNode, imgNode;
let currentElem = 0;

function events() {
    elemMax = document.getElementById("elem-count").innerHTML;
    cycleCaller(1);

    //dinamicki elementi
    videoNode = document.createElement("video");
    videoNode.className = "auto-params-vid-img";
    videoNode.setAttribute("controls", true);
    sourceNode = document.createElement("source");
    videoNode.appendChild(sourceNode);

    imgNode = document.createElement("img");
    imgNode.className = "auto-params-vid-img";

    stringField.forEach((e) => {
        document.getElementById(e).addEventListener("mouseover", function () {
            document.getElementById("elem-arrow-l").style.opacity = "0.8";
            document.getElementById("elem-arrow-r").style.opacity = "0.8";
        });
        document.getElementById(e).addEventListener("mouseout", function () {
            document.getElementById("elem-arrow-l").style.opacity = "0.2";
            document.getElementById("elem-arrow-r").style.opacity = "0.2";
        });
    })
}

window.onload = events;

function cycleCaller(direction) {
    var divCycle = document.getElementById("elem-holdncycle");

    currentElem = cycler(direction, elemMax, currentElem);
    var selectedElement = document.getElementById("elem-cycle-" + currentElem);
    var className = selectedElement.className;

    //clearing previous elems
    divCycle.innerHTML = "";
    if (divCycle.childNodes != null) {
        divCycle.childNodes.forEach((e) => e.remove());
    }

    switch (className) {
        case "img-cycle": imgNode.src = selectedElement.innerHTML; divCycle.appendChild(imgNode); break;
        case "vid-cycle": videoNode.childNodes[0].src = selectedElement.innerHTML; divCycle.appendChild(videoNode); break;
        case "text-cycle": divCycle.innerHTML = selectedElement.innerHTML; break;
        default: console.log("Pozvan nedefiniran tip podatka");
    }
}

function cycler(direction, max, current) {
    if (direction == 0) {
        if (current == 0) {
            current = max - 1;
        } else {
            current -= 1;
        }
    } else {
        if (current == max - 1) {
            current = 0;
        } else {
            current += 1;
        }
    }
    return current;
}