import Axios from 'axios';
const adsUrl = 'http://0.0.0.0:8000/api/ads/';
const catUrl = 'http://0.0.0.0:8000/api/categories/';

const state = {
    ad: null,
    ads: null,
    categories: null,
};
const getters = {
    AD: state => {
        return state.ad;
    },
    ADS: state => {
        return state.ads;
    },
    CATEGORIES: state => {
        return state.categories;
    },
};
const mutations = {
    SET_AD: async (state, payload) => {
        state.ad = payload;
    },

    SET_ADS: async (state, payload) => {
        state.ads = payload;
    },

    SET_CATEGORIES: async (state, payload) => {
        state.categories = payload;
    },

    ADD_AD: async (state, payload) => {
        state.ad.push(payload);
    },

};
const actions = {
    GET_AD(context, payload) {
        return Axios.get(adsUrl + payload)
            .then(res => {
                let ad = res.data;
                context.commit('SET_AD', ad);
            })
    },

    POST_ADS: async (context, payload) => {
        // eslint-disable-next-line
        let {data} = await Axios.post(adsUrl, JSON.stringify(payload), {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
        });
        context.commit('ADD_AD', payload)
    },

    PATCH_ADS(context, payload){
        return Axios.patch(adsUrl + payload.id, payload)
            .then(res => {
                let ad = res.data;
                context.commit('SET_AD', ad);
            })
    },

    DELETE_AD(context, payload) {
        return Axios.delete(adsUrl + payload)
            .then(res => {
                let ad = res.data;
                context.commit('SET_AD', ad);
            })
    },


    GET_ADS: async (context) => {
        let {data} = await Axios.get(adsUrl);
        context.commit('SET_ADS', data)
    },

    GET_CATEGORIES: async (context) => {
        let {data} = await Axios.get(catUrl);
        context.commit('SET_CATEGORIES', data)
    },

};

export default {
    state,
    getters,
    mutations,
    actions,
};