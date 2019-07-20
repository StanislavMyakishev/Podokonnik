<template>
    <div id="app">
        <v-app class="body">
            <div class="wrapper">
                <app-header></app-header>
                <v-container fluid>
                    <v-layout>
                        <router-view></router-view>
                    </v-layout>
                </v-container>
            </div>
            <app-footer></app-footer>
        </v-app>
    </div>
</template>

<script>
    import Footer from './components/core/Footer'
    import Header from './components/core/Header'

    export default {
        data() {
            return {
            }
        },
        components: {
            appFooter: Footer,
            appHeader: Header,
        },
    }
</script>

<style scoped>

    #app {
        background-color: #FFFFFF;
    }

    .body {
        display: flex;
        flex-direction: column;
    }

    .wrapper {
        flex: 1 0 auto;
    }

</style>