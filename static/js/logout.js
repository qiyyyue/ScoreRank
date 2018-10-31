
function logout()
{
    if(sessionStorage.getItem('username') != null)
    {
        sessionStorage.clear();
    }

    window.location.href = '/';
}