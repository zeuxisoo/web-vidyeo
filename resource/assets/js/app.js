import Vue from 'vue';
import VueRouter from 'vue-router';
import VueResource from 'vue-resource';
import Api from './api';

Vue.use(VueRouter);
Vue.use(VueResource);

Vue.http.headers.common['X-CSRF-TOKEN'] = $('meta[name=csrf-token]').attr('content');

var Router = new VueRouter({
    history: true,
    saveScrollPosition: true
});

Router.map({
    '/': {
        name     : 'home',
        component: require('./views/home.vue')
    },

    '/login': {
        name     : 'login',
        component: require('./views/login.vue')
    },

    '/signup': {
        name     : 'signup',
        component: require('./views/signup.vue')
    },

    '*': {
        name     : 'any',
        component: require('./views/not-found.vue')
    }
});

Object.defineProperties(Vue.prototype, {
    $api: {
        get: function() {
            return Api(this);
        }
    }
});

Router.start(Vue.extend(require('./views/layout.vue')), '#app');
