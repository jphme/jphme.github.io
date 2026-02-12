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

The essay source lives at `/Users/jph/dev2/ai-progress-research/blogpost/html/`. To update:

```bash
cp /Users/jph/dev2/ai-progress-research/blogpost/html/index.html essays/a-country-full-of-geniuses/index.html
cp /Users/jph/dev2/ai-progress-research/blogpost/html/images/* essays/a-country-full-of-geniuses/images/
```

After copying, re-apply the back-link nav and canonical URL to the essay's `index.html` (see the `<nav class="site-nav">` element and `<link rel="canonical">` tag near the top of the file).

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
