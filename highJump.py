# High Jump - simulates jumping attempts over a bar with progressively increasing height

wantedBarHeight = int(input())  # Desired height the player wants to jump over
startBarHeight = wantedBarHeight - 30  # Starting bar height is 30 cm less than the desired height
jumpsCount = 0  # Initialize the total number of jumps
failedJumps = 0  # Initialize the count of consecutive failed jumps

# Start the jumping loop
while True:
    jumpHeight = int(input())  # Input the height of the current jump
    jumpsCount += 1  # Increase the total jump count

    # If the jump is successful (jump height is greater than the bar height)
    if jumpHeight > startBarHeight:
        startBarHeight += 5  # Increase the bar height by 5 cm
        failedJumps = 0  # Reset the failed jump count
    else:
        failedJumps += 1  # Count the failed jump

    # If there are 3 consecutive failed jumps, the player fails
    if failedJumps == 3:
        print(f"Jim failed at {startBarHeight}cm after {jumpsCount} jumps.")
        break

    # If the player jumps over the desired bar height, they succeed
    if startBarHeight > wantedBarHeight:
        print(f"Jim succeeded, he jumped over {startBarHeight - 5}cm after {jumpsCount} jumps.")
        break
