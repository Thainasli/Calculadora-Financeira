document.addEventListener('DOMContentLoaded', function () {
    var errorMessage = "{{ error_message }}";
    var showResult = "{{ show_result }}";
  
    var errorMessageElement = document.getElementById('error-message');
    if (errorMessage) {
        errorMessageElement.style.display = 'block';
    } else {
        errorMessageElement.style.display = 'none';
    }
  
    var resultContainer = document.getElementById('result-container');
    if (showResult) {
        resultContainer.style.display = 'block';
    } else {
        resultContainer.style.display = 'none';
    }
});
