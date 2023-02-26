let wordsChange = echarts.init(document.getElementById('wordsChange'))
const updateFrequency = 2000;
const dimension = 0;
const countryColors = {
  '中国': '#00008b',
  '越南': '#f00',
  '总理': '#ffde00',
  '国家': '#002a8f',
  '会见': '#003580',
  '主席': '#ed2939',
  '合作': '#000',
  '委员会': '#003897',
  '发言人': '#f93',
  '会议': '#bc002d',
  '越中': '#024fa2',
  '外交部': '#000',
  '肺炎': '#00247d',
  Norway: '#ef2b2d',
  Poland: '#dc143c',
  Russia: '#d52b1e',
  Turkey: '#e30a17',
  'United Kingdom': '#00247d',
  'United States': '#b22234'
};
function wordsChange_Init() {
  $.when(
    $.getJSON('../static/json/data.json'),
    $.getJSON('../static/json/life-expectancy-table.json')
  ).done(function (res0, res1) {
    const flags = res0[0];
    const data = res1[0];
    const years = [];
    for (let i = 0; i < data.length; ++i) {
      if (years.length === 0 || years[years.length - 1] !== data[i][2]) {
        years.push(data[i][2]);
      }
    }
    function getFlag(countryName) {
      if (!countryName) {
        return '';
      }
      return (
        flags.find(function (item) {
          return item.name === countryName;
        }) || {}
      ).emoji;
    }
    let startIndex = 0;
    let startYear = years[startIndex];
    option = {
      title: {
        text: "热词变化",
        textStyle: {
          color: 'rgba(255,255,255,0.75)',
        },
        left: 'left'
      },
      grid: {
        top: 20,
        bottom: 30,
        left: 150,
        right: 80
      },
      xAxis: {
        max: 'dataMax',
        axisLabel: {
          formatter: function (n) {
            return Math.round(n) + '';
          }
        }
      },
      dataset: {
        source: data.slice(0).filter(function (d) {
          return d[2] === startYear;
        })
      },
      yAxis: {
        type: 'category',
        inverse: true,
        max: 10,
        axisLabel: {
          show: true,
          fontSize: 14,
          color: 'rgba(255,255,255,0.75)',
          formatter: function (value) {
            return value;
          },
          rich: {
            flag: {
              fontSize: 25,
              padding: 5,
            }
          }
        },
        animationDuration: 300,
        animationDurationUpdate: 300
      },
      series: [
        {
          realtimeSort: true,
          seriesLayoutBy: 'column',
          type: 'bar',
          itemStyle: {
            color: function (param) {
              return countryColors[param.value[1]] || '#5470c6';
            }
          },
          encode: {
            x: 0,
            y: 1
          },
          label: {
            show: true,
            precision: 1,
            position: 'right',
            valueAnimation: true,
            fontFamily: 'monospace'
          }
        }
      ],
      // Disable init animation.
      animationDuration: 0,
      animationDurationUpdate: updateFrequency,
      animationEasing: 'linear',
      animationEasingUpdate: 'linear',
      graphic: {
        elements: [
          {
            type: 'text',
            right: 160,
            bottom: 60,
            style: {
              text: startYear,
              font: 'bolder 80px monospace',
              fill: 'rgba(255,255,255,0.75)'
            },
            z: 100
          }
        ]
      }
    };
    // console.log(option);
    wordsChange.setOption(option);
    for (let i = startIndex; i < years.length - 1; ++i) {
      (function (i) {
        setTimeout(function () {
          updateYear(years[i + 1]);
        }, (i - startIndex) * updateFrequency);
      })(i);
    }
    function updateYear(year) {
      let source = data.slice(0).filter(function (d) {
        return d[2] === year;
      });
      option.series[0].data = source;
      option.graphic.elements[0].style.text = year;
      wordsChange.setOption(option);
    }
  });
}