# Front mini-OrigaMe — build Vite puis service statique par nginx
# (plus « prod-ready » que vite preview, utilisé aujourd'hui sur OrigaMe)
# Phase C : épingler ces images par digest (@sha256:...)

# Image de build en glibc (Debian), comme le runner Ubuntu de la CI où le build passe :
# avec Alpine (musl), "vite build" échouait (cause probable : binaires natifs Rollup/esbuild).
FROM node:20-slim AS build
WORKDIR /src
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /src/dist /usr/share/nginx/html
EXPOSE 80
