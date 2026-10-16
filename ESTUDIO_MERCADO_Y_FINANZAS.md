# 📊 Estudio de Mercado y Previsión Financiera: App de Cuidado de Plantas

Documento estratégico y financiero actualizado para el lanzamiento en **Google Play (Android)** y **App Store (iPhone)** de la aplicación bajo una arquitectura **Local-First** (almacenamiento en el dispositivo del usuario + IA bajo demanda).

---

## 1. Situación de Partida y Ventaja Fiscal

> [!IMPORTANT]
> **Situación Fiscal Actual:**
> - Al ser **ya autónomo dado de alta en España**, el lanzamiento de esta aplicación **no supone ningún gasto extra en cuotas de Seguridad Social (RETA)** (ahorro de 1.000 € – 3.600 €/año respecto a un creador que empieza de cero).
> - Solo se requiere añadir de forma telemática y gratuita el epígrafe secundario en Hacienda (Modelo 036/037: Epígrafe IAE 763 o 845).
> - Las liquidaciones de Apple y Google se reciben mensualmente desde Irlanda como **operaciones intracomunitarias exentas de IVA y sin retención de IRPF en origen**, declarándose directamente en los modelos trimestrales habituales (Modelo 130 de IRPF y Modelos 303/349 de IVA).

---

## 2. Tamaño y Tendencias del Mercado (2025–2026)

El sector de aplicaciones móviles de jardinería doméstica e identificación botánica vive un crecimiento sostenido impulsado por la tendencia de **plantas de interior en viviendas urbanas** (*urban jungle*) y la adopción de la **visión artificial (IA)**.

- **Mercado Global (TAM):** Valorado actualmente en más de **360 millones €** anuales (apps puras de identificación y cuidado), con proyección hacia los **920 millones €** en los próximos 7 años (crecimiento anual compuesto **CAGR del 12%–15%**).
- **Mercado Hispano y Catalán (SAM):** España y Latinoamérica representan más de **500 millones de hispanohablantes**, sumado a un nicho local de **~10 millones de hablantes de catalán** donde **no existe ninguna app de referencia con interfaz nativa en catalán**.
- **Comportamiento del Consumidor:** Fuerte rechazo y fatiga hacia las suscripciones recurrentes obligatorias de 30 € a 48 € al año para una utilidad doméstica.

---

## 3. Análisis de la Competencia

| App Competidora | Descargas Estimadas | Modelo de Cobro | Lo mejor | Punto débil (Tu oportunidad) |
| :--- | :--- | :--- | :--- | :--- |
| **Planta** | +10 Millones | Suscripción **35,99 € – 47,99 €/año** | Interfaz nórdica muy pulida, agendas de luz. | **Bloquea el abonado y trasplantes** en la versión gratis. Precio desorbitado para aficionados. |
| **PictureThis** | +100 Millones | Suscripción **39,99 €/año** | Identificación por foto en 2 segundos. | **Paywalls agresivos** continuos. Su gestor de riegos es secundario y rígido. |
| **Plant Parent** | +10 Millones | Suscripción **29,99 €/año** (o 7,99 €/mes) | Calendario visual para principiantes. | Casi cualquier función útil exige suscripción. |
| **Blossom** | +10 Millones | Suscripción **29,99 € – 39,99 €/año** | Artículos botánicos bonitos. | Cara; no resuelve el problema de la tierra aún húmeda. |
| **PlantNet** | +20 Millones | **100% Gratis** (Científica) | Gran base botánica mundial. | **No es una agenda de cuidados** (no avisa cuándo regar ni abona macetas). |
| **🌱 Tu App** | Lanzamiento | **Freemium honesto** (Gratis hasta 5 plantas + Pago único) | **Riego + Abono gratis**, botón **`⏳ +1d` (tierra húmeda)**, Verano/Invierno, Galería con fechas, Calendario y **Catalán/Español**. | Marca nueva; requiere posicionamiento orgánico (ASO) y apoyo de comunidad. |

---

## 4. Estructura de Costes Reales (Gastos Fijos y Variables)

Al guardar todas las imágenes, plantas e historial en el almacenamiento interno del propio teléfono (*Local-First*), **no hay costes de servidores ni bases de datos en la nube**.

