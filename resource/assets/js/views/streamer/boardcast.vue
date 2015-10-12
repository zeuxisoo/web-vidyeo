<template>
    <div id="streamer-stream">
        <h3>Boardcast</h3>
        <hr>
        <div class="row">
            <div class="col-xs-12 text-center">
                <video id="video" muted="muted" autoplay="autoplay" width="0" height="0"></video>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-12 text-center">
                <canvas id="canvas"></canvas>
            </div>
        </div>
        <hr>
        <div class="row">
            <div class="col-xs-12">
                <div class="form-group">
                    <label for="audio-source">Audio source</label>
                    <select class="form-control" id="audio-source">
                    </select>
                </div>
                <div class="form-group">
                    <label for="video-source">Video source</label>
                    <select class="form-control" id="video-source">
                    </select>
                </div>
            </div>
        </div>
    </div>
</template>

<style>

</style>

<script lang="es6">
import MessageHelper from '../../helpers/message'

export default {

    data() {
        return {
            audioes: [],
            videoes: []
        }
    },

    ready() {
        this.openMedia();
    },

    methods: {
        hasGetUserMedia() {
            return !!(navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia);
        },

        openMedia() {
            if (this.hasGetUserMedia() === true) {
                if (typeof MediaStreamTrack !== "undefined") {
                    var $video       = document.querySelector('#video');
                    var $canvas      = document.querySelector('#canvas');
                    var $audioSelect = document.querySelector('#audio-source');
                    var $videoSelect = document.querySelector('#video-source');

                    navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;

                    MediaStreamTrack.getSources((sourceInfos) => {
                        for (var i=0; i !== sourceInfos.length; ++i) {
                            var sourceInfo = sourceInfos[i];

                            switch(sourceInfo.kind) {
                                case 'audio':
                                    var sourceName = sourceInfo.label || "microphone " + ($audioSelect.length + 1);
                                    var option     = document.createElement("option");

                                    option.value = sourceInfo.id,
                                    option.text = sourceName;

                                    $audioSelect.appendChild(option);
                                    break;
                                case 'video':
                                    var sourceName = sourceInfo.label || "camera " + ($videoSelect.length + 1);
                                    var option     = document.createElement("option");

                                    option.value = sourceInfo.id,
                                    option.text = sourceName;

                                    $videoSelect.appendChild(option);
                                    break;
                                default:
                                    console.log("Some other kind of source: ", sourceInfo);
                                    break;
                            }
                        }
                    });

                    $audioSelect.onchange = this.startMedia;
                    $videoSelect.onchange = this.startMedia;

                    this.startMedia();
                }else{
                    MessageHelper.warning("This browser does not support MediaStreamTrack");
                }
            }else{
                MessageHelper.warning("This browser does not support getUserMedia");
            }
        },

        startMedia() {
            var $video       = document.querySelector('#video');
            var $audioSelect = document.querySelector('#audio-source');
            var $videoSelect = document.querySelector('#video-source');

            if (!!window.stream) {
                $video.src = null;

                // window.stream.stop();
                window.stream.getTracks().forEach((track) => {
                    track.stop();
                });
            }

            var audioSource = $audioSelect.value;
            var videoSource = $videoSelect.value;
            var constraints = {
                audio: {
                    optional: [{
                        sourceId: audioSource
                    }]
                },
                video: {
                    optional: [{
                        sourceId: videoSource
                    }]
                }
            };

            var self = this;

            navigator.getUserMedia(
                constraints,
                (stream) => {
                    window.URL    = window.URL || window.webkitURL
                    window.stream = stream;

                    $video.addEventListener('loadedmetadata', function() {
                        var videoWidth  = this.videoWidth / 2;
                        var videoHeight = this.videoHeight / 2;

                        var canvasTimer = setInterval(() => {
                            try {
                                var canvas  = document.querySelector('#canvas');
                                var context = canvas.getContext("2d");

                                canvas.width  = videoWidth;
                                canvas.height = videoHeight;

                                context.drawImage($video, 0, 0, videoWidth, videoHeight);

                                var data = canvas.toDataURL("image/jpeg", 1.0);

                                self.dataURItoBlob(data);
                            }catch(e) {
                                clearInterval(canvasTimer);
                            }
                        }, 150);
                    });

                    $video.src = window.URL.createObjectURL(stream);
                    $video.play();
                },
                (reason) => {
                    if (reason.name === "DevicesNotFoundError") {
                        MessageHelper.warning("Devices not found");
                    }else{
                        MessageHelper.warning("navigator.getUserMedia error: " + reason.name);
                    }
                }
            );
        },

        dataURItoBlob(dataURI) {
            var byteString   = atob(dataURI.split(',')[1]);
            var arrayBuffer  = new ArrayBuffer(byteString.length);
            var integerArray = new Uint8Array(arrayBuffer);

            for (var i=0; i<byteString.length; i++) {
                integerArray[i] = byteString.charCodeAt(i);
            }

            return new Blob([arrayBuffer], { type: 'image/jpeg' });
        }
    }

}
</script>
