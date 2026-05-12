# CLAUDE.md

## Deployment

The site is hosted on GitHub Pages. To deploy:

```bash
git add -A
git commit -m "Update site"
git push origin main
```

Changes go live automatically after pushing to `main` (typically within ~30s–2min).

Verify the deployment by polling the public URL until it returns 200:

```bash
until curl -s -o /dev/null -w "%{http_code}" https://jph.me/<path>/ | grep -q "200"; do sleep 8; done && echo LIVE
```

## Adding / Updating an Essay

Each essay lives in `essays/<slug>/` with an `index.html` and an `images/` folder. Essay HTML is authored elsewhere (e.g. `/Users/jph/dev2/ai-progress-research/<project>/html/`) and then mirrored into this repo with site-specific customizations applied on top.

The source HTML uses the same design system (CSS custom properties like `--amber`, `--horizon`, `--wide-width`, the `.progress-bar` element near the top of `<body>`, etc.), so the customizations below all hook into known anchors.

### 1. Copy files

```bash
SLUG="<essay-slug>"
SRC="/path/to/source/html"
mkdir -p essays/$SLUG/images
cp "$SRC/index.html" essays/$SLUG/index.html
cp "$SRC/images/"* essays/$SLUG/images/
```

### 2. Re-apply site customizations to the essay's `index.html`

These edits are needed because the source HTML doesn't include them. Use the essay's slug everywhere.

- **OG image** (absolute URL): change `content="images/<hero-image-filename>"` to `content="https://jph.me/essays/<slug>/images/<hero-image-filename>"`. The hero image filename is whatever the source file already sets in `<meta property="og:image">`.
- **Canonical URL**: add `<link rel="canonical" href="https://jph.me/essays/<slug>/">` immediately before the `<!-- Fonts -->` comment.
- **Back-link CSS**: add `.site-nav a:hover { color: var(--amber) !important; }` immediately before `</style>`.
- **Back-link nav**: add immediately before the `<div class="progress-bar"` element (this puts the `← jph.me` link in the fixed top bar):

  ```html
  <nav class="site-nav" style="position: fixed; top: 12px; left: max(1rem, calc((100vw - var(--wide-width)) / 2)); z-index: 101; font-family: var(--font-ui); font-size: 13px; letter-spacing: 0.02em;">
      <a href="/" style="color: var(--horizon); text-decoration: none; border-bottom: none; transition: color 0.2s;">&#8592; jph.me</a>
  </nav>
  ```

### 3. Prune unreferenced images

Source `images/` folders often include unused variants (multiple hero candidates, draft figures, replaced charts). List what the HTML actually references and delete the rest before resizing — saves space in the git repo and skips wasted resize work:

```bash
cd essays/$SLUG/images
referenced=$(grep -oE 'src="images/[^"?]+' ../index.html | sed 's|src="images/||' | sort -u)
for f in *; do
  [ -f "$f" ] && ! echo "$referenced" | grep -qx "$f" && rm -v "$f"
done
```

Also cross-check the `og:image` filename — sometimes it's set in `<meta>` but not used in `<img src>`, so don't blindly delete based on `src` alone.

### 4. Compress images

Source images are typically 5000–6000 px wide at 300 DPI (5–9 MB each). Resize to max 2200 px wide (sufficient for 2× retina at max 1100 px display width):

```bash
cd essays/$SLUG/images
for f in *.png; do
  w=$(sips -g pixelWidth "$f" 2>/dev/null | awk '/pixelWidth/{print $2}')
  if [ "$w" -gt 2200 ] 2>/dev/null; then
    echo "Resizing $f (${w}px -> 2200px)"
    sips --resampleWidth 2200 "$f" >/dev/null 2>&1
  fi
done
```

This typically reduces total image size by ~10–20×.

> Gotcha: `sips` writes in place and fails silently with exit 13 inside the Claude Code sandbox (the resize "completes" but file sizes don't change). If you see exit 13 or unchanged sizes, rerun the loop with the sandbox disabled.

### 5. Update `sitemap.xml`

Add the new essay URL with today's date:

```xml
<url>
  <loc>https://jph.me/essays/<slug>/</loc>
  <lastmod>YYYY-MM-DD</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.9</priority>
</url>
```

### 6. Add the homepage link

Edit the `Essays` section in `/index.html` — add the new essay as the **first** (most recent) item in the `<ul class="item-list">`, following the existing format:

```html
<li><a href="essays/<slug>/">Essay Title</a> <span class="subtitle">(Month YYYY)</span></li>
```

The convention is "publish the essay file first, add the homepage link in a separate PR for final review" — keeps the essay URL working for sharing before the link goes public.

### Example essays

- `essays/a-country-full-of-geniuses/` — first essay, February 2026
- `essays/bottlenecks/` — second essay, May 2026

## Local Testing

```bash
uv run python3 -m http.server 3000
# Open http://localhost:3000
```

Do not use port 8000 (may conflict with other local projects).

Quick smoke-test of an essay's customizations without a browser:

```bash
curl -s http://localhost:3000/essays/<slug>/ | grep -E "canonical|og:image|site-nav"
```

## Site Structure

- `index.html` — Homepage (darioamodei.com-style, uses essay visual identity)
- `essays/<slug>/` — One folder per essay, each with its own `index.html` + `images/`
- `CNAME` — Custom domain config (`jph.me`)
- `robots.txt`, `sitemap.xml` — Google indexation (update sitemap when adding essays)
- `.nojekyll` — Disables GitHub Pages Jekyll processing
