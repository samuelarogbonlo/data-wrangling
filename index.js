var parseDate = d3.timeParse("%Y/%d/%m");
d3.csv("gas-details_day.csv")
    .row(function(d) {return { date:parseDate(d.date),price:Number(d.maxHenryHubNaturalGasSpotPriceDollarsperMillionBtu.trim().slice(1))};})
    .get(function(error,data){
        

        var height = 400;
        var width = 600;

        var maxDate = d3.max(data,function(d){return d.day; });
        var minDate = d3.min(data,function(d){return d.day; });
        var maxPrice = d3.max(data,function(d){return d.maxHenryHubNaturalGasSpotPriceDollarsperMillionBtu; });
        console.log(maxDate);
        console.log(minDate);
        console.log(maxPrice);
        
        var y = d3.scaleLinear()
                  .domain([0,maxPrice])
                  .range([height,0]);

        var x = d3.scaleTime()
                  .domain([minDate,maxDate])
                  .range([0,width]);

        var yAxis = d3.axisLeft(y);
        var xAxis = d3.axisBottom(x);

        var svg = d3.select('body').append('svg')
                    .attr('height','100%')
                    .attr('width','100%')

        var chartGroup = svg.append('g')
                            .attr('transform', 'translate(50,50)');
        
        var line = d3.line()
                        .x(function(d){ return x(d.day);})
                        .y(function(d){ return x(d.maxPrice);});

        chartGroup.append('path').attr('d', line(data));
        chartGroup.append('g').attr('class', 'x axis').attr('transform', 'translate(-, '+height+')').call(xAxis);
        chartGroup.append('g').attr('class', 'y axis').call(yAxis);
    });