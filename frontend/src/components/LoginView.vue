<script setup>
import {ref} from 'vue'
import axios from 'axios'
import {useRouter}  from 'vue-router'

const msg = ref('')
const router = useRouter()

function sayHello(){
	const path = 'http://localhost:5000/api/hello/e'
	axios.get(path)
		.then(response => {
		msg.value = response.data.msg
	})
	.catch(error => {
		console.log(error)
	})
}

function login(){
	router.push('top')
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
			<button @click="login" class="btn btn-primary">ログイン</button><button @click="sayHello"/>
		</div>
	</div>
</template>
