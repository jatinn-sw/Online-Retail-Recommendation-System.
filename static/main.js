document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('recommend-form');
    const recommendationsDiv = document.getElementById('recommendations');
    const errorDiv = document.getElementById('error-message');
    const spinner = document.getElementById('loading-spinner');

    function showSpinner(show) {
        spinner.style.display = show ? 'flex' : 'none';
    }

    function fadeIn(element) {
        element.style.opacity = 0;
        element.style.transition = 'opacity 0.7s';
        setTimeout(() => {
            element.style.opacity = 1;
        }, 10);
    }

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        recommendationsDiv.innerHTML = '';
        errorDiv.textContent = '';
        showSpinner(true);
        const customerId = document.getElementById('customer-id').value.trim();
        if (!customerId) {
            errorDiv.textContent = 'Please enter a Customer ID.';
            showSpinner(false);
            return;
        }
        try {
            const response = await fetch(`/recommend?customer_id=${encodeURIComponent(customerId)}`);
            const data = await response.json();
            showSpinner(false);
            if (!response.ok) {
                errorDiv.textContent = data.error || 'An error occurred.';
                return;
            }
            if (data.recommendations && data.recommendations.length > 0) {
                let html = '<h2>Recommended Products:</h2>' +
                    data.recommendations.map(item =>
                        `<div class="recommendation-item">
                            <span class="product-img">🛒</span>
                            <span><strong>${item.Description}</strong> <span style="color:#666;font-weight:400;">(Code: ${item.StockCode})</span></span>
                        </div>`
                    ).join('');
                recommendationsDiv.innerHTML = html;
                fadeIn(recommendationsDiv);
            } else {
                recommendationsDiv.innerHTML = '<p>No recommendations found for this user.</p>';
                fadeIn(recommendationsDiv);
            }
        } catch (err) {
            showSpinner(false);
            errorDiv.textContent = 'Failed to fetch recommendations.';
        }
    });
}); 