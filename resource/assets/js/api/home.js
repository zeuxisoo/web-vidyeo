export default class Home {

    constructor(app) {
        this.app = app;
    }

    signup(data) {
        return this.app.$http.post('signup', data);
    }

    login(data) {
        return this.app.$http.post('auth', data);
    }

}
