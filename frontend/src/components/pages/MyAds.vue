<template>
    <v-container grid-list-md text-center fluid>
        <v-layout wrap>
            <v-flex xl3 l4 md4 sm6 xs12
                    v-for="(ad, index) in ads"
                    :key="ad.id">
                <v-card dark color="primary" :elevation="8">
                    <v-card-actions class="justify-end">
                        <v-btn
                                @click="pushIndex(index)"
                                class="mx-2"
                                fab dark small color="accent">
                            <v-icon dark>close</v-icon>
                        </v-btn>
                    </v-card-actions>
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
            <v-dialog
                    v-model="showDelete"
                    max-width="600">
                <v-card>
                    <v-card-title class="text-xs-center display-1 font-weight-regular">Уверены, что хотите удалить объявление?</v-card-title>
                    <v-card-text class="text-xs-center headline">
                        После удаления объявление перестанет быть доступным другим пользователям, если что.
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                                color="accent lighten-3"
                                text
                                @click="showDelete = false">
                            Отмена
                        </v-btn>
                        <v-btn
                                color="error"
                                text
                                @click="deleteAd()">
                            Удалить
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-layout>
    </v-container>
</template>

<script>
    import axios from 'axios'
    const url = 'http://127.0.0.1:8000/api/ads/';

    export default {
        data() {
            return {
                showDelete: false,
                ads: [],
                id: NaN,
                errors: [],
            };
        },
        mounted() {
            axios
                .get(url)
                .then(response => (this.ads = response.data))
                .catch(e => {this.errors.push(e)})
        },
        methods: {
            pushIndex(index){
                this.id = index;
                this.showDelete = true;
            },
            deleteAd(index = this.id + 1) {
                // eslint-disable-next-line no-console
                console.log(index);
                axios.delete(url + index + '/')
                    .then(() => (this.ads.slice(index, 1)))
                    .catch(e => {this.errors.push(e)});
                this.showDelete = false;
            }
        }
    }
</script>

<style>

</style>