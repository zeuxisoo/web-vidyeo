import UIMixin from './ui'

export default {

    mixins: [UIMixin],

    data() {
        return {
            error: false
        }
    },

    methods: {
        loadAccountInfo() {
            this.$api.account
                .me({})
                .success((response, status, request) => {
                    this.$dispatch('accountLogin', response.data);
                    this.$route.router.go({
                        name: 'home'
                    });
                })
                .error((response, status, request) => {
                    this.$dispatch('accountLogout');

                    if (response) {
                        this.shakeError(response, status, request);
                    }
                });
        }
    }

}
