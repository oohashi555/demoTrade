<template>
	ログインあb<button @click="sayHello">New random number</button>
	{{ msg }}
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      msg: ''
    }
  },
  methods: {
    sayHello () {
      const path = 'http://localhost:5000/api/hello/e'
      axios.get(path)
        .then(response => {
          this.msg = response.data.msg
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    
  }
}
</script>