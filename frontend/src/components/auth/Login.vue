<!--ПОЛНОСТЬЮ РАБОЧАЯ СТРАНИЦА-->
<template>
    <v-content>
        <v-container fluid fill-height>
            <v-layout align-center justify-center>
                <v-flex xs12 sm12 md6>
                    <v-card
                            class="elevation-12">
                        <v-toolbar
                                dark color="primary lighten-1">
                            <v-toolbar-title>Вход</v-toolbar-title>
                        </v-toolbar>
                        <v-card-text>
                            <v-form
                                    v-model="valid"
                                    ref="form"
                                    lazy-validation>
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
                                        counter
                                        v-model="password"
                                        :rules="passwordRules"
                                ></v-text-field>
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                                    @click="loginUser"
                                    color="secondary"
                                    :disabled="!valid"
                            >Войти
                            </v-btn>
                        </v-card-actions>
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
                valid: false,
                emailRules: [
                    v => !!v || 'Введите Ваш e-mail',
                    v => /.+@.+/.test(v) || 'E-mail должен быть реальным'
                ],
                passwordRules: [
                    v => !!v || 'Введите пароль',
                    v => (v && v.length >= 4) || 'Пароль должен состоять не менее чем из 6 символов'
                ]
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
        }
    }
</script>
