# jph.me

Personal website of Jan Philipp Harries, hosted on GitHub Pages.

## Structure

```
├── index.html                              # Homepage
├── essays/
│   └── a-country-full-of-geniuses/
│       ├── index.html                      # Essay page
│       └── images/                         # Essay images
├── bild4.jpg                               # Profile image
├── CNAME                                   # Custom domain config
├── robots.txt                              # Search engine config
├── sitemap.xml                             # Sitemap for indexing
└── .nojekyll                               # Disable Jekyll processing
```

## Updating Essay Content

To update the essay with a new version:

```bash
cp /path/to/new/html/index.html essays/a-country-full-of-geniuses/index.html
cp /path/to/new/html/images/* essays/a-country-full-of-geniuses/images/
```

## Local Testing

```bash
python3 -m http.server 3000
# Open http://localhost:3000
```

## Deployment

The site deploys automatically via GitHub Pages when pushing to `main`:

```bash
git add -A
git commit -m "Update site"
git push origin main
```
