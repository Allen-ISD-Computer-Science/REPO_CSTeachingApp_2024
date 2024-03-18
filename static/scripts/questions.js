var stopAt = 100 / 7;
var progress = 0
var invervalSpeed = 10;
var incrementSpeed = 1;
var isAlreadyChecked = false;

function getInnerHTMLByID(response, id) {
    const parser = new window.DOMParser();
    const doc = parser.parseFromString(response, 'text/html');
    const element = doc.getElementById(id);
    return element.innerHTML;
}

function x(url1, url2) {
    if (isAlreadyChecked == true) {
        $.ajax({
            url: url1,
            type: "GET",
            async: false,
            statusCode: {
                // `202 Accepted` is used to indicate the end of the quiz/test.
                202: () => {
                    let myAudioElement_2 = new Audio("./static/audio/clap.mp3");
                    myAudioElement_2.addEventListener("canplay", (event) => { setTimeout(() => { myAudioElement_2.play(); }, 250); });
                }
            },
            success: function (response) {
                document.getElementById("question").innerHTML = getInnerHTMLByID(response, "question");
            },
        });
        isAlreadyChecked = false;
        return;
    }
    isAlreadyChecked = true;
    try {
        var m = $("input[name=option]:checked");
        m = m[0].id
    } catch (TypeError) {
        isAlreadyChecked = false;
        return
    }
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: url2,
        data: `{"option": ${m}}`,
        async: false,
        success: (data) => { window.sessionStorage.setItem('data', data) },
        processData: false,
        contentType: false
    });
    let dataObject = JSON.parse(window.sessionStorage.getItem('data'))
    if (dataObject.correct == true) {
        let audio = new Audio();
        audio.src = "./static/audio/correct.mp3"; // FIXME: Change to `url_for`
        audio.play();
        var str = [
            '<div class="w-[100%] h-[10%] py-3 bg-lime-300 rounded-lg">',
            '\t<div class="flex items-stretch">',
            '\t\t<svg class="animated-check" viewBox="0 0 24 24" width="5%" height="5%">',
            '\t\t\t<path d="M4.1 12.7L9 17.6 20.3 6.3" fill="none"/>',
            '\t\t</svg>',
            '\t\t<div class="font-bold pl-5 pt-2 text-xl">',
            '\t\t\t<h1>Correct!</h1>',
            '\t\t\t<p class="font-light text-base"><b class="font-bold">Explanation</b>: <u>Arrays are zero indexed in Swift</u>. An array index can be no more than <u><code>length of array - 1</code></u>.</p>',
            '\t\t</div>',
            '\t</div>',
            '</div>'
        ].join("\n")
        var child = document.createElement('div');
        child.innerHTML = str;
        child = child.firstChild;
        document.getElementById('question').appendChild(document.createElement('br'))
        document.getElementById('question').appendChild(document.createElement('br'))
        document.getElementById('question').appendChild(child);
        document.getElementById(`${m}`).parentElement.classList.add('bg-lime-300');
    } else {
        let audio = new Audio();
        audio.src = "./static/audio/fail.mp3"; // FIXME: Change to `url_for`
        audio.play();
        var str = [
            '<div class="w-[100%] h-[10%] py-3 bg-red-300 rounded-lg">',
            '\t<div class="flex items-stretch">',
            '\t\t<div class="font-bold pl-5 pt-2 text-xl">',
            '\t\t\t<h1>Incorrect!</h1>',
            '\t\t\t<p class="font-light text-base"><b class="font-bold">Explanation</b>: <u>Arrays are zero indexed in Swift</u>. An array index can be no more than <u><code>length of array - 1</code></u>.</p>',
            '\t\t</div>',
            '\t</div>',
            '</div>'
        ].join("\n")
        var child = document.createElement('div');
        child.innerHTML = str;
        child = child.firstChild;
        document.getElementById('question').appendChild(document.createElement('br'))
        document.getElementById('question').appendChild(document.createElement('br'))
        document.getElementById('question').appendChild(child);
        document.getElementById(`${m}`).parentElement.classList.add('bg-red-300');
        document.getElementById(`${dataObject.correct_choice}`).parentElement.classList.add('bg-lime-300');
    }
    document.getElementById("1").disabled = true;
    document.getElementById("2").disabled = true;
    document.getElementById("3").disabled = true;
    document.getElementById("4").disabled = true;
    document.getElementById("check").classList.replace("bg-green-600", "bg-blue-500");
    document.getElementById("check").classList.replace("shadow-[0_5px_0px_rgb(21,128,61)]", "shadow-[0_5px_0px_rgb(37,99,235)]");
    document.getElementById("check").innerHTML = "Next";
    stopAt += 25;
    change();
}

function change() {
    let bar = document.getElementById('bar');
    progressInterval = setInterval(function () {
        if (progress >= stopAt) clearInterval(progressInterval);
        progress += incrementSpeed;
        bar.style.width = progress + "%";
        if (progress >= 100) {
            clearInterval(progressInterval);
        }
    }, invervalSpeed);
}
document.addEventListener("DOMContentLoaded", change);