export default class Account {

    constructor(app) {
        this.app = app;
    }

    signup() {
        console.log("Account.signup");
        console.log(this.app.$http);
    }

}
