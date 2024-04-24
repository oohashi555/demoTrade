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
	<div class="container-fluid">
		<div class="form-group">
			<input type="text" name="userId" class="form-control">
		</div>
		<div class="form-group">
			<input type="text" name="passWord" class="form-control">
		</div>
		<div class="form-group">
			<button @click="login" class="btn btn-primary">ログイン</button>
		</div>
		<div class="form-group">
			<button @click="userList" class="btn btn-primary">ユーザ管理</button>
		</div>
	</div>
</template>
