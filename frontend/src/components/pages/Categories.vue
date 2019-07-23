<template>
    <v-layout justify-center>
        <v-flex xs12 sm8>
            <v-card flat>
                <v-container
                        fluid
                        grid-list-md>
                    <v-layout row wrap>
                        <v-flex
                                v-for="card in orders"
                                :key="card.name"
                                xs12 sm3 >
                            <v-card>
                                <v-img
                                        :src=src
                                        aspect-ratio="2.75"
                                ></v-img>

                                <v-card-title primary-title>
                                    <div>
                                        <h3 class="headline mb-0">{{card.name}}</h3>
                                        <p class="mb-0">Компания {{card.customer}}</p>
                                        <p>{{card.date_created}} </p>
                                    </div>
                                </v-card-title>

                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn
                                            class="secondary"
                                            :to="'/order/?id=' + card.id"
                                    >Открыть
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
    export default {
        data() {
            return {
                orders: [{
                    name: 'Category - 1',
                    customer: 'customer',
                    date_created: '14.08.1999',
                },
                ]
            }
        },
    }
</script>
