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
            toast("valid email")
        } else {
            getEmail()
            getRowNumber()
						toast("logged in")
        }    
    }
</script>

<template>
    <div id="form" class="relative left-[40%] translateX-[-50%] mt-10">
        <input v-model="email" placeholder="enter email" class="border border-gray p-3 block outline-none mb-2 text-center">

        <button @click="submit()" class="relative left-[4.5%] bg-green-800 p-3 mt-3 text-slate-100 rounded-full pr-5 pl-5">Submit</button>
    </div>    
</template>
