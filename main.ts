let my_sprite = game.createSprite(0, 4)
let enemy = game.createSprite(4, 4)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    my_sprite.set(LedSpriteProperty.Direction, 90)
    my_sprite.move(-1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    my_sprite.set(LedSpriteProperty.Direction, 90)
    my_sprite.move(1)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    if (my_sprite.get(LedSpriteProperty.Y) == 4) {
        my_sprite.set(LedSpriteProperty.Direction, 0)
        my_sprite.move(3)
    }
    
})
//  game.is_game_over()
basic.forever(function on_forever() {
    my_sprite.set(LedSpriteProperty.Direction, 0)
    my_sprite.move(-1)
    basic.pause(150)
    enemy.move(-1)
    basic.pause(330)
    if (enemy.get(LedSpriteProperty.X) == 0) {
        enemy.set(LedSpriteProperty.X, 4)
        basic.pause(330)
    }
    
    if (my_sprite.get(LedSpriteProperty.X) == enemy.get(LedSpriteProperty.X) && my_sprite.get(LedSpriteProperty.Y) == enemy.get(LedSpriteProperty.Y)) {
        basic.showNumber(0)
    }
    
})
