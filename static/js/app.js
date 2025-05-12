    // Toastlarni avtomatik yo‘qotish
    setTimeout(function () {
        const toasts = document.querySelectorAll('.toast');
        toasts.forEach(toast => {
            toast.style.opacity = '0';
            toast.style.transition = 'opacity 0.5s ease';
            setTimeout(() => toast.remove(), 500);
        });
    }, 3000);

document.getElementById("myForm").addEventListener("submit", function(event) {
    var username = document.getElementById("telegram").value.trim();
    var regex = /^@?[a-zA-Z0-9_]{5,32}$/;

    if (!regex.test(username)) {
        alert("❌ Invalid Telegram username. It must be 5–32 characters, and contain only letters, numbers, and underscores.");
        event.preventDefault(); // Yuborishni to‘xtatish
    }
});