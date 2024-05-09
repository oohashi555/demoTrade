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
const orderErrMsg = ref([])
const data = ref(null)
const selectEl = ref()
const indexOptions = ref([
	{text: '日経平均', value: '^N225'},
	{text: 'ダウ', value: '^DJI'},
	{text: 'SP500', value: '^GSPC'}
])
const selectedIndex = ref()
const selectedOrderIndex = ref()
const buysell = ref('buy')
const lot = ref(0)
const positionList = ref()
const historyList = ref()

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

function getPositionList(){
	const path = 'http://localhost:5000/api/positionlist'
	axios.post(path, {user_id: store.userId})
		.then(response => {
			positionList.value = response.data.position
			historyList.value = response.data.history
		})
		.catch(error => {
			errMsg.value = 'ポジション取得に失敗しました'
			console.log(error)
		})
}

function order(){
	orderErrMsg.value = []
	checklot()
	if(orderErrMsg.value.length == 0){
		const path = 'http://localhost:5000/api/order'
		axios.post(path, {user_id: store.userId, ticker_code: selectedOrderIndex.value, buysell: buysell.value, lot: lot.value})
			.then(response => {
				orderErrMsg.value.push('約定しました')
				positionList.value = response.data
			})
			.catch(error => {
				orderErrMsg.value.push('発注に失敗しました')
				console.log(error)
			})
	}
}

function kessai(positionId, tickerCode){
	orderErrMsg.value = []
	const path = 'http://localhost:5000/api/kessai'
	axios.post(path, {user_id: store.userId, position_id: positionId, ticker_code: tickerCode})
		.then(response => {
			orderErrMsg.value.push('決済しました')
			positionList.value = response.data.position
			historyList.value = response.data.history
		})
		.catch(error => {
			orderErrMsg.value.push('決済に失敗しました')
			console.log(error)
		})
}

function changeIndex(){
	getChart(selectedIndex.value, selectEl.value.options[selectEl.value.selectedIndex].label, updateChart)
}

function checklot(){
  if(lot.value == '' || lot.value == 0){
    orderErrMsg.value.push('取引数量を入力してください')
  }
  if(isNaN(lot.value)){
	orderErrMsg.value.push('取引数量は数値を入力してください')
  }
}

onMounted(() => {
	if(store.userId == ''){
		router.push('/')
	}else{
		selectedIndex.value = indexOptions.value[0].value
		selectedOrderIndex.value = indexOptions.value[0].value
		getPositionList()
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

		<div class="table-responsive small mt-3">
			<p v-for="(error, key) in orderErrMsg" :key="key" class="text-danger">{{error}}</p>
			<table class="table table-striped table-sm">
				<thead>
					<tr>
						<th scope="col">取引銘柄</th>
						<th scope="col">売買</th>
						<th scope="col">取引数量</th>
						<th scope="col"></th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>
							<select v-model="selectedOrderIndex">
								<option v-for="option in indexOptions" :value="option.value" :key="option.value">
									{{ option.text }}
								</option>
							</select>
						</td>
						<td>
							<input type="radio" id="buy" v-model="buysell" value="buy" />
							<label for="buy">買</label>
							<input type="radio" id="sell" v-model="buysell" value="sell" />
							<label for="sell">売</label>
						</td>
						<td>
							<input type="text" class="form-control" v-model="lot">
						</td>
						<td>
							<button @click="order" class="btn btn-primary">注文</button>
						</td>
					</tr>
				</tbody>
			</table>
		</div>

		<div class="table-responsive small mt-3">
			保有ポジション
			<table class="table table-striped table-sm">
				<thead>
					<tr>
						<th scope="col">銘柄</th>
						<th scope="col">売買</th>
						<th scope="col">取得単価</th>
						<th scope="col">ロット</th>
						<th scope="col">決済</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="position in positionList" :key="position.position_id">
						<td class="h5">{{ position[6] }}</td>
						<td class="h5" v-if="position[2] == 'buy'">買</td>
						<td class="h5" v-if="position[2] == 'sell'">売</td>
						<td class="h5">{{ position[3] }}</td>
						<td class="h5">{{ position[5] }}</td>
						<td><button @click="kessai(position[0], position[1])" class="btn btn-primary">決済</button></td>
					</tr>
				</tbody>
			</table>
		</div>
		<div class="table-responsive small mt-3">
			取引履歴
			<table class="table table-striped table-sm">
				<thead>
					<tr>
						<th scope="col">銘柄</th>
						<th scope="col">売買</th>
						<th scope="col">取得単価</th>
						<th scope="col">決済単価</th>
						<th scope="col">ロット</th>
						<th scope="col">評価額</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="history in historyList" :key="history.position_id">
						<td class="h5">{{ history[6] }}</td>
						<td class="h5" v-if="history[2] == 'buy'">買</td>
						<td class="h5" v-if="history[2] == 'sell'">売</td>
						<td class="h5">{{ history[3] }}</td>
						<td class="h5">{{ history[4] }}</td>
						<td class="h5">{{ history[5] }}</td>
						<td class="h5" v-if="history[2] == 'buy'">{{ (history[4] -  history[3]) * history[5]}}円</td>
						<td class="h5" v-if="history[2] == 'sell'">{{ (history[3] -  history[4]) * history[5]}}円</td>
					</tr>
				</tbody>
			</table>
		</div>
</div>
</template>
