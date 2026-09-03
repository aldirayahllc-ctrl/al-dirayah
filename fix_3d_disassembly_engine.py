import re

def fix_page(fname, is_escalators=False):
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Clean conflicting .pin styles
    content = re.sub(r'\.pin\s*\{\s*position:\s*relative;\s*height:\s*auto;[^\}]*\}', '', content)
    content = re.sub(r'\.pinwrap\s*\{\s*position:\s*relative;?[^\}]*\}', '', content)

    # 2. Inject robust Sticky Pin CSS
    pin_fix_css = '''
/* ══════════ REAL-TIME 3D DISASSEMBLY PINNED ENGINE FIX ══════════ */
.pinwrap {
  position: relative !important;
  box-sizing: border-box !important;
  width: 100% !important;
}
.pin {
  position: -webkit-sticky !important;
  position: sticky !important;
  top: 0 !important;
  height: 100vh !important;
  height: 100svh !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  align-items: center !important;
  overflow: hidden !important;
  z-index: 10 !important;
  padding: 1rem 0 !important;
  box-sizing: border-box !important;
}
.img-3d-container {
  position: relative !important;
  width: 100% !important;
  max-width: 540px !important;
  height: clamp(320px, 45vh, 520px) !important;
  margin: 0 auto !important;
  overflow: hidden !important;
  border-radius: 12px !important;
  box-shadow: 0 20px 50px rgba(0,0,0,0.8) !important;
}
.img-3d-layer {
  position: absolute !important;
  inset: 0 !important;
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  transition: opacity 0.1s ease-out, transform 0.1s ease-out !important;
  will-change: opacity, transform !important;
}
.mobile-3d-controls {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  width: 100%;
  max-width: 480px;
  margin: .8rem auto 0;
  padding: .6rem 1rem;
  background: rgba(21,26,32,0.85);
  border: 1px solid var(--line-2, #3A4550);
  border-radius: 8px;
}
.mobile-3d-controls input[type="range"] {
  width: 100%;
  accent-color: var(--amber, #E08A1E);
  cursor: pointer;
  height: 6px;
}
@media (max-width: 900px) {
  .pin {
    height: auto !important;
    min-height: 80vh !important;
    position: relative !important;
    padding: 2rem 0 !important;
  }
}
'''

    if ".pinwrap" in content:
        content = content.replace("</style>", pin_fix_css + "\n</style>")

    # 3. Add Mobile Slider Controls into Section 02 HTML if not present
    slider_html = '''
            <div class="mobile-3d-controls">
              <div style="display:flex;justify-content:space-between;font-family:var(--f-m);font-size:.65rem;color:var(--amber-lt);letter-spacing:1px;text-transform:uppercase">
                <span>01 · ASSEMBLED</span>
                <span>DRAG 3D SLIDER &rarr;</span>
                <span>06 · EXPLODED</span>
              </div>
              <input type="range" id="disassemblySlider" min="0" max="100" value="0" aria-label="3D Disassembly Control Slider">
            </div>
'''
    if 'id="disassemblySlider"' not in content:
        content = content.replace('</figure>', '</figure>\n' + slider_html)

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

    print("Applied Sticky 3D Disassembly engine fix to", fname)

fix_page("lifts.html", False)
fix_page("escalators.html", True)
