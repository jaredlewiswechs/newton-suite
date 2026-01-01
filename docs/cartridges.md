# Extension Cartridges

Newton's constraint engine extends to any domain with definable bounds through Extension Cartridges.

## Overview

| Cartridge | Input | Output | Use Case |
|-----------|-------|--------|----------|
| Visual | Design intent | SVG specification | UI components, diagrams |
| Sound | Audio intent | WAV specification | Sound effects, audio |
| Sequence | Animation intent | Video specification | Animations, videos |
| Data | Report intent | Report specification | Reports, analytics |

All cartridges verify content against both standard constraints and domain-specific rules.

---

## /cartridge/visual

Generate SVG specifications with dimension constraints.

### Request

**POST** `/cartridge/visual`

```json
{
  "intent": "Create a dashboard with progress indicators",
  "width": 800,
  "height": 600,
  "max_elements": 100,
  "color_palette": ["#3b82f6", "#10b981", "#f59e0b"]
}
```

| Field | Type | Required | Default | Max | Description |
|-------|------|----------|---------|-----|-------------|
| `intent` | string | Yes | - | - | Design description |
| `width` | int | No | 800 | 4096 | Canvas width in pixels |
| `height` | int | No | 600 | 4096 | Canvas height in pixels |
| `max_elements` | int | No | 100 | 1000 | Maximum SVG elements |
| `color_palette` | array | No | - | 256 | Color hex codes |

### Response

```json
{
  "verified": true,
  "constraints": {
    "content": {
      "passed": ["harm", "medical", "legal", "security"],
      "failed": []
    },
    "visual": {
      "passed": true,
      "violations": []
    },
    "bounds": {
      "width": 800,
      "height": 600,
      "max_elements": 100
    }
  },
  "spec": {
    "type": "svg",
    "viewBox": "0 0 800 600",
    "width": 800,
    "height": 600,
    "elements": ["rect", "text", "circle"],
    "style": {
      "background": "#ffffff",
      "stroke": "#000000",
      "fill": "#e0e0e0"
    }
  }
}
```

### Visual Constraints

| Constraint | Limit |
|------------|-------|
| Width | 1 - 4096 px |
| Height | 1 - 4096 px |
| Max elements | 1000 |
| Color palette | 256 colors |

### Blocked Patterns

- Offensive/inappropriate imagery
- Logo/trademark plagiarism

### Example

```bash
curl -X POST https://api.parcri.net/cartridge/visual \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{
    "intent": "Create a bar chart showing monthly sales",
    "width": 600,
    "height": 400
  }'
```

---

## /cartridge/sound

Generate audio specifications with frequency and duration limits.

### Request

**POST** `/cartridge/sound`

```json
{
  "intent": "Create a notification chime",
  "duration_ms": 500,
  "min_frequency": 440.0,
  "max_frequency": 880.0,
  "sample_rate": 44100
}
```

| Field | Type | Required | Default | Limits | Description |
|-------|------|----------|---------|--------|-------------|
| `intent` | string | Yes | - | - | Audio description |
| `duration_ms` | int | No | 5000 | 1-300000 | Duration in milliseconds |
| `min_frequency` | float | No | 20.0 | 1+ | Minimum frequency (Hz) |
| `max_frequency` | float | No | 20000.0 | 22050 max | Maximum frequency (Hz) |
| `sample_rate` | int | No | 44100 | 22050, 44100, 48000, 96000 | Sample rate |

### Response

```json
{
  "verified": true,
  "constraints": {
    "content": {
      "passed": ["harm", "medical", "legal", "security"],
      "failed": []
    },
    "sound": {
      "passed": true,
      "violations": []
    },
    "bounds": {
      "duration_ms": 500,
      "frequency_range": [440.0, 880.0]
    }
  },
  "spec": {
    "type": "audio",
    "duration_ms": 500,
    "sample_rate": 44100,
    "frequency_range": {
      "min": 440.0,
      "max": 880.0
    },
    "characteristics": ["tone"],
    "format": "wav",
    "channels": 2
  }
}
```

### Sound Constraints

| Constraint | Limit |
|------------|-------|
| Duration | 1ms - 5 minutes |
| Frequency | 1 - 22050 Hz |
| Sample rates | 22050, 44100, 48000, 96000 |

### Blocked Patterns

- Subliminal messages
- Harmful frequencies

### Example

```bash
curl -X POST https://api.parcri.net/cartridge/sound \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{
    "intent": "Create ambient background music",
    "duration_ms": 30000,
    "sample_rate": 48000
  }'
```

