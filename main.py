from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="API Fesicol - Escenario Apuesta 2025",
    description="API de Business Intelligence basada en el análisis prospectivo de Fesicol.",
    version="1.0.0"
)

# ─────────────────────────────────────────────
# DICCIONARIO DE DATOS - Fase 3: Preparación
# ─────────────────────────────────────────────
escenario_fesicol = {
    "organizacion": "Fesicol - Fondo de Empleados de Siemens en Colombia",
    "horizonte": "Año 2025",
    "escenario_apuesta": "Escenario de Ruptura: Transformación Digital y Economía Colaborativa",
    "variables_estrategicas": [
        {
            "id": "E1",
            "variable": "Administración de la Información",
            "situacion_actual": "La información es subutilizada y no se dispone de competencias organizacionales que permitan generar información de valor para la toma de decisiones.",
            "hipotesis_de_futuro": "Alcanzar un desempeño destacado en la administración y gestión de la información del macro y microentorno, mediante la incorporación de tecnologías de banca digital y banca móvil.",
            "solucion_propuesta": ["Banca Móvil", "Banca Digital"],
            "KPIs_2025": [
                "% de decisiones gerenciales basadas en datos",
                "Nivel de adopción de banca móvil entre asociados (%)",
                "Número de reportes de BI generados por mes",
                "Tiempo promedio de acceso a información estratégica (horas)"
            ]
        },
        {
            "id": "E2",
            "variable": "Tecnología de Punta",
            "situacion_actual": "Los procesos internos están definidos de forma lineal y no se cuenta con un área de I+D que realice vigilancia tecnológica ni incorpore tecnologías innovadoras.",
            "hipotesis_de_futuro": "Alcanzar competencias organizacionales que permitan vigilancia tecnológica y la incorporación oportuna de las últimas tecnologías bajo un enfoque de economía colaborativa.",
            "solucion_propuesta": ["Vigilancia Tecnológica", "Economía Colaborativa"],
            "KPIs_2025": [
                "Número de tecnologías nuevas incorporadas por año",
                "Inversión en I+D como % de los ingresos",
                "Índice de satisfacción de asociados con nuevos servicios digitales (%)",
                "Número de alianzas con fintechs o startups tecnológicas"
            ]
        },
        {
            "id": "E3",
            "variable": "Rentabilidad del Negocio",
            "situacion_actual": "Se compite con un portafolio de poca innovación, muy similar al sistema financiero tradicional, generando beneficios muy por debajo de las posibilidades reales.",
            "hipotesis_de_futuro": "Consolidar una estructura organizacional con competencias dinámicas y tecnologías novedosas que permita atender la creciente demanda de servicios financieros con rentabilidad superior al sector.",
            "solucion_propuesta": ["Competencias Dinámicas", "Portafolio Innovador"],
            "KPIs_2025": [
                "Rentabilidad sobre activos - ROA (%)",
                "Crecimiento de asociados activos año vs año (%)",
                "Número de nuevos productos financieros lanzados",
                "Índice de rentabilidad social de los programas"
            ]
        }
    ],
    "megatendencias_identificadas": [
        "Transformación Digital",
        "Economía Colaborativa",
        "Banca Móvil",
        "Vigilancia Tecnológica",
        "Competencias Dinámicas Organizacionales"
    ],
    "conclusion_ruptura": "Este escenario es disruptivo porque propone que Fesicol abandone su modelo tradicional para convertirse en una entidad financiera inteligente, basada en datos, con tecnología de banca móvil, vigilancia tecnológica activa y un enfoque de economía colaborativa. La ruptura ocurre cuando la organización pasa de subutilizar la información a convertirla en su principal activo estratégico para el año 2025."
}

