<script setup lang="ts">
	import { ref } from 'vue'
  import { RouterLink, RouterView } from 'vue-router'

	const selected = ref('') 
</script>

<template>
	<div>
		<h1 class="mx-10 text-3xl mt-5">What do you want to diagnose?</h1>
		<select v-model="selected" class='p-3 mx-10 mt-4 w-48 bg-transparent border border-slate-500'>
			<option>Obesity</option>
		</select>

		<button v-if="selected.length > 1" class="bg-green-600 text-white p-3 -mx-8">
			<RouterLink :to="'/diagnose-' + selected.toLowerCase()">Go</RouterLink>
		</button>
	</div>
</template>
