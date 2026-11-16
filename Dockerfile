FROM node:24-alpine AS build
WORKDIR /app
COPY package.json design-system.json ./
COPY scripts/ scripts/
COPY site/ site/
RUN npm run build:production && npm run check:production

FROM nginx:stable-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist-production/ /usr/share/nginx/html/
