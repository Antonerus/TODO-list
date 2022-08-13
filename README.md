# TODO-list
A personal simple project to make a webapp utilizing FLASK end product should be a todolist

TODO: Make an implementation where if the user enters an identical topic the app will stop them and prevent sqlite from 
crashing aka make a method where it checks the database if the same topic is already there and if it is if it's not
none stop them from adding it and have the add method not add the same identical thing into the database
make a helper function that checks or do it in add itself either way call it in add and if it's identical have the add
method prevent it from executing the db command if there's no identical proceed and execute the db command as usual
in the add method check if the request.form['topic'] is already in the database if not proceed to add it to the database
if it is don't add it to the database just skip over the adding part or tell the user that it's already added, that or 
ask Truman what's the next move.
After that just do the update method and it should be fine (check for identicals as well for this method when they 
update an item and proceed if new updated item isn't in the database or stop updating if it already is and tell the user
that what they're updating is already there in the list, PS: might want to remove the id on the main webpage

TODO: Make the update page have an option to cancel the update, reverse the order of the list on index so the newest item comes up first likely change to ascending order
