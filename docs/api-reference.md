# API Reference

Complete reference for the Newton OS API.

## Base URL

| Environment | URL |
|-------------|-----|
| Hosted API | `https://api.parcri.net` |
| Self-hosted | `http://localhost:8000` |

---

## Endpoints Overview

### Core Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| [`/verify`](#verify) | POST | Verify text against safety constraints |
| [`/analyze`](#analyze) | POST | Anomaly detection (Z-score, IQR, MAD) |
| [`/analyze/batch`](#analyze-batch) | POST | Batch analysis of multiple datasets |
| [`/compile`](#compile) | POST | Natural language to structured prompts |
| [`/ground`](#ground) | POST | Verify claims against external sources |

### Security & Audit

| Endpoint | Method | Description |
|----------|--------|-------------|
| [`/sign`](#sign) | POST | Generate cryptographic signatures |
| [`/ledger`](#ledger) | GET | Retrieve audit trail |
| [`/ledger/verify`](#ledger-verify) | GET | Verify chain integrity |

### Extension Cartridges

| Endpoint | Method | Description |
|----------|--------|-------------|
| [`/cartridge/visual`](#cartridge-visual) | POST | SVG specification generation |
| [`/cartridge/sound`](#cartridge-sound) | POST | Audio specification generation |
| [`/cartridge/sequence`](#cartridge-sequence) | POST | Video/animation specification |
| [`/cartridge/data`](#cartridge-data) | POST | Report specification |

### Framework Verification

| Endpoint | Method | Description |
|----------|--------|-------------|
| [`/frameworks`](#frameworks) | GET | List available frameworks |
| [`/frameworks/constraints`](#frameworks-constraints) | GET | List framework constraints |
| [`/frameworks/verify`](#frameworks-verify) | POST | Verify against framework constraints |

### Metadata

| Endpoint | Method | Description |
|----------|--------|-------------|
| [`/health`](#health) | GET | System status |
| [`/constraints`](#constraints) | GET | List available constraints |
| [`/methods`](#methods) | GET | List analysis methods |

---

## Core Endpoints

### /verify

Verify text against harm, medical, legal, and security constraints.

**POST** `/verify`

#### Request Body

```json
{
  "input": "string",
  "constraints": ["harm", "medical", "legal", "security"]
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `input` | string | Yes | Text to verify |
| `constraints` | array | No | Constraints to check (defaults to all) |

#### Response

```json
{
  "verified": true,
  "confidence": 92.3,
  "constraints_passed": ["harm", "medical", "legal", "security"],
  "constraints_failed": [],
  "fingerprint": "A7F3B2C8E1D4",
  "engine": "Newton OS 3.0.0"
}
```

#### Example

```bash
curl -X POST https://api.parcri.net/verify \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{"input": "Help me write a business plan"}'
```

---

### /analyze

Perform anomaly detection on numerical data.

**POST** `/analyze`

#### Request Body

```json
{
  "data": [45.2, 46.1, 102.4, 45.8, 47.0],
  "method": "zscore",
  "threshold": 3.0,
  "labels": ["Jan", "Feb", "Mar", "Apr", "May"]
}
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `data` | array | Yes | - | Numerical values to analyze |
| `method` | string | No | `zscore` | Detection method: `zscore`, `iqr`, `mad`, `all` |
| `threshold` | float | No | 3.0 | Sensitivity threshold |
| `labels` | array | No | - | Labels for data points |

#### Response (Z-score method)

```json
{
  "method": "zscore",
  "threshold": 3.0,
  "statistics": {
    "n": 5,
    "mean": 57.3,
    "std_dev": 24.1,
    "min": 45.2,
    "max": 102.4
  },
  "scores": [-0.50, -0.46, 1.87, -0.48, -0.43],
  "anomalies": [],
  "anomaly_values": [],
  "n_anomalies": 0,
  "pct_anomalies": 0.0,
  "fingerprint": "B2C4D6E8F0A1"
}
```

#### Example

```bash
curl -X POST https://api.parcri.net/analyze \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{"data": [10, 12, 11, 50, 12, 11], "method": "zscore"}'
```

---

### /analyze/batch

Analyze multiple datasets in a single request.

**POST** `/analyze/batch`

#### Request Body

```json
{
  "datasets": {
    "sales": [100, 105, 98, 500, 102],
    "costs": [50, 52, 48, 51, 49]
  },
  "method": "zscore",
  "threshold": 3.0
}
```

#### Response

```json
{
  "method": "zscore",
  "threshold": 3.0,
  "results": {
    "sales": {
      "statistics": {...},
      "anomalies": [3],
      "n_anomalies": 1
    },
    "costs": {
      "statistics": {...},
      "anomalies": [],
      "n_anomalies": 0
    }
  },
  "fingerprint": "C3D5E7F9A1B2"
}
```

---

### /compile

Transform natural language intent into structured AI prompts.

**POST** `/compile`

#### Request Body

```json
{
  "intent": "Build a fitness app with workout tracking",
  "target_platform": "iOS",
  "ios_version": "18.0",
  "constraints": ["app_store", "privacy", "hig"]
}
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `intent` | string | Yes | - | Natural language description |
| `target_platform` | string | No | `iOS` | Target platform |
| `ios_version` | string | No | `18.0` | iOS version target |
| `constraints` | array | No | - | Additional constraints |

#### Response

```json
{
  "parsed": {
    "platform": "ios",
    "app_type": "health",
    "components": ["list", "form", "chart"],
    "frameworks": ["SwiftUI", "HealthKit"],
    "tokens": 7
  },
  "content_constraints": {
    "passed": ["harm", "medical", "legal", "security"],
    "failed": []
  },
  "app_constraints": {
    "passed": ["app_store", "privacy", "hig"],
    "failed": [],
    "warnings": ["HealthKit requires special entitlements..."],
    "compliant": true
  },
  "verified": true,
  "prompt": "TARGET: IOS 18.0\nFRAMEWORK: SwiftUI\n...",
  "fingerprint": "D4E6F8A0B2C3"
}
```

---

### /ground

Verify factual claims against external sources.

**POST** `/ground`

#### Request Body

```json
{
  "query": "Apple released the first iPhone in 2007"
}
```

#### Response

```json
{
  "query": "Apple released the first iPhone in 2007",
  "result": {
    "claim": "Apple released the first iPhone in 2007",
    "confidence_score": 1.5,
    "status": "VERIFIED",
    "sources": [
      "https://apple.com/...",
      "https://reuters.com/..."
    ],
    "timestamp": 1735689600,
    "signature": "E5F7A9B1C3D4"
  },
  "verified": true
}
```

#### Confidence Scores

| Score | Status | Meaning |
|-------|--------|---------|
| 0-2 | VERIFIED | Strong supporting evidence |
| 2-5 | LIKELY | Moderate evidence |
| 5-8 | UNCERTAIN | Weak evidence |
| 8-10 | UNVERIFIED | No supporting evidence |

---

## Security & Audit

### /sign

Generate cryptographic signatures for payloads.

**POST** `/sign`

#### Request Body

```json
{
  "payload": "content to sign",
  "context": "optional context"
}
```

#### Response

```json
{
  "signature": "a7b3c8f2e1d4...",
  "token": "F6A8B0C2D4E5...",
  "timestamp": 1735689600,
  "payload_hash": "G7B9C1D3E5F7",
  "verified": true
}
```

---

### /ledger

Retrieve the append-only audit trail.

**GET** `/ledger`

#### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | int | 100 | Maximum entries to return |
| `offset` | int | 0 | Offset for pagination |

#### Response

```json
{
  "entries": [
    {
      "id": 0,
      "type": "verification",
      "payload": {...},
      "timestamp": 1735689600,
      "prev_hash": "GENESIS",
      "nonce": "a1b2c3d4",
      "hash": "H8C0D2E4F6A8"
    }
  ],
  "total": 1247,
  "merkle_root": "I9D1E3F5A7B9"
}
```

---

### /ledger/verify

Verify the integrity of the cryptographic ledger chain.

**GET** `/ledger/verify`

#### Response

```json
{
  "valid": true,
  "entries": 1247,
  "message": "Chain intact - all entries verified",
  "merkle_root": "I9D1E3F5A7B9",
  "first_entry": 1735600000,
  "last_entry": 1735689600
}
```

---

## Metadata Endpoints

### /health

Get system status and version.

**GET** `/health`

#### Response

```json
{
  "status": "ok",
  "version": "3.0.0",
  "engine": "Newton OS 3.0.0",
  "timestamp": 1735689600
}
```

---

### /constraints

List available content constraints.

**GET** `/constraints`

#### Response

```json
{
  "constraints": {
    "harm": {
      "name": "No Harm",
      "patterns": 4
    },
    "medical": {
      "name": "Medical Bounds",
      "patterns": 3
    },
    "legal": {
      "name": "Legal Bounds",
      "patterns": 3
    },
    "security": {
      "name": "Security",
      "patterns": 2
    }
  }
}
```

---

### /methods

List available analysis methods.

**GET** `/methods`

#### Response

```json
{
  "methods": {
    "zscore": {
      "name": "Z-Score",
      "default_threshold": 3.0,
      "description": "Standard deviation-based anomaly detection"
    },
    "iqr": {
      "name": "Interquartile Range",
      "default_threshold": 1.5,
      "description": "Quartile-based outlier detection"
    },
    "mad": {
      "name": "Median Absolute Deviation",
      "default_threshold": 3.0,
      "description": "Robust median-based detection"
    }
  }
}
```

---

## Error Responses

### 400 Bad Request

```json
{
  "detail": "Invalid request body"
}
```

### 401 Unauthorized

```json
{
  "detail": "Missing API key. Include X-API-Key header."
}
```

### 403 Forbidden

```json
{
  "detail": "Invalid API key"
}
```

### 429 Too Many Requests

```json
{
  "detail": "Rate limit exceeded. Max 60 requests per minute."
}
```

### 500 Internal Server Error

```json
{
  "detail": "Internal server error"
}
```
