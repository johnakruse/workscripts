#!/bin/bash

#to be honest, this is a pretty hacky script but it got the job done and it wasn't something I imagine would need to be maintained
#It would take a saved page, that had a bunch of form links on it which required an authorized login
#the user would provide the path to the saved HTML page, and a cookie file to login
#then it would use lynx to get all the links and use wget to download them
#there were always a predictable set of links I didn't want, so I just had vim open up the file and delete
#them before use
#after it fetched the forms, I made a list of the files and generated a list of commands to be read as
#standard input to wkhtmltopdf. This got me the forms in PDF, which I needed in order to migrate them

echo "This is a tool for downloading a forms by using a saved html page and a cookie to login to <site withheld>. Please make sure you have these two items before continuing.\n\nAlso, please make sure you have the following software installed: lynx, wkhtmltopdf\n\nAre you ready to continue?"

select yn in "Yes" "No"; do
    case $yn in
        Yes ) break;;
        No ) exit;;
    esac
done

echo "Please provide the path to the HTML file from your current directory\n>"

read webpage

export PRIMARY=`pwd`

mkdir newforms

lynx -dump -hiddenlinks=listonly $webpage > newforms/links.txt

cd newforms

vim links.txt -c 'g!/http/d' -c '%s/\s*[0-9]*. h/h/g' -c '1,6d' -c 'wq'

echo "Please provide the path to a cookies file to use for login\n>"

read cookies

wget --load-cookies $cookies -E -H -k -p -r --level=1 --content-disposition -i links.txt

cd $PRIMARY/newforms/<site-withheld>/OU_Forms/[A-Z]*

ls > $PRIMARY/newforms/list.txt

cat $PRIMARY/newforms/list.txt | awk '{print $1 " "$1 ".pdf"}' > $PRIMARY/newforms/cmds.txt

export HTML=`pwd`

cd $PRIMARY/newforms

mkdir pdfs

vim cmds.txt -c '%s/^/<long-directory-from-url-withheld>//g' -c '%s/.html.pdf/.pdf/g' -c '%s/ / pdfs\//g' 

wkhtmltopdf --read-args-from-stdin < cmds.txt
