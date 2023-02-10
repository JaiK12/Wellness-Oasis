<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
import { useSigned } from '@/stores/signedIn';

const signedIn = useSigned()
// array of routes and its name
const NavElements = [ 
    { 
        routeName: 'Home',
        routeUrl: '/'
    },
    {
        routeName: 'Diagnose',
        routeUrl: '/diagnose'
    },
    {
        routeName: 'About',
        routeUrl: '/about'
    }
]

async function signout() {
  const { error } = await supabase.auth.signOut()
}
</script>

<template>
    <nav>
        <div v-for="element in NavElements" class="links">
            <RouterLink :to="element.routeUrl" style="color: darkslategrey; text-decoration: none; margin-right: 0.5em; font-family: Inter">{{ element.routeName }}</RouterLink> 
        </div>
        <div class="register" v-if="!signedIn.signedIn">
            <a href="/signUp" class="mr-6">Sign Up</a>
            <a href="/login">Login</a>
        </div>
				<div class="login" v-if="signedIn.signedIn">
					<button
						@click="() => { 
											signedIn.signedIn = false; 
											signedIn.userName = ''; 
											signedIn.rowNumber = 0;
											signOut()
										}
										"
					>Log Out</button>
				</div>
    </nav>     
</template>

<style scoped>
nav{
    display: flex;
}

nav > .links{
   display: inline-block;
   text-decoration: none; 
   padding: 1em;
}

nav > .register, .login{
    position: relative;
    left: 65%;
    margin-top: 1em;
}

nav > .register, .login > a, button{
   margin-right: 1em; 
   font-family: Inter;
   background: none;
   color: darkslategrey;
   border: none;
   text-decoration: none;
   cursor: pointer;
   font-size: 0.9em;
}

nav > .register > a:hover{
   text-decoration: underline; 
}
</style>
