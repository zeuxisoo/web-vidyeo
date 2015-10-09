<template>
    <div id="signup">
        <h3>Sign up</h3>
        <hr>
        <div class="panel panel-default">
            <div class="panel-body">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" class="form-control" id="username" placeholder="Username" v-model="username">
                </div>
                <div class="form-group">
                    <label for="email">Email address</label>
                    <input type="email" class="form-control" id="email" placeholder="Email" v-model="email">
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
                </div>
            </div>
        </div>
        <hr>
        <button type="button" class="btn btn-default" v-on:click="signup()">Sign up</button>
    </div>
</template>

<script lang="es6">
export default {
    data() {
        return {
            username: "",
            email   : "@",
            password: ""
        }
    },

    methods: {
        signup() {
            this.$api.account.signup({
                username: this.username,
                email   : this.email,
                password: this.password
            }).success(function(data, status, request) {
                console.log('success');
                console.log(data);
            }).error(function(data, status, request) {
                console.log('error');
                console.log(data);
            });
        }
    }
}
</script>
