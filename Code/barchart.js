function dropdown(){
    let menuselector = d3.select("#selDataset")
    d3.json(url).then(function(data) {
        console.log(data);
        let names = data.names
        console.log(names);
        names.forEach((sample) => {
            menuselector
              .append("option")
              .text(sample)
              .property("value", sample);
          });
          createcharts(names[0])
          createtable(names[0])


      });

}
dropdown()





function optionChanged(new_id) {

    createcharts(new_id);
  }


function createcharts(input_id){
    d3.json(url).then(function(data) {
        console.log(data);
        let samples = data.samples
        console.log(samples);

        let sampleresult = samples.filter(x => x.id==input_id);
        sampleresult = sampleresult[0]

        sample_values = sampleresult.sample_values

        otu_ids = sampleresult.otu_ids
        
        otu_labels = sampleresult.otu_labels

        var bardata = [{
            x: sample_values.slice(0, 10).reverse(),
            y: otu_ids.slice(0, 10).map(otuID => `OTU ${otuID}`).reverse(),
            text: otu_labels.slice(0, 10).reverse(),
            orientation: 'h',
            type: 'bar'
          }];
          
          var barlayout = {
            title: 'Bar Chart',
          };
        }
    )}