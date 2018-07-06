	
$( document ).ready(function() {
  
var grafico1 = function(data){ 
 
//1
nv.addGraph(function() {
  var chart = nv.models.discreteBarChart()
      .x(function(d) { return d.label })    //Specify the data accessors.
      .y(function(d) { return d.value })
      .staggerLabels(true)    //Too many bars and not enough room? Try staggering labels.
      .tooltips(true)        //Don't show tooltips
      .showValues(true)       //...instead, show the bar value right on top of each bar.
      .transitionDuration(3600)
      ;

  d3.select('#chart2 svg')
      .datum(data)
      .call(chart);

  nv.utils.windowResize(chart.update);

  return chart;
});

console.log(data)

}

//2 

var grafico2 = function(data2){ 
 		
nv.addGraph(function() {
  var chart = nv.models.discreteBarChart()
      .x(function(d) { return d.label })    //Specify the data accessors.
      .y(function(d) { return d.value })
      .staggerLabels(true)    //Too many bars and not enough room? Try staggering labels.
      .tooltips(true)        //Don't show tooltips
      .showValues(true)       //...instead, show the bar value right on top of each bar.
      .transitionDuration(3600)	  
	 
    ;
	
  d3.select('#chart3 svg')
      .datum(data2)
      .call(chart);

  nv.utils.windowResize(chart.update);

  return chart;
});

console.log(data2)

}



//1
var prueba = function(){
	$.ajax({
    type: "POST",
    url: "/polls/prueba/",
    success: function(data) {
        if (data.error !== ""){
            console.log(data.error)
        }else{
            console.log(data.response)
			grafico1(data.response)
        }
    }
});	

};

//2
var prueba2 = function(){
	$.ajax({
    type: "POST",
    url: "/polls/prueba2/",
    success: function(data2) {
        if (data2.error !== ""){
            console.log(data2.error)
        }else{
            console.log(data2.response)
			grafico2(data2.response)
        }
    }
});	

};

prueba();
prueba2();



});