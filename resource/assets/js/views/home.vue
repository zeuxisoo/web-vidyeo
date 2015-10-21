<template>
    <div id="home">
        <div class="row">
            <div class="col-xs-3" v-for="streaming in streamings">
                <div class="thumbnail">
                    <a v-link="{ name: 'room.index', params: { channel: streaming.channel } }">
                        <img v-bind:src="streaming.cover" alt="{{ streaming.channel }}">
                        <div class="caption">
                            <h3>{{ streaming.id }}</h3>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="es6">
export default {

    data() {
        return {
            streamings: []
        }
    },

    ready() {
        this.$api.home
            .streaming({})
            .success((response, status, request) => {
                let streamings = response.data;

                this.streamings = streamings;
            })
            .error((response, status, request) => {
                console.log(response);
            });
    }

}
</script>
