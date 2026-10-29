# Moissanite Labs website

The organization website lives at **https://moissanite-labs.github.io/.github/**.
The GitHub organization profile remains in `profile/README.md`.

## Develop

The site is static HTML, CSS, JavaScript, and SVG in `docs/`. No package install or build is required.

```sh
python3 scripts/check_site.py
python3 -m http.server 8000 --directory docs --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. Keep local asset paths relative so the site also works at GitHub Pages' `/.github/` project path. Core content and navigation are available without JavaScript.

## Publish

The `Website` workflow checks pull requests and publishes only `docs/` from `main` through GitHub Pages. Repository Pages settings use **GitHub Actions**. Deployment credentials come from the workflow's scoped GitHub token; the website contains no keys or access gate.

To roll back, revert the website change through a reviewed pull request. The next successful workflow deploys the reverted tree.

## Content and design

The site follows Exo's warm black, orange, and steel-blue palette, with an original Moissanite Labs crystal motif. Its diagrams illustrate the collaboration metaphor; they are not scientific crystal models.

The source of the mission and ecosystem is the [constitution repository](https://github.com/Moissanite-Labs/constitution), especially `FOUNDER-VISION.md` and `SILICONCORDAT.md`. These documents are working proposals. Preserve that distinction and the project maturity labels when updating the site.

The protected Exo site and pitch deck are references, not assets to republish. Do not add access tokens or confidential material to this repository.
