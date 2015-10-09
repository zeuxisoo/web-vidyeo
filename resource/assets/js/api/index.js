import Home from './home'
import Account from './account'

export default function Api(app) {

    return {
        home   : new Home(app),
        account: new Account(app)
    }

}
