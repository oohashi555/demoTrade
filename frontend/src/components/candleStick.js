var barCount = 60;

var chart
export function createCandleChart(ctx, data){
  ctx.canvas.width = 1000;
  ctx.canvas.height = 250;
  
  chart = new window.Chart(ctx, {
  type: 'candlestick',
  data: {
    datasets: [{
      label: '',
      data: data,
    }]
  }
});
}

var update = function() {
  var dataset = chart.config.data.datasets[0];

  // candlestick vs ohlc
  var type = document.getElementById('type').value;
  chart.config.type = type;

  // linear vs log
  var scaleType = document.getElementById('scale-type').value;
  chart.config.options.scales.y.type = scaleType;

  // color
  var colorScheme = document.getElementById('color-scheme').value;
  if (colorScheme === 'neon') {
    chart.config.data.datasets[0].backgroundColors = {
      up: '#01ff01',
      down: '#fe0000',
      unchanged: '#999',
    };
  } else {
    delete chart.config.data.datasets[0].backgroundColors;
  }

  // border
  var border = document.getElementById('border').value;
  if (border === 'false') {
    dataset.borderColors = 'rgba(0, 0, 0, 0)';
  } else {
    delete dataset.borderColors;
  }

  // mixed charts
  var mixed = document.getElementById('mixed').value;
  if (mixed === 'true') {
    chart.config.data.datasets[1].hidden = false;
  } else {
    chart.config.data.datasets[1].hidden = true;
  }

  chart.update();
};
