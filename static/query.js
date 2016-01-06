$(document).ready(function () {
    $('#query_sim').click(function (){
        // alert($('#sim').val());
        $.ajax({
            url: '/vote2016/handler/',
            // crossDomain: true,
            dataType: 'html',
            type:'POST',
            data: { 'query': $('#sim').val() },
            error: function(xhr) {
                alert('Ajax request ERROR:'+xhr);
            },
            success: function(response) {
                // alert(response);
                $("#result").html(response);
            }
        });
    });
});
