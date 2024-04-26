<script setup>
//import {ref} from 'vue'
//import axios from 'axios'
import {useRouter}  from 'vue-router'

const router = useRouter()

function login(){
	router.push('top')
}

function userList(){
	router.push('userList')
}

</script>
<template>
	<div class="container" style="max-width: 300px">
		<h1 class="mt-3">ログイン</h1>
			<div class="form-group">
				<label for="userId">ユーザID</label>
				<input type="text" id="userId" class="form-control">
			</div>
			<div class="form-group">
				<label for="password">パスワード</label>
				<input type="password" id="password" class="form-control">
			</div>
			<div class="form-group">
				<button @click="login" class="btn btn-primary">ログイン</button>
			</div>
			<div class="form-group">
				<button @click="userList" class="btn btn-primary">ユーザ管理</button>
			</div>
	</div>
</template>
