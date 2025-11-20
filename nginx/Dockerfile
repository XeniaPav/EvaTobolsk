FROM nginx:latest

RUN mkdir -p /app/staticfiles

COPY nginx.conf /etc/nginx/nginx.conf

COPY static/ /usr/share/nginx/static/

EXPOSE 443