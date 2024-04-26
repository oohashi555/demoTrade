<script setup>
import {ref} from 'vue'
import axios from 'axios'
import {useRouter}  from 'vue-router'
import { onMounted } from 'vue'
import UserCreateModal from './UserCreateModal'
import ConfirmDialog from './ConfirmDialog.vue'

const userList = ref([])
const router = useRouter()
const showUserModal = ref(false)
const showConfirm = ref(false)
const selectUserId = ref()

function registUser(user){
	const path = 'http://localhost:5000/api/user/regist'
	axios.post(path, user)
		.then(response => {
			userList.value = response.data
		})
		.catch(error => {
			console.log(error)
		})
	showUserModal.value = false
}

function deleteUser(){
	const path = 'http://localhost:5000/api/user/delete'
	axios.post(path, {id:selectUserId.value})
		.then(response => {
			userList.value = response.data
		})
		.catch(error => {
			console.log(error)
		})
	showConfirm.value = false
}

function clickDelete(id){
	selectUserId.value = id
	showConfirm.value = true
}

function goBack(){
	router.push('/')
}

onMounted(() => {
	const path = 'http://localhost:5000/api/user/list'
	axios.get(path)
		.then(response => {
			userList.value = response.data
		})
		.catch(error => {
			console.log(error)
		})
})
</script>
<template>
	<div class="container">
		<li v-for="user in userList" :key="user.id">
			ユーザID：{{ user[0] }}
			ユーザ名：{{ user[1] }}
			<button @click="clickDelete(user[0])" class="btn btn-primary">削除</button>
		</li>
		<button id="show-modal" @click="showUserModal = true" class="btn btn-primary">追加</button>
		<button @click="goBack" class="btn btn-primary">戻る</button>
		<Teleport to="body">
			<UserCreateModal :show="showUserModal" @close="showUserModal = false" @regist="registUser"/>
		</Teleport>
		<Teleport to="body">
			<ConfirmDialog msg="削除します。よろしいですか？" yes="はい" no="いいえ" :show="showConfirm" @ok="deleteUser" @no="showConfirm = false"/>
		</Teleport>
	</div>
</template>
