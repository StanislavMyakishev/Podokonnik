<template>
    <v-content>
        <v-container
                fluid fill-height>
            <v-layout
                    v-show="!showResetWindow"
                    align-center
                    justify-center>
                <v-flex xs12 sm12 md6>
                    <v-card
                            class="elevation-8">
                        <v-toolbar
                                dark color="primary lighten-1">
                            <v-toolbar-title>Вход</v-toolbar-title>
                        </v-toolbar>
                        <v-card-text>
                            <v-form
                                    v-model="valid"
                                    ref="form"
                                    :lazy-validation="lazy">
                                <v-text-field
                                        prepend-icon="person"
                                        name="email"
                                        label="Email"
                                        type="email"
                                        v-model="email"
                                        :rules="emailRules"
                                ></v-text-field>
                                <v-text-field
                                        prepend-icon="lock"
                                        name="password"
                                        label="Пароль"
                                        type="password"
                                        v-model="password"
                                        :rules="passwordRules"
                                ></v-text-field>
                            </v-form>
                        </v-card-text>
                        <v-card-actions class="justify-center">
                            <v-btn
                                    @click="loginUser"
                                    color="secondary"
                                    :disabled="!valid"
                            >Войти
                            </v-btn>
                        </v-card-actions>
                        <v-layout justify-center>
                            <v-card-actions>
                                <a
                                        class="secondary--text lighten-1"
                                        v-bind:href="register">
                                    Ещё не зарегистрированы?
                                </a>
                            </v-card-actions>
                        </v-layout>
                        <v-layout justify-center>
                            <v-card-actions>
                                <a
                                        v-on:click="passwordReset"
                                        class="secondary--text lighten-1">
                                    Забыли пароль
                                </a>
                            </v-card-actions>
                        </v-layout>
                    </v-card>
                </v-flex>
            </v-layout>
            <v-layout
                    v-show="showResetWindow"
                    align-center
                    justify-center>
                <v-flex xs12 sm12 md6>
                    <v-card
                            class="elevation-8">
                        <v-toolbar
                                dark color="primary lighten-1">
                            <v-toolbar-title>Введите свой e-mail</v-toolbar-title>
                        </v-toolbar>
                        <v-card-text>
                            <v-form
                                    v-model="valid"
                                    ref="form"
                                    :lazy-validation="lazy">
                                <v-text-field
                                        prepend-icon="person"
                                        name="email"
                                        label="Email"
                                        type="email"
                                        v-model="email"
                                        :rules="emailRules"
                                ></v-text-field>
                            </v-form>
                        </v-card-text>
                        <v-card-actions class="justify-center">
                            <v-btn
                                    @click="loginUser"
                                    color="secondary"
                                    :disabled="!valid"
                            >Восстановить пароль
                            </v-btn>
                        </v-card-actions>
                        <v-layout justify-center>
                            <v-card-actions>
                                <a
                                        v-on:click="passwordReset"
                                        class="secondary--text lighten-1">
                                    Назад
                                </a>
                            </v-card-actions>
                        </v-layout>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios'
    const url = 'http://127.0.0.1:8000/api/login/';

    export default {
        data() {
            return {
                email: '',
                password: '',
                register: '/registration',
                showResetWindow: false,
                lazy: true,
                valid: true,
                emailRules: [
                    v => !!v || 'Введите Ваш e-mail',
                    v => /.+@.+/.test(v) || 'E-mail должен быть реальным'
                ],
                passwordRules: [
                    v => !!v || 'Введите пароль',
                    v => (v && v.length >= 4) || 'Пароль должен состоять не менее чем из 6 символов'
                ],
            }
        },
        methods: {
            loginUser() {
                if (this.$refs.form.validate()) {
                    const user = {
                        "email": this.email,
                        "password" : this.password
                    }
                    axios
                        .post(url, JSON.stringify(user), {
                            headers: {
                                'Accept': 'application/json',
                                'Content-Type': 'application/json',
                            }
                        })
                        .catch(e => {this.errors.push(e)})
                }
            },
            passwordReset(){
                this.showResetWindow = !this.showResetWindow
            },
        }
    }
</script>

<style>
    a {
        text-decoration: underline;
    }
</style>
