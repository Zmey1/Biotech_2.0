$(document).ready(function() {
    $('#predictionForm').submit(function(event) {
        event.preventDefault(); // Prevent form submission

        // Get input data
        var inputData = $('#inputData').val();

        // Send input data to server for prediction
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: JSON.stringify({ inputData: inputData }),
            contentType: 'application/json',
            success: function(response) {
                $('#predictionResult').show();
                $('#resultText').text(response.prediction);
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});
