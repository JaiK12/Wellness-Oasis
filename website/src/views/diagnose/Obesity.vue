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
  <div id="form" class="bg-gray-200 p-6 rounded-md border border-gray-300 shadow-2xl">
		<input type="text" placeholder="enter height (feet)" v-model="height" class="border border-gray p-3 block outline-none mb-5 text-center shadow-inner border border-gray-300 rounded-3xl">	
		<input type="text" placeholder="enter weight (kg)" v-model="weight" class="border border-gray p-3 block outline-none mb-5 text-center shadow-inner border border-gray-300 rounded-3xl">	
		<button @click="submit" class="mx-16 bg-green-800 p-3 mt-3 text-white rounded-full pr-5 pl-5 shadow-2xl border border-gray-300">submit</button>
	</div>
</template>
