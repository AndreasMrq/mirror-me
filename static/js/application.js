$(document).ready(function(){
    var socket = io.connect();
    socket.on('weather', function(msg) {
        $('#weather_data').append('<p>Temperature: ' + msg.data + '</p>');
    });
});