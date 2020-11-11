var app = new Vue({
  el: '#app',
  data: {
    big: true,
  },
  mounted:function(){
        this.checkScreenWidth()
  },
  methods:{
    checkScreenWidth:function(){
      let width = screen.width;
      if (width<641){
        this.big = false
      }
      console.log(this.big)
    }
  },
})
