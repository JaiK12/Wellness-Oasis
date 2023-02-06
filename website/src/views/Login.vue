<script setup lang="ts">
    import { ref } from 'vue'
    import supabase from '@/config/supabaseClient';
    import { useToast } from 'vue-toastification';
    import { useSigned } from '@/stores/signedIn';

    const email = ref("");
    const toast = useToast()
    const signedIn = useSigned()


    console.log(signedIn.rowNumber)
    const getRowNumber = async () => {
		// check if given email exists in databse
        const { data, error } = await supabase
            .from("UserData")
            .select()

        if(data) { 
            data.map((user, index) => {
                console.log(user.email)
                if (user.email === email.value) {
                    signedIn.$patch({ rowNumber: index})
                }
            })
        }
        if(error) { 
            console.log(error) 
        }    
    }

    const getEmail = async () => {
		// check if given email exists in databse
        const { data, error } = await supabase
            .from("UserData")
            .select()
            .eq("email", email.value)
            .single()

        if(data) { 
            console.log("signed in")
            signedIn.$patch({ userName: email.value, signedIn: true})
        }
        if(error) { 
            console.log("create account") 
        }    
    }

    const submit =() => {
        if (email.value.trim().length < 1){
            toast("fill all fields")
        } else if (!email.value.toLowerCase().match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)) {
            toast("enter valid email")
        } else {
            getEmail()
            getRowNumber()
						toast("logged in")
        }    
    }
</script>

<template>
  <div id="form" class="bg-gray-200 p-6 rounded-md border border-gray-300 shadow-2xl">
    <input v-model="email" placeholder="enter email" class="border border-gray p-3 block outline-none mb-5 text-center shadow-inner border border-gray-300 rounded-3xl">
    <button @click="submit()" class="mx-16 bg-green-800 p-3 mt-3 text-white rounded-full pr-5 pl-5 shadow-2xl border border-gray-300">Submit</button>
    </div>
</template>
