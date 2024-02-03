import * as THREE from 'https://cdn.skypack.dev/three@0.133.0/build/three.module.js'
import { OrbitControls } from 'https://cdn.skypack.dev/three@0.133.0/examples/jsm/controls/OrbitControls'
import { GLTFLoader } from 'https://cdn.skypack.dev/three@0.133.0/examples/jsm/loaders/GLTFLoader.js'
import { FontLoader } from 'https://cdn.skypack.dev/three@0.133.0/examples/jsm/loaders/FontLoader.js'
import { TextGeometry } from 'https://cdn.skypack.dev/three@0.133.0/examples/jsm/geometries/TextGeometry.js'
import Stats from 'https://cdn.skypack.dev/three@0.133.0/examples/jsm/libs/stats.module'

const scene = new THREE.Scene()
// scene.add(new THREE.AxesHelper(5))
scene.background = new THREE.Color(0x2e2d2d);

// const ambientLighting = new THREE.AmbientLight(0xffffff, 0.5)
// scene.add(ambientLighting)

const pointLight = new THREE.POINT

// 0xffbb73
const light = new THREE.SpotLight(0xffffff, Math.PI * 20)
light.position.set(5, 5, 5)
light.shadow.mapSize.width = 1024;
light.shadow.mapSize.height = 1024;
light.shadow.camera.near = 500;
light.shadow.camera.far = 4000;
light.shadow.camera.fov = 30;
scene.add(light);

let innerWidth = window.innerWidth;
let innerHeight = window.innerHeight;

const camera = new THREE.PerspectiveCamera(75, (innerWidth / innerHeight), 0.1, 1000)
camera.position.x = -0.8414902736183079
camera.position.y = 4.371964245573707
camera.position.z = 8.834879651486299
// Make the camera not interactive

const renderer = new THREE.WebGLRenderer()
renderer.physicallyCorrectLights = true //deprecated
renderer.shadowMap.enabled = true
renderer.setSize(window.innerWidth, window.innerHeight)
// renderer.useLegacyLights = false //deprecated
document.body.appendChild(renderer.domElement)

const GLTFLoaderInstance = new GLTFLoader()
GLTFLoaderInstance.load(
    '{{ url_for("static", filename="models/server_computer_simple/scene.glb") }}',
    function (gltf) {
        gltf.scene.traverse(function (child) {
            if (child.isMesh) {
                const m = child // as THREE.Mesh
                m.receiveShadow = true
                m.castShadow = true
            }
            if (child.isLight) {
                const l = child // as THREE.SpotLight
                l.castShadow = true
                l.shadow.bias = -0.003
                l.shadow.mapSize.width = 2048
                l.shadow.mapSize.height = 2048
            }
        })
        scene.add(gltf.scene)
    },
    (xhr) => { console.log((xhr.loaded / xhr.total) * 100 + '% loaded') },
    (error) => { console.log(error) }
)

// TODO: Have text that renders 404 Not Found and the Logo.
// https://stackoverflow.com/questions/9718130/three-js-insert-image
var img = new THREE.MeshBasicMaterial({ map: new THREE.TextureLoader().load('{{ url_for("static", filename="imgs/extras/logo.svg") }}'), transparent: true });
img.map.needsUpdate = true;
console.log(img)

var plane = new THREE.Mesh(new THREE.PlaneGeometry(5, 5), img);
plane.overdraw = true;
plane.position.x = 2.5;
plane.position.y = 2.5;
plane.position.z = 4;
scene.add(plane);

// https://github.com/mrdoob/three.js/tree/master/examples/fonts
// https://threejs.org/docs/#examples/en/geometries/TextGeometry
const loader = new FontLoader();

loader.load('fonts/helvetiker_regular.typeface.json', function (font) {

    const geometry = new TextGeometry('Hello three.js!', {
        font: font,
        size: 80,
        height: 5,
        curveSegments: 12,
        bevelEnabled: true,
        bevelThickness: 10,
        bevelSize: 8,
        bevelOffset: 0,
        bevelSegments: 5
    });
});

window.addEventListener('resize', onWindowResize, false)
function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.setSize(window.innerWidth, window.innerHeight)
    render()
}

const stats = new Stats()
// document.body.appendChild(stats.dom)

const controls = new OrbitControls(camera, renderer.domElement)
controls.enableDamping = true

function animate() {
    // console.log(camera.position)
    requestAnimationFrame(animate)
    controls.update()
    render()
    stats.update()
}

function render() { renderer.render(scene, camera) }

animate()