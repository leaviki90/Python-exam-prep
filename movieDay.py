# movieDay - calculates if the movie can be completed within the allocated shooting time

shootingTime = int(input())  # Total available time for shooting the movie in minutes
scenesNumber = int(input())  # Number of scenes to shoot
sceneDuration = int(input())  # Duration of one scene in minutes

terrainPrep = shootingTime * 0.15  # Time required for terrain preparation, which is 15% of the total shooting time

filmingTime = scenesNumber * sceneDuration  # Total time needed to film all the scenes
neededTime = terrainPrep + filmingTime  # Total time needed for preparation and filming

# Check if the allocated shooting time is enough to finish the movie
if shootingTime >= neededTime:
    # If enough time is available, calculate and display the remaining time
    print(f"You managed to finish the movie on time! You have {round(shootingTime - neededTime)} minutes left!")
else:
    # If not enough time, calculate and display how much more time is needed
    print(f"Time is up! To complete the movie you need {round(neededTime - shootingTime)} minutes.")
