console.log('hello world!')

function makeRequest (endpoint, symbol) {
    numberOne = $('#numberOne').val()
    numberTwo = $('#numberTwo').val()
    $.post(endpoint, {
        numberOne,
        numberTwo
    }, function (response) {
        solution_formatted = numberOne + ' ' + symbol + ' ' + numberTwo + ' = ' + response
        $('#solutions').prepend('<p>' + solution_formatted + '</p>')
    });
}

$('#add').click(function () {
    makeRequest('/add', '+')
});

$('#subtract').click(function () {
    makeRequest('/subtract', '-')
});

$('#divide').click(function () {
    makeRequest('/divide', '÷')
});

$('#multiply').click(function () {
    makeRequest('/multiply', '×')
});
