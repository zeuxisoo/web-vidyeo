import Vue from 'vue';
import VueRouter from 'vue-router';
import VueResource from 'vue-resource';
import StoreHelper from './helpers/store';
import MessageHelper from './helpers/message';
import Api from './api';

Vue.use(VueRouter);
Vue.use(VueResource);

Vue.http.options.root  = SITE_URL.replace(/\/+$/,'') + '/api';
Vue.http.headers.common['X-CSRF-TOKEN'] = $('meta[name=csrf-token]').attr('content');

Vue.http.transforms.response.push((response) => {
    if (response.ok === false) {
        let responseData = response.data,
            backendData  = responseData.data;

        if (backendData.status_code === 401) {
            MessageHelper.error('Session timeout, Please login again');

            Router.app.$boardcast('accountLogout');
        }
    }

    return response;
});

var Router = new VueRouter({
    hashbang: false,
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

    '/streamer': {
        auth      : true,
        name      : 'streamer.index',
        component : require('./views/streamer/index.vue'),
    },

    '/streamer/boardcast': {
        auth     : true,
        name     : 'streamer.boardcast',
        component: require('./views/streamer/boardcast.vue')
    },

    '*': {
        name     : 'any',
        component: require('./views/not-found.vue')
    }
});

Router.beforeEach((transition) => {
    StoreHelper.getInstance().getItem('jwt-token').then((token) => {
        if (transition.to.auth) {
            if (!token) {
                transition.redirect({ name: 'login' });
            }
        }

        if (transition.to.guest) {
            if (token) {
                transition.redirect({ name: 'home' });
            }
        }

        transition.next()
    });
});

Object.defineProperties(Vue.prototype, {
    $api: {
        get: function() {
            return Api(this);
        }
    },

    $store: {
        get: function() {
            return StoreHelper.getInstance();
        }
    }
});

Router.start(Vue.extend(require('./views/layout.vue')), '#app');
