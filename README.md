# 🌌 Night Sky — Aurora Borealis & Mountain Lake
### Standalone GPU Real-Time Wallpaper Engine Application (.EXE)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Wallpaper%20Engine-brightgreen.svg)]()
[![Rendering](https://img.shields.io/badge/Rendering-OpenGL%203.3%20%2F%20ModernGL-orange.svg)]()
[![Audio](https://img.shields.io/badge/Audio-Real%20Nature%20Soundscapes-purple.svg)]()

A photorealistic, relaxing, and real-time GPU-rendered night mountain lake wallpaper. Features dynamic atmospheric weather, silky moonlight water reflections, procedural multi-octave Aurora Borealis, autonomous shooting stars, bioluminescent fireflies, an articulated flying owl silhouette, and 100% real recorded nature audio.

---

## 🌟 Key Features

* **⚡ Real-Time GPU Shader Engine**: Full custom GLSL shader pipeline rendering procedurally with VSync locked to your monitor's native refresh rate (60Hz / 120Hz / 144Hz / 240Hz). Ultra-low CPU & GPU footprint.
* **⛅ Dynamic Atmospheric Weather Cycles**:
  * **Auto-Cycles** randomly every **180–250 seconds** with **10-second cinematic smooth crossfades**.
  * **6 Weather States**: *Clear Starry Night*, *Gentle Mountain Breeze*, *Light Rain & Drizzle*, *Thunderstorm & Lightning*, *Winter Snowfall*, and *Lake Mist & Fog*.
* **🌌 Dynamic Aurora Borealis**:
  * Procedural multi-layer ribbon curtain simulation.
  * **Auto-Bloom Scheduler** (every 80–150s for 45s at 70% brightness).
  * **+50% Higher Bloom Chance** during snowfall.
  * **3 Color Palettes**: *Emerald Green*, *Purple / Violet*, and *Arctic Cyan*.
* **🔮 Ethereal Void Purple Torch Surge**:
  * Natural warm golden campfire during fair weather.
  * Magically surges into an **Ethereal Void Purple Flame** with ultraviolet core and +240% illumination radius during severe storms and snow.
* **✨ Bioluminescent Fireflies**:
  * **12 Fireflies Total**: 4 paired circling couples (Golden-Yellow + Emerald-Green orbiting each other over the lake) + 4 solitary fireflies hovering near the torch, evergreen tree, and shore knoll with real-time water reflections.
* **🦉 Articulated Flying Owl Silhouette**:
  * Side-profile nocturnal owl with realistic 3-beat wing flaps and gliding motion skimming low above the mountain lake.
  * Synchronized distant owl calls.
* **🌠 Autonomous Meteors (Shooting Stars)**:
  * Periodic shooting stars (7–25s) with fading ionization trails.
* **🔊 High-Fidelity Nature Audio Engine**:
  * Multi-track layered audio: crackling campfire, lake water lap, alpine wind, gentle rain, heavy storm, snow crunch, crickets, 3 real recorded thunder claps, and 5 authentic owl calls.
* **🕐 Minimalist Clock & Customization**:
  * High-DPI clock and date display in top-right corner.
  * Full Wallpaper Engine properties integration via `project.json`.

---

## 🎮 Keyboard Controls

| Key | Action |
| :---: | :--- |
| **`1`** | Set Weather: **Clear Starry Night** |
| **`2`** | Set Weather: **Gentle Mountain Breeze** |
| **`3`** | Set Weather: **Light Rain & Drizzle** |
| **`4`** | Set Weather: **Thunderstorm & Lightning** |
| **`5`** | Set Weather: **Winter Snowfall** |
| **`6`** | Set Weather: **Lake Mist & Fog** |
| **`A` / Space** | Toggle **Auto Weather Cycle** (180–250s) |
| **`T`** | Cycle **Aurora Intensity** (Off $\rightarrow$ Soft $\rightarrow$ Moderate $\rightarrow$ Bright $\rightarrow$ Auto Bloom) |
| **`N`** | Cycle **Aurora Color Palette** (Emerald $\rightarrow$ Purple $\rightarrow$ Arctic Cyan) |
| **`S`** | Trigger instant **Shooting Star** |
| **`O`** | Trigger instant **Flying Owl** |
| **`M`** | **Mute / Unmute** Audio |
| **`B` / `H`** | Toggle Onscreen Pill Buttons visibility |
| **`ESC`** | Exit Application |

---

## 🚀 Installation

### In Wallpaper Engine:
1. Open **Wallpaper Engine**.
2. Click **Open Wallpaper** $\rightarrow$ **Open from File / Application**.
3. Select `wallpaper_app.exe` (or `project.json`).
4. Click **Apply**.

### Standalone:
Simply double-click `wallpaper_app.exe` on any Windows PC.

---

## 📜 License & Author

Created by **Samandar Abdullaev Sobirovich**.  
Licensed under the [MIT License](LICENSE).
