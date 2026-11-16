FROM node:24-alpine AS build
WORKDIR /app
COPY package.json design-system.json ./
COPY scripts/ scripts/
COPY site/ site/
RUN npm run build:production && npm run check:production

FROM nginx:stable-alpine
RUN sed -i '1iload_module modules/ngx_http_js_module.so;' /etc/nginx/nginx.conf \
 && sed -i '/^types {/a\    text/markdown md;' /etc/nginx/mime.types
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY nginx-accept.js /etc/nginx/nginx-accept.js
COPY --from=build /app/dist-production/ /usr/share/nginx/html/
