<template>
    <div id="app">
        <v-app light>
            <v-container fluid grid-list-md>
                <v-layout low wrap>
                    <v-flex xs12>
                        <section
                                v-for="category in categories"
                                :key="category.name"
                                color="white"
                                flat
                        ><v-parallax
                                :key="renderKey"
                                :src=category.src
                                height="380">
                            <v-layout column align-center justify-center>
                                <h2 class="secondary--text text-uppercase text-truncate font-weight-bold mb-2 display-2">{{category.name}}</h2>
                                <div class="white--text text-uppercase text-truncate text--lighten-1 font-weight-regular headline mb-3 text-xs-center">{{category.categ_descr}}
                                </div>
                                <v-btn
                                        @click="forceReload"
                                        light large
                                        class="success white--text"
                                       href="/">Перейти
                                </v-btn>
                            </v-layout>
                        </v-parallax>
                            <v-item-group>
                                <v-container fluid grid-list-md>
                                    <v-layout row wrap>
                                        <v-flex
                                                v-for="add in category.adds"
                                                :key="add.name"
                                                class="content"
                                                xs12 sm12 md4>
                                            <v-item>
                                                <v-card class="elevation-0">
                                                    <v-img height="45px" class="text-xs-center">
                                                        <v-icon x-large class="brown--text">{{add.icon}}</v-icon>
                                                    </v-img>
                                                    <v-card-title primary-title>
                                                        <div class="secondary--text text--lighten-1 text-uppercase text-truncate font-weight-bold mb-2 headline text-xs-center" style="width:100%">{{add.name}}
                                                        </div>
                                                    </v-card-title>
                                                    <v-card-text class="subheading">
                                                        {{add.add_descr}}
                                                    </v-card-text>
                                                </v-card>
                                            </v-item>
                                        </v-flex>
                                    </v-layout>
                                </v-container>
                            </v-item-group>
                        </section>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-app>
    </div>
</template>

<script>
    export default {
        data: () => ({
            renderkeY: 0,
            categories: [{
                name: 'Категория 1',
                categ_descr: 'Описание категории 1',
                src: 'https://github.com/vwxyzjn/vuetify-parallax-starter2/raw/master/src/assets/background1.jpg',
                url: '/about',
                adds: [{
                    name: 'Add name 1',
                    add_descr: 'We did most of the heavy lifting for you to provide\n' +
                        'a default stylings that incorporate our custom components.\n' +
                        'Additionally, we refined animations and transitions to\n' +
                        'provide a smoother experience for developers.',
                    icon: 'flash_on',
                },{
                    name: 'Add name 2',
                    add_descr: 'By utilizing elements and principles of Material Design,\n' +
                        'we were able to create a framework that incorporates components\n' +
                        'and animations that provide more feedback to users. Additionally,\n' +
                        'a single underlying responsive system across all platforms allow\n' +
                        'for a more unified user experience.',
                    icon: 'group',
                },{
                    name: 'Add name 3',
                    add_descr: 'We have provided detailed documentation as well as specific code\n' +
                        'examples to help new users get started. We are also always open\n' +
                        'to feedback and can answer any questions a user may have about\n' +
                        'Materialize.',
                    icon: 'settings',
                },
                ],
            }, {
                name: 'Категория 2',
                categ_descr: 'Описание категории 2',
                src: 'https://github.com/vwxyzjn/vuetify-parallax-starter2/raw/master/src/assets/background2.jpg',
                url: '/team',
                adds: [{
                    name: 'Add name 1',
                    add_descr: 'We did most of the heavy lifting for you to provide\n' +
                        'a default stylings that incorporate our custom components.\n' +
                        'Additionally, we refined animations and transitions to\n' +
                        'provide a smoother experience for developers.',
                    icon: 'flash_on',
                },{
                    name: 'Add name 2',
                    add_descr: 'By utilizing elements and principles of Material Design,\n' +
                        'we were able to create a framework that incorporates components\n' +
                        'and animations that provide more feedback to users. Additionally,\n' +
                        'a single underlying responsive system across all platforms allow\n' +
                        'for a more unified user experience.',
                    icon: 'group',
                },{
                    name: 'Add name 3',
                    add_descr: 'We have provided detailed documentation as well as specific code\n' +
                        'examples to help new users get started. We are also always open\n' +
                        'to feedback and can answer any questions a user may have about\n' +
                        'Materialize.',
                    icon: 'settings',
                },
                ],
            }, {
                name: 'Категория 3',
                categ_descr: 'Описание категории 3',
                src: 'https://github.com/vwxyzjn/vuetify-parallax-starter2/raw/master/src/assets/background3.jpg',
                url: '/blog',
                adds: [{
                    name: 'Add name 1',
                    add_descr: 'We did most of the heavy lifting for you to provide\n' +
                        'a default stylings that incorporate our custom components.\n' +
                        'Additionally, we refined animations and transitions to\n' +
                        'provide a smoother experience for developers.',
                    icon: 'flash_on',
                },{
                    name: 'Add name 2',
                    add_descr: 'By utilizing elements and principles of Material Design,\n' +
                        'we were able to create a framework that incorporates components\n' +
                        'and animations that provide more feedback to users. Additionally,\n' +
                        'a single underlying responsive system across all platforms allow\n' +
                        'for a more unified user experience.',
                    icon: 'group',
                },{
                    name: 'Add name 3',
                    add_descr: 'We have provided detailed documentation as well as specific code\n' +
                        'examples to help new users get started. We are also always open\n' +
                        'to feedback and can answer any questions a user may have about\n' +
                        'Materialize.',
                    icon: 'settings',
                },
                ],
            },],
        }),
        methods: {
            forceReload(){
                this.renderKey += 1;
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