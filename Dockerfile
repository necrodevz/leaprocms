FROM odoo:10.0

LABEL author=Devroy Blake <dkb@dkblake.com>

COPY ./config /etc/odoo

COPY ./addons /mnt/extra-addons

#RUN mkdir -p /mnt/project-addons 

#VOLUME [ "/mnt/project-addons" ]

#WORKDIR /mnt/project-addons

#RUN git clone https://github.com/necrodevz/project.git .

CMD [ "odoo" ]