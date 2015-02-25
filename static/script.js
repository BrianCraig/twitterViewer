var App = {}


App.inicializar = function () {}
App.obtenerPosicion = function () {}
App.recargarMarcadores = function (objeto) {


    for(var x in App.marcadores){
        App.marcadores[x].setMap(null);
    }
    App.marcadores = []

  for(var x in objeto){
    var y = objeto[x]
    var myLatlng = new google.maps.LatLng(y.coordenadas[0], y.coordenadas[1]);

    var mark = new google.maps.Marker({
    position: myLatlng,
    map: App.map,
    title: y.tweet
  });
    App.marcadores.push(mark);
  }


}

App.buscar = function () {}

App.map
App.marcadores = []


App.inicializar = function () {
  var mapOptions = {
    center: {
      lat: -34.397,
      lng: -58.381667
    },
    zoom: 8
  };

  App.map = new google.maps.Map(document.getElementById('map-canvas'),
    mapOptions);

  var myLatlng = new google.maps.LatLng(-34.397, -58.381667);

  var marker = new google.maps.Marker({
    position: myLatlng,
    map: App.map,
    draggable: true,
    icon:'/static/mark.png',
    title: "Posicion a buscar",
    style:{
    fillColor:'#ccc'
    }
  });

    var circuloOpciones = {
      strokeColor: '#FF0000',
      strokeOpacity: 0.4,
      strokeWeight: 2,
      fillColor: '#FF0000',
      fillOpacity: 0.15,
      map: App.map,
      center: myLatlng,
      radius: 15000
    };
    // Add the circle for this city to the map.
    circulo = new google.maps.Circle(circuloOpciones);

    google.maps.event.addListener(marker, 'drag', function(){
    console.log(circulo)
        circulo.setCenter(App.obtenerPosicion())
        return false;
    });

  App.obtenerPosicion = function () {
    return marker.getPosition();
  }
  $('#km').keyup(function(){
  console.log(circulo)
    circulo.setRadius(parseInt(this.value*1000))
  })

  document.getElementById("buscar").onclick = App.buscar;
}

App.buscar = function () {
  var query = document.getElementById('query').value
  var km = document.getElementById('km').value

  $.get(
    "/api/buscar/" + query + "/", {
        lat : App.obtenerPosicion().lat(),
        lng : App.obtenerPosicion().lng(),
        km : km
    },
    function (data) {
      App.recargarMarcadores(JSON.parse(data))
    }
  );

}



function addmarker(obj) {
  var myLatlng = new google.maps.LatLng(obj[0], obj[1]);

  // To add the marker to the map, use the 'map' property
  var marker = new google.maps.Marker({
    position: myLatlng,
    map: map,
    title: "Hello World!"
  });
  google.maps.event.addListener(marker, 'click', function () {
    console.log(marker.getPosition());
    console.log(marker)
    console.log(obj)
  });
  console.log(marker)
}


google.maps.event.addDomListener(window, 'load', App.inicializar);