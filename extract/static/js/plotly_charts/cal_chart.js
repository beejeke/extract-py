// CAL chart for CAMDEX data visualization

$('#cal_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/cal";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('cal_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-cal-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('cal_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');