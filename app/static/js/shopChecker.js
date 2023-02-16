const form = document.getElementById('shopChecker');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const accountID = document.getElementById('accountID').value;
    const refreshToken = document.getElementById('refreshToken').value;
    if (accountID === '') {
        snackbar('error', 'Account ID cannot be empty', 3000);
        return;
    } else if (refreshToken === '') {
        snackbar('error', 'Refresh token cannot be empty', 3000);
        return;
    }
    form.submit();
});