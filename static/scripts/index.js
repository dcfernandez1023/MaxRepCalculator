function calculateOneRepMax() {
    var weightLifted = document.getElementById("weight_lifted").value;
    var numReps = document.getElementById("num_reps").value;
    if(weightLifted.trim().length === 0 || numReps.trim().length === 0) {
        alert("Please enter a value in both input fields.");
        return;
    }
    var full = location.protocol+'//'+location.hostname+(location.port ? ':'+location.port: '');
    var endpoint = full + "/api/calculateOneRepMax/" + weightLifted + "/" + numReps;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            var res = JSON.parse(this.responseText);
            var resultContainer = document.getElementById("result-container");
            resultContainer.innerText = "Estimated one rep max: " + res.one_rep_max.toString();
        }
        else if(this.readyState == 4 && this.status == 400) {
            alert("Bad request. The data you entered is likely invalid. Please enter numbers only.");
        }
        else if(this.readState == 4) {
            alert("An unexpected error occurred. Your request could not be processed.")
        }
    };
    xhttp.open("GET", endpoint, true);
    xhttp.send();
}