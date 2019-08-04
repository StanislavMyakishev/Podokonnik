<template>
    <v-container grid-list-md text-center fluid>
        <v-layout wrap>
            <v-flex xl3 l4 md4 sm6 xs12
                    v-for="(ad) in ads"
                    :key="ad.id">
                <v-card
                        dark color="primary"
                        :elevation="8">
                    <v-card-actions class="justify-end">
                        <v-btn
                                @click="pushIndexEdit(ad.id)"
                                class="mx-2"
                                fab dark small color="warning">
                            <v-icon vdark>edit</v-icon>
                        </v-btn>
                        <v-btn
                                @click="pushIndexDelete(ad.id)"
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
                        <h1 class="text-xs-center justify-center  pointer text-truncate ma-auto"> {{ad.descr}}</h1>
                        <h2 class="text-xs-center justify-center text-truncate my-2"> {{ad.price}} </h2>
                        <h3 class="text-xs-center justify-center text-truncate ma-auto"> {{ad.date}}</h3>
                    </v-card-text>
                </v-card>
            </v-flex>
            <v-dialog
                    v-model="showDelete"
                    max-width="600">
                <v-card>
                    <v-card-title class="text-xs-center display-1 font-weight-regular">Уверены, что хотите удалить
                        объявление?
                    </v-card-title>
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
            <v-dialog
                    v-model="showEdit"
                    max-width="600">
                <v-card>
                    <v-card-title class="text-xs-center display-1 font-weight-regular">Редактирование объявления
                    </v-card-title>
                    <v-card-text>
                        <v-form
                                v-model="valid"
                                ref="form"
                                :key="renderKey"
                                lazy-validation>
                            <v-text-field
                                    v-model="adName"
                                    label="Название объявления"
                                    :rules="nameRules"
                                    required
                            ></v-text-field>
                            <v-textarea
                                    v-model="adDescr"
                                    label="Описание"
                                    :rules="descrRules"
                                    required
                            ></v-textarea>
                            <v-text-field
                                    v-model="adPrice"
                                    label="Цена"
                                    :rules="priceRules"
                                    required
                            ></v-text-field>
                            <v-select
                                    :items="categories"
                                    v-model="adCategory"
                                    item-text="name"
                                    item-value="id"
                                    label="Категория"
                                    :rules="selectRules"
                                    required
                            ></v-select>
                        </v-form>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                                color="accent lighten-3"
                                text
                                @click="showEdit = false">
                            Отмена
                        </v-btn>
                        <v-btn
                                :disabled="!valid"
                                @click="patchPost"
                                text
                                class="secondary"
                        >Разместить
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-layout>
    </v-container>
</template>

<script>
    import axios from 'axios'

    const adsUrl = 'http://0.0.0.0:8000/api/ads/';
    const catUrl = 'http://0.0.0.0:8000/api/categories/';

    export default {
        data() {
            return {
                valid: true,
                adName: '',
                adDescr: '',
                adPrice: '',
                adCategory: '',
                categories: null,
                renderKey: 0,
                showDelete: false,
                showEdit: false,
                ad: [],
                ads: [],
                id: NaN,
                interval: null,
                errors: [],
                nameRules: [
                    v => !!v || 'Назовите объявление',
                    v => (v && v.length >= 10) || 'Название объявления должно содержать минимум 10 символов'
                ],
                descrRules: [
                    v => !!v || 'Опишите объявление'
                ],
                priceRules: [
                    v => !!v || 'Введите цену объявления',
                    v => (v && !isNaN(v) && /^\d+$/.test(v))|| 'Цена должна быть целым числом'
                ],
                selectRules: [
                    v => !!v || "Выберите категорию объявления"
                ],
            };
        },
        created() {
            this.interval = setInterval(this.refreshData, 5)
        },
        beforeDestroy() {
            clearInterval(this.interval)
        },
        mounted() {
            axios
                .get(catUrl)
                .then(response => (this.categories = response.data))
                .catch(e => {
                    this.errors.push(e)
                })
        },
        methods: {
            refreshData() {
                axios
                    .get(adsUrl)
                    .then(response => (this.ads = response.data))
                    .catch(e => {
                        this.errors.push(e)
                    })
            },
            pushIndexDelete(index) {
                this.id = index;
                this.showDelete = true;
            },
            pushIndexEdit(index) {
                this.id = index;
                axios
                    .get(adsUrl + this.id)
                    .then(response => (this.ad = response.data))
                    .then(() => this.adName = this.ad.name)
                    .then(() => this.adPrice = this.ad.price)
                    .then(() => this.adDescr = this.ad.descr)
                    .then(() => this.renderKey += 1)
                    .catch(e => {
                        this.errors.push(e)
                    });
                setTimeout(() => this.showEdit = true, 5)
            },
            deleteAd() {
                axios.delete(adsUrl + this.id)
                    .then(() => {
                        this.ads.slice(this.id, 1)
                    })
                    .then(() => {
                        this.showDelete = false
                    })
                    .catch(e => {
                        this.errors.push(e)
                    })
            },
            patchPost() {
                if (this.$refs.form.validate()) {
                    axios
                        .patch(adsUrl + this.id, {
                            'name': this.adName,
                            'descr':  this.adDescr,
                            'price': this.adPrice,
                            'category': this.adCategory,
                    })
                        .catch(e => {this.errors.push(e)})
                }
            },
        },
    }
</script>

<style>

</style>