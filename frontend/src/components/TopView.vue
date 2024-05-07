<script setup>
import {ref} from 'vue'
import axios from 'axios'
import { onMounted } from 'vue'
import {useRouter}  from 'vue-router'
import {createCandleChart, updateChart} from './candleStick'
import { store } from './store.js'

const router = useRouter()
const ctx = ref(null)
const errMsg = ref()
const data = ref(null)
const selectEl = ref()
const indexOptions = ref([
	{text: '日経平均', value: '^N225'},
	{text: 'ダウ', value: '^DJI'},
	{text: 'SP500', value: '^GSPC'}
])
const selectedIndex = ref()

function getChart(ticker, label, drawChart){
	const path = 'http://localhost:5000/api/getchart'
	axios.post(path, {ticker: ticker})
		.then(response => {
			errMsg.value = ''
			data.value = response.data
			drawChart(data.value, label, ctx.value.getContext('2d'))
		})
		.catch(error => {
			errMsg.value = 'データ取得に失敗しました'
			console.log(error)
		})
}

function changeIndex(){
	getChart(selectedIndex.value, selectEl.value.options[selectEl.value.selectedIndex].label, updateChart)
}

onMounted(() => {
	if(store.userId == ''){
		router.push('/')
	}else{
		selectedIndex.value = indexOptions.value[0].value
		getChart(indexOptions.value[0].value, indexOptions.value[0].text, createCandleChart)
	}
})
</script>
<template>
	<div class="container" style="max-width: 700px">
		<p v-if="errMsg != ''" class="text-danger">{{errMsg}}</p>
		<select v-model="selectedIndex" @change="changeIndex" ref="selectEl">
			<option v-for="option in indexOptions" :value="option.value" :key="option.value">
				{{ option.text }}
			</option>
		</select>
		<canvas id="chart" ref="ctx"></canvas>
	</div>
</template>
