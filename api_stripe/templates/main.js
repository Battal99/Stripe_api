const stripe = Stripe('pk_test_51M4rA9Gjg9ZFyR2kyF5VYvYnCOVgRJWqTkeYt7l1bK2ZeHh08Ol2TUxASr0iCsxLCjr2o6o0VmQdNrAkqNrAKuEF00uHZamumd');
var buyButton = document.getElementById("buy-button");
buyButton.addEventListener('click', function() {
    fetch("{% url 'buy' product.id %}", {method: 'GET'})
    .then((result) => { return result.json(); })
    .then((data) => {
            console.log(data);
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({sessionId: data.sessionId})
          })
          });
