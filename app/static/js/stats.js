document.getElementById('meleeActionsBtn').addEventListener('click', hideMeleeActions);

function hideMeleeActions() {
    var meleeActions = document.getElementById("meleeActions")
    var meleeBars = document.getElementById("meleeBars")
    var meleeTable = document.getElementById("meleeTable")
    if (meleeActions.style.display === "none") {
        meleeActions.style.display = "block";
        meleeBars.style.display = "none";
        meleeTable.style.display = "none";
    } else {
        meleeActions.style.display = "none"
    }

}

document.getElementById('meleeBarsBtn').addEventListener('click', hideMeleeBars);

function hideMeleeBars() {
    var meleeActions = document.getElementById("meleeActions")
    var meleeBars = document.getElementById("meleeBars")
    var meleeTable = document.getElementById("meleeTable")
    if (meleeBars.style.display === "none") {
        meleeActions.style.display = "none";
        meleeBars.style.display = "block";
        meleeTable.style.display = "none";
    } else {
        meleeBars.style.display = "none"
    }
}

document.getElementById('meleeTableBtn').addEventListener('click', hideMeleeWeaponTable);

function hideMeleeWeaponTable() {
    var meleeActions = document.getElementById("meleeActions")
    var meleeBars = document.getElementById("meleeBars")
    var meleeTable = document.getElementById("meleeTable")
    if (meleeTable.style.display === "none") {
        meleeActions.style.display = "none";
        meleeBars.style.display = "none";
        meleeTable.style.display = "block";
    } else {
        meleeTable.style.display = "none"
    }
}

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