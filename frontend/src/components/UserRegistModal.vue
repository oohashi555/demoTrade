<script setup>
import {ref} from 'vue'

const props = defineProps(['show', 'newUser'])
const emit = defineEmits(['close', 'regist', 'update'])
defineExpose({setUserInfo})

const user = ref({user_id:'', name:'', password:''})
const errors = ref([])

function close(){
  errors.value = []
  emit('close')
  resetForm()
}

function regist(){
  errors.value = []
  checkUserName()
  checkPassword()
  if(errors.value.length == 0){
    emit('regist', user.value)
    resetForm()
  }
}

function update(){
  errors.value = []
  checkUserName()
  checkPassword()
  if(errors.value.length == 0){
    emit('update', user.value)
    resetForm()
  }
}

function setUserInfo(userId, userName){
  user.value.user_id = userId
  user.value.name = userName
}

function resetForm(){
  user.value = {user_id:'', name:'', password:''}
}

function checkUserName(){
  if(user.value.name == ''){
    errors.value.push('ユーザ名を入力してください')
  }
}

function checkPassword(){
  if(user.value.password == ''){
    errors.value.push('パスワードを入力してください')
  }
}

</script>
<template>
    <Transition name="modal">
        <div v-if="show" class="modal-mask">
            <div class="modal-container">
                <div class="modal-body">
                    <p v-for="(error, key) in errors" :key="key" class="text-danger">{{error}}</p>
                    ユーザ名：<input v-model.trim="user.name">
                    パスワード：<input v-model="user.password" type="password">
                </div>
                <div class="modal-footer">
                    <button v-if="newUser" class="modal-default-button" @click="regist">登録</button>
                    <button v-else class="modal-default-button" @click="update">更新</button>
                    <button class="modal-default-button" @click="close">閉じる</button>
                </div>
            </div>
        </div>
    </Transition>
</template>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  transition: opacity 0.3s ease;
}

.modal-container {
  width: 300px;
  margin: auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
