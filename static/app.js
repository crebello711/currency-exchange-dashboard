const base_url = "http://127.0.0.1:5000/api/v1.0/"
const bydate_url = "http://127.0.0.1:5000/api/v1.0/by_date"
const data_url = "http://127.0.0.1:5000/api/v1.0/data"

function init() {
  let dropDownMenu = d3.select("#selDataset");

  d3.json(data_url).then((data) => {
    console.log(data[0]['date']);
    data.forEach((datum) => {
      dropDownMenu.append("option").text(datum.date).property("value",datum.date)
    });

    let initDate = data[0]['date'];
    buildBar(initDate);
    buildBubble(initDate);
    buildTimeSeries();
  });
};

function buildBar(date) { 
  d3.json(bydate_url).then((data) => {
  
    Plotly.newPlot("bar", data1, layout1);  
  });
};

function buildBubble(date) {
  d3.json(bydate_url).then((data) => {

    Plotly.newPlot("bubble",data2,layout2);
  });
};

function buildTimeSeries() {

};

function optionChanged(date) {
  buildBar(date);
  buildBubble(date);
};


init();