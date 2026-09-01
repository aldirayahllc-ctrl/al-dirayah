import re

solutions_section = '''
<!-- ══════════ 5 — SPECIALIZED SOLUTIONS (DROPDOWN / TAB SELECTOR) ══════════ -->
<section id="f5" class="pad" data-floor="5" data-label="Solutions" style="background:var(--ink-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
  <div class="wrap">
    <p class="eyebrow rv">05 — Solutions &amp; Services</p>
    <h2 class="big rv" data-d="1" style="font-size:clamp(2rem,5vw,3.4rem);margin-bottom:.6rem">Specialized Transport Offerings</h2>
    <p class="lede rv" data-d="2" style="margin-bottom:2.5rem">Select a specialized domain from the dropdown or tabs below to inspect tailored engineering specifications, custom configurators, and 3D architectural cutaway renders.</p>

    <!-- Dropdown / Tab Navigation Selector -->
    <div style="margin-bottom:2.5rem;display:flex;flex-wrap:wrap;gap:1rem;align-items:center;justify-content:space-between">
      <!-- Desktop Tabs -->
      <div class="sol-tabs" style="display:flex;gap:.5rem;background:rgba(14,17,21,0.8);padding:4px;border-radius:10px;border:1px solid var(--line)">
        <button class="sol-tab active" onclick="switchSolTab(0)" id="solTab0">🏡 Residential Villa Elevators</button>
        <button class="sol-tab" onclick="switchSolTab(1)" id="solTab1">🏢 Commercial Tower Elevators</button>
        <button class="sol-tab" onclick="switchSolTab(2)" id="solTab2">🛠 Maintenance &amp; Fit-Out</button>
        <button class="sol-tab" onclick="switchSolTab(3)" id="solTab3">📐 Engineering &amp; Safety Audits</button>
      </div>

      <!-- Mobile Dropdown Selector -->
      <div class="sol-dropdown-wrap" style="width:100%;max-width:340px;">
        <select id="solSelect" onchange="switchSolTab(parseInt(this.value))" style="width:100%;background:var(--surface);border:1px solid var(--amber);color:var(--paper);padding:.75rem 1rem;font-family:var(--f-m);font-size:.85rem;border-radius:8px">
          <option value="0">🏡 01 — Residential Villa Elevators</option>
          <option value="1">🏢 02 — Commercial Tower Elevators</option>
          <option value="2">🛠 03 — Maintenance & Fit-Out Works</option>
          <option value="3">📐 04 — Engineering & Safety Audits</option>
        </select>
      </div>
    </div>

    <!-- Tab 0: Residential Villa Elevators -->
    <div class="sol-panel" id="solPanel0" style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center">
      <div>
        <span class="badge" style="font-family:var(--f-m);color:var(--amber-lt);background:rgba(224,138,30,0.12);padding:.3rem .75rem;border-radius:4px;border:1px solid var(--amber-dim);display:inline-block;margin-bottom:1rem">01 · PRIVATE VILLA ESTATES</span>
        <h3 style="font-family:var(--f-d);font-size:2.2rem;color:var(--white);margin-bottom:1rem">Custom Luxury Villa Elevators</h3>
        <p style="color:var(--steel-lt);font-size:1rem;margin-bottom:1.5rem;line-height:1.65">Seamlessly integrated Machine-Room-Less (MRL) gearless and hydraulic residential lifts. Certified to EN 81-41 standards with bespoke Italian marble, champagne gold, and 360° panoramic glass finishes.</p>
        
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:2rem">
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">CAPACITY RANGE</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">320 kg – 630 kg</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">NOISE RATING</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">&lt; 40 dB Silent</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">MINIMUM PIT</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">200 mm Low-Pit</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">STANDARDS</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">EN 81-41 Villa</b>
          </div>
        </div>

        <a href="residential-elevators.html" class="big-cta" style="display:inline-flex;align-items:center;gap:.6rem;padding:.75rem 1.6rem;font-size:.9rem">Open Full Villa Configurator &rarr;</a>
      </div>
      <figure style="margin:0;position:relative;border-radius:14px;overflow:hidden;border:1px solid var(--amber-dim);box-shadow:0 20px 50px rgba(0,0,0,0.8)">
        <img src="residential_lift_3d.jpg" alt="3D Luxury Villa Panoramic Elevator" style="width:100%;height:auto;display:block">
        <div style="position:absolute;bottom:1rem;left:1rem;background:rgba(14,17,21,0.9);backdrop-filter:blur(10px);padding:.8rem 1.2rem;border-radius:8px;border:1px solid var(--amber-dim)">
          <div style="font-family:var(--f-d);font-size:1rem;color:var(--white);font-weight:600">Bespoke Circular Glass Lift</div>
          <div style="font-size:.78rem;color:var(--amber-lt);font-family:var(--f-m)">EN 81-41 Certified • Abu Dhabi Villa Estate</div>
        </div>
      </figure>
    </div>

    <!-- Tab 1: Commercial Tower Elevators -->
    <div class="sol-panel" id="solPanel1" style="display:none;grid-template-columns:1fr 1fr;gap:3rem;align-items:center">
      <div>
        <span class="badge" style="font-family:var(--f-m);color:var(--amber-lt);background:rgba(224,138,30,0.12);padding:.3rem .75rem;border-radius:4px;border:1px solid var(--amber-dim);display:inline-block;margin-bottom:1rem">02 · HIGH-RISE TOWERS</span>
        <h3 style="font-family:var(--f-d);font-size:2.2rem;color:var(--white);margin-bottom:1rem">Commercial Skyscraper Elevators</h3>
        <p style="color:var(--steel-lt);font-size:1rem;margin-bottom:1.5rem;line-height:1.65">High-capacity passenger, heavy freight, and hospital stretcher elevator installations for commercial towers, hotels, and government headquarters across Abu Dhabi &amp; Dubai. Certified to EN 81-20/50.</p>
        
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:2rem">
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">HIGH SPEED</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">Up to 4.0 m/s</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">PAYLOAD RANGE</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">1,000 kg – 5,000 kg</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">DISPATCH CONTROLS</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">Smart Kiosk Kiosks</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">FIRE RATING</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">EN 81-72 Firefighting</b>
          </div>
        </div>

        <a href="commercial-elevators.html" class="big-cta" style="display:inline-flex;align-items:center;gap:.6rem;padding:.75rem 1.6rem;font-size:.9rem">Explore Commercial Elevators &rarr;</a>
      </div>
      <figure style="margin:0;position:relative;border-radius:14px;overflow:hidden;border:1px solid var(--amber-dim);box-shadow:0 20px 50px rgba(0,0,0,0.8)">
        <img src="commercial_tower_lift_3d.jpg" alt="Commercial Skyscraper Elevator Bank" style="width:100%;height:auto;display:block">
        <div style="position:absolute;bottom:1rem;left:1rem;background:rgba(14,17,21,0.9);backdrop-filter:blur(10px);padding:.8rem 1.2rem;border-radius:8px;border:1px solid var(--amber-dim)">
          <div style="font-family:var(--f-d);font-size:1rem;color:var(--white);font-weight:600">Destination Control Elevator Bank</div>
          <div style="font-size:.78rem;color:var(--amber-lt);font-family:var(--f-m)">High-Speed 4.0 m/s • Abu Dhabi Tower</div>
        </div>
      </figure>
    </div>

    <!-- Tab 2: Maintenance & Fit-Out -->
    <div class="sol-panel" id="solPanel2" style="display:none;grid-template-columns:1fr 1fr;gap:3rem;align-items:center">
      <div>
        <span class="badge" style="font-family:var(--f-m);color:var(--amber-lt);background:rgba(224,138,30,0.12);padding:.3rem .75rem;border-radius:4px;border:1px solid var(--amber-dim);display:inline-block;margin-bottom:1rem">03 · 24/7 RAPID DISPATCH</span>
        <h3 style="font-family:var(--f-d);font-size:2.2rem;color:var(--white);margin-bottom:1rem">Maintenance &amp; Cabin Fit-Out</h3>
        <p style="color:var(--steel-lt);font-size:1rem;margin-bottom:1.5rem;line-height:1.65">Comprehensive 24/7 annual maintenance contracts (AMC), full microprocessor control panel modernization, and bespoke luxury cabin interior fit-outs for residential and commercial properties across Abu Dhabi &amp; UAE.</p>
        
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:2rem">
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">EMERGENCY SLA</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">&lt; 30 Min Dispatch</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">ENERGY SAVINGS</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">Up to 40% VVVF</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">CABIN FIT-OUT</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">Backlit Onyx &amp; COP</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">SAFETY CLEARANCE</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">Civil Defence Approved</b>
          </div>
        </div>

        <a href="maintenance-modernization.html" class="big-cta" style="display:inline-flex;align-items:center;gap:.6rem;padding:.75rem 1.6rem;font-size:.9rem">View AMC Maintenance Packages &rarr;</a>
      </div>
      <figure style="margin:0;position:relative;border-radius:14px;overflow:hidden;border:1px solid var(--amber-dim);box-shadow:0 20px 50px rgba(0,0,0,0.8)">
        <img src="maintenance_modernization_3d.jpg" alt="Modernized Elevator Cabin Interior Fit-out" style="width:100%;height:auto;display:block">
        <div style="position:absolute;bottom:1rem;left:1rem;background:rgba(14,17,21,0.9);backdrop-filter:blur(10px);padding:.8rem 1.2rem;border-radius:8px;border:1px solid var(--amber-dim)">
          <div style="font-family:var(--f-d);font-size:1rem;color:var(--white);font-weight:600">Luxury Cabin Refurbishment</div>
          <div style="font-size:.78rem;color:var(--amber-lt);font-family:var(--f-m)">Mirror Stainless &amp; Onyx • Touchscreen COP</div>
        </div>
      </figure>
    </div>

    <!-- Tab 3: Engineering Services -->
    <div class="sol-panel" id="solPanel3" style="display:none;grid-template-columns:1fr 1fr;gap:3rem;align-items:center">
      <div>
        <span class="badge" style="font-family:var(--f-m);color:var(--amber-lt);background:rgba(224,138,30,0.12);padding:.3rem .75rem;border-radius:4px;border:1px solid var(--amber-dim);display:inline-block;margin-bottom:1rem">04 · HIGH-PRECISION VTI</span>
        <h3 style="font-family:var(--f-d);font-size:2.2rem;color:var(--white);margin-bottom:1rem">Engineering &amp; Safety Audits</h3>
        <p style="color:var(--steel-lt);font-size:1rem;margin-bottom:1.5rem;line-height:1.65">Specialized traffic calculation simulations, EN 81-20/50 third-party compliance audits, 3D BIM shaft load modeling, and Civil Defence safety certification by Al Dirayah Electromechanical Contracting LLC.</p>
        
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:2rem">
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">TRAFFIC SIMULATION</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">CIBSE Guide D / ISO</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">BIM CAD MODELING</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">Revit 3D Shaft Loads</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">SAFETY AUDITS</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">EN 81-20/50 Third-Party</b>
          </div>
          <div style="background:var(--surface);padding:1rem;border-radius:8px;border-left:3px solid var(--amber)">
            <span style="font-family:var(--f-m);font-size:.7rem;color:var(--steel);display:block">GREEN BUILDING</span>
            <b style="font-family:var(--f-d);font-size:1.15rem;color:var(--white)">Estidama &amp; LEED</b>
          </div>
        </div>

        <a href="engineering-services.html" class="big-cta" style="display:inline-flex;align-items:center;gap:.6rem;padding:.75rem 1.6rem;font-size:.9rem">Open Traffic Calculator &amp; Audits &rarr;</a>
      </div>
      <figure style="margin:0;position:relative;border-radius:14px;overflow:hidden;border:1px solid var(--amber-dim);box-shadow:0 20px 50px rgba(0,0,0,0.8)">
        <img src="engineering_audit_3d.jpg" alt="3D Structural Shaft Analysis" style="width:100%;height:auto;display:block">
        <div style="position:absolute;bottom:1rem;left:1rem;background:rgba(14,17,21,0.9);backdrop-filter:blur(10px);padding:.8rem 1.2rem;border-radius:8px;border:1px solid var(--amber-dim)">
          <div style="font-family:var(--f-d);font-size:1rem;color:var(--white);font-weight:600">BIM 3D Shaft Load Analysis</div>
          <div style="font-size:.78rem;color:var(--amber-lt);font-family:var(--f-m)">ISO 22559 • EN 81-20/50 Compliance</div>
        </div>
      </figure>
    </div>
  </div>
</section>

<style>
.sol-tab{padding:.55rem 1.15rem;font-family:var(--f-m);font-size:.8rem;color:var(--steel);background:transparent;border:none;border-radius:7px;cursor:pointer;transition:all .2s}
.sol-tab:hover{color:var(--white);background:rgba(255,255,255,0.06)}
.sol-tab.active{color:var(--amber-lt);background:var(--surface);border:1px solid var(--amber-dim);font-weight:600}
@media(max-width:960px){
  .sol-tabs{display:none !important}
  .sol-panel{grid-template-columns:1fr !important}
}
@media(min-width:961px){
  .sol-dropdown-wrap{display:none !important}
}
</style>

<script>
function switchSolTab(idx){
  for(var i=0;i<4;i++){
    var t=document.getElementById("solTab"+i);
    var p=document.getElementById("solPanel"+i);
    if(t) t.classList.toggle("active", i===idx);
    if(p) p.style.display = (i===idx) ? "grid" : "none";
  }
  var sel=document.getElementById("solSelect");
  if(sel) sel.value = idx.toString();
}
</script>
'''

with open("lifts.html", "r", encoding="utf-8") as f:
    content = f.read()

# Insert before section #ph
content = content.replace('<!-- ══════════ PH — CONTACT ══════════ -->', solutions_section + '\n<!-- ══════════ PH — CONTACT ══════════ -->')

with open("lifts.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully inserted Solutions section into lifts.html")
