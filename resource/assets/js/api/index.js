import Home from './home'
import Account from './account'
import Streamer from './streamer'

export default function Api(app) {

    return {
        home    : new Home(app),
        account : new Account(app),
        streamer: new Streamer(app)
    }

}
