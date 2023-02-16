document.getElementById('rangedActionsBtn').addEventListener('click', hideRangedActions);

function hideRangedActions() {
    var rangedActions = document.getElementById("rangedActions")
    var rangedBars = document.getElementById("rangedBars")
    var rangedTable = document.getElementById("rangedTable")
    var rangedPerWeapon = document.getElementById("rangedPerWeapon")
    if (rangedActions.style.display === "none") {
        rangedActions.style.display = "block";
        rangedBars.style.display = "none";
        rangedTable.style.display = "none";
        rangedPerWeapon.style.display = "none";
    } else {
        rangedActions.style.display = "none"
    }
}

document.getElementById('rangedBarsBtn').addEventListener('click', hideRangedBars);

function hideRangedBars() {
    var rangedActions = document.getElementById("rangedActions")
    var rangedBars = document.getElementById("rangedBars")
    var rangedTable = document.getElementById("rangedTable")
    var rangedPerWeapon = document.getElementById("rangedPerWeapon")
    if (rangedBars.style.display === "none") {
        rangedActions.style.display = "none";
        rangedBars.style.display = "block";
        rangedTable.style.display = "none";
        rangedPerWeapon.style.display = "none";
    } else {
        rangedBars.style.display = "none"
    }
}

document.getElementById('rangedTableBtn').addEventListener('click', hideRangedTable);

function hideRangedTable() {
    var rangedActions = document.getElementById("rangedActions")
    var rangedBars = document.getElementById("rangedBars")
    var rangedTable = document.getElementById("rangedTable")
    var rangedPerWeapon = document.getElementById("rangedPerWeapon")
    if (rangedTable.style.display === "none") {
        rangedActions.style.display = "none";
        rangedBars.style.display = "none";
        rangedTable.style.display = "block";
        rangedPerWeapon.style.display = "none";
    } else {
        rangedTable.style.display = "none"
    }
}

document.getElementById('rangedPerWeaponBtn').addEventListener('click', hideRangedPerWeapon);

function hideRangedPerWeapon() {
    var rangedActions = document.getElementById("rangedActions")
    var rangedBars = document.getElementById("rangedBars")
    var rangedTable = document.getElementById("rangedTable")
    var rangedPerWeapon = document.getElementById("rangedPerWeapon")
    if (rangedPerWeapon.style.display === "none") {
        rangedActions.style.display = "none";
        rangedBars.style.display = "none";
        rangedTable.style.display = "none";
        rangedPerWeapon.style.display = "block";
    } else {
        rangedPerWeapon.style.display = "none"
    }
}