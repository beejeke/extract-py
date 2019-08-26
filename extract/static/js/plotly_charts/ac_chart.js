// AC chart for CAMDEX data visualization

$('#ac_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/ac";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('ac_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-ac-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('ac_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');