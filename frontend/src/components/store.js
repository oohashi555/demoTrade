import { reactive } from 'vue'

export const store = reactive({
  userId: '',
  login(id){
    this.userId = id
  },
  logout(){
    this.userId = ''
  }
})