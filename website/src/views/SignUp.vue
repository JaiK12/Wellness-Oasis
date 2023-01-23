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
            toast("valid email")
        } else {    
            addUser(name.value, email.value, password.value)
        }    
    }
</script>

<template>
    <div id="form" class="mt-10 mx-10">
        <input v-model="name" placeholder="enter name" class="border border-gray p-3 block outline-none mb-2 text-center">
        <input v-model="email" placeholder="enter email" class="border border-gray p-3 block outline-none mb-2 text-center">
        <input v-model="password" placeholder="enter password" class="border border-gray p-3 block outline-none mb-2 text-center">

        <button @click="submit()" class="mx-16 bg-green-800 p-3 mt-3 text-white rounded-full pr-5 pl-5">Submit</button>
    </div>    
</template>
