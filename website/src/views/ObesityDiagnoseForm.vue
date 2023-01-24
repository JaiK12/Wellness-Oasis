<script setup lang="ts">
	import { ref } from 'vue'
	import supabase from '@/config/supabaseClient.ts'
	import { useSigned } from '@/stores/signedIn.ts' 

	const store = useSigned()
	
	const height = ref('')
	const weight = ref('')
	const obesity = ref(false)

	async function submit(){
		height.value = parseInt(height.value) * 0.3045
		const bmi = weight.value / ( height.value ^ 2 );
	
		if(bmi > 30) {
			console.log("you are obese")
			obesity.value = true

			const { data, error } = await supabase
				.from("UserData")
				.update({ disease: "obesity" })
				.eq("id", store.rowNumber + 1)

			
			console.log(data)	
		}
	}
</script>

<template>
	<div>
		<input type="text" placeholder="enter height (feet)" v-model="height">	
		<input type="text" placeholder="enter weight (kg)" v-model="weight">	
		<button @click="submit">submit</button>
		
		<h1 v-if="obesity">Obese</h1>
	</div>
</template>
