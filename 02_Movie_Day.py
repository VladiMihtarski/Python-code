photo_time = int(input())
number_of_scenes = int(input())
scene_duration = int(input())

field_preparation = photo_time * 0.15
time_for_shoot_scenes = number_of_scenes * scene_duration
necessary_time = field_preparation + time_for_shoot_scenes

if photo_time < necessary_time:
    print(f"Time is up! To complete the movie you need {abs(photo_time - necessary_time):.0f} minutes.")
else:
    print(f"You managed to finish the movie on time! You have {abs(photo_time - necessary_time):.0f} minutes left!")
