# swida assignment

# setup

- install frontend packages 
    ```
    $ cd frontend
    $ npm i
    ```
- run backend migrations
    ```
    $ cd backend
    $ python manage.py migrate
    ```
- start backend server
    ```
    $ cd backend
    $ ./runserver
    ```
- start frontend server 
    ```
    $ cd frontend
    $ npm run build
    $ npm run preview
    ```


# closing thoughts

Having never worked with django or vue, I mostly relied on online written tutorials to get me started and went from there. As a result, I unfortunately don't really have any reason or explanation behind my approach aside from "it just worked out that way". I did, however, decide to use a SPA approach to vue - going with what I'm already familiar with (in different frontend frameworks of course) instead of SSR. That decision did make it more difficult to integrate the frontend and backend (mostly due to time constraints) - so instead of having django directly serve the vue app, vue is served with the help of vite. As for assumptions - before going into this, I had assumed django was a lot more barebones than it is, I guess something akin to express in nodejs. I was under the assumption that I would not only have to figure out django, but also a python database library, so I was pleasantly surprised seeing django not only have a robust database integration, but also an admin panel with which you could easily view or edit the data. 