# Khalitos Way

Khalitos Way is a webserver used to monitor the temperatures of a bearded dragon enclosure. 

The application is essentially 3 pieces. The DJango webserver, the Pi monitor and the postgres database.

## Architecture

```
    pi              db              Django
----------       ----------       ----------
|        |       |        |       |        |
|        |  <->  |        |  <->  |        |
|        |       |        |       |        |
----------       ----------       ----------
```

## Applications

### Temperature Monitor App

Just like it sounds, this app will consistently communicate with the temperature sensors on the
board and put the results into teh data base. Additionally, the app will also control power to
the heat lamps and light sources based on a user defined parameters.

### Webpage Interface App

This will be the app that the user will interact with directly. This app will pull json data from
the Temperature Monitor App, or maybe query it from the database, I do not know yet.

### Video Stream App

Finally, this app will provide a video feed to the user using two different cameras. The first is a
daytime logitech webcam and the other is a night time pi camera.
