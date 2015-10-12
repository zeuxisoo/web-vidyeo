import BaseApi from '../constracts/api'

export default class Account extends BaseApi {

    me(data) {
        return this.app.$http.get('account/me', data);
    }

}
