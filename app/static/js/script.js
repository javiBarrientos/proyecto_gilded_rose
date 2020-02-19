function loadItems() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var myObj = JSON.parse(this.responseText);

        var taula = document.getElementById("taulaItems");

        taula.innerHTML = "";

        for (let item in myObj.items) {
          var row = taula.insertRow(-1);
          
          var cell0 = row.insertCell(0);
          var cell1 = row.insertCell(1);
          var cell2 = row.insertCell(2);
          var cell3 = row.insertCell(3);
          cell0.innerHTML = parseInt(item)+1;
          cell1.innerHTML = myObj.items[item].name;
          cell2.innerHTML = myObj.items[item].sell_in;
          cell3.innerHTML = myObj.items[item].quality;
        }
        //document.getElementById("demo").innerHTML = myObj.name;
      }
    };
    xmlhttp.open("GET", "/static/json/items.json", true);
    xmlhttp.send();
  }        

window.onload = function() {
  loadItems();
};