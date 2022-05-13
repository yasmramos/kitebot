git inithttps://git.heroku.com/kitedownldr.git

$ heroku login

$ cd my-project/
$ git init
$ heroku git:remote -a kitedownldr

$ git add .
$ git commit -am "make it better"
$ git push heroku master