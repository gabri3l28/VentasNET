# Casos de prueba

## INC-001 — Cálculo del monto total según unidades

| Costo unitario | Cantidades | Valor esperado | Valor obtenido | Estatus |
| --- | --- | --- | --- | --- |
| S/ 50 | 3 unidades | S/ 150 | S/ 150 | Validada |

Comando ejecutado: `python src/ventas.py`

## CR-002 — Descuento del 10 % desde S/ 200

| Precio unitario | Cantidad | Subtotal esperado / obtenido | Total esperado | Total obtenido | Estado |
| --- | ---: | --- | --- | --- | --- |
| S/ 50 | 3 | S/ 150 / S/ 150 | S/ 150 | S/ 150 | Aprobada |
| S/ 50 | 4 | S/ 200 / S/ 200 | S/ 180 | S/ 180.0 | Aprobada |
| S/ 100 | 3 | S/ 300 / S/ 300 | S/ 270 | S/ 270.0 | Aprobada |

Comando ejecutado para cada caso: `python src/ventas.py`