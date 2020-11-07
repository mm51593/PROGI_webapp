function removeElement(self)
{
    self.parentElement.remove()
}


function addTextField()
{
    var newlistitem = document.createElement("li");
    var textinput = document.createElement("input");
    textinput.type = "text";


    var removebutton = document.createElement("button");
    removebutton.type = "button";
    removebutton.textContent = "Remove";
    removebutton.onclick = function() {return removeElement(removebutton);};
    newlistitem.append(textinput);
    newlistitem.append(removebutton);
    document.getElementById("InputList").append(newlistitem);
}
