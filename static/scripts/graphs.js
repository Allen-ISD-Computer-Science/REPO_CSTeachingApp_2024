function Graph1(url) {
    const today = new Date();
    const sevenDaysAgo = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 6);
    const labels = [];
    const data = [];

    // nasty hack
    let x = $.ajax({
        url: url, // "{{ url_for('stats_json') }}",
        type: "GET",
        async: false,
    });
    let m = JSON.parse(x.responseText);

    for (let i = 0; i < 7; i++) {
        const date = new Date(sevenDaysAgo.getTime() + i * 24 * 3600 * 1000);
        labels.push(date.toDateString());
        data.push(m[6 - i]);
    }

    let total = data.reduce((a, b) => a + b, 0);
    if (total == 0) {
        // Change this to be server side. (How?)
        // https://v1.tailwindcss.com/components/cards
        document.getElementById("content").innerHTML = `
        <div class="flex flex-col items-center">
            <picture class="w-[20%] h-[20%]">
                <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f61e/512.webp" type="image/webp">
                <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f61e/512.gif" alt="😞">
            </picture>
            <h1 class='text-4xl font-bold'>No Progress this week.</h1>
            <h3 class='text-xl'>Try completing some practice questions.</h3>
        </div>
        `
    }

    const ctx = document.getElementById('myCanvas').getContext('2d');

    var gradient = ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, 'rgb(8, 87, 156)');
    gradient.addColorStop(1, 'rgb(255, 99, 132)');
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                fillcolor: gradient,
                label: 'Number of Questions',
                data: data,
                backgroundColor: gradient,
                // borderRadius: 10,
                fill: false
            }]
        },
        options: {
            // backgroundColor: "#2e2e2d"
        }
    });
    // Use `data[data.length]` to update the content of the tag in line 23.
}
function Graph2(url) {
    let x = $.ajax({
        url: url,
        type: "GET",
        async: false,
    });
    let m = JSON.parse(x.responseText);
    const ctx = document.getElementById('myCanvas2').getContext('2d');
    let data = [];
    let labels = [
        'Miscellaneous',
        'Arrays',
        'Loops',
        'Types',
        'Object Oriented Programming',
    ]
    for (let i = 0; i < labels.length; i++) {
        data.push(m[labels.length - i - 1]);
    }
    const chart = new Chart(ctx, {
        type: 'polarArea',
        data: {
            labels: labels,
            datasets: [{
                // fillcolor: gradient,
                label: 'Number of Questions',
                data: data,
                backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(75, 192, 192)',
                    'rgb(255, 205, 86)',
                    'rgb(201, 203, 207)',
                    'rgb(54, 162, 235)'
                ],
                // borderRadius: 10,
                fill: false
            }]
        },
        options: {
            // backgroundColor: "#2e2e2d"
        }
    });
}

function load(url1, url2) {
    Graph1(url1);
    Graph2(url2);
}
// Chart1();
// Chart2();
// Can't find variable: Graph1 in html file
