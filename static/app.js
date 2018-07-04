function get_random_featured() {
    $.ajax({
        'type': 'GET',
        'url': '/get_random_featured',
        'async': false,
        'cache': true,
        'success': function(data) {
            if (CLASS_TOGGLE) {
                CLASS_TOGGLE ^= true
                $('#featured_img').removeClass("");('src', data)
        },
        'failed': function() {
            console.log('featured image failed to udpate')
        }
    })
}

$(document).ready(function() {
    CLASS_TOGGLE = true;

    setTimeout(get_random_featured, 5000)
});
