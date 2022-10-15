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
  d3.json(data_url).then((data) => {
    let date_data = {}
    data.forEach((datum) => {
      if (datum.date == date) {
        date_data = datum
      }
    })
    console.log(date_data)

  
    var final_data = [
      {
        x: ['aud', 'cad', 'chf', 'eur', 'gbp', 'jpy', 'nok', 'nzd', 'sek', 'usd'],
        y: [date_data['aud'], 
        date_data['cad'], 
        date_data['chf'], 
        date_data['eur'], 
        date_data['gbp'],
        date_data['jpy'], 
        date_data['nok'], 
        date_data['nzd'], 
        date_data['sek'],
        date_data['usd']],
        type: 'bar'
      }
    ];

    var layout = {
      title: {
        text:'US Dollar vs Other Currencies',
      },
      xaxis: {
        title: {
          text: 'Currency',
        },
      },
      yaxis: {
        title: {
          text: 'Price in USD',
        }
      }
    };
    
    Plotly.newPlot('bar', final_data, layout);

  });
};

function buildBubble(date) {
  d3.json(bydate_url).then((data) => {

    // Plotly.newPlot("bubble",data2,layout2);
  });
};

function buildTimeSeries() {

};

function optionChanged(date) {
  buildBar(date);
  buildBubble(date);
};


init();