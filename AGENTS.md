# AGENTS.md - Project Youth

## Running the Game
- From SDK root: `./renpy.sh Project-Youth`
- Alternative: `renpy /path/to/Project-Youth` (if renpy in PATH)

## Project Structure
- Game source: `game/` directory
- Main entry: `game/script.rpy` (calls label start from prologue_mpls.rpy)
- Labels: prologue_mpls.rpy (start), week1.rpy (week1_start), rhythm_game.rpy (rhythm_minigame)
- Screens: `game/screens.rpy` (defines all UI)
- Options: `game/options.rpy` (configurable settings)
- GUI: `game/gui.rpy` (style definitions)

## Generated Files (Do Not Edit)
- Compiled scripts: `game/**/*.rpyc`, `game/**/*.rpymc`
- Cache: `game/cache/`, `game/saves/`
- Logs: `errors.txt`, `log.txt`, `traceback.txt` (in project root and game/)
- These are auto-generated; deleting them forces recompilation.

## Common Issues
- Menu indentation: Ensure menu options are indented under `menu:` (see errors.txt examples)
- Save compatibility: Changing script structure may break saves (see traceback for load errors)
- Developer mode: Enables MCP bridge for live debugging (see game/mcp_bridge.rpy)

## VS Code Integration
- Uses renpyWarp extension (see .vscode/settings.json)
- Live communication via MCP bridge (game/_mcp/ directory)
- Do not edit game/_mcp_bridge.rpy (auto‑overwritten)

## Build & Distribution
- Build settings in `game/options.rpy` (build.* variables)
- Excludes: `**~`, `**.bak`, hidden files, thumbs.db
- Archive: Uncomment build.classify lines for assets

## No Formal Test Suite
- Verify by running game and checking for errors in log.txt
- Manual testing of labels/screens required.

## Conventions
- Character definitions: `define <var> = Character("<name>", color="#hex")`
- Labels: snake_case with prefix (e.g., week1_start, trida_lunch)
- Screens: lowercase with underscores (e.g., screen navigation())
- Init python: Used for build classification, MCP setup, custom classes.