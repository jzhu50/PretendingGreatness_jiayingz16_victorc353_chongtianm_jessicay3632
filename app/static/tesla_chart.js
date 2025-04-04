const ApexChart = () => {
    const[state, setState] = useState({
        series: [{
            name: 'Tesla Stock Price',
            data: dates
        }],
        options: {
            chart: {
                type: 'area',
                stacked: false,
                height: 350,
                zoom: {
                    type: 'x',
                    enabled: true,
                    autoScaleYaxis: true
                },
                toolbar: {
                    autoSelected: 'zoom'
                }
            },
            dataLabels: {
                enabled: false
            },
            markers: {
                size: 0
            },
            title: {
                text: 'Tesla Stock Price',
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
                },
            },
            yaxis: {
                labels: {
                    formatter: function (val) {
                        return (val / 100000).toFixed(0);
                    },
                },
                title: {
                    text: 'Price',
                },
            },
            xaxis: {
                type: 'datetime',
            },
            tooltip: {
                shared: false,
                y: {
                    formatter: function (val) {
                        return (val / 100000).toFixed(0);
                    }
                }
            }
        },
    });

    return (
        <div>
            <div id="chart">
                <ReactApexChart options={state.options} series={state.series} type="area" height={350} />
            </div>
            <div id="html-dist"></div>
        </div>
    );
}

const domContainer = document.querySelector('#app');
ReactDOM.render(<ApexChart />, domContainer);