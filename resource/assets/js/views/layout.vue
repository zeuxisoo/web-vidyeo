<template>
    <div id="wrapper">
        <div id="sidebar-wrapper">
            <ul class="sidebar-nav">
                <li class="sidebar-brand">
                    <a href="#">
                        Vidyeo
                    </a>
                </li>
                <li>
                    <a v-link="{ name: 'home' }">Home</a>
                </li>
                <li>
                    <a v-link="{ name: 'streamer.index' }">Streamer</a>
                </li>
            </ul>

            <div class="sidebar-bottom">
                <div class="control text-center" v-if="!authenticated">
                    <div class="col-xs-6">
                        <a class="btn btn-sm btn-primary full-width" v-link="{ name: 'login' }">Log In</a>
                    </div>
                    <div class="col-xs-6">
                        <a class="btn btn-sm btn-primary full-width" v-link="{ name: 'signup' }">Sign Up</a>
                    </div>
                </div>
                <div class="control text-center" v-if="authenticated">
                    <div class="col-xs-12">
                        <a class="btn btn-sm btn-primary full-width" v-on:click="logout">Log Out</a>
                    </div>
                </div>
            </div>
        </div>

        <div id="page-content-wrapper">
            <nav class="navbar navbar-inverse navbar-fixed-top visible-xs-block">
                <div class="container">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle collapsed" id="menu-toggle">
                            <span class="sr-only">Toggle navigation</span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <a class="navbar-brand" href="#">Vidyeo</a>
                    </div>
                </div>
            </nav>

            <div class="row margin-bottom-20px visible-xs-block">&nbsp;</div>

            <div class="row">
                <div class="col-xs-12">
                    <router-view class="view" transition="fade-and-slide" transition-mode="out-in"></router-view>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.sidebar-bottom {
    position: absolute;
    width: 250px;
    bottom: 0px;
    margin: 0px;
    padding: 0px;
}

.sidebar-bottom .control {
    display: block;
}

.full-width {
    width: 100%;
}

.margin-bottom-20px {
    margin-bottom: 20px;
}

.rotate-90 {
    animation:rotate-90-animation 1s linear forwards;
}

@keyframes rotate-90-animation {
    100% {
        transform:rotate(90deg);
    }
}

.view {
    transition: all .5s ease;
}

.fade-and-slide-enter, .fade-and-slide-leave {
    opacity: 0;
    transform: translate3d(10px, 0, 0);
}
</style>

<script lang="es6">
import AccountMixin from '../mixins/account'

export default {

    mixins: [AccountMixin],

    data() {
        return {
            account      : {},
            authenticated: false
        }
    },

    ready() {
        $("#menu-toggle").click((e) => {
            e.preventDefault();

            if ($(this).hasClass("rotate-90") === true) {
                $(this).removeClass("rotate-90");
            }else{
                $(this).addClass("rotate-90");
            }

            $("#wrapper").toggleClass("toggled");
        });

        // Active account when jwt token is exists
        this.$store.getItem('jwt-token').then((token) => {
            if (token) {
                this.setJWTAuthorization(token);
                this.loadAccountInfo();
            }
        });

        // Listen application events
        this.$on('tokenSaved', (token) => {
            this.setJWTAuthorization(token);
        });

        this.$on('accountLogin', (account) => {
            this.setLoginState(account);
        });

        this.$on('accountLogout', () => {
            this.removeLoginState();
        })
    },

    methods: {
        setJWTAuthorization(token) {
            this.$http.headers.common["Authorization"] = "JWT " + token;
        },

        setLoginState(account) {
            this.account       = account;
            this.authenticated = true;
        },

        removeLoginState() {
            this.account       = {};
            this.authenticated = false;

            this.$store.removeItem('jwt-token');

            if (this.$route.auth) {
                this.$route.router.go({
                    name: 'login'
                });
            }
        },

        logout() {
            this.removeLoginState();
        }
    }
}
</script>
