// MA chart for CAMDEX data visualization

$('#ma_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/ma";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('ma_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-mem-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('ma_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');