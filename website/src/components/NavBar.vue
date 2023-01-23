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
        routeName: 'About',
        routeUrl: '/about'
    }
]
</script>

<template>
    <nav>
        <div v-for="element in NavElements" class="links">
            <RouterLink :to="element.routeUrl" style="color: darkslategrey; text-decoration: none; margin-right: 0.5em; font-family: Inter">{{ element.routeName }}</RouterLink> 
        </div>
        <div class="register">
            <a href="/signUp">Sign Up</a>
            <a href="/login">Login</a>
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

nav > .register{
    position: relative;
    left: 75%;
    margin-top: 1em;
}

nav > .register > a{
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
