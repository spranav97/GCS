import pygame

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION:print(event.dict, int(event.value*1000))
            elif event.type == pygame.JOYBALLMOTION:print(event.dict, event.ball)
            elif event.type == pygame.JOYBUTTONDOWN:print(event.dict, event.button, 'pressed')
            elif event.type == pygame.JOYBUTTONUP:print(event.dict, event.button, 'released')
            elif event.type == pygame.JOYHATMOTION:print(event.dict, event.hat)
except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
    pygame.quit()