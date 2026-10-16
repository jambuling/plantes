# 📋 Hoja de Ruta: De la Web Actual al Lanzamiento en Stores

Plan de acción paso a paso con todas las tareas técnicas, operativas y administrativas para llevar la aplicación desde su estado actual en [index.html](file:///Users/juanluisnaranjomora/Documents/Plantes/index.html) hasta las tiendas de **Google Play** y **App Store**.

---

## Fase 1: Adaptación del Código a Arquitectura «Multi-Usuario Local»

En el estado actual, el código tiene tus 15 plantas de muestra cargadas por defecto (`INITIAL_CATALOG`) y se conecta a la fila fija `'default'` de tu Supabase personal. Para lanzarla al público, debe funcionar **100% en local en el dispositivo de cada usuario**.

- [ ] **1.1. Eliminar datos fijos personales:**
  - Cambiar el catálogo inicial para que la app arranque con una **pantalla de bienvenida limpia** (*Onboarding* breve con botón *"Añade tu primera planta"*) o con **1 sola planta de ejemplo** que el usuario pueda editar o borrar.
- [ ] **1.2. Almacenamiento Local-First Autónomo:**
  - Desconectar la sincronización obligatoria con tu clave fija de Supabase.
  - Asegurar que todas las fotos, fechas de riego, notas y datos se guarden en la memoria interna del teléfono mediante **IndexedDB / SQLite local** (sin coste de servidor y funcionando sin conexión a internet).
- [ ] **1.3. Herramienta de Copia de Seguridad (Backup):**
  - Añadir dentro del modal de `⚙️ Preferencias` dos botones:
    - **📥 Exportar copia de seguridad:** Descarga un archivo con todas las plantas, riegos y fotos para guardarlo en Google Drive o iCloud.
    - **📤 Restaurar copia de seguridad:** Permite recuperar todos los datos si el usuario cambia de teléfono.
- [ ] **1.4. Lógica de Límites Freemium (Modelo 5 Plantas Gratis + Pro):**
  - Permitir añadir hasta 5 plantas con todas las funciones activas.
  - Al pulsar en *"Añadir planta"* teniendo 5, mostrar la ventana explicativa del **Pase Pro / Jardín Ilimitado** (con el precio de lanzamiento de 4,99 € o definitivo de 7,99 €).
- [ ] **1.5. Lógica del Escáner IA (Créditos de Bienvenida):**
  - Conceder **3 identificaciones por foto con IA gratuitas** a cada nuevo usuario para que experimente la velocidad de la herramienta.
  - Proteger la clave de API (Gemini/OpenAI) redirigiendo la petición a través de un proxy ligero y gratuito (*Cloudflare Worker*) para que nadie pueda extraer tu API Key privada desde la app.
  - El buscador manual de especies de la app permanecerá siempre gratuito e ilimitado rellenando todos los campos con 1 clic.

---

## Fase 2: Conversión a App Nativa Móvil (iOS & Android)

- [ ] **2.1. Inicializar Capacitor en el proyecto:**
  - Instalar Capacitor (`@capacitor/core`, `@capacitor/cli`, `@capacitor/android`, `@capacitor/ios`).
  - Configurar `capacitor.config.json` con el identificador del paquete (ejemplo: `com.tudominio.plantes`).
- [ ] **2.2. Adaptación visual de pantalla (*Safe Areas*):**
  - Añadir reglas CSS con `env(safe-area-inset-top)` y `env(safe-area-inset-bottom)` para que la cabecera y los botones respeten la isla dinámica, el *notch* y la barra inferior de gestos en iPhone y Android modernos.
  - Desactivar el rebote elástico no deseado del navegador web.
- [ ] **2.3. Notificaciones Locales Nativas:**
  - Integrar el plugin `@capacitor/local-notifications`.
  - Programar una alarma local diaria a las 09:00 AM que revise si hay plantas con riego o abono pendiente y lance un aviso nativo al teléfono: *"💧 Tienes 2 plantas por revisar hoy"*.
- [ ] **2.4. Integración de Pasarela de Pagos (In-App Purchases):**
  - Integrar el SDK de **RevenueCat** (plugin oficial de Capacitor).
  - Configurar el producto de pago único de por vida (*Non-Consumable Product*):
    - *Identificador:* `plantes_pro_lifetime`
    - *Precio promocional:* 4,99 € / *Precio estándar:* 7,99 €
  - RevenueCat se encarga automáticamente de procesar Apple Pay, Google Pay y el botón obligatorio de *"Restaurar compras"*.

---

## Fase 3: Preparación Legal y Cuentas de Desarrollador

- [ ] **3.1. Gestión Fiscal en Hacienda (0 €):**
  - Añadir el epígrafe secundario IAE en tu Modelo 036/037 (Epígrafe 763: *Programadores y profesionales de la informática*).
  - Solicitar el alta en el **ROI** (Registro de Operadores Intracomunitarios) si no lo tienes ya, para emitir/recibir facturas intracomunitarias sin IVA a Apple/Google Irlanda.
- [ ] **3.2. Cuenta de Google Play Console (Android):**
  - Registro en Google Play Console con pago único de **25 USD (~23 €)**.
  - Invitar a 12 testers conocidos durante 14 días (requisito actual de Google para cuentas personales nuevas antes de publicar en abierto).
- [ ] **3.3. Cuenta de Apple Developer Program (iOS):**
  - Registro en el Apple Developer Program (**99 €/año**).
  - Aceptar los acuerdos de aplicaciones de pago (*Paid Applications Agreement*) e introducir tu IBAN para recibir las transferencias mensuales.
- [ ] **3.4. Política de Privacidad y Soporte:**
  - Publicar una página web estática sencilla (en GitHub Pages / Cloudflare, coste 0 €) con la Política de Privacidad donde se detalle que las fotos y datos permanecen en el dispositivo del usuario.

---

## Fase 4: Material de Tienda y Lanzamiento

- [ ] **4.1. Icono de la Aplicación:**
  - Diseñar el icono oficial en alta resolución (1024x1024 px) con motivo botánico limpio y reconocible.
- [ ] **4.2. Capturas de Pantalla (Screenshots):**
  - Generar 4 o 5 capturas enmarcadas para iPhone y Android con textos breves en español y catalán:
    1. *Agenda de riego adaptada a verano e invierno.*
    2. *Botón `+1d` para posponer si la tierra sigue húmeda.*
    3. *Galería fotográfica con fechas para seguir la evolución.*
    4. *Control de abono, trasplantes y seguridad para mascotas.*
- [ ] **4.3. Textos ASO (Título, Subtítulo y Descripción):**
  - Redactar los textos optimizados con las palabras clave estudiadas para posicionar alto en búsquedas orgánicas en España y Latinoamérica.
- [ ] **4.4. Lanzamiento y Activación del Plan de Difusión:**
  - Publicación oficial en tiendas con precio de lanzamiento de **4,99 €**.
  - Contacto directo con micro-creadores de contenido botánico regalando licencias Pro y códigos para sorteos (según la [Estrategia de Promoción](file:///Users/juanluisnaranjomora/Documents/Plantes/ESTRATEGIA_PROMOCION.md)).
