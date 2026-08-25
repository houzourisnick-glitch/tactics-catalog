\# CRITICAL INQUIRY AI CURRICULUM ENGINE    
\#\# Deployment Guide for Knowledge Base and System Instructions (v2.0)

Use this document together with the Core System Instructions, Knowledge Base, QA Checklist, and Tactics Catalog. It explains how to organize, version, and deploy these resources so that the AI curriculum engine operates consistently and safely.

\---

\#\# Recommended Document Stack

| Document | Purpose | Deployment Location |  
|----------|---------|---------------------|  
| System Instructions | Governs behavior, priorities, output contract, conflict handling, and validation. | System/developer instruction field of the AI application. |  
| Knowledge Base | Provides definitions, design patterns, lens discipline, differentiation, and assessment knowledge. | Retrieval knowledge base or project files. |  
| Quality Assurance Checklist | Audits generated output before release. | Knowledge base plus teacher review workflow. |  
| Grade-Level Specifications | Adds grade-specific progression, texts, standards, and developmental constraints. | Separate grade-level knowledge base or project file. |  
| Unit Matrices | Defines active texts, inquiry tensions, standards, and sequence. | Project-specific retrieval folder. |  
| Tactic Catalog | Defines reusable instructional moves and exact tactic IDs. | Structured JSON knowledge base. |

\---

\#\# Deployment Principle

Do not place every document in one undifferentiated prompt. Use a layered architecture:

\- \*\*System instructions\*\* govern.    
\- The \*\*knowledge base\*\* informs.    
\- \*\*Project files\*\* specialize.    
\- The \*\*user request\*\* selects the active task.    
\- \*\*Quality assurance\*\* audits the result.

\---

\#\# Step-by-Step Deployment

1\. Create a permanent system-instruction file from the Core System Instructions document.    
2\. Create a retrieval collection named \*\*Critical Inquiry AI Knowledge Base\*\* and upload the Knowledge Base document.    
3\. Create a separate collection named \*\*Critical Inquiry QA\*\* and upload the checklist.    
4\. Create separate folders for each grade level rather than embedding grade rules in the core foundation.    
5\. Create project folders for each distinct unit or curriculum initiative.    
6\. Store unit matrices, anchor texts, source metadata, standards, and exemplar lessons inside the relevant project folder.    
7\. Store the instructional tactics catalog as structured JSON with tactic names, IDs, purpose, cognitive demand, grouping, timing, and contraindications.    
8\. At the start of each generation, identify the active project and schedule.    
9\. Generate the plan.    
10\. Run the Quality Assurance Checklist.    
11\. Revise failed items before sharing or classroom deployment.  

\---

\#\# Retrieval and File Naming

| Layer | Recommended Naming Pattern |  
|-------|----------------------------|  
| Core system | \`CI\_CORE\_SYSTEM\_INSTRUCTIONS\_v2.0.md\` |  
| Core knowledge | \`CI\_CORE\_KNOWLEDGE\_BASE\_v2.0.md\` |  
| QA | \`CI\_CORE\_QA\_CHECKLIST\_v2.0.md\` |  
| Grade specification | \`CI\_GRADE\_11\_SPECIFICATION\_v1.0.md\` |  
| Unit matrix | \`CI\_G11\_U1\_TEXT\_MATRIX\_v1.0.md\` |  
| Lesson exemplar | \`CI\_G11\_U1\_L05\_EXEMPLAR\_v1.0.md\` |  
| Tactic catalog | \`CI\_TACTICS\_CATALOG\_v2.0.json\` |

Use consistent versioning (\`v1.0\`, \`v1.1\`, \`v2.0\`) and avoid overwriting an approved version without a change log.

\---

\#\# Standard Request Template

Use a request template that supplies the missing variables without repeating the entire theory:

\> “Active project: \_\_\_\_\_\_. Grade/course: \_\_\_\_\_\_. Schedule: \_\_\_\_\_\_ minutes. Unit/lesson: \_\_\_\_\_\_. Anchor text/source: \_\_\_\_\_\_. Required standards: \_\_\_\_\_\_. Student context and access needs: \_\_\_\_\_\_. Desired output: unit plan / lesson / SAY-DO / HTML / DOCX / JSON. Use the active unit matrix and run the full QA protocol. Disclose assumptions and source-verification needs.”

Adjust fields as needed for your context, but always include:

\- Active project    
\- Grade/course    
\- Schedule    
\- Unit/lesson    
\- Anchor text/source    
\- Standards    
\- Student context and access needs    
\- Desired output format  

\---

\#\# Deployment Modes

| Mode | Use |  
|------|-----|  
| Unit generation | Use system instructions \+ core KB \+ grade specification \+ unit matrix. |  
| Lesson generation | Use system instructions \+ core KB \+ active unit \+ relevant lesson exemplars \+ schedule. |  
| Revision | Provide the existing lesson and identify exact changes; preserve unaffected elements. |  
| Source audit | Use core KB \+ source metadata; request verification rather than generating uncertain quotations. |  
| Format conversion | Preserve content and structure; do not silently alter alignment or pedagogy. |  
| JSON export | Use the formal schema and validate required fields. |

\---

\#\# Teacher Review Workflow

\- Check source accuracy and quotation integrity.    
\- Check that the lesson is possible in the declared time.    
\- Check that the critical lens is appropriate and not superficial.    
\- Check that students can disagree responsibly.    
\- Check that the action or public artifact is authentic and feasible.    
\- Check cultural and historical framing with authoritative sources.    
\- Check accessibility and sensitive-content protocols.    
\- Record revisions and retain the approved version as an exemplar.  

\---

\#\# Version Control

\- Version system instructions separately from the knowledge base.    
\- Do not overwrite an approved version without a change log.    
\- When a lesson exposes a recurring problem, revise the system rule or knowledge base—not only the individual lesson.    
\- Maintain an exemplar bank tagged by grade, standard, text type, duration, tactic, and cognitive move.  

\---

\#\# Implementation Cautions

\- The system is a design assistant, not an autonomous curriculum authority.    
\- Do not deploy a generated lesson without teacher review.    
\- Do not publish student work publicly without consent and local policy compliance.    
\- Do not expose student-identifying information in prompts or dossier artifacts.    
\- Do not treat a critical pedagogy framework as permission to predetermine student conclusions.    
\- Do not overpopulate lessons with every tactic; cognitive coherence matters more than feature count.    
\- The Tactics Catalog must be stored as structured JSON conforming to the schema. Any tactic missing required fields must be flagged and excluded from retrieval until corrected.  

\---

\#\# Minimum Acceptance Test

Before treating the engine as production-ready, test it with at least five requests:

1\. A literary lesson.    
2\. An informational/legal lesson.    
3\. A visual/multimodal lesson.    
4\. A 60-minute lesson.    
5\. A unit with sensitive historical content.  

Run each through the QA checklist and compare outputs for consistency, source integrity, timing, differentiation, and genuine claim revision.

\---

\*Critical Inquiry AI Curriculum Engine | Deployment Guide (v2.0)\*  
