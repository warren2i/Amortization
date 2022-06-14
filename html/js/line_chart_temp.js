var options = {
  type: 'line',
  data: {
    label: 'months',
    labels: {months},

    datasets: [
	    {
	      label: 'total payments',
	      data: {data_1},
	      borderColor: "#bae755",
	      fill: false,
      	borderWidth: 1
    	},
			{
				label: 'total interest',
				data: {data_2},
				borderColor: "#a534eb",
				fill: false,
				borderWidth: 1
			},
			{
				label: 'principal balance',
				data: {data_3},
				borderColor: "#eb3a34",
				fill: false,
				borderWidth: 1
			}
		]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
  	scales: {
    	yAxes: [{
        ticks: {
					reverse: false
        }
      }]
    }
  },

}

var ctx = document.getElementById('chartJSContainer').getContext('2d');
new Chart(ctx, options);