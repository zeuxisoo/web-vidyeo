import BaseApi from '../constracts/api'

export default class Room extends BaseApi {

    info(data) {
        return this.app.$http.get('room/info', data);
    }

}
