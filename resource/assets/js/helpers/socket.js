class SocketHelper {

    constructor() {
        this.namespace = "/socket/stream";
        this.socket    = io.connect("//" + document.domain + ":" + location.port + this.namespace);

        this.socket.on("log", (message) => {
            console.log("[Received server log] " + message.data);
        });

        this.socket.on("connect", () => {
            this.socket.emit("message", {
                data: "I am connected"
            })
        }.bind(this));
    }

    joinChannel(channel) {
        this.socket.emit("join channel", {
            channel: channel
        });
    }

    leaveChannel(channel) {
        this.socket.emit("leave channel", {
            channel: channel
        });
    }

    disconnect() {
        this.socket.emit("disconnect request");
        this.socket.disconnect();
    }

    sendMedia(channel, blob) {
        this.socket.emit("send media", {
            channel: channel,
            blob   : blob
        });
    }

    receiveMedia(callback) {
        this.socket.on("receive media", message => callback(message.blob));
    }

}

export default new SocketHelper
