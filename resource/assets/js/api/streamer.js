export default class Streamer {

    constructor(app) {
        this.app = app;
    }

    tryIt(data) {
        return this.app.$http.get('streamer/try-it', data);
    }

}
