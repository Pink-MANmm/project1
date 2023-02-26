var chartDom = document.getElementById('mood');
var Mood = echarts.init(chartDom);
var moodOption;
var size = 8;//字体大小
moodOption = {
  title: {
    text: "情感趋势",
    textStyle: {
      color: 'rgba(255,255,255,0.75)'
    }
  },
  legend: {
    data: ['积极趋势', '消极趋势', '总体趋势'],
    textStyle: {
      color: 'rgba(255,255,255,0.75)'
    }
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: []
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      name: '总体趋势',
      label: {
        show: 'true',
        position: 'top',
        textStyle: {
          fontSize: size,
        }
      },
      data: [],
      type: 'line',
      color: '#eb3434',

      areaStyle: {}
    },
    {
      name: '积极趋势',
      data: [],
      type: 'line',
      color: '#eba834',

      label: {
        show: 'true',
        position: 'top',
        textStyle: {
          fontSize: size,
        },
      },
      areaStyle: {}
    },
    {
      name: '消极趋势',
      data: [],
      type: 'line',
      label: {
        show: 'true',
        position: 'bottom',
        textStyle: {
          fontSize: size,
        },
      },
      color: "#3172eb",
      areaStyle: {}
    }
  ]
};



Mood.setOption(moodOption)