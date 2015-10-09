export default class Account {

    constructor(app) {
        this.app = app;
    }

    signup(data, success) {
        return this.app.$http.post('/api/signup', data);
    }

}
