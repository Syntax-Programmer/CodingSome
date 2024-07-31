These are the important concepts i learned from internet.

1. Diagonal movement when both horizontal and vertical keys are pressed is faster than normal moving due to pythagoras theorem.
    So normalize the movement vector for consistent speed.

2. Everything on the screen should be drawn from top down So that thing that are up can be covered by thing that are below them.
    Refer: https://www.youtube.com/watch?v=EBZt_2NQwp0&list=PLwy3y9Ks8DoYUbP6J9E5FjaPGVVnRUIFf&index=2
    for more explanation.

3. A background should move with the player to make a nice effect. Consider Single layer parallax or multiple layer parallax.

4. To make the enemies turn around when ledge or wall appears we can check for it by having a rect constantly check for colliders.
    If the rect is getting colliding then we know the object has encountered something.

5. To make the animation smooth make different parts of the sprite separate.
    Refer: https://www.youtube.com/watch?v=Jji8LJToZYc&list=PLwy3y9Ks8DoYUbP6J9E5FjaPGVVnRUIFf&index=5
           https://www.youtube.com/watch?v=kYPMIfROc_A&list=PLwy3y9Ks8DoYUbP6J9E5FjaPGVVnRUIFf&index=10
    for more explanation.

6.  Lighting can be made better by making the sprite's normal map: A map of how the character reflects light.
    Refer: https://www.youtube.com/watch?v=rzm8v5gx7l0&list=PLwy3y9Ks8DoYUbP6J9E5FjaPGVVnRUIFf&index=6
    for more explanation.

7. We can pull the player to the ground with more gravity than going up to make it feel more natural.

8. Coyote time is the time we can allow the player to jump even if the player is not on the ground to make it more natural for the users.

9. Jump buffering iws when the game holds onto the jump action for sometime if the jump is not currently available.
    During the time if the jump becomes available we can perform a jump. This is so that the user has much natural controls.

10. RayCasting: https://www.youtube.com/watch?v=wCG3Nq_iibA&list=PLwy3y9Ks8DoYUbP6J9E5FjaPGVVnRUIFf&index=12

11. For small or medium jumps for the player : https://www.youtube.com/watch?v=jd91r5kwdnc&list=PLwy3y9Ks8DoYUbP6J9E5FjaPGVVnRUIFf&index=13
    We just give the player some speed till no jump button is pressed and then make the vertical vel 0

12. Changing the pitch of a sound effect each time its played by a little bit to make the sound effect more natural.
    Refer: https://www.youtube.com/watch?v=ZYZRr05AMNE&list=PLwy3y9Ks8DoYUbP6J9E5FjaPGVVnRUIFf&index=14

13. Some algorithms like path finding that don't need to be executed each frame. We can run them every couple frames.
    This can optimize the performance.
    Refer: https://www.youtube.com/watch?v=8_5Zrgek1p8&list=PLwy3y9Ks8DoYUbP6J9E5FjaPGVVnRUIFf&index=16

14. To make different type of floors: https://www.youtube.com/watch?v=G-Fd3-AcgKo&list=PLwy3y9Ks8DoYUbP6J9E5FjaPGVVnRUIFf&index=17