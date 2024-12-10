label start:


    scene nightsky
     # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "e Good morning MC!"
        "say it back":
            "Hello, good mornin' LoveInterest"

            "Yay! You said it back!!!"

            $game_player.increaseRelationship("LiName_Dynamic",1)

            "This conversation defenitely earned me some points."
        "ignore her":
            "Not winning any points by ignorning her..."



    # This ends the game.

    return
