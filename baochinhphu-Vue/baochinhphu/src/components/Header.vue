<template>
  <div ref="nav" id="navigation">
    <div id="logo">夷风</div>
    <div id="countries">
      <div id="yuenan" class="country" @click="changeCountry">
        <div id="target"></div>越南
      </div>
      <div id="pakistan" class="country" @click="changeCountry">
        <div></div>巴基斯坦
      </div>
      <div id="yindu" class="country" @click="changeCountry">
        <div></div>印度
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    changeCountry(event) {
      const countries = event.target.parentNode.children
      for (var i = 0; i < countries.length; i++) {
        if (countries[i] !== event.target) {
          countries[i].children[0].id = ''
        }
      }
      event.target.children[0].id = 'target'
      this.$emit('countryChange', event.target.id)
    },
    navigatioin() {
      const scrollHeight = 0
      window.addEventListener('scroll', () => {
        var scrollPos
        if (window.pageYOffset) {
          //IE
          scrollPos = window.pageYOffset
        } else if (document.compatMode && document.compatMode != 'BackCompat') {
          //谷歌
          scrollPos = document.documentElement.scrollTop
        } else if (document.body) {
          //火狐
          scrollPos = document.body.scrollTop
        }
        if (scrollPos > scrollHeight) {
          this.$refs.nav.style.position = 'fixed'
        } else {
          this.$refs.nav.style.position = 'absolute'
        }
      })
    }
  },
  mounted() {
    this.navigatioin()
  }
}
</script>

<style lang="less" scoped>
#navigation {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 48px;
  background: black;
  color: rgb(130 131 225);
  z-index: 3;
  box-shadow: 0 2px 7px #0a090a;
}

#logo {
  position: absolute;
  left: 24px;
  height: 48px;
  width: 80px;
  font: bold 40px/48px cursive;
}

#countries {
  position: absolute;
  height: 100%;
  left: 40%;
  width: 30%;
  overflow: hidden;
}

.country {
  float: left;
  width: 100px;
  height: 48px;
  font: normal 14px/48px '';
  line-height: 48px;
  text-align: center;
  cursor: pointer;
}

.country:hover {
  background-color: rgba(32, 31, 32, 0.6);
}

#target {
  position: absolute;
  width: 100px;
  height: 5px;
  background-color: orangered;
  border-radius: 5px;
}
</style>