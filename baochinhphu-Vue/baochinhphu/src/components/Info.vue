<template>
  <div id="Info">
    <div id="category">
      <div id="Year" @mouseenter="showYears" @mouseleave="hideYears">
        <div ref="all" class="year active" id="Y-all" @click="allYearsData">全部</div>
        <div class="year" v-for="item in years" :key="item" @click="yearData(item,$event)">{{ item }}</div>
      </div>
      <div id="search" style="position: absolute;top: -5px;right: 13px;width: 260px">
        <input type="text" id="idSearch" ref="searchContent" @keyup.enter="search" placeholder="请输入关键字" style="position:absolute; top:5px;height: 24px">
        <button id="Search" @click="search" style="position:absolute;top: 5px;right: 0;height: 30px;width: 60px">搜索</button>
      </div>
    </div>
    <table class="table table-hover">
      <thead>
        <th style="color: #0f0f0f;" class="list1">
          <div style="margin: 2px 0;border-radius: 5px;background-color: #c9c5c5">时间</div>
        </th>
        <th style="color: #0f0f0f;" class="list2">
          <div style="margin: 2px 0;border-radius: 5px;background-color: #c9c5c5">题目</div>
        </th>
      </thead>
      <tbody>
        <tr class="singleInfo" v-if="country === 'yuenanDB'" v-for="item in Info" :key="item.id">
          <td class="list1">{{item.date}}</td>
          <td class="list2"><a class="link" target="_blank" :href="'https://baochinhphu.vn'+item.href">{{item.title}}</a></td>
        </tr>
        <tr class="singleInfo" v-if="country === 'pakistanDB'" v-for="item in Info" :key="item.id">
          <td class="list1">{{item.date}}</td>
          <td class="list2"><a class="link" target="_blank" :href="item.href">{{item.title}}</a></td>
        </tr>
        <tr class="singleInfo" v-if="country === 'yinduDB'" v-for="item in Info" :key="item.id">
          <td class="list1">{{item.date}}</td>
          <td class="list2"><a class="link" target="_blank" :href="'https://timesofindia.indiatimes.com'+item.href">{{item.title}}</a></td>
        </tr>
      </tbody>
    </table>
    <div id="pagenumber" style="width: 250px;height: 30px;">
      <button ref="pre" id="previous" @click="pre" style="position: absolute;left: 0px;width: 70px;height: 30px">上一页</button>
      <span id="page" style="position: absolute;left: 90px;width:100px ;font: normal 15px/30px '宋体'">第{{ page }}/{{ pageLength }}页</span>
      <button ref="nex" id="next" @click="nex" style="position: absolute;right: 0px;width: 70px;height: 30px">下一页</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    country: {
      type: String,
      default: ''
    },
    countryInfo: {
      type: Object
    }
  },
  data() {
    return {
      contentStart: 0,
      contentEnd: 20,
      page: 1,
      Info: [],
      storeInfo: [],
      years: []
    }
  },
  methods: {
    pre() {
      this.page -= 1
      if (this.page === 1) {
        this.$refs.pre.disabled = 'true'
        this.$refs.nex.disabled = ''
      } else {
        this.$refs.pre.disabled = ''
        this.$refs.nex.disabled = ''
      }
      ;(this.contentStart -= 20), (this.contentEnd -= 20)
    },
    nex() {
      this.page += 1
      if (this.page === this.pageLength) {
        this.$refs.nex.disabled = 'true'
        this.$refs.pre.disabled = ''
      } else {
        this.$refs.nex.disabled = ''
        this.$refs.pre.disabled = ''
      }
      this.contentStart += 20
      this.contentEnd += 20
    },
    InfoInit() {
      this.Info = this.storeInfo.slice(this.contentStart, this.contentEnd)
    },
    pageInit() {
      if (this.page === 1) {
        this.$refs.pre.disabled = 'true'
      } else {
        this.$refs.pre.disabled = ''
      }
      if (this.page === this.pageLength) {
        this.$refs.nex.disabled = 'true'
      } else {
        this.$refs.nex.disabled = ''
      }
    },
    yearsInit() {
      this.years = []
      this.storeInfo.forEach(x => {
        if (this.years.indexOf(x.date.slice(0, 4)) === -1) {
          this.years.push(x.date.slice(0, 4))
        }
      })
    },
    toggleYears(Dom, position1, position2) {
      for (var i = 0; i < Dom.children.length; i++) {
        if (Dom.children[i].className === 'year active') {
          Dom.children[i].style.position = position1
        } else {
          Dom.children[i].style.position = position2
        }
      }
    },
    showYears(event) {
      event.target.style.height = 'fit-content'
      this.toggleYears(event.target, 'static', 'static')
    },
    hideYears(event) {
      event.target.style.height = '32px'
      this.toggleYears(event.target, 'absolute', 'static')
    },
    toggleYearData(Dom) {
      for (var i = 0; i < Dom.parentNode.children.length; i++) {
        if (Dom.parentNode.children[i] !== Dom) {
          Dom.parentNode.children[i].className = 'year'
        } else {
          Dom.className = 'year active'
        }
      }
      this.toggleYears(Dom, 'absolute', 'static')
    },
    async allYearsData(event) {
      event.target.parentNode.style.height = '32px'
      this.storeInfo = this.countryInfo
      this.toggleYearData(event.target)
      let { data: yearData } = await this.$http.post('/get_yearData', { year: 'total', country: this.country })
      let words = []
      for (var index in yearData.wordsData) {
        words.push(yearData.wordsData[index])
      }
      this.$emit('yearChange', words)
    },
    async yearData(year, event) {
      event.target.parentNode.style.height = '32px'
      this.toggleYearData(event.target)
      this.storeInfo = []
      this.countryInfo.forEach(x => {
        if (x.date.slice(0, 4) === year) {
          this.storeInfo.push(x)
        }
      })
      let { data: yearData } = await this.$http.post('/get_yearData', { year: year, country: this.country })
      let words = []
      for (var index in yearData.wordsData) {
        words.push(yearData.wordsData[index])
      }
      this.$emit('yearChange', words)
    },
    async search() {
      const searchContent = this.$refs.searchContent.value.trim()
      if (searchContent !== '') {
        this.storeInfo = []
        let title = []
        this.countryInfo.forEach(x => {
          if (x.title.indexOf(searchContent) !== -1) {
            this.storeInfo.push(x)
            title.push(x.title)
          }
        })
        let { data: searchData } = await this.$http.post('/get_searchWords', { searchData: title })
        this.$refs.searchContent.value = ''
        this.$emit('searchKeyWord', searchData.data)
      }
    }
  },
  computed: {
    pageLength() {
      return Math.ceil(this.storeInfo.length / 20)
    }
  },
  watch: {
    country: {
      handler() {
        this.storeInfo = this.countryInfo
        this.yearsInit()
        this.$nextTick(() => {
          this.toggleYearData(this.$refs.all)
        })
      }
    },
    //watch很重要。data（）函数只是在初始化的时候会运行一次。所以总是空。而我们异步过来的数据，需要watch他 才能得到。
    countryInfo: {
      handler(newVal, oldVal) {
        this.storeInfo = newVal
        this.yearsInit()
      }
    },
    contentStart: {
      handler() {
        this.InfoInit()
      }
    },
    contentEnd: {
      handler() {
        this.InfoInit()
      }
    },
    storeInfo: {
      handler() {
        this.InfoInit()
        this.pageInit()
      }
    }
  }
}
</script>

