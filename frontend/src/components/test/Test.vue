<!--<template>
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
!-->
<template>
    <div>
        <button type=”button” name=”button” @click='getAds'>get ads</button>
        <table>
            <th>name</th>
            <th>descr</th>
            <th>price</th>
            <tbody>
            <tr v-for="elem in ads" :key="elem.key">
                <td>{{elem.name}}</td>
                <td>{{elem.descr}}</td>
                <td>{{elem.price}}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>


<script>
 /*   import axios from 'axios'
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
                // .catch(e => {this.errors.push(e)})
        },
        // filters: {
        //     parseDate(date) {
        //         return date.replace(/(\d+)-(\d+)-(\d+)T(\d+):(\d+).+/, '$1-$2-$3 $4:$5')
        //     }
        // },
    }*/
 import axios from 'axios'
export default {
    data () {
        return {
            ads: [],
            errors: []
        }
    },
    methods: {
        getAds() {
            axios.get('http://0.0.0.0:8000/api/ads/')
                .then(res => this.ads=res.data)
        }
    }
}
</script>