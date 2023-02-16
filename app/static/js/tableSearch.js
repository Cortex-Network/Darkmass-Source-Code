function glossarySearch() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("glossaryInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("glossaryTable")
    tr = table.getElementsByTagName("tr")

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function rangedTableSearch() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("weaponsTableInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("weaponsTableGroup")
    tr = table.getElementsByTagName("tr")

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}


function meleeTableSearch() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("weaponsTableInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("weaponsTable")
    tr = table.getElementsByTagName("tr")

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}