<style lang="less" scoped>
#Info {
  position: absolute;
  top: 15px;
  left: 1%;
  padding: 10px;
  height: 650px;
  width: 48%;
  box-shadow: 5px 5px 7px rgb(58 55 55);
  border-radius: 5px;
  background-color: #17102a;
}

#idSearch {
  width: 170px;
  border-radius: 24px;
  padding: 0 10px;
}

#Search {
  border-radius: 30px;
  cursor: pointer;
}

#category {
  position: absolute;
  left: 0;
  top: 10px;
  width: 100%;
  height: 50px;
}

table {
  position: absolute;
  top: 50px;
  width: 100%;
}

tr {
  border-bottom: 1px solid #585656;
}

#Year {
  position: absolute;
  right: 290px;
  top: -1.5px;
  width: 110px;
  height: 32px;
  overflow: hidden;
  border: 1px solid black;
  background-color: white;
  border-radius: 5px;
  z-index: 2;
}

.year {
  margin: 1px 2px;
  height: 30px;
  color: #9b9797;
  background-color: #0f0f0f;
  text-align: center;
  border-radius: 5px;
  font: normal 20px/30px '宋体';
  cursor: pointer;
}
.year:hover {
  background-color: #2f2e2e;
}

.list1 {
  width: 8.5%;
  height: 20px;
  text-align: center;
  color: rgba(255, 255, 255, 0.75);
}

.list2 {
  padding: 0 20px;
  width: 91.5%;
  height: 20px;
  text-align: center;
}

.link {
  text-decoration: none;
  color: rgba(255, 255, 255, 0.75);
}

.active {
  position: absolute;
  top: 0;
  width: 106px;
  height: 30px;
  margin: 1px 2px;
}

#pagenumber {
  position: absolute;
  bottom: 10px;
  left: 275px;
}

#page {
  color: rgba(255, 255, 255, 0.75);
}

#previous,
#next {
  border-radius: 30px;
  cursor: pointer;
}
</style>