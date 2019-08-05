<template>
    <div id="app">
        <v-app light>
            <v-container fluid grid-list-md>
                <v-layout low wrap>
                    <v-flex xs12>
                        <v-card>
                            <v-card-text>
                                {{property}}
                            </v-card-text>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-app>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                property: 'Blank'
            }
        },

        computed: {
            propertyComputed() {
                // eslint-disable-next-line no-console
                console.log('I change when this.property changes.')
                return this.property
            }
        },

        created() {
            this.property = 'Example property update.'
            // eslint-disable-next-line no-console
            console.log('propertyComputed will update, as this.property is now reactive.')
        }
    }
</script>