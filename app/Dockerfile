# Front mini-OrigaMe — build Vite puis service statique par nginx
# (plus « prod-ready » que vite preview, utilisé aujourd'hui sur OrigaMe)
# Phase C : épingler ces images par digest (@sha256:...)

FROM node:20-alpine AS build
WORKDIR /src
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /src/dist /usr/share/nginx/html
EXPOSE 80
