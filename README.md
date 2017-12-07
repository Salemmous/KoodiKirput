# KoodiKirput
Paras projekti ikinä

REQUIREMENTS:
Solr 7 or higher
Python 3 or higher
Django 1.11 or higher

SET UP INSTRUCTIONS:
Solr:
    - No special config or schema is needed since we are just going to add data through a GET request.
    - Create a core, call it "somali"
    - Go in a terminal to the directory where you have the "somAddRequest.txt"
    - Make a GET request to your Solr as follow:
        curl http://localhost:8983/solr/somali/update -H "Content-Type: text/xml" --data-binary @somAddRequest.txt
      Modify the port if needed
    - Restart your Solr or commit the changes with the following command line:
        curl http://localhost:8983/solr/my_collection/update?stream.body=%3Ccommit/%3E
    Solr is now ready! Make a query to test it.

Web app:
    - Just run the manage.py with python3 and the parametter "runserver"

API:
/api/translation/<word>
    Gives the possible translations of a word. Returns multiple results arranged in HTML-ready form. The English word is
    h2, which id is the id of the current word in Solr, a span with the given translation.

/api/id/<id>
    Works as /api/translation/<word> but requires the id of the word in the Solr database. Gives only one result, while
    /api/translation/<word> can output more than one word.

/api/suggest/<enword>
    Returns the suggestion in a JSON array (id + text, id being the id in Solr and text the English field) for the
    incomplete English search word <enword>.

/api/edit?id=...&en=...&so=...
    Edit the entry based on the given id. <en> should be the field in English and <so> the field in Somali.