From nginx:alpine

#remove default nginx html

RUN rm -rf /usr/share/nginx/html/*

#Copy only frontend files

COPY frontend/  /usr/share/nginx/html/

CMD ["nginx", "-g", "daemon off;"]