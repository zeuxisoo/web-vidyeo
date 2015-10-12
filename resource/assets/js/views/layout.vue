<template>
    <div class="navbar navbar-default">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" v-link="{ name: 'home' }">
                    <span>Vidyeo</span>
                </a>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li>
                        <a v-link="{ name: 'home' }">Home</a>
                    </li>
                    <li>
                        <a v-link="{ name: 'streamer.index' }">Streamer</a>
                    </li>
                </ul>

                <ul class="nav navbar-nav navbar-right" v-if="authenticated">
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                            {{ account.username }} <b class="caret"></b>
                        </a>
                        <ul class="dropdown-menu">
                            <li ><a v-on:click="logout">Sign Out</a></li>
                        </ul>
                    </li>
                </ul>

                <ul class="nav navbar-nav navbar-right" v-if="!authenticated">
                    <li><a v-link="{ name: 'login' }">Sign In</a></li>
                    <li><a v-link="{ name: 'signup' }">Sign Up</a></li>
                </ul>
            </div>
        </div>
    </div>

    <div class="content">
        <div class="container">
            <router-view class="view" transition="fade-and-slide" transition-mode="out-in"></router-view>
        </div>
    </div>

    <div class="footer">
        <div class="container">
            <hr>
            <small>
                <span class="pull-left">&copy; Vidyeo 2015</span>
                <span class="pull-right">&nbsp;</span>
            </small>
        </div>
    </div>
</template>

<style>
.view {
    transition: all .3s ease;
}

.fade-and-slide-enter, .fade-and-slide-leave {
    opacity: 0;
    transform: translate3d(10px, 0, 0);
}
</style>

<script lang="es6">
export default {

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

        $("#sidebar-wrapper .sidebar-nav li a").click((e) => {
            if ($("menu-toggle").hasClass("display")) {
                $("#menu-toggle").click();
            }
        });

        // Page refreshed handling
        // => Active account and fetch information when jwt token is exists
        this.$store.getItem('jwt-token').then((token) => {
            if (token) {
                this.setJWTAuthorization(token);
                this.fetchAccountInfo();
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
        },

        fetchAccountInfo() {
            this.$api.account
                .me()
                .success((response, status, request) => {
                    this.$emit('accountLogin', response.data);
                })
                .error((response, status, request) => {
                    this.$emit('accountLogout');
                });
        }
    }
}
</script>
