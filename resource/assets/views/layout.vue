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
            </ul>

            <div class="sidebar-nav bottom text-center">
                <div class="col-xs-6">
                    <a class="btn btn-sm btn-primary full-width" v-link="{ name: 'login' }">Log In</a>
                </div>
                <div class="col-xs-6">
                    <a class="btn btn-sm btn-primary full-width" v-link="{ name: 'signup' }">Sign Up</a>
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

            <div class="row">
                <div class="col-xs-12">
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.sidebar-nav.bottom {
    bottom: 20px;
    top: inherit;
}

.full-width {
    width: 100%;
}

.rotate-90 {
    animation:rotate-90-animation 1s linear forwards;
}

@keyframes rotate-90-animation {
    100% {
        transform:rotate(90deg);
    }
}
</style>

<script lang="es6">
export default {
    ready() {
        $("#menu-toggle").click(function(e) {
            e.preventDefault();

            if ($(this).hasClass("rotate-90") === true) {
                $(this).removeClass("rotate-90");
            }else{
                $(this).addClass("rotate-90");
            }

            $("#wrapper").toggleClass("toggled");
        });
    }
}
</script>
