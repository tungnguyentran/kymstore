FROM nginx:stable

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY uwsgi_params /etc/nginx/uwsgi_params

USER root

RUN apt-get update
RUN apt-get install -y --no-install-recommends certbot python3-certbot-nginx

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

RUN useradd user
USER user
# RUN certbot --nginx --email "${CERTBOT_EMAIL}" --agree-tos --no-eff-email -d "${DOMAIN_LIST}"
