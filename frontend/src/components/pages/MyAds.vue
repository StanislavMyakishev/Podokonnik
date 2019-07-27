<template>
    <v-container grid-list-md text-center fluid>
        <v-layout wrap>
            <v-flex xl3 l4 md4 sm6 xs12
                    v-for="ad in ads"
                    :key="ad.id"
            >
                <v-card dark color="primary" :elevation="8">
                    <v-card-title class="justify-center ma-auto">
                        <h1 class="text-xs-center justify-center display-1 text-truncate">
                            {{ad.name}}
                        </h1>
                    </v-card-title>
                    <v-card-text class="">
                        <h1 class="text-xs-center justify-center  pointer text-truncate ma-auto" > {{ad.descr}}</h1>
                        <h2 class="text-xs-center justify-center text-truncate my-2"> {{ad.price}} </h2>
                        <h3 class="text-xs-center justify-center text-truncate ma-auto"> {{ad.date}}</h3>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import axios from 'axios'
    const url = 'http://127.0.0.1:8000/api/ads/';

    export default {
        data() {
            return {
                ads: null,
                errors: [],
            };
        },
        mounted() {
            axios
                .get(url)
                .then(response => (this.ads = response.data))
                .catch(e => {this.errors.push(e)})
        },
    }
</script>

<style>

</style>