def when_started1():
    for repeat_count in range(3):
        magnet.energize(BOOST)
        drivetrain.drive_for(FORWARD, 1600, MM)
        drivetrain.turn_for(RIGHT, 180, DEGREES)
        drivetrain.drive_for(FORWARD, 1600, MM)
        magnet.energize(DROP)
        drivetrain.turn_for(RIGHT, 180, DEGREES)
    for repeat_count2 in range(1):
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 800, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
    for repeat_count3 in range(3):
        magnet.energize(BOOST)
        drivetrain.drive_for(FORWARD, 1600, MM)
        drivetrain.turn_for(RIGHT, 180, DEGREES)
        drivetrain.drive_for(FORWARD, 1600, MM)
        magnet.energize(DROP)
        drivetrain.turn_for(RIGHT, 180, DEGREES)
    for repeat_count4 in range(1):
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 800, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
    for repeat_count5 in range(3):
        magnet.energize(BOOST)
        drivetrain.drive_for(FORWARD, 1600, MM)
        drivetrain.turn_for(RIGHT, 180, DEGREES)
        drivetrain.drive_for(FORWARD, 1600, MM)
        magnet.energize(DROP)
        drivetrain.turn_for(RIGHT, 180, DEGREES)

vr_thread(when_started1)
