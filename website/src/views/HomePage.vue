<script setup lang="ts">
  import { RouterLink, RouterView } from 'vue-router'
  import { useSigned } from '@/stores/signedIn'
	import supabase from '@/config/supabaseClient'
	import { ref, onMounted } from 'vue'

  const store = useSigned()
	const data = ref()
	const loading = ref(true)

	const getName = async () => {
		const { data, error } = await supabase
			//get data from the table UserData
			.from("UserData")
			//select all columns
			.select()
			//select row whose rownumber / id == rowNumber + 1
			.eq("id", store.rowNumber + 1)
			//single that record
			.single()

		//if no error
		if (data) {
			return data
		}
	}

	// when site is loaded
	// WARNING: do not remove async part
	onMounted(async () => {
		data.value = await getName()
		loading.value = false
	})

</script>

<template>
  <main>
		<div v-if="!store.signedIn">
			
		</div>

		<h1 v-if="loading && store.signedIn" class='text-center text-5xl mt-10'>loading...</h1>
		<div v-if="!loading && store.signedIn" id="user-card" class="bg-green-700 text-white pb-10 pt-2 mt-10 w-1/2 relative left-80 rounded-lg shadow-2xl">
  		<h1 class='text-5xl mt-11 text-center'>Hi!, {{ data.name }}</h1>
  		<h1 v-if="data.disease !== null" class='text-center text-5xl mt-11'>You have {{ data.disease }}</h1>
			
			<div id="unregistered" class="text-center mt-20 bg-green-700 w-32 text-white p-3 rounded-md relative left-10" v-else>
					<button>
						<RouterLink to="/diagnose" >Diagnose</RouterLink>
					</button>
			</div>
		</div>
  </main>
</template>
