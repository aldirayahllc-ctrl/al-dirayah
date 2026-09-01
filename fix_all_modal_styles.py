import os, re

files = [
    "index.html", "lifts.html", "escalators.html", "al-dirayah-unified.html",
    "residential-elevators.html", "commercial-elevators.html",
    "maintenance-modernization.html", "engineering-services.html"
]

modal_css = '''
/* ══════════ REQUEST SURVEY MODAL STYLING ══════════ */
.modal-overlay {
  position: fixed !important;
  inset: 0 !important;
  z-index: 9999 !important;
  background: rgba(10,13,16,.88) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  display: none;
  place-items: center !important;
  padding: 1.5rem !important;
  overflow-y: auto !important;
}
.modal-overlay.active {
  display: grid !important;
}
.modal-card {
  background: #151A20 !important;
  border: 1px solid #E08A1E !important;
  border-radius: 12px !important;
  max-width: 580px !important;
  width: 100% !important;
  padding: 2.2rem !important;
  box-shadow: 0 25px 60px rgba(0,0,0,0.9) !important;
  position: relative !important;
  box-sizing: border-box !important;
  margin: auto !important;
}
.modal-card h3 {
  font-family: "Barlow Condensed", "Arial Narrow", sans-serif !important;
  font-size: 2.2rem !important;
  color: #ffffff !important;
  margin: 0 0 .4rem 0 !important;
  text-transform: uppercase !important;
  line-height: 1 !important;
}
.modal-card p {
  font-family: "IBM Plex Sans", system-ui, sans-serif !important;
  font-size: .9rem !important;
  color: #9AA3B0 !important;
  margin: 0 0 1.4rem 0 !important;
  line-height: 1.5 !important;
  max-width: 100% !important;
}
.modal-card form {
  display: grid !important;
  gap: .9rem !important;
  width: 100% !important;
}
.modal-card label {
  font-family: "IBM Plex Mono", ui-monospace, monospace !important;
  font-size: .66rem !important;
  letter-spacing: .14em !important;
  text-transform: uppercase !important;
  color: #F5A93C !important;
  display: flex !important;
  flex-direction: column !important;
  gap: .35rem !important;
  width: 100% !important;
  box-sizing: border-box !important;
}
.modal-card input,
.modal-card select,
.modal-card textarea {
  background: #1B2128 !important;
  border: 1px solid #3A4550 !important;
  color: #E9E7E2 !important;
  padding: .7rem .9rem !important;
  font-family: "IBM Plex Sans", system-ui, sans-serif !important;
  font-size: .9rem !important;
  border-radius: 4px !important;
  width: 100% !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
  display: block !important;
  outline: none !important;
}
.modal-card input:focus,
.modal-card select:focus,
.modal-card textarea:focus {
  border-color: #E08A1E !important;
  box-shadow: 0 0 12px rgba(224,138,30,0.35) !important;
}
.modal-close {
  position: absolute !important;
  right: 1.2rem !important;
  top: 1.2rem !important;
  background: transparent !important;
  border: none !important;
  color: #6E7885 !important;
  font-size: 1.8rem !important;
  cursor: pointer !important;
  line-height: 1 !important;
  padding: 0 !important;
}
.modal-close:hover {
  color: #F5A93C !important;
}
'''

for fname in files:
    if not os.path.exists(fname):
        continue
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove existing modal styles block if present
    content = re.sub(r'/\* ══════════ REQUEST SURVEY MODAL STYLING ══════════ \*/.*?\n\n', '', content, flags=re.DOTALL)
    content = re.sub(r'\.modal-overlay\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.modal-overlay\.active\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.modal-card\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.modal-card\s+h3\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.modal-card\s+p\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.modal-card\s+form\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.modal-card\s+label\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.modal-card\s+input[^{]*\{[^}]*\}', '', content)
    content = re.sub(r'\.modal-card\s+input:focus[^{]*\{[^}]*\}', '', content)
    content = re.sub(r'\.modal-close[^{]*\{[^}]*\}', '', content)
    content = re.sub(r'\.modal-close:hover[^{]*\{[^}]*\}', '', content)

    # Inject modal_css right before </style>
    if "</style>" in content:
        content = content.replace("</style>", modal_css + "\n</style>")

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected robust modal styles into", fname)

