// PR chart for CAMDEX data visualization

$('#pr_chart').on('update', function() {
    var url = "/chart/" + $('#patient').val() + "/pr";
    var data = {
        patient: $('#patient').val(),
    }

    $.get(url, data, function(chart) {
        Plotly.react('pr_chart', chart.data, chart.layout, chart.config);
    });

    $('#collapse-pr-chart').on('shown.bs.collapse', function() {
        var update = {
	        autosize: true
        }

        Plotly.relayout('pr_chart', update);
    });
});

$('#patient').on('change', function() {
    $('.data_chart').trigger('update');
} );

$('.data_chart').trigger('update');