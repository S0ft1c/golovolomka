def terminal_hint_check(terminal, player):
    if terminal.rect.colliderect(player.rect):
        terminal.is_near = True
    else:
        terminal.is_near = False
