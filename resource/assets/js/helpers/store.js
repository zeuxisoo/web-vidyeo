import localForage from 'localforage';

let instance = null;

export default class StoreHelper {

    static getInstance() {
        if (instance === null) {
            localForage.config({
                driver      : localForage.LOCALSTORAGE,
                name        : 'vidyeo',
                version     : 1.0,
                storeName   : 'vidyeo',
                description : 'The database for vidyeo application'
            });

            instance = localForage;

            return instance;
        }

        return instance;
    }

}
