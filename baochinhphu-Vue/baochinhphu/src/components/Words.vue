<template>
  <div ref="wordcloud" id="wordcloud">
  </div>
</template>

<script>
import { init } from 'events'

export default {
  props: {
    country: {
      type: String,
      default: ''
    },
    words: {
      type: Array
    }
  },
  methods: {
    wordsCloud(data) {
      let wordcloud = this.$echarts.init(this.$refs.wordcloud)
      let wordcloud_option = {
        // backgroundColor: '#515151',
        title: {
          text: '新闻热词',
          textStyle: {
            color: 'rgba(255,255,255,0.75)'
          },
          left: 'left'
        },
        tooltip: {
          show: false
        },
        series: [
          {
            type: 'wordCloud',
            // drawOutOfBound:true,
            gridSize: 1,
            sizeRange: [12, 55],
            rotationRange: [-45, 0, 45, 90],
            // maskImage: maskImage,

            //这是让词云图的颜色随机
            textStyle: {
              normal: {
                color: function () {
                  return 'rgb(' + [Math.round(Math.random() * 160), Math.round(Math.random() * 160), Math.round(Math.random() * 160)].join(',') + ')'
                }
              }
            },
            // left: 'center',
            // top: 'center',
            // // width: '96%',
            // // height: '100%',
            right: null,
            bottom: null,
            // width: 300,
            // height: 200,
            // top: 20,
            data: data
          }
        ]
      }
      wordcloud.setOption(wordcloud_option)
    },
    echartsInit(data) {
      let myChart = this.$echarts.init(this.$refs.wordcloud)
      //myChart.clear() //清空当前实例，会移除实例中所有的组件和图表
      myChart.dispose() //销毁实例，实例销毁后无法再被使用
      this.wordsCloud(data)
    }
  },
  watch: {
    country: {
      handler() {
        this.echartsInit(this.words)
      }
    },
    words: {
      handler(newVal, oldVal) {
        this.echartsInit(newVal)
      }
    }
  }
}
</script>

<style lang="less" scoped>
#wordcloud {
  position: absolute;
  top: 15px;
  left: 52%;
  padding: 10px;
  width: 45.5%;
  height: 220px;
  box-shadow: 5px 5px 7px rgb(58 55 55);
  border-radius: 5px;
  background-color: #17102a;
}

#wordcloud div {
  width: 100%;
  height: 100%;
}
</style>