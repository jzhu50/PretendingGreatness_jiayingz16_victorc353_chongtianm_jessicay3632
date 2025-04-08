const { useState, useEffect } = React;

const ApexChart = () => {
  const [data, setData] = useState([]);

  // Fetch Tesla stock data from the server and format it for ApexCharts
  // The data should be in the format [{ x: timestamp, y: price }, ...]
  // The server should return data in JSON format
  useEffect(() => {
    fetch('/api/tesla_stock_data')
      .then(res => res.json())
      .then(stockData => {
        const formattedData = Object.entries(stockData).map(([date, price]) => ({
          x: new Date(date).getTime(),
          y: parseFloat(price)
        }));

        setData(formattedData);

        const options = {
          chart: {
            type: 'area',
            height: 350,
            zoom: {
              type: 'x',
              enabled: true,
              autoScaleYaxis: true
            },
            events: {
                dataPointSelection: function(event, chartContext, config) {
                  const clickedDate = new Date(config.w.config.series[0].data[config.dataPointIndex].x);
                  const dateStr = clickedDate.toISOString().split('T')[0];  // Get YYYY-MM-DD format
              
                  // Redirect to a new page with the clicked date
                  window.location.href = `/tweet/${dateStr}`;
                }
            }
          },
          dataLabels: {
            enabled: false
          },
          markers: {
            size: 0
          },
          title: {
            text: 'Tesla Stock Price Movement',
            align: 'left'
          },
          fill: {
            type: 'gradient',
            gradient: {
              shadeIntensity: 1,
              inverseColors: false,
              opacityFrom: 0.5,
              opacityTo: 0,
              stops: [0, 90, 100]
            }
          },
          yaxis: {
            labels: {
              formatter: function (val) {
                return parseFloat(val).toFixed(2);
              }
            },
            title: {
              text: 'Price (USD)'
            }
          },
          xaxis: {
            type: 'datetime'
          },
          tooltip: {
            shared: false,
            y: {
              formatter: function (val) {
                return parseFloat(val).toFixed(2);
              }
            }
          },
          series: [{
            name: "Tesla Stock Price",
            data: formattedData
          }]
        };

        const chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();
      })
    }, []);

  return React.createElement('div', { id: 'chart' });
};

document.addEventListener('DOMContentLoaded', function () {
  ReactDOM.render(
    React.createElement(ApexChart),
    document.getElementById('app')
  );
});