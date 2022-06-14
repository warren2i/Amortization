var options = {
  type: 'pie',
  data: {
  labels: ['Interest', 'Principle'],
  datasets: [
    {
      label: 'Interest',
      data: [{interest}, {principal}],
      backgroundColor: [
        "#2ecc71",
        "#3498db"]
    }
  ]},
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Pie Chart'
      }
    }
  },
}

var ctx = document.getElementById('piechartJSContainer').getContext('2d');
new Chart(ctx, options);