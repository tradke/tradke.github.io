var button_chron = document.getElementById("button-chron");
var button_sorted = document.getElementById("button-sorted");
var chart_container = document.getElementById("best-races-charts");

button_chron.onclick = function() {
    if(button_chron.className == "br-button-displayed"){
        // Do nothing
    } else {
        // Update button classes
        button_chron.className = "br-button-displayed";
        button_sorted.className = "br-button-hidden";

        // Update button indicators
        button_chron.style.borderColor = "white";
        button_sorted.style.borderColor = "#404040";

        // display chronological charts
        display_charts("chron");
    }
}

button_sorted.onclick = function() {
    if(button_sorted.className == "br-button-displayed"){
        // Do nothing
    } else {
        // Update button classes
        button_sorted.className = "br-button-displayed";
        button_chron.className = "br-button-hidden";

        // Update button indicators
        button_chron.style.borderColor = "#404040";
        button_sorted.style.borderColor = "white";

        // display sorted charts
        display_charts("sorted");
    }
}

function display_charts(filename_prefix) {
    // Changes the src of img tags

    const path = "./images/charts/best-races/";
    const suffixes = ["-gains.svg", "-races.svg", "-days.svg"];
    var i = 0;

    if (chart_container.children.length == suffixes.length){
        for (const child of chart_container.children) {
            if (child.tagName == "IMG") {
                child.src = path+filename_prefix+suffixes[i];
                i++;
            } else {
                console.log("Incompatible child tag");
                return;
            }
        }
    } else {
        console.log("Incompatible number of children");
        return;
    }
}