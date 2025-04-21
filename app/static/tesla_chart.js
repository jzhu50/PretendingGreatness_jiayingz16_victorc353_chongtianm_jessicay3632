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
                  // display message while loading
                  const msg = document.getElementById('loading')
                  if(loading) {
                    msg.style.display = 'flex';
                    msg.style.justifyContent = 'center';
                    msg.style.alignItems = 'center';
                    msg.style.height = '60vh';
                    msg.style.width = '100vw';
                    msg.style.position = 'absolute';
                    msg.style.color = 'red';
                  }
                  // get the clicked date
                  const clickedDate = new Date(config.w.config.series[0].data[config.dataPointIndex].x);
                  // formate it properly
                  const dateStr = clickedDate.toISOString().split('T')[0];
                  // redirect to tweet page
                  window.location.href = `/tweet/${dateStr}`;
                }
            }
          },
          dataLabels: {
            enabled: false
          },
          markers: {
            size: 5, // makes data points larger/visible
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
              opacityFrom: 0.8,
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
            intersect: true, // makes data points selectable
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
  const msg = document.getElementById('loading');
  if (msg) {
    msg.style.display = 'none';
  }

  ReactDOM.render(
    React.createElement(ApexChart),
    document.getElementById('app')
  );
});
