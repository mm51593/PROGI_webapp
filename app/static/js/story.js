function removeElement(self)
{
    self.parentElement.remove()
    document.getElementById("input-number").value--;
}

function reevaluateNames()
{
    var list = document.getElementById("InputList").childNodes;
    var index = 1;

    for (var item of list)
    {
        item.getElementsByTagName("input")[0].name = item.inputtype + "-" + index.toString();
        index++;
    }
}


function addTextField(type)
{
    var newlistitem = document.createElement("li");

    var field = document.createElement("input");

    if (type == "text")
    {
        newlistitem.inputtype = "text";
        field.type = "text";
    }
    else if (type == "image")
    {
        newlistitem.inputtype = "image";
        field.type = "file";
        field.accept = "image/*";
    }
    else
    {
        newlistitem.inputtype = "video";
        field.type = "file";
        field.accept = "video/*";
    }

    var newlabel = document.createElement("label");
    newlabel.textContent = "Add " + type;

    var removebutton = document.createElement("button");
    removebutton.type = "button";
    removebutton.textContent = "Remove";
    removebutton.onclick = function() {return removeElement(removebutton);};

    newlistitem.append(newlabel);
    newlistitem.append(field);
    newlistitem.append(removebutton);

    document.getElementById("input-number").value++;
    document.getElementById("InputList").append(newlistitem);

    reevaluateNames();
}