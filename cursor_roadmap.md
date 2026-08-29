# Internalize: Development Roadmap

## Phase 1: Stabilization & Data Provenance (Immediate)
*The goal of this phase is to ensure the database perfectly reflects the user's visual actions and that text anchoring is bulletproof.*

- [x] **Fix Text Anchoring (DOM Offsets):** Persist `start_offset` / `end_offset` on excerpt nodes; selection create captures range offsets; highlight rendering prefers stored offsets with TOC-aware fallback for duplicates.
- [x] **Enforce True Provenance in `traceNodeLineage`:** Walk `SUMMARIZES` / `CONTAINS` via `ConnectionManager` (and resolve summaries downward to root excerpts). No DOM-indent provenance fallback.
- [x] **Legacy Offset Backfill:** `scripts/backfill_excerpt_offsets.py` dry-run / `--apply` fills missing offsets for L2 excerpts under each source.
- [x] **Re-anchor UX:** "Fix Highlight Position" (excerpt card menu) and "Fix Highlight for Active Excerpt" (source selection menu) rewrite offsets from the current Source Document selection.
- [ ] ~~**Database Edge Sync for Spatial Hierarchy (real-time Tab/drag):**~~ **Deferred by design.** Source Tree (sensemaking) and Synthesis (storytelling) stay separate; the Board explores alternate / lateral connections. Synthesis indent remains outline metadata.

## Phase 2: Workflow & UX Polish (Short-Term)
*The goal of this phase is to make the Sensemaking and Synthesis loops frictionless.*

- [x] **Chronological Source Tree Sorting:** Column 1 sorts by source-document highlight order (`sortColumn1NodesBySourceDocumentOrder`). Further hardening via `start_offset` sort is optional.
- [x] **Create Connection UX:** No auto-elevate of L2→L1 on SUMMARIZES; lightweight edge refresh (no full canvas remount) preserves scroll; source highlights only for density-2 excerpts.
- [x] **Persist prose `node_type`:** document-canvas returns `node_type`; Chapter/Part labels survive reload.
- [x] **Click source highlight → focus excerpt:** Clicking `.excerpt-highlight` activates the matching Source Tree card.
- [x] **Multi-Select Payload Upgrades:** Dragging a multi-selected group into Synthesis preserves relative tree-column indents; Connections List A/B accepts all IDs from the drag payload.
- [x] **"Summarize-in-Place" Edge Creation:** Synthesis / tree summarize flows create `SUMMARIZES` edges from the new summary to the child excerpt/node.
- [x] **`DEFINITION_OF` ontology + Connections:** Logical axis type for name→passage links; Connections dropdown loads it; distinct amber LeaderLine stroke (not hierarchy).
- [x] **Click-to-reveal topology:** Selecting a hub highlights `DEFINITION_OF` partners + `SUMMARIZES` children (and source spans); active connection mode includes those edges in lineage. Multi-summary visual “swath” deferred.
- [x] **Duplicate hub collapse:** Same `start_offset`/`end_offset` (or identical title/text) Concepts collapse to one Source Tree card; edges remap onto the canonical hub.
- [x] **Column 2+ document order:** Higher columns sort by hub/child `start_offset` (not created_at).
- [x] **Source Tree click priority:** Topology-first (definition + children + Active lines); own source scroll only when the hub has no partners. Focus/Board remain the deep neighborhood views.
- [x] **Connection line layering:** Lines render behind cards (`z-index`); default dim (0.15) with hover-focus brightening on incident edges.
- [x] **Workspace pin hotkeys:** Alt+1/2/3 pin Source / Board / Synthesis layouts; repeat the same key to cycle context-aware presets (Read, split, studio).
- [x] **Isolation Degree:** Isolate Off/1–4/All folds non-neighborhood cards; composes with taxonomy filters.

## Phase 3: Taxonomy & Filtering (Mid-Term)
*The goal of this phase is to utilize the new strict node typing (Excerpt, Summary, Concept, Chapter, Part) to empower navigation.*

