# 🌿 Registre i Guia de Cures de Plantes

Aquest document conté el registre de totes les plantes de la llar (interior, balcó i aromàtiques), amb una taula resum per a consulta ràpida i fitxes tècniques detallades de cadascuna amb recomanacions específiques de dificultat, abonament, reg, llum, substrat i manteniment.

---

## 📋 Taula Resum de Cures

| Foto | Nom Comú | Nom Científic | Dificultat | Abonament (Tipus · Freqüència · Mesos) | Reg (Estiu) | Reg (Hivern) | Substrat | Mascotes |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- | :--- | :---: |
| [📷](./01_chamaedorea_elegans.jpeg) | **Palmera de saló** | *Chamaedorea elegans* | 🔵 Fàcil | Líquid plantes verdes · Cada 3-4 setmanes (Abr-Set) | 1-2 cops / setm. | Cada 10-14 dies | Universal + perlita | 🟢 Segura |
| [📷](./02_spathiphyllum_espatifil.jpeg) | **Espatifil·le** | *Spathiphyllum wallisii* | 🔵 Fàcil | Líquid plantes amb flor · Cada 15-20 dies (Mar-Oct) | 2 cops / setm. | 1 cop / setm. | Orgànic torba + perlita | 🔴 Tòxica |
| [📷](./03_anthurium_anturi.jpeg) | **Anturi rosa** | *Anthurium andreanum* | 🟡 Mitjana | Plantes flor/orquídies (dosi 1/2) · Cada 2-3 setmanes (Mar-Set) | 1 cop / setm. | Cada 10-12 dies | Porós (escorça + perlita) | 🔴 Tòxica |
| [📷](./04_pothos_epipremnum.jpeg) | **Potos penjant** | *Epipremnum aureum* | 🟢 Molt fàcil | Líquid plantes verdes · Cada 15 dies (Mar-Oct) | Cada 5-7 dies | Cada 10-15 dies | Universal + perlita | 🔴 Tòxica |
| [📷](./05_sansevieria_trifasciata.jpeg) | **Llengua de sogra (Gran)** | *Sansevieria trifasciata* | 🟢 Molt fàcil | Cactus/suculentes (suau) · 1 cop al mes (Mai-Ago) | Cada 15-20 dies | 1 cop al mes | Cactus / molt drenant | 🔴 Tòxica |
| [📷](./06_dracaena_tronc_brasil.jpeg) | **Tronc del Brasil** | *Dracaena fragrans* | 🔵 Fàcil | Líquid plantes verdes · Cada 3-4 setmanes (Abr-Set) | Cada 7-10 dies | Cada 15-20 dies | Universal + perlita | 🔴 Tòxica |
| [📷](./07_pothos_tutor_bambu.jpeg) | **Potos enfiladís** | *Epipremnum aureum* | 🟢 Molt fàcil | Líquid plantes verdes · Cada 15 dies (Mar-Oct) | Cada 5-7 dies | Cada 10-14 dies | Universal + perlita | 🔴 Tòxica |
| [📷](./08_callisia_fragrans.jpeg) | **Callisia (Cistella)** | *Callisia fragrans* | 🟢 Molt fàcil | Universal/suculentes (suau) · 1 cop al mes (Abr-Set) | 1-2 cops / setm. | Cada 10-15 dies | Universal drenant | 🟢 Segura |
| [📷](./09_romani_salvia_rosmarinus.jpeg) | **Romaní** | *Salvia rosmarinus* | 🔵 Fàcil | 🌱 Orgànic/Humus cuc · Cada 2 mesos (Mar-Jun) | 1 cop / setm. | Cada 15-20 dies | Molt porós, secà | 🟢 Segura |
| [📷](./10_menta_mentha.jpeg) | **Menta (Herba-sana)** | *Mentha spicata* | 🔵 Fàcil | 🌱 Orgànic hort/humus · Cada 3 setmanes (Mar-Set) | 2-3 cops / setm. | 1 cop / setm. | Ric en humus, fresc | 🟢 Segura |
| [📷](./11_farigola_thymus_vulgaris.jpeg) | **Farigola (Timó)** | *Thymus vulgaris* | 🔵 Fàcil | 🌱 Pessic d'humus a la base · 1 cop a l'any (Mar-Abr) | Cada 7-10 dies | Cada 2-3 setm. | Pobre, sec, drenant | 🟢 Segura |
| [📷](./12_calaminta_neveda.jpeg) | **Calaminta (Neveda)** | *Clinopodium nepeta* | 🔵 Fàcil | Líquid flor o ecològic · 1 cop al mes (Mai-Set) | 2 cops / setm. | Cada 10-15 dies | Universal drenant | 🟢 Segura |
| [📷](./13_sansevieria_esqueix.jpeg) | **Llengua de sogra (Esqueix)** | *Sansevieria trifasciata* | 🟢 Molt fàcil | Cactus (molt diluït) · 1 sol cop a l'estiu (Jun-Jul) | Cada 15-20 dies | Cada 4-5 setm. | Cactus / molt porós | 🔴 Tòxica |

---

## 🚨 Sistema d'Alertes i Històric a l'Aplicació Web (`index.html`)

A la versió web [**index.html**](./index.html) s'ha implementat el sistema de seguiment actiu:

1. **Càlcul automàtic de la propera data**:
   - En clicar a **`💧 Regar avui`** o **`🧪 Abonar avui`**, el sistema enregistra la data i hora exactes.
   - Segons l'època de l'any (estiu vs. tardor/hivern), calcula automàticament quants dies falten per al proper reg o abonament.
2. **Codi d'alertes per colors**:
   - 🔴 **Vermell (Alerta urgent)**: Toca regar o abonar avui, o porta dies de retard.
   - 🟡 **Groc (Avís preventiu)**: Falten 1 o 2 dies perquè toqui regar.
   - 🟢 **Verd (Al dia)**: La planta està hidratada i alimentada.
   - ❄️ **Blau (Repòs hivernal)**: A la tardor i hivern s'activa l'estat de repòs per a l'adob, recordant que no s'ha d'aplicar fins a la primavera.
   - ⚪ **Gris**: Sense registre previ.
3. **Històric complet**:
   - Fent clic a l'enllaç **`📜 Històric`** de cada planta es pot consultar tot el llistat de regs i adobs anteriors amb opció d'eliminar entrades errònies.
4. **Còpies de seguretat (sense base de dades externa)**:
   - Botons superiors per **Descarregar còpia (`.json`)** i **Restaurar còpia**, garantint que mai es perdin les dades entre dispositius.
