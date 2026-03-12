---
description: "Game project coding standards and conventions for Pygame development"
---

# Game Project Guidelines

Workspace-wide conventions for the Python game project (`/game`).

## Project Structure

```
game/
├── cenarios/          # Game scenarios and levels
├── configure/         # Configuration and settings
│   └── ConfigureGame.ini
├── fontes/           # Font files
├── img/              # Image assets
├── livro/            # Game dialogue/story
├── lutador/          # Fighter/combat classes
├── personagem/       # Character definitions
├── power/            # Power-up implementations
├── sound/            # Audio files
├── MinhaTela.py      # Main display/UI class
├── Controler.py      # Game controller/logic
├── ChamarCenario.py  # Scenario loader
└── CharacterRaffles.py  # Character selection/randomization
```

## Coding Standards

### Naming Conventions
- **Classes**: PascalCase (`MinhaTela`, `Controler`)
- **Functions/Methods**: snake_case (`load_scenario`, `handle_input`)
- **Constants**: UPPER_SNAKE_CASE (`SCREEN_WIDTH`, `GAME_FPS`)
- **Private members**: prefix with `_` (`_internal_state`)

### File Organization
- One main class per file when possible
- Related utilities grouped together
- Imports at top: stdlib → third-party → local
- Type hints for public methods (Python 3.5+)

### Performance
- Avoid heavy operations in game loops—precompute when possible
- Use sprite groups efficiently (Pygame best practices)
- Cache frequently accessed resources
- Profile before optimizing; use `cProfile` or `memory_profiler`

### Configuration
- Use `ConfigureGame.ini` for game settings—**never hardcode constants**
- Load configuration once at startup
- Environment-specific settings: development vs. production

### Testing & Debugging
- Add logging for game state transitions
- Use print-based debugging sparingly; prefer logging module
- Test scenario loading and character initialization separately

## Common Tasks

### Adding a New Scenario
1. Create scenario class in `cenarios/`
2. Register in `ChamarCenario.py`
3. Update `ConfigureGame.ini` if needed
4. Test with `MinhaTela.py`

### Adding Character Powers
1. Implement power class in `power/`
2. Register in `CharacterRaffles.py`
3. Apply power effect in `lutador/` (fighter class)
4. Test collision and removal

### Modifying Game UI
1. Update `MinhaTela.py` rendering logic
2. Adjust sprite positions/sizes
3. Test on different screen resolutions
4. Profile FPS impact

## Tools & Workflow

- **Editor**: VS Code
- **Agents Available**:
  - `@python-game-refactor`: Clean up code, remove duplication
  - `game-performance-analysis` (prompt `/`): Audit performance
- **Run Game**: `source .venv/bin/activate && python3 MinhaTela.py`
- **Environment**: Python 3.x with Pygame

## Common Issues

| Problem | Solution |
|---------|----------|
| "Module not found" | Activate venv: `source .venv/bin/activate` |
| Slow rendering | Check sprite count; profile with `-m cProfile` |
| Memory leaks | Use `memory_profiler`; check resource cleanup |
| Sound/Image not loading | Verify path in `configure/` and file exists |