---

## /cartridge/sequence

Generate video/animation specifications with frame constraints.

### Request

**POST** `/cartridge/sequence`

```json
{
  "intent": "Create a product demo animation",
  "duration_seconds": 15.0,
  "fps": 30,
  "width": 1920,
  "height": 1080,
  "max_scenes": 5
}
```

| Field | Type | Required | Default | Limits | Description |
|-------|------|----------|---------|--------|-------------|
| `intent` | string | Yes | - | - | Animation description |
| `duration_seconds` | float | No | 30.0 | 0.1-600 | Duration in seconds |
| `fps` | int | No | 30 | 1-120 | Frames per second |
| `width` | int | No | 1920 | 7680 max | Resolution width |
| `height` | int | No | 1080 | 4320 max | Resolution height |
| `max_scenes` | int | No | 10 | 50 | Maximum scene count |

### Response

```json
{
  "verified": true,
  "constraints": {
    "content": {
      "passed": ["harm", "medical", "legal", "security"],
      "failed": []
    },
    "sequence": {
      "passed": true,
      "violations": []
    },
    "bounds": {
      "duration": 15.0,
      "fps": 30,
      "resolution": "1920x1080"
    }
  },
  "spec": {
    "type": "animation",
    "duration_seconds": 15.0,
    "fps": 30,
    "total_frames": 450,
    "resolution": {
      "width": 1920,
      "height": 1080
    },
    "max_scenes": 5,
    "format": "mp4",
    "codec": "h264"
  }
}
```

### Sequence Constraints

| Constraint | Limit |
|------------|-------|
| Duration | 0.1s - 10 minutes |
| FPS | 1 - 120 |
| Resolution | Up to 8K (7680x4320) |
| Scenes | 50 max |

### Blocked Patterns

- Seizure/epilepsy-inducing content
- Rapid strobing/flashing

### Example

```bash
curl -X POST https://api.parcri.net/cartridge/sequence \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{
    "intent": "Create a slideshow presentation",
    "duration_seconds": 60,
    "fps": 24,
    "max_scenes": 10
  }'
```

---

## /cartridge/data

Generate report specifications with statistical bounds.

### Request

**POST** `/cartridge/data`

```json
{
  "intent": "Generate a financial summary report",
  "data": {
    "revenue": [100000, 120000, 115000, 130000],
    "expenses": [80000, 85000, 82000, 90000]
  },
  "format": "json",
  "max_rows": 1000,
  "include_statistics": true
}
```

| Field | Type | Required | Default | Limits | Description |
|-------|------|----------|---------|--------|-------------|
| `intent` | string | Yes | - | - | Report description |
| `data` | object | No | - | - | Data to include |
| `format` | string | No | `json` | json, csv, markdown, html | Output format |
| `max_rows` | int | No | 1000 | 100000 | Maximum row count |
| `include_statistics` | bool | No | true | - | Include statistical analysis |

### Response

```json
{
  "verified": true,
  "constraints": {
    "content": {
      "passed": ["harm", "medical", "legal", "security"],
      "failed": []
    },
    "data": {
      "passed": true,
      "violations": []
    },
    "bounds": {
      "max_rows": 1000,
      "format": "json"
    }
  },
  "spec": {
    "type": "report",
    "report_type": "financial",
    "format": "json",
    "max_rows": 1000,
    "include_statistics": true,
    "sections": ["header", "summary", "data", "footer"],
    "data_provided": true,
    "statistics": {
      "count": 8,
      "sum": 802000,
      "mean": 100250,
      "min": 80000,
      "max": 130000
    }
  }
}
```

### Report Types

Automatically detected from intent:

| Type | Keywords |
|------|----------|
| financial | financial, revenue, profit, expense, budget |
| analytics | analytics, metrics, kpi, performance |
| summary | summary, overview, report, digest |
| comparison | comparison, compare, versus, vs |
| trend | trend, growth, change, over time |

### Data Constraints

| Constraint | Limit |
|------------|-------|
| Rows | 100,000 max |
| Columns | 1,000 max |
| Formats | json, csv, markdown, html |

### Blocked Patterns

- Data fabrication/falsification
- Metric manipulation

### Example

```bash
curl -X POST https://api.parcri.net/cartridge/data \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{
    "intent": "Create a user analytics report",
    "data": {"users": [1000, 1500, 2000], "sessions": [5000, 7500, 10000]},
    "format": "markdown",
    "include_statistics": true
  }'
```
