# Mini OrigaMe — banc d'essai CI/CD sécurisée

Réplique miniature d'OrigaMe pour apprendre et valider le pipeline **avant** de le poser sur le vrai projet.
Même structure, mêmes technos, mêmes workflows :

| Dossier | Contenu | Équivalent OrigaMe |
|---|---|---|
| `server/` | Spring Boot 2.7, Java 8, Maven, routes `/api/hello`, `/api/version`, `/actuator/health`, 3 tests JUnit | `server/` |
| `app/` | Vue 3 + Vite + TypeScript, ESLint, vue-tsc, Vitest (1 test) | `app/` |
| `.github/workflows/ci.yml` | **Phase A** — build + tests front et back en parallèle | identique |
| `.github/workflows/security.yml` | **Phase B** — gitleaks (secrets) + Trivy (dépendances) | identique |
| `.github/dependabot.yml` | PR automatiques de mise à jour | quasi identique |
| `.trivyignore` | Exceptions de sécurité datées | identique |

Les anciens fichiers d'essai Git (`*.txt`, `src/`, `functions/`) ne sont pas utilisés par le pipeline.

---

## 1. Installation (une seule fois, en local)

Prérequis : Java 8+ et Maven, Node 20+.

```bash
git checkout -b ci-setup
# copier les fichiers de l'archive à la racine du dépôt, puis :

cd app
npm install          # génère package-lock.json — OBLIGATOIRE, la CI utilise "npm ci"
npm run type-check && npm run lint:ci && npm run test:unit -- --run && npm run build
cd ../server
mvn -B verify        # compile + 3 tests
cd ..

git add .
git commit -m "ci: mini OrigaMe + workflows CI et sécurité"
git push -u origin ci-setup
```

Puis sur GitHub : **ouvrir une Pull Request** `ci-setup` → `main`. Les jobs apparaissent en bas de la PR.

## 2. Lancer l'appli en local (facultatif)

```bash
cd server && mvn spring-boot:run        # http://localhost:8080/api/hello
cd app && npm run dev                   # http://localhost:5173 (affiche la version du back)
```

Avec Docker :

```bash
docker build -t mini-server --build-arg APP_VERSION=$(git rev-parse --short HEAD) server
docker run --rm -p 8080:8080 mini-server
curl localhost:8080/api/version
```

## 3. Rendre la CI obligatoire (protection de branche)

GitHub → **Settings → Branches → Add branch ruleset** (ou *branch protection rule*) sur `main` :
- ✅ Require a pull request before merging
- ✅ Require status checks to pass → cocher **Back (Spring Boot / Java 8)**, **Front (Vue / Node 20)**, **Secrets (gitleaks)**, **Dépendances (Trivy fs)**
- ✅ Block force pushes

Les noms des checks n'apparaissent dans la liste qu'après **un premier passage** des workflows.

## 4. Lire un échec

| Job rouge | Cause probable | Que faire |
|---|---|---|
| Back | test JUnit cassé, erreur de compilation | ouvrir le job → étape « Build + tests » ; rapports dans l'artefact `surefire-reports` |
| Front — `npm ci` | `package-lock.json` absent ou désynchronisé | `npm install` en local, commiter le lock |
| Front — Lint | erreur ESLint | `npm run lint` en local (corrige auto), commiter |
| Secrets | gitleaks a trouvé un secret | **le révoquer** chez le fournisseur, le retirer du code ; s'il est dans l'historique → baseline |
| Dépendances | CVE HIGH/CRITICAL corrigeable | monter la version ; sinon exception datée dans `.trivyignore` |

Relancer un run : onglet **Actions** → le run → **Re-run jobs**.

## 5. Démo « la CI bloque » (critère n°8 du ticket)

Sur une branche `demo-blocage`, une seule chose à la fois :

**Faux secret** — créer un faux jeton GitHub (la chaîne est coupée en deux ici pour que gitleaks ne bloque pas ce README) :
```bash
echo "github.token=ghp_""ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" > server/src/main/resources/demo-secret.properties
```
→ job **Secrets** rouge. Supprimer le fichier **et** refaire la branche (le secret reste dans l'historique sinon) → vert.

**Dépendance vulnérable** — dans `app/package.json`, ajouter `"lodash": "4.17.20"` aux `dependencies`, puis `npm install` :
→ job **Dépendances** rouge (CVE-2021-23337, HIGH, corrigée en 4.17.21). Passer à `4.17.21` → vert.

Ne **jamais** merger la branche de démo.

---

## Feuille de route

- [x] **Phase A** — build + tests
- [x] **Phase B** — secrets + dépendances
- [ ] **Phase C** — build des images Docker en CI (tag = SHA), scan Trivy image, SBOM, signature Cosign
- [ ] **Phase D** — push DOCR + déploiement + smoke tests (`/actuator/health`, `/api/version` = SHA)
- [ ] **Phase E** — politique écrite, OWASP ZAP baseline
