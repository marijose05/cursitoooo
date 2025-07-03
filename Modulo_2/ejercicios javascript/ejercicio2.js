const cantidadComprada = 2;
const subtotal = precio * cantidadComprada;
const impuesto = subtotal * 0.07;
const totalFinal = subtotal + impuesto;

console.log("Subtotal: $${subtotal.toFixed(2)}");
console.log("Total con impuestos: $${totalFinal.toFixed(2)}");