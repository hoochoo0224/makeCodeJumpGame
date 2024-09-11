my_sprite = game.create_sprite(0, 4)
enemy = game.create_sprite(4, 4)
def on_button_pressed_a():
    my_sprite.set(LedSpriteProperty.DIRECTION, 90)
    my_sprite.move(-1)
def on_button_pressed_b():
    my_sprite.set(LedSpriteProperty.DIRECTION, 90)
    my_sprite.move(1)
def on_logo_event_pressed():
    if my_sprite.get(LedSpriteProperty.Y) == 4:
        my_sprite.set(LedSpriteProperty.DIRECTION, 0)
        my_sprite.move(3)
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)
def on_forever():
    my_sprite.set(LedSpriteProperty.DIRECTION, 0)
    my_sprite.move(-1)
    basic.pause(150)

    enemy.move(-1)
    basic.pause(330)
    if enemy.get(LedSpriteProperty.X) == 0:
        enemy.set(LedSpriteProperty.X, 4)
        basic.pause(330)
    if my_sprite.get(LedSpriteProperty.X) == enemy.get(LedSpriteProperty.X) and my_sprite.get(LedSpriteProperty.Y) == enemy.get(LedSpriteProperty.Y):
        basic.show_number(0)
        # game.is_game_over()

basic.forever(on_forever)

# def on_forever():
#     pins.digital_write_pin(DigitalPin.P0, 1)
#     basic.pause(1000)
#     pins.digital_write_pin(DigitalPin.P0, 0)
#     basic.pause(1000)
# basic.forever(on_forever)