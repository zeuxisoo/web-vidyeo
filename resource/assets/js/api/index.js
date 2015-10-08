import Account from './account'

export default function Api(app) {

    return {
        account: new Account(app)
    }

}
