new_element = SnakeElement()
        new_element.goto(snake[0].pos())
        new_element.setheading(snake[0].heading())
        new_element.forward(20)
        snake.insert(0, new_element)