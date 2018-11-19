FROM odoo:11.0

LABEL author="Devroy Blake <dkb@dkblake.com>"

COPY ./config /etc/odoo

COPY ./addons /mnt/extra-addons/custom-addons

RUN mkdir -p /mnt/extra-addons/project-addons 

#VOLUME [ "/mnt/project-addons" ]

WORKDIR /mnt/project-addons

RUN git clone https://github.com/necrodevz/project.git .

CMD [ "odoo" ]
