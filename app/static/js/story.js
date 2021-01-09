function removeElement(self)
{
    self.parentElement.parentElement.remove()
    document.getElementById("input-number").value--;
}

function resetCounter()
{
    document.getElementById("input-number").value = 0;
}
 
function reevaluateNames()
{
    var list = document.getElementById("InputList").childNodes;
    var index = 1;

    for (var item of list)
    {   
        var searchHelp = item.childNodes;
        searchHelp = searchHelp[0].childNodes;

        if(searchHelp[0].getElementsByTagName("input")[0] == undefined) {
            searchHelp[0].getElementsByTagName("textarea")[0].name = item.inputtype + "-" + index.toString();
        } else {
            searchHelp[0].getElementsByTagName("input")[0].name = item.inputtype + "-" + index.toString();
        }
        index++;
    }
}


function addTextField(type)
{
    var newlistitem = document.createElement("li");

    var field;

    if (type == "text")
    {
        field = document.createElement("textarea");
        newlistitem.inputtype = "text";
        field.type = "text";
        field.className = "text-field-class";
    }
    else if (type == "image")
    {
        field = document.createElement("input");
        newlistitem.inputtype = "image";
        field.type = "file";
        field.accept = "image/*";
        field.className = "elem-check-selected";
    }
    else
    {
        field = document.createElement("input");
        newlistitem.inputtype = "video";
        field.type = "file";
        field.accept = "video/*";
        field.className = "elem-check-selected";
    }


    var listDiv = document.createElement("div");
    listDiv.className = "listDiv";

    var contentDiv = document.createElement("div");
    contentDiv.className = "div-content";

    var newlabel = document.createElement("label");
    switch(type) {
        case "image" : newlabel.textContent = "Dodaj sliku";
                       break;
        case "video" : newlabel.textContent = "Dodaj video";
                       break;
        case "text" : newlabel.textContent = "Dodaj tekst";
                       break;
    }
    newlabel.className = "elem-submit-" + type;

    var removebutton = document.createElement("button");
    removebutton.type = "button";
    removebutton.textContent = "Remove";
    removebutton.className = "rmv-prijedlog-elem";
    removebutton.onclick = function() {return removeElement(removebutton);};

    contentDiv.append(newlabel);
    contentDiv.append(field);
   
    listDiv.append(contentDiv);
    listDiv.append(removebutton);
    
    newlistitem.append(listDiv);
    newlistitem.className = "elem-liste";
    
    

    document.getElementById("input-number").value++;
    document.getElementById("InputList").append(newlistitem);

    reevaluateNames();
}

resetCounter()
