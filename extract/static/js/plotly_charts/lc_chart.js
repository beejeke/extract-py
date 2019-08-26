// LC chart for CAMDEX data visualization

$('#lc_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/lc";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('lc_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-lc-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('lc_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');