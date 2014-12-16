if (!$) {
    var $ = jQuery = django.jQuery;
}


$(function() {

    var prefix = $('select.fontawesome-select').data('fontawesome-prefix');

    function format(state) {
        if (!state.id) { return state.text; }
        var icon = $(state.element).data('icon');
        return '<i class="' + prefix + ' ' + prefix + '-' + icon + '"></i> ' + state.text;
    }


    $('.fontawesome-select').select2({
        width:'element',
        formatResult:format,
        formatSelection:format,
        escapeMarkup: function(m) {return m;}
    });
});