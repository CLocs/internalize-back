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
- [ ] **Multi-Select Payload Upgrades:** Ensure that dragging a multi-selected group of nodes from the Source Tree into the Synthesis pane (or into the Connections List A/B) transfers all IDs seamlessly and preserves their relative indentations upon dropping. *(IDs already transfer; relative indent preservation still open.)*
- [x] **"Summarize-in-Place" Edge Creation:** Synthesis / tree summarize flows create `SUMMARIZES` edges from the new summary to the child excerpt/node.

## Phase 3: Taxonomy & Filtering (Mid-Term)
*The goal of this phase is to utilize the new strict node typing (Excerpt, Summary, Concept, Chapter, Part) to empower navigation.*

- [ ] **Taxonomy Filters:** Build a UI toggle in the Source Tree to filter nodes by type (e.g., "Show only Prose Structure" or "Hide Excerpts").
- [ ] **Batch Type Reassignment:** Create a robust UI to multi-select nodes and assign them a new type simultaneously, utilizing the custom prompt modal.
- [ ] **Visual Node Distinctions:** Implement subtle CSS variations for Prose Structure nodes (e.g., Chapters and Parts) to visually separate them from Knowledge Graph nodes (Excerpts, Summaries) in the Synthesis outliner.

## Phase 4: Export & Advanced "Side-Quests" (Long-Term)
*The goal of this phase is to turn the synthesized graph into portable knowledge.*

- [ ] **Linear Document Export:** Build an export engine that traverses the Synthesis pane from top to bottom, reading the hierarchical structure, and exporting a clean, formatted Markdown document. *(Clipboard markdown export exists as a baseline.)*
- [ ] **Smart Import Parser:** Upgrade the copy/paste text ingestion engine. If a user pastes a bulleted list (like from OneNote), the parser should read the tab/spacing indents and automatically assign `Excerpt` to root bullets, `Summary` to indented bullets, and generate the proper hierarchical database edges immediately.
- [ ] **Graph Visualization (Flow View):** Polish the 2D canvas view to visualize the lateral and hierarchical edges generated during the Synthesis phase, allowing for a mind-map style alternative to the columnar outliner.
