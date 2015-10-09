export default class MessageHelper {

    static info(message, title) {
        return MessageHelper.show('info', message, title)
    }

    static error(message, title) {
        return MessageHelper.show('error', message, title)
    }

    static success(message, title) {
        return MessageHelper.show('success', message, title)
    }

    static warning(message, title) {
        return MessageHelper.show('warning', message, title)
    }

    static show(method, message, title) {
        toastr.options = jQuery.extend(toastr.options, {
            positionClass: 'toast-bottom-full-width'
        });

        toastr[method](message, title);

        return toastr;
    }

}
