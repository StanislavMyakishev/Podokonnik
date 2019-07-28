<template>
    <v-container>
        <v-layout>
            <v-toolbar app dark color="primary">
                <v-toolbar-side-icon
                        class="hidden-lg-and-up"
                        @click="drawer = !drawer"
                ></v-toolbar-side-icon>
                <v-toolbar-title class="display-1">
                    <router-link
                            to="/"
                            tag="span"
                            class="pointer">
                        Подоконник
                    </router-link>
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <v-toolbar-items class="hidden-md-and-down">
                    <v-btn
                            v-for="link of links"
                            :key="link.title"
                            :to="link.url"
                            flat
                    >
                        <v-icon left>{{link.icon}}</v-icon>
                        {{link.title}}
                    </v-btn>
                </v-toolbar-items>
            </v-toolbar>
            <v-navigation-drawer
                    app
                    temporary=""
                    v-model="drawer">
                <v-list>
                    <v-list-tile
                            v-for="link of links"
                            :key="link.title"
                            :to="link.url"
                    >
                        <v-list-tile-action>
                            <v-icon>{{link.icon}}</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                            <v-list-tile-title v-text="link.title"></v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </v-list>
            </v-navigation-drawer>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        data: () => ({
            drawer: false,
            links: [{
                title: 'Главная',
                icon: 'home',
                url: '/',
            },{
                title: 'Категории',
                icon: 'home',
                url: '/categories',
            },{
                title: 'Мои объявления',
                icon: 'face',
                url: '/myads',
            }, {
                title: 'Избранное',
                icon: 'turned_in',
                url: '/favorite',
            },{
                title: 'Личный кабинет',
                icon: 'person',
                url: '/profile',
            },{
                title: 'Вход',
                icon: 'lock',
                url: '/login'
            },]
        })
    }
</script>

<style>
    .pointer {
        cursor: pointer;
    }
</style>