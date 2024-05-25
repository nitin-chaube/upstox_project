async function fetchHoldings() {
    const response = await fetch('/api/holdings/');
    const data = await response.json();
    document.getElementById('holdings-result').innerText = JSON.stringify(data, null, 2);
}

async function getBrokerageDetails(event) {
    event.preventDefault();
    const form = document.getElementById('brokerage-form');
    const formData = new FormData(form);
    const json = JSON.stringify(Object.fromEntries(formData));

    const response = await fetch('/api/brokerage/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: json,
    });

    const data = await response.json();
    document.getElementById('brokerage-result').innerText = JSON.stringify(data, null, 2);
}

async function placeOrder(event) {
    event.preventDefault();
    const form = document.getElementById('order-form');
    const formData = new FormData(form);
    const json = JSON.stringify(Object.fromEntries(formData));

    const response = await fetch('/api/order/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: json,
    });

    const data = await response.json();
    document.getElementById('order-result').innerText = JSON.stringify(data, null, 2);
}

async function getPrices() {
    const symbol = document.getElementById('price-symbol').value;
    const response = await fetch(`/api/prices/${symbol}/`);
    const data = await response.json();
    document.getElementById('prices-result').innerText = JSON.stringify(data, null, 2);
}
