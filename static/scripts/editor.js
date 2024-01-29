class IDE {
    constructor(language, theme, value, submission_url) {
	this.submission_url = submission_url;
        require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs' }});
        window.MonacoEnvironment = { getWorkerUrl: () => proxy };
        this.proxy = URL.createObjectURL(new Blob([`
            self.MonacoEnvironment = {
                baseUrl: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min'
            };
            importScripts('https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs/base/worker/workerMain.min.js');
        `], { type: 'text/javascript' }));
        this.editor = new Promise((resolve, reject) => {
            require(["vs/editor/editor.main"], () => {
                this.editor = monaco.editor.create(document.getElementById('container'), {
                    value: value,
                    language: language,
                    theme: theme,
                    fontSize: 24,
                    tabSize: 4,
                    mouseWheelZoom: true,
                    // fontFamily: "string"
                    // quickSuggestions: true
                });
                const model = this.editor.getModel();
                // globalThis.model = model;
                resolve(model)
            });
        })
    }
    submit() {
        /*
        if (this.editor instanceof Promise) {
            this.editor.then((value) => {
                $.ajax({
                    type: 'POST',
                    contentType: 'text/plain',
                    url: '/verify/code',
                    data: value,
                    async: false,
                    success: (data) => {window.sessionStorage.setItem('data', data)},
                    processData: false,
                    contentType: false
                });
            })
            return;
        } 
        */
	console.log(this.submission_url);
        $.ajax({
            type: 'POST',
            contentType: 'text/plain',
            url: this.submission_url, // '/verify/code',
            data: this.editor.getValue(),
            async: false,
            success: (data) => {window.sessionStorage.setItem('data', data)},
            processData: false,
            contentType: false
        });
        return window.sessionStorage.getItem('data')
    }
}


/*

<div id="container" style="width: 50%; height:50vh;"></div>
<script>new DemoIDE('swift', 'vs-light', "print(\"Hello, World!\")").typeString()</script>

class DemoIDE {
    constructor(language, theme, value) {
        require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs' }});
        window.MonacoEnvironment = { getWorkerUrl: () => proxy };
        this.proxy = URL.createObjectURL(new Blob([`
            self.MonacoEnvironment = {
                baseUrl: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min'
            };
            importScripts('https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs/base/worker/workerMain.min.js');
        `], { type: 'text/javascript' }));
        this.editor = new Promise((resolve, reject) => {
            require(["vs/editor/editor.main"], () => {
                this.editor = monaco.editor.create(document.getElementById('container'), {
                    value: value,
                    language: language,
                    theme: theme,
                    fontSize: 24,
                    tabSize: 4,
                    mouseWheelZoom: true,
                    minimap: { enabled: false },
                    readOnly: true,
                });
                const model = this.editor.getModel();
                // globalThis.model = model;
                resolve(model)
            })
        })
        // this.textToType = 'This is a typewriter effect in Monaco Editor.';
        this.currentIndex = 0;
        this.column = 1;
        this.line = 1;        
    }
    typeString() {
        this.editor.then((value) => {
            // const string = String('This is a typewriter effect in Monaco Editor.')
            const string = [
                "struct Player {",
                "\tvar name: String",
                "\tvar highScore: Int = 0",
                "\tvar history: [Int] = []",
                "\t",
                "\tinit(_ name: String) {",
                "\t\tself.name = name",
                "\t}",
                "}",
                "var player = Player(\"Tomas\")\0"
            ].join("\n")
            var final = () => {
                // https://microsoft.github.io/monaco-editor/typedoc/interfaces/editor.IStandaloneCodeEditor.html#setPosition
                if (this.currentIndex == string.length - 1) return
                var currentText = string.slice(0, this.currentIndex);
                let character = string.charAt(this.currentIndex);
                currentText += character
                if (character == '\n') {
                    this.line += 1
                    this.column = 1
                } else {
                    this.column += 1
                }
                value.setValue(currentText);
                // value.setSelection({column: this.column, lineNumber: this.line})
                this.currentIndex++;
                return setTimeout(final, 100);
            }
            console.log(value)
            final()
        })
    }
}
*/
