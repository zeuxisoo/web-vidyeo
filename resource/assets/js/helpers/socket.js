class SocketHelper {

    constructor() {
        this.namespace = "/socket/stream";
        this.socket    = io.connect("//" + document.domain + ":" + location.port + this.namespace);

        // Global logger
        this.socket.on("log", function(message) {
            console.log("[Received server log] " + message.data);
        });

        // Connect event
        this.socket.on("connect", function() {
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

}

export default new SocketHelper
