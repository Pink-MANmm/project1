<template>
  <div>
    <Header @countryChange="getCountry"></Header>
    <div id="container">
      <Info :countryInfo="countryInfo" :country="country" @yearChange="yearChange" @searchKeyWord="searchKeyWord"></Info>
      <Words :country="country" :words="wordsCloud"></Words>
      <WordsChange :country="country"></WordsChange>
      <Mood :moodData="moodData"></Mood>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'

import Info from '@/components/Info.vue'
import Words from '@/components/Words.vue'
import WordsChange from '@/components/WordsChange.vue'
import Mood from '@/components/Mood.vue'

export default {
  data() {
    return {
      country: 'yuenanDB',
      countryInfo: [],
      yuenanInfo: [],
      pakistanInfo: [],
      yinduInfo: [],
      wordsCloud: [],
      yuenanWordsCloud: [],
      pakistanWordsCloud: [],
      yinduWordsCloud: [],
      moodData: []
    }
  },
  methods: {
    async getMoodData(country) {
      let { data: moodData } = await this.$http.post('/get_mood', { Country: country })
      this.moodData = moodData
    },
    getCountry(cou) {
      if (cou === 'yuenan') {
        this.country = 'yuenanDB'
        this.countryInfo = this.yuenanInfo
        this.wordsCloud = this.yuenanWordsCloud
      } else if (cou === 'pakistan') {
        this.country = 'pakistanDB'
        this.countryInfo = this.pakistanInfo
        this.wordsCloud = this.pakistanWordsCloud
      } else if (cou === 'yindu') {
        this.country = 'yinduDB'
        this.countryInfo = this.yinduInfo
        this.wordsCloud = this.yinduWordsCloud
      }
      this.getMoodData(this.country)
    },
    async getInfo() {
      let { data: yuenanData } = await this.$http.post('/table_data', { Country: 'yuenanDB' })
      let { data: pakistanData } = await this.$http.post('/table_data', { Country: 'pakistanDB' })
      let { data: yinduData } = await this.$http.post('/table_data', { Country: 'yinduDB' })
      for (var index in yuenanData.data) {
        this.yuenanInfo.push(yuenanData.data[index])
      }
      for (var index in pakistanData.data) {
        this.pakistanInfo.push(pakistanData.data[index])
      }
      for (var index in yinduData.data) {
        this.yinduInfo.push(yinduData.data[index])
      }
      this.countryInfo = this.yuenanInfo
      for (var index in yuenanData.wordsData) {
        this.yuenanWordsCloud.push(yuenanData.wordsData[index])
      }
      for (var index in pakistanData.wordsData) {
        this.pakistanWordsCloud.push(pakistanData.wordsData[index])
      }
      for (var index in yinduData.wordsData) {
        this.yinduWordsCloud.push(yinduData.wordsData[index])
      }
      let wordsCloud = []
      for (var index in yuenanData.wordsData) {
        wordsCloud.push(yuenanData.wordsData[index])
      }
      this.wordsCloud = wordsCloud
      this.getMoodData(this.country)
    },
    async yearChange(yearWords) {
      this.wordsCloud = yearWords
    },
    searchKeyWord(searchWords) {
      this.wordsCloud = searchWords
    }
  },
  async created() {
    this.getInfo()
  },
  components: {
    Header,
    Info,
    Words,
    WordsChange,
    Mood
  }
}
</script>

<style lang="less" scoped>
#container {
  position: relative;
  width: 100%;
  top: 48px;
  height: 1550px;
}
</style>