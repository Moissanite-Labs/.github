# Moissanite Labs website

The organization website lives at **https://moissanite-labs.github.io/.github/**.
The GitHub organization profile remains in `profile/README.md`.

An ecosystem-focused index is prepared at `docs/ml/index.html` for future `/ml` hosting alongside the main `docs/index.html` entry (including a future siliconcordat.com map).

## Develop

The site is static HTML, CSS, and image assets in `docs/`. No package install or build is required.

```sh
python3 scripts/check_site.py
python3 -m http.server 8000 --directory docs --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. Keep local asset paths relative so the site also works at GitHub Pages' `/.github/` project path. Core content and navigation are available without JavaScript.

## Publish

The `Website` workflow checks pull requests and publishes only `docs/` from `main` through GitHub Pages. Repository Pages settings use **GitHub Actions**. Deployment credentials come from the workflow's scoped GitHub token; the website contains no keys or access gate.

To roll back, revert the website change through a reviewed pull request. The next successful workflow deploys the reverted tree.

## Content and design

The site follows Exo's warm black, champagne gold (`--gold-flat`), and steel-blue palette, with an original Moissanite Labs crystal motif. Its diagrams illustrate the collaboration metaphor; they are not scientific crystal models.

Siliconcordat mission text and the six principles are carried on the public page in `docs/index.html` from the compass working proposal (with the public-site banner wording). Preserve that distinction and the project maturity labels when updating the site. Do not link private compass, constitution, credos, or weft implementation repositories from the published HTML.

The protected Exo site and pitch deck are references, not assets to republish. Do not add access tokens or confidential material to this repository.

### November 2026 ecosystem refresh

The site and organization profile distinguish early implementation (Exo), protocol work
(Ethos), design proposals (Exofab), a working local reference (Synbios), an
experimental reference (Synmerit), and the live Weft public site. The map and journey
express intended relationships, not a shipped integrated platform. Keep these
limitations next to capability claims.

ASKA Digital, Foundation-0, and Proven Commons appear as connected efforts, not M Labs
products. Weft is linked only at https://w3ft.org.

A merge to `main` publishes the site automatically. Keep the refresh in a PR until
production publication is explicitly authorized.