# ─────────────────────────────────────────────
# HTML DASHBOARD
# ─────────────────────────────────────────────
HTML_DASHBOARD = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Fesicol — Escenario Apuesta 2025</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --navy:#0a1628;--navy2:#0f2040;--blue:#1a4fd6;--blue-light:#3b82f6;
  --accent:#00d4aa;--accent2:#f59e0b;--text:#e8edf5;--text-muted:#7a8ba8;
  --surface:#111e35;--surface2:#162240;--border:rgba(255,255,255,0.08)
}
body{background:var(--navy);color:var(--text);font-family:'DM Sans',sans-serif;min-height:100vh;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;background-image:linear-gradient(rgba(26,79,214,0.04) 1px,transparent 1px),linear-gradient(90deg,rgba(26,79,214,0.04) 1px,transparent 1px);background-size:40px 40px;pointer-events:none;z-index:0}
.glow{position:fixed;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(0,212,170,0.06) 0%,transparent 70%);top:-200px;right:-200px;pointer-events:none;z-index:0}
.glow2{position:fixed;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,rgba(26,79,214,0.08) 0%,transparent 70%);bottom:100px;left:-100px;pointer-events:none;z-index:0}
.wrapper{position:relative;z-index:1;max-width:1100px;margin:0 auto;padding:48px 24px 80px}
.header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:48px;gap:24px;flex-wrap:wrap}
.badge{display:inline-flex;align-items:center;gap:6px;background:rgba(0,212,170,0.12);border:1px solid rgba(0,212,170,0.3);color:var(--accent);font-size:11px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;padding:5px 12px;border-radius:20px;margin-bottom:16px}
.badge::before{content:'●';font-size:8px;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
h1{font-family:'Syne',sans-serif;font-size:clamp(28px,4vw,48px);font-weight:800;line-height:1.1;letter-spacing:-.02em}
h1 span{color:var(--accent)}
.subtitle{color:var(--text-muted);font-size:14px;margin-top:8px}
.year-pill{background:var(--surface2);border:1px solid var(--border);border-radius:16px;padding:12px 24px;text-align:center;flex-shrink:0}
.year-pill .yr{font-family:'Syne',sans-serif;font-size:36px;font-weight:800;color:var(--accent2)}
.year-pill .lbl{font-size:11px;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em}
.divider{height:1px;background:linear-gradient(90deg,var(--accent) 0%,rgba(26,79,214,.4) 40%,transparent 100%);margin-bottom:40px}
.section-label{font-size:11px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--text-muted);margin-bottom:16px}
.trends-row{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:48px}
.trend-chip{background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:8px 16px;font-size:13px;color:var(--text);transition:border-color .2s,color .2s;cursor:default}
.trend-chip:hover{border-color:var(--accent);color:var(--accent)}
.cards-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin-bottom:40px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px;position:relative;overflow:hidden;transition:transform .2s,border-color .2s}
.card:hover{transform:translateY(-3px)}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px}
.card.e1::before{background:linear-gradient(90deg,var(--accent),var(--blue-light))}
.card.e2::before{background:linear-gradient(90deg,var(--accent2),#f97316)}
.card.e3::before{background:linear-gradient(90deg,#a855f7,var(--blue-light))}
.card.e1:hover{border-color:rgba(0,212,170,.3)}
.card.e2:hover{border-color:rgba(245,158,11,.3)}
.card.e3:hover{border-color:rgba(168,85,247,.3)}
.card-id{font-family:'Syne',sans-serif;font-size:11px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;margin-bottom:8px}
.e1 .card-id{color:var(--accent)}.e2 .card-id{color:var(--accent2)}.e3 .card-id{color:#a855f7}
.card h2{font-family:'Syne',sans-serif;font-size:18px;font-weight:700;margin-bottom:20px;line-height:1.3}
.situation-box{background:rgba(255,255,255,.03);border-left:3px solid rgba(255,255,255,.1);border-radius:0 8px 8px 0;padding:12px 14px;margin-bottom:14px}
.situation-box .lbl,.future-box .lbl,.kpi-title{font-size:10px;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--text-muted);margin-bottom:6px}
.situation-box p{font-size:13px;color:var(--text-muted);line-height:1.6}
.future-box{border-left:3px solid var(--accent);border-radius:0 8px 8px 0;padding:12px 14px;margin-bottom:20px;background:rgba(0,212,170,.04)}
.e2 .future-box{background:rgba(245,158,11,.04);border-left-color:var(--accent2)}
.e3 .future-box{background:rgba(168,85,247,.04);border-left-color:#a855f7}
.future-box p{font-size:13px;line-height:1.6}
.solutions{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:20px}
.sol-tag{font-size:11px;font-weight:500;padding:4px 10px;border-radius:6px;border:1px solid}
.e1 .sol-tag{background:rgba(0,212,170,.1);border-color:rgba(0,212,170,.3);color:var(--accent)}
.e2 .sol-tag{background:rgba(245,158,11,.1);border-color:rgba(245,158,11,.3);color:var(--accent2)}
.e3 .sol-tag{background:rgba(168,85,247,.1);border-color:rgba(168,85,247,.3);color:#a855f7}
.kpi-title{margin-bottom:10px}
.kpi-list{list-style:none}
.kpi-list li{display:flex;align-items:flex-start;gap:10px;font-size:12px;color:var(--text-muted);padding:6px 0;border-bottom:1px solid var(--border);line-height:1.5}
.kpi-list li:last-child{border-bottom:none}
.kpi-list li::before{content:'›';font-size:16px;line-height:1;flex-shrink:0;margin-top:1px}
.e1 .kpi-list li::before{color:var(--accent)}.e2 .kpi-list li::before{color:var(--accent2)}.e3 .kpi-list li::before{color:#a855f7}
.conclusion-card{background:linear-gradient(135deg,rgba(26,79,214,.15) 0%,rgba(0,212,170,.08) 100%);border:1px solid rgba(0,212,170,.2);border-radius:16px;padding:32px;margin-bottom:40px;position:relative;overflow:hidden}
.conclusion-card::before{content:'"';position:absolute;top:-20px;left:20px;font-family:'Syne',sans-serif;font-size:160px;font-weight:800;color:rgba(0,212,170,.06);line-height:1;pointer-events:none}
.conclusion-card h3{font-family:'Syne',sans-serif;font-size:14px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin-bottom:16px}
.conclusion-card p{font-size:15px;line-height:1.8;position:relative}
.conclusion-card strong{color:var(--accent)}
.footer{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;padding-top:32px;border-top:1px solid var(--border)}
.footer-left{font-size:12px;color:var(--text-muted)}
.api-links{display:flex;gap:10px;flex-wrap:wrap}
.api-link{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:6px 14px;font-size:12px;font-family:monospace;color:var(--accent);text-decoration:none;transition:border-color .2s}
.api-link:hover{border-color:var(--accent)}
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.wrapper>*{animation:fadeUp .5s ease both}
.wrapper>*:nth-child(1){animation-delay:.05s}.wrapper>*:nth-child(2){animation-delay:.1s}
.wrapper>*:nth-child(3){animation-delay:.15s}.wrapper>*:nth-child(4){animation-delay:.2s}
.wrapper>*:nth-child(5){animation-delay:.25s}.wrapper>*:nth-child(6){animation-delay:.3s}
.cards-grid .card:nth-child(1){animation:fadeUp .5s ease .2s both}
.cards-grid .card:nth-child(2){animation:fadeUp .5s ease .3s both}
.cards-grid .card:nth-child(3){animation:fadeUp .5s ease .4s both}
</style>
</head>
<body>
<div class="glow"></div><div class="glow2"></div>
<div class="wrapper">
  <div class="header">
    <div>
      <div class="badge">API activa · Business Intelligence</div>
      <h1>Fesicol<br><span>Escenario Apuesta</span></h1>
      <p class="subtitle">Fondo de Empleados de Siemens en Colombia · Proyecto CRISP-DM</p>
    </div>
    <div class="year-pill">
      <div class="yr">2025</div>
      <div class="lbl">Horizonte</div>
    </div>
  </div>
  <div class="divider"></div>
  <div class="section-label">Megatendencias identificadas</div>
  <div class="trends-row">
    <div class="trend-chip">Transformación Digital</div>
    <div class="trend-chip">Economía Colaborativa</div>
    <div class="trend-chip">Banca Móvil</div>
    <div class="trend-chip">Vigilancia Tecnológica</div>
    <div class="trend-chip">Competencias Dinámicas Organizacionales</div>
  </div>
  <div class="section-label">Variables estratégicas</div>
  <div class="cards-grid">
    <div class="card e1">
      <div class="card-id">E1</div>
      <h2>Administración de la Información</h2>
      <div class="situation-box"><div class="lbl">Situación actual</div><p>La información es subutilizada y no se dispone de competencias para generar valor desde los datos.</p></div>
      <div class="future-box"><div class="lbl">Hipótesis de futuro</div><p>Desempeño destacado en gestión de información mediante banca digital y banca móvil, generando valor agregado para asociados.</p></div>
      <div class="solutions"><span class="sol-tag">Banca Móvil</span><span class="sol-tag">Banca Digital</span></div>
      <div class="kpi-title">KPIs 2025</div>
      <ul class="kpi-list">
        <li>% de decisiones gerenciales basadas en datos</li>
        <li>Nivel de adopción de banca móvil entre asociados (%)</li>
        <li>Número de reportes de BI generados por mes</li>
        <li>Tiempo promedio de acceso a información estratégica (horas)</li>
      </ul>
    </div>
    <div class="card e2">
      <div class="card-id">E2</div>
      <h2>Tecnología de Punta</h2>
      <div class="situation-box"><div class="lbl">Situación actual</div><p>Procesos lineales sin área de I+D ni vigilancia tecnológica. Sin innovación en productos y servicios.</p></div>
      <div class="future-box"><div class="lbl">Hipótesis de futuro</div><p>Competencias de vigilancia tecnológica e incorporación de tecnologías bajo enfoque de economía colaborativa, diferenciado de la banca tradicional.</p></div>
      <div class="solutions"><span class="sol-tag">Vigilancia Tecnológica</span><span class="sol-tag">Economía Colaborativa</span></div>
      <div class="kpi-title">KPIs 2025</div>
      <ul class="kpi-list">
        <li>Número de tecnologías nuevas incorporadas por año</li>
        <li>Inversión en I+D como % de los ingresos</li>
        <li>Índice de satisfacción de asociados con nuevos servicios digitales (%)</li>
        <li>Número de alianzas con fintechs o startups tecnológicas</li>
      </ul>
    </div>
    <div class="card e3">
      <div class="card-id">E3</div>
      <h2>Rentabilidad del Negocio</h2>
      <div class="situation-box"><div class="lbl">Situación actual</div><p>Portafolio sin innovación, similar a la banca tradicional. Beneficios por debajo de las posibilidades reales.</p></div>
      <div class="future-box"><div class="lbl">Hipótesis de futuro</div><p>Estructura con competencias dinámicas y tecnologías novedosas que permitan rentabilidad superior al promedio del sector.</p></div>
      <div class="solutions"><span class="sol-tag">Competencias Dinámicas</span><span class="sol-tag">Portafolio Innovador</span></div>
      <div class="kpi-title">KPIs 2025</div>
      <ul class="kpi-list">
        <li>Rentabilidad sobre activos — ROA (%)</li>
        <li>Crecimiento de asociados activos año vs año (%)</li>
        <li>Número de nuevos productos financieros lanzados</li>
        <li>Índice de rentabilidad social de los programas</li>
      </ul>
    </div>
  </div>
  <div class="conclusion-card">
    <h3>¿Por qué es un escenario disruptivo?</h3>
    <p>Este escenario es disruptivo porque propone que Fesicol abandone su modelo tradicional para convertirse en una entidad financiera inteligente, basada en datos, con tecnología de banca móvil, vigilancia tecnológica activa y un enfoque de economía colaborativa. La ruptura ocurre cuando la organización pasa de <strong>subutilizar la información</strong> a convertirla en su <strong>principal activo estratégico</strong> para el año 2025.</p>
  </div>
  <div class="footer">
    <div class="footer-left">API Fesicol v1.0 · CRISP-DM · FastAPI</div>
    <div class="api-links">
      <a class="api-link" href="/fesicol-estrategia">/fesicol-estrategia</a>
      <a class="api-link" href="/variables">/variables</a>
      <a class="api-link" href="/kpis">/kpis</a>
      <a class="api-link" href="/docs">/docs</a>
    </div>
  </div>
</div>
</body>
</html>"""


# ─────────────────────────────────────────────
# ENDPOINTS
# ─────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
def dashboard():
    """Dashboard visual del escenario estratégico de Fesicol 2025."""
    return HTML_DASHBOARD


@app.get("/fesicol-estrategia")
def fesicol_estrategia():
    """Devuelve el escenario de ruptura completo en JSON."""
    return escenario_fesicol


@app.get("/variables")
def listar_variables():
    """Devuelve solo los nombres e IDs de las variables estratégicas."""
    return {
        "variables": [
            {"id": v["id"], "nombre": v["variable"]}
            for v in escenario_fesicol["variables_estrategicas"]
        ]
    }


@app.get("/kpis")
def listar_kpis():
    """Devuelve todos los KPIs agrupados por variable estratégica."""
    return {
        "KPIs_Fesicol_2025": [
            {"variable": v["variable"], "kpis": v["KPIs_2025"]}
            for v in escenario_fesicol["variables_estrategicas"]
        ]
    }