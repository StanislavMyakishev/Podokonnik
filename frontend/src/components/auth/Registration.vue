<template>
    <v-content>
        <v-container fluid fill-height>
            <v-layout
                    v-show="!showConfirmPassword"
                    align-center
                    justify-center>
                <v-flex xs12 sm8 md8>
                    <v-card
                            class="elevation-10">
                        <v-toolbar
                            dark color="primary lighten-1">
                        <v-toolbar-title>Регистрация</v-toolbar-title>
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
                                        counter
                                        v-model="password"
                                        :rules="passwordRules"
                                ></v-text-field>
                                <v-text-field
                                        prepend-icon="lock"
                                        name="confirm-password"
                                        label="Подтвердитe пароль"
                                        type="password"
                                        counter
                                        v-model="confirmPassword"
                                        :rules="confirmPasswordRules"
                                ></v-text-field>
                                <v-checkbox
                                        color="secondary"
                                        v-model="checkbox"
                                        label="Я согласен с условиями Пользовательского соглашения"
                                        :rules="checkboxRules"
                                        required
                                ></v-checkbox>
                            </v-form>
                        </v-card-text>
                        <v-card-actions class="justify-center">
                            <v-btn
                                    color="secondary"
                                    @click="createUser"
                                    :disabled="!valid"
                            >Создать аккаунт
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-flex>
            </v-layout>
            <v-layout
                    v-show="showConfirmPassword"
                    align-center
                    justify-center>
                <v-flex xs12 sm8 md8>
                    <v-card
                            class="elevation-10">
                        <v-card-title>
                            <v-card-text>
                                <h1 class="text-xs-center primary--text lighten-1">
                                    На ваш email отправлено письмо. Пожалуйста, перейдите по ссылке в письме для подтверждения своего email.
                                </h1>
                            </v-card-text>
                            <v-layout justify-center>
                                <v-card-actions>
                                    <a
                                            class="title secondary--text lighten-1"
                                            v-bind:onclick="sendVerification">
                                        Письмо не пришло. Отправить ещё раз
                                    </a>
                                </v-card-actions>
                            </v-layout>
                        </v-card-title>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    import axios from 'axios'
    const url = 'http://127.0.0.1:8000/api/registration/';

    export default {
        data() {
            return {
                email: '',
                password: '',
                confirmPassword: '',
                valid: true,
                checkbox: false,
                showConfirmPassword: false,
                emailRules: [
                    v => !!v || 'Введите Ваш e-mail',
                    v => /.+@.+/.test(v) || 'E-mail должен быть реальным'
                ],
                passwordRules: [
                    v => !!v || 'Введите пароль',
                    v => (v && v.length >= 4) || 'Пароль должен состоять не менее чем из 6 символов'
                ],
                confirmPasswordRules: [
                    v => !!v || 'Подтвердите пароль',
                    v => v === this.password || 'Пароли должны совпадать'
                ],
                checkboxRules: [
                    v => !!v || 'Чтобы продолжить Вы должны принять условия Пользовательского Соглашения'
                ]
            }
        },
        methods: {
            sendVerification() {},
            createUser() {
                if (this.$refs.form.validate()) {
                    const user = {
                        "email": this.email,
                        "password1" : this.password,
                        "password2" : this.confirmPassword,
                    }
                    axios
                        .post(url, JSON.stringify(user), {
                            headers: {
                                'Accept': 'application/json',
                                'Content-Type': 'application/json',
                            }
                        })
                        .catch(e => {this.errors.push(e)})
                    this.showConfirmPassword = true;
                }
            },
        }
    }
</script>