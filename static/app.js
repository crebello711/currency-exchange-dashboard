const base_url = "http://127.0.0.1:5000/api/v1.0/"
const bydate_url = "http://127.0.0.1:5000/api/v1.0/by_date"
const data_url = "http://127.0.0.1:5000/api/v1.0/data"
const timeseries_url = "http://127.0.0.1:5000/api/v1.0/time-series"

function init() {
  let dropDownMenu = d3.select("#selDataset");
  d3.json(data_url).then((data) => 
  {
    console.log(data[0]['date']);
    data.forEach((datum) => {
        dropDownMenu.append("option").text(datum.date).property("value", datum.date)
    });

    let initDate = data[0]['date'];
    buildBar(initDate);
    buildBubble(initDate);
    buildTimeSeries();
    
  });

  // timeseries
   //buildTimeSeries();

   
};
/////////////////////////////////////////////////////////////////////////////////
function buildBar(date) { 
  d3.json(bydate_url).then((data) => {
  
    //Plotly.newPlot("bar", data, layout1);  
  });
};
//////////////////////////////////////////////////////////////////////////////////
function buildBubble(date) {
  d3.json(bydate_url).then((data) => {

    // Plotly.newPlot("bubble",data2,layout2);
  });
};
//////////////////////////////////////////////////////////////////////////////////

var dict = {}
function buildTimeSeries()
{
    d3.json(timeseries_url).then((data_2) => {
        console.log(data_2)
        // let ts = {}

        var aud = {
            x: data_2[0],
            y: data_2[1],
            mode: 'lines+markers',
            name: 'Australian dollar'
        };

        var cad = {
            x: data_2[0],
            y: data_2[2],
            mode: 'lines+markers',
            name: 'Canadian dollar'
        };

        var eur = {
            x: data_2[0],
            y: data_2[3],
            mode: 'lines+markers',
            name: 'Euro'
        };

        var jpy = {
            x: data_2[0],
            y: data_2[4],
            mode: 'lines+markers',
            name: 'Japanese yen'
        };
        var nzd = {
            x: data_2[0],
            y: data_2[5],
            mode: 'lines+markers',
            name: 'New Zealand dollar'
            
        };
        var nok = {
            x: data_2[0],
            y: data_2[6],
            mode: 'lines+markers',
            name: 'Norwegian krone'
        };
        var sek = {
            x: data_2[0],
            y: data_2[7],
            mode: 'lines+markers',
            name: 'Swedish krona'
        };
        var chf = {
            x: data_2[0],
            y: data_2[8],
            mode: 'lines+markers',
            name: 'Swiss franc'
        };
        var cbp = {
            x: data_2[0],
            y: data_2[9],
            mode: 'lines+markers',
            name: 'U.K. pound'
        };

        var usd = {
            x: data_2[0],
            y: data_2[10],
            mode: 'lines+markers',
            name: 'U.S. dollar'
        };
        var data = [aud, cad, eur, jpy, nzd, nok, sek, chf, cbp, usd];

        var layout = {
            title: 'Averagr Exchange Currency Rate per Year [1998-2022]',
            xaxis: {
                title: 'Year',
                showgrid: false,
                //zeroline: false
            },
            yaxis: {
                title: 'Average Exchange Rate',
                showline: false
            }
        };

        Plotly.newPlot('myDiv', data,layout);
        //dictionary for drop down option if created 
        //["aud"] = au
        //dict["cad"] = ca
        //dict["eur"] = eu
        //dict["nzd"] = nz
        //dict["nok"] = no
        //dict["sek"] = sk
        //dict["chf"] = ch
        //dict["cbp"] = cb
        //dict["usd"] = us
        
    });
};

function optionChanged(date) {
  buildBar(date);
  buildBubble(date);
};

function optionChanged2() {
    buildTimeSeries();
};

init();