| Concepto | Tipo de Coste | Importe | Notas |
| :--- | :--- | :--- | :--- |
| **Cuota de Autónomos (Seguridad Social)** | Fijo mensual | **0,00 €** | Ya cubierto por tu actividad profesional actual. |
| **Google Play Console** (Android) | Pago único | **~23,00 €** (25 USD) | Licencia de por vida para publicar apps ilimitadas. |
| **Apple Developer Program** (iOS) | Anual | **99,00 € / año** | Requerido por Apple para mantener la app en App Store. |
| **Base de datos / Servidores** | Mensual | **0,00 €** | Arquitectura local en el dispositivo del usuario. |
| **Gestión de compras (RevenueCat)** | Mensual | **0,00 €** | Gratuito hasta superar los 2.500 USD de facturación mensual. |
| **API de Visión IA (Gemini Flash)** | Variable por uso | **~0,0008 € / escaneo** | 1.000 fotos escaneadas por usuarios cuestan solo **0,80 €**. |
| **Hosting web para Política de Privacidad** | Anual | **0,00 €** | Alojamientos gratuitos en GitHub Pages o Cloudflare Pages. |

> [!NOTE]
> **Inversión técnica total para el Año 1:**
> - Lanzando solo en **Android**: **23,00 €** (pago único de por vida).
> - Lanzando en **Android + iPhone**: **122,00 €** el primer año (**99,00 €/año** a partir del segundo).

---

## 5. Estrategia de Precios y Margen Neto

Se adopta el modelo de **pago único de por vida** para romper el mercado frente a las suscripciones de 40 €/año:

- **Precio de Lanzamiento (Oferta especial):** **4,99 €**
- **Precio Definitivo:** **7,99 €** (o **8,99 €**)

### Desglose de ingresos por venta en España (IVA 21% y comisión Apple/Google 15%):
- **A 4,99 €:** 
  - Base neta sin IVA: 4,12 €
  - Comisión de la tienda (-15%): -0,62 €
  - **Ingreso neto limpio en tu cuenta bancaria: 3,50 € / venta**
- **A 7,99 €:**
  - Base neta sin IVA: 6,60 €
  - Comisión de la tienda (-15%): -0,99 €
  - **Ingreso neto limpio en tu cuenta bancaria: 5,61 € / venta** (+60% de margen)

---

## 6. Previsión Financiera a 12 Meses (3 Escenarios)

Estimación combinando compras de la versión Pro (lanzamiento a 4,99 € y consolidación a 7,99 €, media neta de ~4,50 €) más ingresos pasivos por afiliación de Amazon (sustratos y fertilizantes recomendados en cada ficha):

### Escenario 1: Conservador (Crecimiento 100% orgánico sin apenas difusión)
- **Descargas en el Año 1:** 1.800 descargas (~150 al mes).
- **Conversión a Pro (2,5%):** 45 ventas × 4,50 € netos = **202,50 €**
- **Ingresos por Afiliados (Amazon):** **55,00 €**
- **Ingresos Netos Totales:** **257,50 €**
- **Gastos Técnicos (Apple 99 € + Google 23 € + IA):** **-124,00 €**
- **Resultado Neto Año 1:** **+133,50 € de beneficio** *(o **+232,50 €** si se lanza primero solo en Android).*

### Escenario 2: Moderado / Realista (Buen ASO + Colaboraciones con micro-creadores)
- **Descargas en el Año 1:** 16.000 descargas (~1.300 al mes).
- **Conversión a Pro (3,5%):** 560 ventas × 4,50 € netos = **2.520,00 €**
- **Ingresos por Afiliados (Amazon):** **640,00 €**
- **Ingresos Netos Totales:** **3.160,00 €**
- **Gastos Técnicos (Apple 99 € + Google 23 € + IA ~15 €):** **-137,00 €**
- **Resultado Neto Año 1:** **+3.023,00 € de beneficio limpio**

### Escenario 3: Optimista (Referente en el nicho España/Catalunya + Viralidad en redes)
- **Descargas en el Año 1:** 55.000 descargas (~4.500 al mes).
- **Conversión a Pro (4,0%):** 2.200 ventas × 4,80 € netos = **10.560,00 €**
- **Ingresos por Afiliados (Amazon / Viveros):** **2.200,00 €**
- **Ingresos Netos Totales:** **12.760,00 €**
- **Gastos Técnicos (Apple 99 € + Google 23 € + IA ~60 €):** **-182,00 €**
- **Resultado Neto Año 1:** **+12.578,00 € de beneficio limpio**
