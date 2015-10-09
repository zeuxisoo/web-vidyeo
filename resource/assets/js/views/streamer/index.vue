<template>
    <div id="streamer-index">
        <h3>Streamer</h3>
        <hr>
        <div class="panel panel-default">
            <div class="panel-heading">Be a streamer</div>
            <div class="panel-body">
                <a v-link="{ name: 'streamer.apply' }" class="btn btn-lg btn-primary col-xs-12">Let's try</a>
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
export default {

}
</script>
