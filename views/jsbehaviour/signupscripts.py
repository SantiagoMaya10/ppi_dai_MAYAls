js_code = """
// Function to toggle the register button based on checkbox state
        function toggleRegisterButton() {
            document.getElementById('register-btn').disabled = !document.getElementById('privacy_policy').checked;
        }

        // Run the toggle function on page load to disable the button initially if checkbox is not checked
        document.addEventListener('DOMContentLoaded', function() {
            toggleRegisterButton();  // Ensure initial state
        });

        // Add event listener for changes in the checkbox state
        document.getElementById('privacy_policy').addEventListener('change', function() {
            toggleRegisterButton();  // Update button state when checkbox changes
        });

        // Function to redirect to the sign-in page after successful registration
        function redirectToSignIn() {
            setTimeout(function() {
                window.location.href = '/sign-in';
            }, 3000); // 3-second delay before redirect
        }
"""

def sign_up_js_scripts():
    return js_code