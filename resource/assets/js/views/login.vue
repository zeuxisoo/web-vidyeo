<template>
    <div id="login" v-bind:class="{ 'shake': error, 'animated': error }">
        <h3>Login</h3>
        <hr>
        <div class="panel panel-default">
            <div class="panel-body">
                <div class="form-group">
                    <label for="account">Account</label>
                    <input type="text" class="form-control" id="account" placeholder="Username or Email" v-model="account">
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
                </div>
            </div>
        </div>
        <hr>
        <button type="submit" class="btn btn-default" v-on:click="login">Login</button>
    </div>
</template>

<script lang="es6">
import UIMixin from '../mixins/ui'
import AccountMixin from '../mixins/account'

export default {

    mixins: [UIMixin, AccountMixin],

    data() {
        return {
            account : "",
            password: ""
        }
    },

    methods: {
        login() {
            this.$api.home.login({
                username: this.account,
                password: this.password
            }).success((response, status, request) => {
                let token = response.token;

                this.$store.setItem('jwt-token', token).then((token) => {
                    this.$dispatch('tokenSaved', token);
                    this.loadAccountInfo();
                }.bind(this));
            }).error(this.shakeError);
        }
    }

}
</script>
