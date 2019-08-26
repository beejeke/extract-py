// RyH chart for CAMDEX data visualization

$('#ryh_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/ryh";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('ryh_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-ryh-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('ryh_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');