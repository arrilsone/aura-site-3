# AURA Advisory · website

Landing site for AURA Advisory (Venture Intelligence), built from the partner deck.

## Versions

| Path | What it is |
|---|---|
| `/` (`index.html`) | **Main version.** One continuous scroll flight: two Kirlian coronas (investor and startup) drift together and fuse. Built with the Scroll Craft worldflight engine (`scrollcraft.js` / `scrollcraft.css`). |
| `/v1-threejs/` | First version: a Three.js eclipse with a Kirlian corona and the five-stage method drawn as orbital rings. Self-contained, Three.js loads from jsDelivr. |

## How the main page works

- `assets/leg1..5.mp4` are five consecutive cuts of one 15 s generated clip (Seedance 2, via MEGG), encoded with dense keyframes for scrubbing. `-m` files are portrait-cropped phone variants; `p1..5.webp` are posters taken from each leg's first frame.
- Scroll position drives the video playhead. Copy appears in fixed windows along the track (`data-sc-window`).
- The pointer is an "aura sensor": Kirlian strands around the cursor and hidden readings revealed under it (desktop with a fine pointer only; off on touch and with reduced motion).
- The contact form is a front-end preview only. It does not send anything until it is wired to an endpoint.

## Run locally

Any static server works, for example:

```bash
npx serve .
# or
python3 -m http.server 8000
```

Videos need a browser with H.264 support (Chrome, Safari, Edge, Firefox).

## Deploy

Works as-is on GitHub Pages (Settings → Pages → Deploy from branch → `main` / root), Netlify or Vercel.

## Editing

`src/page.tpl.html` is the page template and `src/build.py` fills in the track numbers (leg weights, copy windows, map). The creative brief is in `BRIEF.md`.
