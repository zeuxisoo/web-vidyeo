<template>
    <div id="room" v-bind:class="{ 'shake': error, 'animated': error }">
        <h3>{{ room.channel }}</h3>
        <hr>
        <div class="row">
            <div class="col-xs-12 text-center">
                <canvas id="canvas"></canvas>
            </div>
        </div>
    </div>
</template>

<script lang="es6">
import SocketHelper from '../../helpers/socket'
import UIMixin from '../../mixins/ui'

export default {

    mixins: [UIMixin],

    data() {
        return {
            room: {}
        }
    },

    ready() {
        let channel = this.$route.params.channel;

        this.$api.room
            .info({
                channel: channel
            })
            .success((response, status, request) => {
                var room = response.data;

                this.room = room;

                SocketHelper.joinChannel(this.room.channel);
                SocketHelper.receiveMedia(this.drawMedia);
            })
            .error(this.shakeError)
    },

    methods: {
        drawMedia(blob) {
            var canvas  = document.querySelector("#canvas");
            var context = canvas.getContext("2d");
            var image   = new Image();

            image.onload = () => {
                canvas.width  = image.width;
                canvas.height = image.height;

                context.drawImage(image, 0, 0, canvas.width, canvas.height);
            };

            image.src = "data:image/jpeg;base64," + blob;
        }
    }

}
</script>
