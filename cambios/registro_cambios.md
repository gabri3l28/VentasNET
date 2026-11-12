## INC-001 — Fallo en el cálculo del monto total de venta

- **Origen:** Error identificado dentro del módulo de ventas.
- **Descripción:** La aplicación retorna únicamente el valor unitario como monto final, sin importar si se adquieren múltiples unidades.
- **Justificación:** El monto a cobrar debe contemplar la totalidad de los artículos adquiridos para prevenir errores de facturación.
- **Requisito afectado:** RF-001.
- **Archivo involucrado:** `src/ventas.py`.
- **Riesgo:** Facturar un monto inferior al valor real de la compra.
- **Criterio de aceptación:** Para un costo unitario de S/ 50 y una cantidad de 3 unidades, el resultado final debe arrojar S/ 150.
- **Prioridad:** Alta.
- **Decisión:** Validada a través de una revisión académica simulada.
- **Responsable:** Gabriel Ordoñez Garcia.

- **Estado:** Completada y comprobada. La ejecución con S/ 50 × 3 unidades arrojó S/ 150 correctamente. La solución quedó registrada en el commit `9556c31` e integrada en `main`.

## CR-002 — Aplicación de descuento según subtotal

- **Origen:** Requerimiento emitido por el departamento comercial.
- **Descripción:** Implementar una rebaja del 10 % en aquellas ventas cuyo subtotal alcance o supere los S/ 200.
- **Justificación:** Integrar la oferta definida por el equipo comercial dentro de la lógica de cálculo de ventas.
- **Requisito afectado:** RF-002 (nuevo).
- **Archivos involucrados:** `src/ventas.py` y `docs/requisitos.md`.
- **Riesgo:** Cálculo erróneo de la rebaja al evaluar el umbral exacto de S/ 200.
- **Criterio de aceptación:** Si el subtotal es de S/ 150, el monto final queda en S/ 150. Si es de S/ 200, el total pasa a ser S/ 180. Si alcanza los S/ 300, el total finaliza en S/ 270.
- **Prioridad:** Media.
- **Decisión:** Validada a través de una revisión académica simulada.
- **Responsable:** Gabriel Ordoñez Garcia.

## Matriz de impacto

| Criterio | INC-001 | CR-002 |
| --- | --- | --- |
| Requisito | RF-001. Se corrige la obtención del monto total en función del costo unitario y las cantidades. | RF-002 (nuevo). Se incorpora la condición del 10 % de rebaja a partir de un subtotal de S/ 200. |
| Archivos afectados | `src/ventas.py`, encargado de la lógica del cálculo final. | `src/ventas.py` para aplicar la rebaja y `docs/requisitos.md` para registrar el nuevo RF-002. |
| Riesgo | Facturar únicamente el valor individual a pesar de adquirir múltiples artículos. | Fallar en el cálculo de la rebaja al evaluar el límite exacto de S/ 200 o aplicarla incorrectamente. |
| Prueba prevista | S/ 50 × 3 unidades debe arrojar S/ 150. | Con S/ 150 se mantiene en S/ 150, con S/ 200 desciende a S/ 180 y con S/ 300 baja a S/ 270. |
| Decisión simulada | Aprobada para enmendar un fallo crítico en la facturación. | Aprobada para incorporar la oferta requerida por el equipo comercial. |