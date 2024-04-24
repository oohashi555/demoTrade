<script setup>
import {ref} from 'vue'
import axios from 'axios'
//import {useRouter}  from 'vue-router'
import { onMounted } from 'vue'
import UserCreateModal from './UserCreateModal'

const userList = ref([])
//const router = useRouter()
const showUserModal = ref(false)

function add(user){
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
	<div class="container-fluid">
		<li v-for="user in userList" :key="user.id">
			{{ user[0] }}{{ user[1] }}
		</li>
		<button id="show-modal" @click="showUserModal = true" class="btn btn-primary">追加</button>
		<Teleport to="body">
			<userCreateModal :show="showUserModal" @close="showUserModal = false" @add="add">
				<template></template>
			</userCreateModal>
		</Teleport>
	</div>
</template>
