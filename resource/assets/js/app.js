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
        component: require('../views/home')
    },

    '*': {
        name     : 'any',
        component: require('../views/not-found')
    }
});

Vue.http.headers.common['X-CSRF-TOKEN'] = $('meta[name=csrf-token]').prop('content');

Router.start(Vue.extend(require('../views/layout')), '#app');
