<template>
  <div ref="mo" id="mood">
  </div>
</template>

<script>
export default {
  props: {
    moodData: {
      type: Object
    }
  },
  methods: {
    Mood(data) {
      var chartDom = this.$refs.mo
      var Mood = this.$echarts.init(chartDom)
      var moodOption
      var size = 8 //字体大小
      moodOption = {
        title: {
          text: '情感趋势',
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
                fontSize: size
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
                fontSize: size
              }
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
                fontSize: size
              }
            },
            color: '#3172eb',
            areaStyle: {}
          }
        ]
      }
      moodOption.xAxis.data = data['data']['date']
      moodOption.series[0].data = data['data']['title']
      moodOption.series[1].data = data['data']['positive']
      moodOption.series[2].data = data['data']['negetive']
      Mood.setOption(moodOption)
    }
  },
  watch: {
    moodData: {
      handler() {
        var myChart = this.$echarts.init(this.$refs.mo)
        myChart.dispose()
        this.Mood(this.moodData)
      }
    }
  }
}
</script>

<style lang="less" scoped>
#mood {
  position: absolute;
  left: 1%;
  top: 700px;
  width: 98%;
  height: 800px;
  box-shadow: 5px 5px 7px rgb(58 55 55);
  border-radius: 5px;
  background-color: #17102a;
}
</style>