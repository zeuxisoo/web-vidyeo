export default class Streamer {

    constructor(app) {
        this.app = app;
    }

    create(data) {
        return this.app.$http.get('streamer/create', data);
    }

}
