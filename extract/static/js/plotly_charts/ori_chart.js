// Ori chart for CAMDEX data visualization

$('#ori_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/ori";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('ori_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-others-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('ori_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');