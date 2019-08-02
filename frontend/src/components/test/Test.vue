<template>
    <div id="app">
        <v-app light>
            <v-container fluid grid-list-md>
                <v-layout low wrap>
                    <v-flex xs12>
                        <v-card
                                v-for="category in {
                                        'id': categories.map((category) => { return(category.id)}),
                                        'name': categories.map((category) => {return(category.name)})}"
                                :key="category.id">
                            <v-card-text>
                                <v-select
                                        :items="category.name"
                                        item-text="name"
                                        item-value="id"
                                        label="Категория"
                                        :rules="selectRules"
                                        required
                                ></v-select>
                            </v-card-text>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-app>
    </div>
</template>

<script>
    import axios from 'axios'
    const adsUrl = 'http://0.0.0.0:8000/api/ads/';

    export default {
        data: () => ({
            valid: true,
            errors: [{id: '', name: ''}],
            name: '',
            descr: '',
            price: '',
            select: null,
            categories: [{id: '', name: ''}],
            names: [],
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
        }),
        created() {
            axios
                .get(adsUrl)
                .then(response => (this.categories = response.data))
                .catch(e => {this.errors.push(e)})
        },
        methods: {
            postPost() {
                if (this.$refs.form.validate()) {
                    let date = new Date();
                    const ad = {
                        "name": this.name,
                        "descr" : this.descr,
                        "price": this.price,
                        "category": this.select,
                        "date": `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`,
                    }
                    axios
                        .post(adsUrl, JSON.stringify(ad), {
                            headers: {
                                'Accept': 'application/json',
                                'Content-Type': 'application/json',
                            }
                        })
                        .catch(e => {this.errors.push(e)})
                }
            },
            clear() {
                this.name = '';
                this.descr = '';
                this.select = null;
            },
        }
    }
</script>

<style>
    #app {
        background-color: #FFFFFF;
    }
    @media (min-width: 800px) {
        .content {
            width: 70%;
            margin: auto;
        }
    }

    footer {
        overflow: auto;
    }

    a {
        color: #fff;
    }
</style>