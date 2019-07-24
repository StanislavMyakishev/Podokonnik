<template>
    <v-app>
        <v-layout justify-center>
            <v-flex xs12 sm8>
                <v-card
                        min-width="500"
                        min-height="500"
                >
                    <v-card-text>{{ads}}</v-card-text>
                    <ul v-if="errors && errors.length">
                        <li v-for="error of errors" :key="error.message">
                            {{error.message}}
                        </li>
                    </ul>
                </v-card>
            </v-flex>
        </v-layout>
    </v-app>
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
