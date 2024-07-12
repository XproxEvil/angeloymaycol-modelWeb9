document.addEventListener('DOMContentLoaded', function() {
    const dias = Object.keys(predicciones).map(dia => parseInt(dia));
    const ventas = Object.values(predicciones);

    const ctx = document.getElementById('prediccionChart').getContext('2d');
    const prediccionChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dias,
            datasets: [{
                label: 'Ventas',
                data: ventas,
                borderColor: 'rgba(46, 66, 201)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: false,
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Días',
                        color: 'white',
                        font: {
                            size: 14
                        }
                    },
                    ticks: {
                        color: 'white',
                        font: {
                            size: 10
                        }
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Ventas',
                        color: 'white',
                        font: {
                            size: 14
                        }
                    },
                    ticks: {
                        color: 'white',
                        font: {
                            size: 10
                        },
                        beginAtZero: false,
                        suggestedMin: 2000 
                    }
                }
            }
        }
    });
});
