import BaseApi from '../constracts/api'

export default class Streamer extends BaseApi {

    create(data) {
        return this.app.$http.get('streamer/create', data);
    }

    start(data) {
        return this.app.$http.post('streamer/start', data);
    }

    stop(data) {
        return this.app.$http.post('streamer/stop', data);
    }

}
