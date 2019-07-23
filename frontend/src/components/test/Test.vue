<template>
    <v-app>
        <v-layout justify-center>
            <v-flex xs12 sm8>
                <v-card
                        v-for="ad in ads"
                        :key="ad.name"
                        min-width="540"
                >
                    <v-card-title>Order title</v-card-title>
                    <v-card-text>{{ad.name}}</v-card-text>
                    <v-card-actions>
                        <v-btn text>Click</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-app>
</template>
<script>
    //import axios from 'axios'

    export default {
        data() {
            return {
                ads: [{name: 'Gavno tupogo govno govna'}],
                src: 'https://picjumbo.com/wp-content/uploads/modern-desktop-setup-2210x1473.jpg'
            }
        },
        // async mounted() {
        //     await this.showOrders();
        // },
        // methods: {
        //     async showOrders() {
        //         axios
        //             .get('http://127.0.0.1:8000/api/orders/')
        //             .then(response => (this.info = response.data.bpi));
        //     },
        // },

        filters: {
            parseDate(date) {
                return date.replace(/(\d+)-(\d+)-(\d+)T(\d+):(\d+).+/, '$1-$2-$3 $4:$5')
            }
        },
    }

</script>