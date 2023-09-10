document.addEventListener('DOMContentLoaded', function () {
    const commentButtons = document.querySelectorAll('.commentButton');
    const commentPopups = document.querySelectorAll('.commentPopup');

    commentButtons.forEach(function (button, index) {
        button.addEventListener('click', function () {
            commentPopups[index].style.display = 'block';
        });

        const closePopupButtons = commentPopups[index].querySelectorAll('.closePopup');
        closePopupButtons.forEach(function (closeButton) {
            closeButton.addEventListener('click', function () {
                commentPopups[index].style.display = 'none';
            });
        });
    });
});