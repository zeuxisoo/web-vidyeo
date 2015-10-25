<template>
    <div id="room" v-bind:class="{ 'shake': error, 'animated': error }">
        <h3>{{ room.channel }}</h3>

        <hr>
    </div>
</template>

<script lang="es6">
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
            })
            .error(this.shakeError)
    }

}
</script>
