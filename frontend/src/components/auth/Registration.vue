<!--ПОЛНОСТЬЮ РАБОЧАЯ СТРАНИЦА-->

<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <v-content>
        <v-container fluid fill-height>
            <v-layout align-center justify-center>
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
                                    lazy-validation>
                                <v-text-field
                                        prepend-icon="person"
                                        class="compact-form"
                                        name="first_name"
                                        label="Имя"
                                        type="text"
                                        v-model="first_name"
                                ></v-text-field>
                                <v-text-field
                                        prepend-icon="person"
                                        name="last_name"
                                        class="compact-form"
                                        label="Фамилия"
                                        type="text"
                                        v-model="last_name"
                                ></v-text-field>
                                <v-text-field
                                        prepend-icon="home"
                                        class="compact-form"
                                        name="room_number"
                                        label="Номер комнаты"
                                        type="text"
                                        v-model="room_number"
                                ></v-text-field>
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
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn
                                    color="secondary"
                                    @click="onSubmit"
                                    :disabled="!valid"
                            >Создать аккаунт
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </v-content>
</template>

<script>
    export default {
        data() {
            return {
                first_name: '',
                last_name: '',
                email: '',
                password: '',
                room_number: '',
                valid: false,
                confirmPassword: '',
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
            }
        },
    }
</script>