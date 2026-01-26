From nginx:alpine

#remove default nginx html

RUN rm -rf /usr/share/nginx/html/*

#Copy only frontend files

COPY .  /usr/share/nginx/html/

COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
