<script setup>
import {ref} from 'vue'
import axios from 'axios'
import { onMounted } from 'vue'
import {createCandleChart} from './candleStick'

const ctx = ref(null)
const errMsg = ref()
const data = ref(null)

function getChart(){
	const path = 'http://localhost:5000/api/getchart'
	axios.post(path, {})
		.then(response => {
			data.value = response.data
			createCandleChart(ctx.value.getContext('2d'), data.value)
			errMsg.value = ''
		})
		.catch(error => {
			errMsg.value = 'データ取得に失敗しました'
			console.log(error)
		})
}

onMounted(() => {
	getChart()	
})
</script>
<template>
	<p v-if="errMsg != ''" class="text-danger">{{errMsg}}</p>
	<canvas id="chart" ref="ctx"></canvas>
</template>
