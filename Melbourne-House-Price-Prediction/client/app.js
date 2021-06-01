
function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var type = document.getElementById("uiTypes");
  var rooms = document.getElementById("uiRooms");
  var distance = document.getElementById("uiDistance");
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
      type: type.value,
      rooms: rooms.value,
      distance: distance.value,
      suburb: location.value
  },function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " AUD</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
   var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

   var url2 = "http://127.0.0.1:5000/get_type_names";

  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });

  $.get(url2,function(data, status) {
      console.log("got response for get_type_names request");
      if(data) {
          var types = data.types;
          var uiTypes = document.getElementById("uiTypes");
          $('#uiTypes').empty();
          for(var i in types) {
              var opt = new Option(types[i]);
              $('#uiTypes').append(opt);
          }
      }
  });


}

window.onload = onPageLoad;
