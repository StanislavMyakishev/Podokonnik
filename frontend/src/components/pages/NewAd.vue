<template>
    <v-content>
        <v-container fluid fill-height>
            <v-layout align-center justify-center>
                <v-flex>
                    <v-card
                            class="elevation-8">
                        <v-toolbar
                                dark color="primary lighten-1">
                            <v-toolbar-title>Новое объявление</v-toolbar-title>
                        </v-toolbar>
                        <v-card-text>
                            <v-form
                                    v-model="valid"
                                    ref="form"
                                    lazy-validation>
                                <v-text-field
                                        v-model="name"
                                        label="Название объявления"
                                        :rules="nameRules"
                                        required
                                ></v-text-field>
                                <v-textarea
                                        v-model="descr"
                                        label="Описание"
                                        :rules="descrRules"
                                        required
                                ></v-textarea>
                                <v-text-field
                                        v-model="price"
                                        label="Цена"
                                        :rules="priceRules"
                                        required
                                ></v-text-field>
                                <v-select
                                        :items="categories"
                                        v-model="select"
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
                                    @click="postPost"
                                    :disabled="!valid"
                                    class="secondary"
                            >Разместить</v-btn>
                            <v-btn
                                    @click="clear"
                                    class="error"
                            >Стереть</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>


<script>
    export default {
        data: () => ({
            valid: true,
            name: '',
            descr: '',
            price: '',
            select: null,
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
        mounted() {
            this.$store.dispatch('GET_CATEGORIES');
        },
        computed: {
            categories() {
                return this.$store.getters.CATEGORIES;
            },
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
                    };
                    this.$store.dispatch('POST_ADS', ad);
                    this.$router.push('/myads')
                }
            },
            clear() {
                this.name = '';
                this.descr = '';
                this.select = null;
                this.checkbox = false;
            },
        }
    }
</script>