# Reference Implementation Plan

## Overview
This document outlines the steps to implement the Web4 Civic system, including the relay, client, and law engine components.

---

## 1. Relay
### Responsibilities:
- Store cards by hash.
- Maintain indexes for topics, jurisdictions, and geohashes.
- Implement the sync protocol.

### Steps:
1. Define the Relay API:
   - `POST /cards`: Submit a card.
   - `GET /cards/{hash}`: Retrieve a card by hash.
   - `POST /sync`: Sync cards between client and relay.
   - `GET /heads`: Retrieve Merkle heads for a topic/jurisdiction.
   - `GET /query`: Query cards by filters.

2. Implement storage:
   - Use a database or file system to store cards.
   - Create indexes for efficient querying.

3. Implement sync protocol:
   - Handle client requests for missing hashes.
   - Return cards in batches.

4. Enforce relay policies:
   - Require postage stamps for unattested keys.
   - Quarantine suspicious publishers.

---

## 2. Client
### Responsibilities:
- Provide a user interface for interacting with the system.
- Compute feeds locally using Law Packs.
- Sync with relays.

### Steps:
1. Develop the UI:
   - Screens:
     - Onboard: Create keypair, select jurisdictions, choose Law Pack.
     - Feed: Display ranked feed with explanations.
     - Publish: Create CivicCards.
     - Explain: Show rule traces for feed items.
     - Search: Query by topic/jurisdiction/time/geo.
     - Trust: Manage followed keys and Law Packs.

2. Implement the feed engine:
   - Sync cards from relays.
   - Deduplicate and validate signatures.
   - Resolve attestations and Law Packs.
   - Apply Law Pack rules.
   - Rank and render feed items.

3. Add explainability:
   - Display top rules and features for each feed item.
   - Show reasons for blocks or labels.

---

## 3. Law Engine
### Responsibilities:
- Process and apply Law Packs.
- Validate cards against rules.
- Compute rankings and explainability traces.

### Steps:
1. Parse Law Packs:
   - Implement a parser for the Law DSL.
   - Validate rules and weights.

2. Apply rules:
   - Evaluate cards against hard constraints.
   - Compute scores and rankings.

3. Generate explainability traces:
   - Record rules that fired for each card.
   - Provide human-readable explanations.

---

## 4. Integration
1. Connect the client, relay, and law engine components.
2. Test end-to-end functionality:
   - Submit cards via the client.
   - Sync with the relay.
   - Apply Law Packs and compute feeds.

3. Optimize performance:
   - Ensure efficient sync and feed computation.
   - Minimize latency for user interactions.

---

## 5. Deployment
1. Deploy the relay server.
2. Package the client app for local use.
3. Provide documentation for setting up the system.

---

## 6. Future Work
- Add support for offline-first sync.
- Implement QUIC transport for relays.
- Expand Law DSL with more conditions and actions.
- Develop mobile and desktop clients.