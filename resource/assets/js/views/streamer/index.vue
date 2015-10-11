<template>
    <div id="streamer-index">
        <h3>Streamer</h3>
        <hr>
        <div class="panel panel-default" v-bind:class="{ 'shake': error, 'animated': error }">
            <div class="panel-heading">Be a streamer</div>
            <div class="panel-body">
                <a class="btn btn-lg btn-primary col-xs-12" v-on:click="create">Let's try</a>
            </div>
        </div>
        <hr>
        <div class="panel panel-default">
            <div class="panel-heading">Is streamer ?</div>
            <div class="panel-body">
                <a v-link="{ name: 'streamer.boardcast' }" class="btn btn-lg btn-success col-xs-12">Boardcast</a>
            </div>
        </div>
    </div>
</template>

<script lang="es6">
import MessageHelper from '../../helpers/message'
import UIMixin from '../../mixins/ui'

export default {

    mixins: [UIMixin],

    methods: {
        create() {
            this.$api.streamer
                .create({})
                .success((response, status, request) => {
                    var response = response.data;
                        message = response.message;

                    MessageHelper.success(message);
                })
                .error(this.shakeError);
        }
    }

}
</script>
