document.getElementById('glossaryBtn').addEventListener('click', hideGlossary);

function hideGlossary() {
    var glossaryTable = document.getElementById("glossaryTable")
    var critTable = document.getElementById("critTable")
    if (glossaryTable.style.display === "none") {
        glossaryTable.style.display = "block";
        critTable.style.display = "none";
    } else {
        glossaryTable.style.display = "none"
    }

}

document.getElementById('CritBtn').addEventListener('click', hideCritTable);

function hideCritTable() {
    var glossaryTable = document.getElementById("glossaryTable")
    var critTable = document.getElementById("critTable")
    if (critTable.style.display === "none") {
        critTable.style.display = "block";
        glossaryTable.style.display = "none";
    } else {
        critTable.style.display = "none"
    }

}