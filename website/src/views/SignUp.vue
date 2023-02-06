<script setup lang="ts">
    import { ref } from 'vue'
    import supabase from '../config/supabaseClient'
    import { useToast } from "vue-toastification";

    const toast = useToast()

    let name = ref('');
    let email = ref('');
    let password = ref('');
    let dataUsers = ref(['']);

		let emailRegex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

    const addUser = async (name: String, email: String, password: String) => {
        const { data, error } = await supabase
            .from('UserData')
            .insert([{ email, name, password }])
            .select()

        if (data)
            dataUsers.value = data 

        if (error)
            console.log(error)  
    }

    function submit(){
        if (name.value.trim().length < 1|| email.value.trim().length < 1 || password.value.trim().length < 1 ) {
            toast("fill all fields")
        } else if (!email.value.toLowerCase().match(emailRegex)) {
            toast("enter valid email")
        } else {    
            addUser(name.value, email.value, password.value)
						toast("signed up!")
        }    
    }
</script>

<template>
    <div id="form" class="bg-gray-200 p-6 rounded-md border border-gray-300 shadow-2xl">
        <input v-model="name" placeholder="enter name" class="border border-gray p-3 block outline-none mb-5 text-center shadow-inner border border-gray-300 rounded-3xl">
        <input v-model="email" placeholder="enter email" class="border border-gray p-3 block outline-none mb-5 text-center shadow-inner border border-gray-300 rounded-3xl">
        <input v-model="password" placeholder="enter password" class="border border-gray p-3 block outline-none mb-5 text-center shadow-inner border border-gray-300 rounded-3xl">

        <button @click="submit()" class="mx-16 bg-green-800 p-3 mt-3 text-white rounded-full pr-5 pl-5 shadow-2xl border border-gray-300">Submit</button>
    </div>    
</template>

<style>
#form{
	position: relative;
	margin-top: 10vh;
	margin-left: 42.5%;
	width: 20%;
}
</style>