- [x] **Taxonomy Filters:** Source Tree header filter (All / Excerpts / Summaries / Prose / Concepts) composes with Isolation Degree folding.
- [x] **Batch Type Reassignment:** Multi-select + context menu opens the type modal and `PUT /api/nodes` for each selected node.
- [x] **Visual Node Distinctions:** Chapter/Part/Section/Sub-section styling in the Synthesis outliner (aligned with Source Tree prose cues).

## Phase 4: Export & Advanced "Side-Quests" (Long-Term)
*The goal of this phase is to turn the synthesized graph into portable knowledge.*

- [ ] **Linear Document Export:** Build an export engine that traverses the Synthesis pane from top to bottom, reading the hierarchical structure, and exporting a clean, formatted Markdown document. *(Clipboard markdown export exists as a baseline.)*
- [ ] **Smart Import Parser:** Upgrade the copy/paste text ingestion engine. If a user pastes a bulleted list (like from OneNote), the parser should read the tab/spacing indents and automatically assign `Excerpt` to root bullets, `Summary` to indented bullets, and generate the proper hierarchical database edges immediately.
- [ ] **Graph Visualization (Flow View):** Polish the 2D canvas view to visualize the lateral and hierarchical edges generated during the Synthesis phase, allowing for a mind-map style alternative to the columnar outliner.

## Phase 5: Continuous Core Tuning & Source Expansion (Track 1)
*The goal of this phase is to eliminate UI/UX friction in the core extraction loop and expand ingestion beyond raw text pasting.*

- [x] **Fluidity & Mode Switching:** Alt+1/2/3 workspace pins with repeat-to-cycle presets (Read, Source+Tree, split Board/Synthesis, Studio when both exist). Manual layout toggle remains available.
- [ ] **Web Ingestion:** Integrate a web-clipper (e.g., Mozilla Readability) to parse URLs into standard Document nodes natively within the Source Tab.
- [ ] **PDF Ingestion:** Implement `pdf.js` in the Source pane. Map PDF bounding boxes (X/Y coordinate space) to the existing `start_offset` / `end_offset` extraction engine to maintain perfect data provenance.
- [ ] **Continuous Ergonomics:** Refine the "Compressed Tree-View" for progressive summarization and ensure multi-select drag-and-drop mechanics remain responsive as graph size scales.

## Phase 6: Multi-Modal Sensemaking (Track 2)
*The goal of this phase is to break out of text-only nodes and allow users to map parallel histories, timelines, and quantitative data.*

- [ ] **Metadata Schema Expansion:** Update the `PUT /api/nodes` logic and "Change Node Type" modal to accept structural metadata properties: `date_start`, `date_end`, `location`, and `numeric_value`.
- [ ] **Timeline View:** Create a new workspace tab that plots nodes horizontally based on their `date` properties, automatically drawing lateral edges to show event causality.
- [ ] **Matrix/Table View:** Build a dynamic grid view where the Y-axis represents `location` (or entity) and the X-axis represents `time`, dropping connected summary nodes into the intersecting cells.
- [ ] **Quantitative Charting:** Introduce a Chart tab (using Chart.js or Recharts). Link excerpted numeric values to chart data points, allowing visual graphs (e.g., GDP, Deaths over time) to update dynamically when the underlying source excerpt is modified.

## Phase 7: The Multiplayer Horizon (Track 3)
*The goal of this phase is to transition the graph from a private PKM into a collaborative, crowdsourced sensemaking network.*

- [ ] **User & Role Authentication:** Refactor the backend database schema to associate nodes and edges with specific `user_id`s and roles (e.g., verified MD, community contributor).
- [ ] **Reputation & Edge Weighting:** Implement a scoring system where connections validated by domain experts carry heavier mathematical weight, altering the visual gravity and layout of shared graph views.
- [ ] **Spoken Layer (Audio Integration):** Configure cloud storage (e.g., AWS S3) to host audio files. Link audio URLs to specific `node_id`s and build an in-app audio player.
- [ ] **Gamification Engine:** Create a ledger to track and display "contribution points" for users who narrate nodes or accurately map complex connections.