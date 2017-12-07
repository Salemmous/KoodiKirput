# KoodiKirput
Paras projekti ikinä

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

/api/edit/<id>/<en>/<so>    or /api/edit?id=...&en=...&so=...
    Edit the entry based on the given id. <en> should be the field in English and <so> the field in Somali.