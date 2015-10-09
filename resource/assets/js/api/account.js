export default class Account {

    constructor(app) {
        this.app = app;
    }

    me(data) {
        return this.app.$http.get('account/me', data);
    }

}
