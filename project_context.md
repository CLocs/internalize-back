# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.# Project: Internalize (Spatial Knowledge Engine)

## Core Philosophy & Goals
Internalize is a Personal Knowledge Management (PKM) application designed to bridge the gap between Sensemaking (reading/extracting) and Synthesis (writing/outlining). The primary goal is to maintain absolute data provenance. A user must be able to click a highly synthesized summary in their outline and trace it visually and chronologically all the way back to the original highlight in the source text. 

## Architectural Layout
The UI is a dark-themed, 3-pane spatial workspace tailored for desktop usage. 
* View 1: Source Document (Left) - Renders the raw text (e.g., articles, books) with physical highlight spans (`.excerpt-highlight`).
* View 2: Source Tree (Center) - A columnar view acting as the extraction inbox. Column 1 holds raw Excerpts. Column 2 holds Summaries.
* View 3: Synthesis Workspace (Right) - A spatial canvas/outliner where nodes are dragged, dropped, indented, and edited in place.

## Data Model
The system uses a graph database approach (Nodes and Edges) mapped to the DOM.
* Nodes possess a strict ontology: 'Excerpt', 'Summary', 'Concept', and Prose Structures ('Chapter', 'Part').
* Nodes track spatial visual state: `data-indent-level`, `data-density-level`, and `data-node-id`.
* Edges track relationships: Hierarchical (parent/child data provenance) and Lateral (cross-connections).

## Core UX Mechanics (The Engine)
* Spatial Drag and Drop: Nodes can be dragged from the Source Tree into the Synthesis Workspace. An injection indicator calculates the precise Y-coordinate drop point and inherits the visual indentation of the surrounding blocks.
* In-Place Progressive Summarization: Triggering a summary (via shortcut or right-click) instantly generates a child node, pushes the original excerpt down/right in the visual hierarchy, and highlights the text for immediate elision editing. 
* Multi-Select: The app utilizes industry-standard DOM tracking. Ctrl+Click toggles individual nodes. Shift+Click selects a contiguous range. Tab indents entire selected groups simultaneously.
* Deep Trace Back-Propagation: Clicking any node in the Synthesis pane triggers a recursive function that climbs the hierarchical graph and illuminates the ancestor cards, ultimately smooth-scrolling the Source Document to the exact origin text.

## Current Technical Priorities
* Refactoring text extraction to use precise DOM offset anchoring (startOffset/endOffset) instead of naive string matching to prevent duplicate string targeting.
* Hardening the `traceNodeLineage` engine to strictly prioritize database graph edges (`parent_id`) over visual DOM indentation to ensure true data provenance.