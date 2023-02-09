# Filter
#### Video Demo:  https://www.youtube.com/watch?v=7dBjnmV7Hqg
#### Description:
I chose this project because I couldn't find any social media that could filter my pictures on my computer. For example, when I post a picture on instagram, facebook or snapchat the website does not provide a filter option. This is why I built this simple web app to do it for me very quickly. The only thing it does is take the image the user enters and then let the user choose the type of filter they want, after which the web app filters the image and displays it on a new page.

My web app was built with the Flask framework. On the "/" route that leads to index.html (via a GET method), there's a form with three inputs: one for a file that only accepts jpg or png, another for selecting which filter to use, and finally a submit input. If a user is unsure what each filter name does, there is a help button that will take them to a page with an image of what each filter does. The image is from the github of the library pilgrim.

When the method in app.py is POST (there was no particular reason why I chose the POST method), it checks if the user specified a file and type of filter, and if not, it redirects to the same route. There is also an if statement that determines whether the file is supported (png or jpg). If all of these checks are successful, the image will be saved in the static folder. To prevent the web app from saving multiple images in the static folder, each new image will overwrite the previous image.

This website (https://flask.palletsprojects.com/en/2.2.x/patterns/fileuploads/) was extremely helpful in figuring out how to perform those checks.

The filtering process then begins, thanks to the PIL and pilgrim libraries. The PIL library is used to open and save the image, whereas the pilgrim library is used to create the filtered image. Rather than writing if statements for each filter type, I created a dictionary and a list with all filter methods and a variable called func that gets the filter method that the user selected to then filter the image and save it in the static folder. Just like the non filtered images, to prevent the web app from saving multiple pictures in the static folder, each new picture will overwrite the previous image.

After saving the new image, the user is redirected to a new page (filtered.html) that displays their newly filtered image.

We have one CSS file in the static folder that styles all of my inputs and buttons as well as the page's background. I added a hover effect that I think is pretty cool. I also added a max height and max width to ensure that the filtered image displayed on filtered.html isn't too large for the device.
