import BaseApi from '../constracts/api'

export default class Home extends BaseApi {

    signup(data) {
        return this.app.$http.post('signup', data);
    }

    login(data) {
        return this.app.$http.post('auth', data);
    }

}
