# Newton Suite

A curated collection of Newton Supercomputer components for development and deployment.

## Components Included

This suite includes the following Newton projects:

- **realTinyTalk** - The verified general-purpose programming language with Monaco editor
- **adan** - Advanced agent framework
- **adan_portable** - Portable version of the agent framework
- **newton_agent** - Core Newton agent implementation
- **statsy** - Statistical analysis and visualization tools

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. If you only want to run the realTinyTalk web IDE locally, ensure Flask is installed:
   ```bash
   pip install flask
   ```

3. Start the realTinyTalk Monaco editor:
   ```bash
   python realTinyTalk/web/server.py
   ```
   Then visit http://localhost:5555

4. Run Newton demos:
   ```bash
   python -m newton_sdk.cli demo
   ```


## Recent Updates

- **TinyTalk FFI import wiring fixed**: runtime imports now consume parser `ImportStmt.items`, restoring robust `import "@..."` behavior for built-in and external modules.
- **FFI builtins now globally registered**: helpers like `eval_python`, `python`, `http_get`, and `http_post` are available in runtime global scope without manual registration.
- **New Monaco starter example**: `🏈 Betting Verifier (Parlay + Monte Carlo)` was added to the realTinyTalk examples API for local experimentation with implied probability math and random simulation.

For details on web IDE behavior and storage endpoints, see `realTinyTalk/web/README.md`.

## Architecture

The Newton Supercomputer implements verified computation where:
- The constraint IS the instruction
- The verification IS the computation
- The network IS the processor

All computations are bounded, deterministic, and cryptographically verifiable.

## Documentation

See the main [Newton README](../README.md) for comprehensive documentation, API reference, and guides.

- **iOS Blueprint (2026)** - `IOS_APP_BLUEPRINT_2026.md` for building a SwiftUI-first Apple app from this codebase

## License

See [LICENSE](../LICENSE) and [USAGE_AGREEMENT.md](../USAGE_AGREEMENT.md) for licensing terms.
