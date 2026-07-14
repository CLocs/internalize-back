# Internalize: Development Roadmap

## Phase 1: Stabilization & Data Provenance (Immediate)
*The goal of this phase is to ensure the database perfectly reflects the user's visual actions and that text anchoring is bulletproof.*

- [ ] **Fix Text Anchoring (DOM Offsets):** Replace naive string matching (`indexOf`) in the document highlight rendering with precise DOM offset tracking (e.g., `startOffset`, `endOffset`, or XPath). This will fix the bug where identical strings (like "CHAPTER 2") incorrectly anchor to the first instance (Table of Contents) instead of the actual body text.
- [ ] **Enforce True Provenance in `traceNodeLineage`:** Refactor the deep trace engine. It must query `ConnectionManager.edges` for `type: 'hierarchy'` to find a node's true origin. It should only use visual spatial indentation as a fallback if the edge explicitly does not exist.
- [ ] **Database Edge Sync for Spatial Hierarchy:** Currently, indenting a node (`Tab` / `Shift+Tab`) or dragging a node under another updates the `data-indent-level`. This must be wired to the backend API to physically create/update/delete `hierarchy` edges in the graph database in real-time.

## Phase 2: Workflow & UX Polish (Short-Term)
*The goal of this phase is to make the Sensemaking and Synthesis loops frictionless.*

- [ ] **Chronological Source Tree Sorting:** Refine the logic from Kaizen 120 so that Column 1 (Excerpts) strictly sorts nodes based on their physical top-to-bottom appearance in the Source Document, rather than creation date or alphabetical order.
- [ ] **Multi-Select Payload Upgrades:** Ensure that dragging a multi-selected group of nodes from the Source Tree into the Synthesis pane (or into the Connections List A/B) transfers all IDs seamlessly and preserves their relative indentations upon dropping.
- [ ] **"Summarize-in-Place" Edge Creation:** Ensure that when a user hits `Ctrl+S` in the Synthesis pane, the API call explicitly creates a hierarchical edge linking the new Summary node (parent) to the pushed-down Excerpt node (child).

## Phase 3: Taxonomy & Filtering (Mid-Term)
*The goal of this phase is to utilize the new strict node typing (Excerpt, Summary, Concept, Chapter, Part) to empower navigation.*

- [ ] **Taxonomy Filters:** Build a UI toggle in the Source Tree to filter nodes by type (e.g., "Show only Prose Structure" or "Hide Excerpts").
- [ ] **Batch Type Reassignment:** Create a robust UI to multi-select nodes and assign them a new type simultaneously, utilizing the custom prompt modal.
- [ ] **Visual Node Distinctions:** Implement subtle CSS variations for Prose Structure nodes (e.g., Chapters and Parts) to visually separate them from Knowledge Graph nodes (Excerpts, Summaries) in the Synthesis outliner.

## Phase 4: Export & Advanced "Side-Quests" (Long-Term)
*The goal of this phase is to turn the synthesized graph into portable knowledge.*

- [ ] **Linear Document Export:** Build an export engine that traverses the Synthesis pane from top to bottom, reading the hierarchical structure, and exporting a clean, formatted Markdown document. 
- [ ] **Smart Import Parser:** Upgrade the copy/paste text ingestion engine. If a user pastes a bulleted list (like from OneNote), the parser should read the tab/spacing indents and automatically assign `Excerpt` to root bullets, `Summary` to indented bullets, and generate the proper hierarchical database edges immediately.
- [ ] **Graph Visualization (Flow View):** Polish the 2D canvas view to visualize the lateral and hierarchical edges generated during the Synthesis phase, allowing for a mind-map style alternative to the columnar outliner.
