var Vue = require('vue'),
    VueRouter = require('vue-router'),
    VueResource = require('vue-resource');

Vue.use(VueRouter);
Vue.use(VueResource);

var Router = new VueRouter({
    history: true,
    saveScrollPosition: true
});

Router.map({
    '/': {
        name     : 'home',
        component: require('../views/home.vue')
    },

    '/login': {
        name     : 'login',
        component: require('../views/login.vue')
    },

    '/signup': {
        name     : 'signup',
        component: require('../views/signup.vue')
    },

    '*': {
        name     : 'any',
        component: require('../views/not-found.vue')
    }
});

Vue.http.headers.common['X-CSRF-TOKEN'] = $('meta[name=csrf-token]').prop('content');

Router.start(Vue.extend(require('../views/layout.vue')), '#app');
