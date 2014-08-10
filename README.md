playing around with newspaper <https://github.com/codelucas/newspaper>

for setting up on a digital ocean droplet:

    apt-get install python-pip
    apt-get install libxml2-dev libxslt-dev
    sudo apt-get install libjpeg-dev zlib1g-dev libpng12-dev
    sudo apt-get install python-dev
    easy_install lxml
    pip install newspaper
    curl https://raw.github.com/codelucas/newspaper/master/download_corpora.py | python2.7
