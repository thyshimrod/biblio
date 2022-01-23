function createTR(typeLivre, nomLivre, numeros){
    table = document.getElementById('tablelivre')
    var row = table.insertRow(1);
    var tdNumeros = row.insertCell(0);
    var tdTitle = row.insertCell(0);
    var tdType = row.insertCell(0);
    let typeVal = "Roman";
    if (typeLivre == 1){
        typeVal = "Manga";
    }else if (typeLivre == 2){
        typeVal = "BD";
    }else if (typeLivre == 3){
        typeVal = "Comics";
    }
    tdTitle.innerHTML = nomLivre;
    tdNumeros.innerHTML = numeros;
    tdType.innerHTML = typeVal;
}

function eraseTR(){
    var table = document.getElementById('tablelivre')
    var trs = table.getElementsByTagName("tr");
    while(trs.length>1) trs[0].parentNode.removeChild(trs[1]);
}

eraseTR();

function onSearch(){
    var inputSearch = document.getElementById('searchInput').value.toUpperCase();
    eraseTR();
    for (let i = 0; i < data.length ;i++){
        if (data[i].title.toUpperCase().indexOf(inputSearch) != -1){
            createTR(data[i].type, data[i].title,data[i].numeros);
        }
    }
}