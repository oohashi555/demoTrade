<script setup>
import {ref} from 'vue'
import axios from 'axios'
import {useRouter}  from 'vue-router'
import { onMounted } from 'vue'
import UserRegistModal from './UserRegistModal'
import ConfirmDialog from './ConfirmDialog.vue'

const userList = ref([])
const router = useRouter()
const showUserModal = ref(false)
const showConfirm = ref(false)
const selectUserId = ref()
const userModal = ref(null)
const newUser = ref(true)
const errMsg = ref()

function registUser(user){
	const path = 'http://localhost:5000/api/user/regist'
	axios.post(path, user)
		.then(response => {
			userList.value = response.data
			errMsg.value = ''
		})
		.catch(error => {
			errMsg.value = '登録に失敗しました'
			console.log(error)
		})
	showUserModal.value = false
}

function updateUser(user){
	const path = 'http://localhost:5000/api/user/update'
	axios.post(path, user)
		.then(response => {
			userList.value = response.data
			errMsg.value = ''
		})
		.catch(error => {
			errMsg.value = '更新に失敗しました'
			console.log(error)
		})
	showUserModal.value = false
}

function deleteUser(){
	const path = 'http://localhost:5000/api/user/delete'
	axios.post(path, {user_id:selectUserId.value})
		.then(response => {
			userList.value = response.data
			errMsg.value = ''
		})
		.catch(error => {
			errMsg.value = '削除に失敗しました'
			console.log(error)
		})
	showConfirm.value = false
}

function clickAdd(){
	userModal.value.setUserInfo('', '')
	newUser.value = true
	showUserModal.value = true
}

function clickUpdate(userId, userName){
	userModal.value.setUserInfo(userId, userName)
	newUser.value = false
	showUserModal.value = true
}

function clickDelete(userId){
	selectUserId.value = userId
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
			errMsg.value = 'データ取得に失敗しました'
			console.log(error)
		})
	userModal.value
})
</script>
<template>
	<div class="container" style="max-width: 500px">
		<h2 class="mt-3">ユーザ一覧</h2>
		<p v-if="errMsg != ''" class="text-danger">{{errMsg}}</p>
		<div class="table-responsive small">
			<table class="table table-striped table-sm">
				<thead>
					<tr>
						<th scope="col">ID</th>
						<th scope="col">名前</th>
						<th scope="col">削除</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="user in userList" :key="user.id">
						<td class="h5">{{ user[0] }}</td>
						<td><a href="#" v-on:click.stop.prevent="clickUpdate(user[0], user[1])" class="icon-link h5">{{ user[1] }}</a></td>
						<td><button @click="clickDelete(user[0])" class="btn btn-primary">削除</button></td>
					</tr>
				</tbody>
			</table>
		</div>
		<div class="form-group text-right">
			<button id="show-modal" @click="clickAdd" class="btn btn-primary">追加</button>
		</div>
		<div class="form-group text-right">
			<button @click="goBack" class="btn btn-primary">戻る</button>
		</div>
		<Teleport to="body">
			<UserRegistModal :show="showUserModal" :newUser="newUser" @close="showUserModal = false" @regist="registUser" @update="updateUser" ref="userModal"/>
		</Teleport>
		<Teleport to="body">
			<ConfirmDialog msg="削除します。よろしいですか？" yes="はい" no="いいえ" :show="showConfirm" @ok="deleteUser" @no="showConfirm = false"/>
		</Teleport>
	</div>
</template>
