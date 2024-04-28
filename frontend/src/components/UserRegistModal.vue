<script setup>
import {ref} from 'vue'

const props = defineProps(['show', 'newUser'])

const emit = defineEmits(['close', 'regist', 'update'])

defineExpose({setUserInfo})

const user = ref({id:'', name:'', password:''})

function close(){
  emit('close')
  resetForm()
}

function regist(){
  emit('regist', user.value)
  resetForm()
}

function update(){
  emit('update', user.value)
  resetForm()
}

function setUserInfo(id, userName){
  user.value.id = id
  user.value.name = userName
}

function resetForm(){
  user.value = {id:'', name:'', password:''}
}

</script>
<template>
    <Transition name="modal">
        <div v-if="show" class="modal-mask">
            <div class="modal-container">
                <div class="modal-body">
                    ユーザ名：<input v-model="user.name">
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
