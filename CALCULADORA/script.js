// almacenar la operación y el resultado
let operacionActual = '';
let resultadoActual = '0';

// DOM
const pantallaOperacion = document.getElementById('operacion');
const pantallaResultado = document.getElementById('resultado');

// actualizar la pantalla
function actualizarPantallas() {
    pantallaOperacion.textContent = operacionActual;
    pantallaResultado.textContent = resultadoActual;
}

// agregar
function agregarOperacion(valor) {
    if (operacionActual === '0' && valor !== '.' && !isNaN(valor)) {
        operacionActual = '';
    }
    
    operacionActual += valor;
    actualizarPantallas();
}

// limpiar todo
function limpiarTodo() {
    operacionActual = '';
    resultadoActual = '0';
    actualizarPantallas();
}

// borrar el ultimo numero
function borrarUltimo() {
    operacionActual = operacionActual.slice(0, -1);
    if (operacionActual === '') {
        operacionActual = '0';
    }
    actualizarPantallas();
}

// calcular
function calcular() {
    try {
    

        let expresion = operacionActual
            .replace(/×/g, '*')
            .replace(/÷/g, '/')
            .replace(/\^/g, '**')
            .replace(/%/g, '*0.01*');
        

        const resultado = eval(expresion);
        
        resultadoActual = resultado.toString();
        operacionActual = resultadoActual;
        actualizarPantallas();
    } catch (error) {
        resultadoActual = 'Error';
        actualizarPantallas();
        setTimeout(() => {
            resultadoActual = '0';
            operacionActual = '';
            actualizarPantallas();
        }, 1000);
    }
}

//  teclado
document.addEventListener('keydown', (evento) => {
    const tecla = evento.key;
    
    if (/[0-9]/.test(tecla)) {
        agregarOperacion(tecla);
    } else if (tecla === '.') {
        agregarOperacion('.');
    } else if (tecla === '+' || tecla === '-' || tecla === '*' || tecla === '/') {
        agregarOperacion(tecla);
    } else if (tecla === '(' || tecla === ')') {
        agregarOperacion(tecla);
    } else if (tecla === 'Enter') {
        calcular();
    } else if (tecla === 'Escape') {
        limpiarTodo();
    } else if (tecla === 'Backspace') {
        borrarUltimo();
    } else if (tecla === '^') {
        agregarOperacion('**');
    } else if (tecla === '%') {
        agregarOperacion('%');
    }
});


limpiarTodo();