# CLAUDE.md

## Deployment

The site is hosted on GitHub Pages. To deploy:

```bash
git add -A
git commit -m "Update site"
git push origin main
```

Changes go live automatically after pushing to `main`.

## Updating the Essay

The essay source lives at `/Users/jph/dev2/ai-progress-research/blogpost/html/`. Full update process:

### 1. Copy files

```bash
cp /Users/jph/dev2/ai-progress-research/blogpost/html/index.html essays/a-country-full-of-geniuses/index.html
cp /Users/jph/dev2/ai-progress-research/blogpost/html/images/* essays/a-country-full-of-geniuses/images/
```

### 2. Re-apply site customizations to the essay's `index.html`

These edits are needed because the source HTML doesn't include them:

- **OG image**: Change `content="images/graphic_02_country_full_of_geniuses.png"` to `content="https://jph.me/essays/a-country-full-of-geniuses/images/graphic_02_country_full_of_geniuses.png"`
- **Canonical URL**: Add `<link rel="canonical" href="https://jph.me/essays/a-country-full-of-geniuses/">` before the `<!-- Fonts -->` comment
- **Back-link CSS**: Add `.site-nav a:hover { color: var(--amber) !important; }` before `</style>`
- **Back-link nav**: Add before the `<div class="progress-bar"` element:
  ```html
  <nav class="site-nav" style="position: fixed; top: 12px; left: max(1rem, calc((100vw - var(--wide-width)) / 2)); z-index: 101; font-family: var(--font-ui); font-size: 13px; letter-spacing: 0.02em;">
      <a href="/" style="color: var(--horizon); text-decoration: none; border-bottom: none; transition: color 0.2s;">&#8592; jph.me</a>
  </nav>
  ```

### 3. Compress images

Source images are typically 5000-6000px wide at 300 DPI (5-9MB each). Resize to max 2200px wide (sufficient for 2x retina at max 1100px display width):

```bash
cd essays/a-country-full-of-geniuses/images
for f in *.png; do
  w=$(sips -g pixelWidth "$f" 2>/dev/null | awk '/pixelWidth/{print $2}')
  if [ "$w" -gt 2200 ] 2>/dev/null; then
    echo "Resizing $f (${w}px -> 2200px)"
    sips --resampleWidth 2200 "$f" >/dev/null 2>&1
  fi
done
```

This typically reduces total image size from ~114MB to ~6MB.

## Local Testing

```bash
python3 -m http.server 3000
# Open http://localhost:3000
```

Do not use port 8000 (may conflict with other local projects).

## Site Structure

- `index.html` — Homepage (darioamodei.com-style, uses essay visual identity)
- `essays/a-country-full-of-geniuses/` — Essay page + images
- `CNAME` — Custom domain config (`jph.me`)
- `robots.txt`, `sitemap.xml` — Google indexation
- `.nojekyll` — Disables GitHub Pages Jekyll processing
