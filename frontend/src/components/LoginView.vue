<script setup>
import {ref} from 'vue'
import axios from 'axios'
import {useRouter}  from 'vue-router'
import { store } from './store.js'

const router = useRouter()
const user = ref({user_id:'', password:''})
const errors = ref([])

function login(){
	errors.value = []
	checkUserId()
	checkPassword()
	if(errors.value.length == 0){
		const path = 'http://localhost:5000/api/login'
		axios.post(path, user.value)
			.then(response => {
				if(response.data){
					store.login(user.value.user_id)
					router.push('top')
					resetForm()
				}else{
					errors.value.push('パスワードが間違っています')
				}
			})
			.catch(error => {
				errors.value.push('システムエラー')
				console.log(error)
			})
	}
}

function checkUserId(){
	if(user.value.user_id == ''){
		errors.value.push('ユーザIDを入力してください')
	}
}

function checkPassword(){
	if(user.value.password == ''){
		errors.value.push('パスワードを入力してください')
	}
}

function resetForm(){
	user.value = {user_id:'', name:'', password:''}
}

function userList(){
	router.push('userList')
}

</script>
<template>
	<div class="container" style="max-width: 300px">
		<h1 class="mt-3">ログイン</h1>
		<p v-for="(error, key) in errors" :key="key" class="text-danger">{{error}}</p>
			<div class="form-group">
				<label for="userId">ユーザID</label>
				<input type="text" id="userId" class="form-control" v-model="user.user_id">
			</div>
			<div class="form-group">
				<label for="password">パスワード</label>
				<input type="password" id="password" class="form-control" v-model="user.password">
			</div>
			<div class="form-group">
				<button @click="login" class="btn btn-primary">ログイン</button>
			</div>
			<div class="form-group">
				<button @click="userList" class="btn btn-primary">ユーザ管理</button>
			</div>
	</div>
</template>
