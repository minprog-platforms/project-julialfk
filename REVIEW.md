# Code Review
Reviewed by Lance van Duin

## Use more comments to make the code clearer
I got many questions about how the code worked and what the functions did. Lance told me that it would be useful if I used more comments to explain these points. Summaries at the top of every script and mentioning which functions and files are referenced could also help.

## Code could be written more efficiently/less cluttered
For example, I could have merged the double return statement in the views.home into a single one if I wrote it outside of the inner if statement. I could have also made a new functions for blocks of code that I have used multiple times in the code, like creating the url in first_search and retry_search.

## Bare except
In my code, I use try-except statements, but do not take full advantage of the statement. I should use different exceptions to log the errors or specify more clearly for each type of error what went wrong in the flashed message.

## Prettier frontend
If I had more time, I would have put more effort in making my web pages more aesthetically pleasing. Since I wanted to focus more on the functionality of the program, I did not change much HTML from the guide format I used.

## Javascript
I feel like I could have moved the piece of script at the end of the base template to index.js in the static directory, but because of my limited knowledge of JavaScript, I did not know how to go about this well. In the future, I would like to learn more JS, to understand how these static folders work best and to implement more JS functionality.