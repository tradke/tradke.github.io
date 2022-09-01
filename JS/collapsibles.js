var buttons = document.getElementsByClassName("collapsible-button");
var i;

for (i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function() {
        var content = this.nextElementSibling;
        if (content.style.maxHeight==="fit-content"){
            // if non-zero, collapse it
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = "fit-content";
        }
    });
}