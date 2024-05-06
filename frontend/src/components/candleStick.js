
var chart
export function createCandleChart(data, label, ctx){
  chart = new window.Chart(ctx, {
    type: 'candlestick',
    data: {
      datasets: [{
        label: label,
        data: data,
      }]
    }
  });
}

export function updateChart(data, label) {
  var dataset = chart.config.data.datasets[0];
  dataset.label = label
  dataset.data = data
  chart.update();
}
