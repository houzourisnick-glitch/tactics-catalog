\# CRITICAL INQUIRY AI CORE FOUNDATIONS AND DEPLOYMENT GUIDE

\#\# How to Use the Critical Inquiry AI Curriculum Engine (v3.0)

This guide explains how to use the Critical Inquiry AI Curriculum Engine as a design assistant for secondary English Language Arts. It describes the core documents, the deployment workflow, and the protocols that keep the engine rigorous, accessible, and ethically grounded.

\---

\#\# 1\. PURPOSE OF THIS GUIDE

This guide helps teachers, curriculum leaders, and instructional designers:

\- Understand what the engine is for and what it is not.  
\- Use the core documents together as a coherent system.  
\- Deploy lessons and units with appropriate verification, adaptation, and care.  
\- Maintain version control and continuous improvement.

The engine is a \*\*design assistant\*\*, not an autonomous curriculum authority. All outputs require human review before classroom use.

\---

\#\# 2\. CORE DOCUMENTS AND THEIR ROLES

The engine consists of five interlocking documents. Use them together, not in isolation.

\#\#\# 2.1 CI\_CORE\_SYSTEM\_INSTRUCTIONS\_v3.0.md

\*\*Role:\*\* Governing behavior and priorities.

This document defines:

\- The engine’s stance, epistemology, and non-negotiable principles.  
\- The authority and conflict protocol.  
\- The core inquiry architecture and constructive alignment chain.  
\- Text-set, critical perspective, and claim-revision requirements.  
\- Disciplinary-practice modules (craft, writing process, test-adjacent, aesthetic).  
\- Instructional design rules and tactic selection constraints.  
\- Access, differentiation, and care principles.  
\- Sensitivity and safeguarding decision tree.  
\- Source integrity and Source Verification Gate.  
\- Standards Resolution Protocol and Standards Alignment Record.  
\- Framing Transparency and leading-language rules.  
\- Output contract (required sections for every lesson or unit).

\*\*Use this document when:\*\*

\- Configuring the engine in an AI environment.  
\- Resolving conflicts between attachments, assumptions, or requests.  
\- Auditing whether a lesson’s design logic matches the engine’s stance.

\---

\#\#\# 2.2 CI\_CORE\_KNOWLEDGE\_BASE\_v3.0.md

\*\*Role:\*\* Conceptual and procedural grounding.

This document provides:

\- Definitions of core concepts (Justice, Inquiry, Action, critical literacy, counter-archive, provisional claim, ethical limit, etc.).  
\- The Beach, Thein, & Webb (BTW) Justice–Inquiry–Action framework.  
\- Core inquiry movement and text-set design patterns.  
\- Critical inquiry lesson patterns and the 3-Turn Claim Revision Model.  
\- Language and literacy frames (morphology, syntax, modality, enthymeme).  
\- Critical perspective knowledge (definitions, guiding questions, evidence requirements).  
\- Disciplinary-practice modules (craft/structure, writing process, test-adjacent, aesthetic).  
\- Differentiation and access patterns.  
\- Assessment knowledge and UDL principles.  
\- Source Verification Knowledge and Standards Alignment Knowledge.  
\- Action design sequence and safeguards.  
\- Framing, leading language, and critical stance guidance.  
\- Retrieval use protocol (which sections to retrieve for which tasks).

\*\*Use this document when:\*\*

\- Designing or revising units and lessons.  
\- Selecting or refining critical perspectives.  
\- Planning text sets and multi-source inquiry.  
\- Designing assessments and action artifacts.  
\- Supporting vocabulary, syntax, and academic discourse.

\---

\#\#\# 2.3 CI\_CORE\_QA\_CHECKLIST\_v3.0.md

\*\*Role:\*\* Pre-release validation.

This checklist ensures that lessons and units are:

\- Aligned to standards and objectives.  
\- Inquiry-rich and claim-revision oriented.  
\- Source-verified and ethically bounded.  
\- Accessible and developmentally appropriate.  
\- Sensitively handled where content is high-risk.  
\- Tactically coherent and schema-compliant.  
\- Framing-transparent where critical lenses are used.

\*\*Use this document when:\*\*

\- Reviewing any generated lesson or unit before classroom use.  
\- Identifying critical failures, warnings, and required revisions.  
\- Documenting the QA decision and approved version.

No lesson or unit should be released until all critical failures are resolved.

\---

\#\#\# 2.4 CI\_TACTICS\_CATALOG\_v3.0.json

\*\*Role:\*\* Authorized instructional moves.

The Tactics Catalog is a structured JSON file containing reusable instructional tactics. Each tactic includes:

\- \`tactic\_id\` (unique identifier)  
\- \`tactic\_name\`  
\- \`phase\` (e.g., warm\_up, direct\_instruction, guided\_practice, independent\_practice, closure)  
\- \`text\_type\` (e.g., literary, informational, legal, visual, multimodal, data)  
\- \`scaffold\_level\` (e.g., high, medium, low)  
\- \`cognitive\_demand\` (e.g., DOK 1–4 or descriptive equivalent)  
\- \`grouping\` (e.g., individual, pairs, VRG\_small, whole\_class)  
\- \`estimated\_time\_minutes\_min\`  
\- \`estimated\_time\_minutes\_max\`  
\- \`instructional\_moves\` (ordered list of teacher and student moves)  
\- \`output\_product\` (description of the student artifact or observable behavior)  
\- \`contraindications\` (conditions under which the tactic should not be used)  
\- \`grade\_band\` (e.g., \`"9-10"\`, \`"11-12"\`, \`"9-12"\`)  
\- \`formative\_check\` (boolean)  
\- \`framing\_stance\` (\`explicitly\_critical\`, \`open\_exploratory\`, \`neutral\_descriptive\`)

\*\*Use this document when:\*\*

\- Selecting instructional tactics for a lesson.  
\- Ensuring tactics match phase, text type, grade band, and time.  
\- Verifying that tactics include formative checks and appropriate framing stance.  
\- Updating or extending the catalog with new tactics.

\---

\#\#\# 2.5 CI\_CORE\_QA\_DECISION\_RECORD\_TEMPLATE.md (Optional but Recommended)

\*\*Role:\*\* Documenting QA decisions.

A simple template for recording:

\- Overall status (PASS / WARNING / FAIL).  
\- Critical failures identified.  
\- Warnings requiring teacher judgment.  
\- Required revisions before release.  
\- Reviewer, date, plan version, and approval status.

\*\*Use this document when:\*\*

\- Maintaining an audit trail for curriculum decisions.  
\- Supporting collaboration and continuity across teachers or departments.  
\- Tracking revisions and approved versions.

\---

\#\# 3\. DEPLOYMENT WORKFLOW

Use this end-to-end workflow to deploy lessons and units responsibly.

\#\#\# 3.1 PRE-GENERATION: CONTEXT AND PARAMETERS

Before generating a lesson or unit, clarify:

1\. \*\*Grade/course context\*\*    
   \- Grade level, course name, and student context.  
   \- Any known access needs, language profiles, or local constraints.

2\. \*\*Unit or lesson focus\*\*    
   \- Anchor text(s) or disciplinary practice focus (craft, writing process, test-adjacent, aesthetic).  
   \- Unit theme, essential question, or problem.

3\. \*\*Schedule\*\*    
   \- Minutes per period.  
   \- Number of periods for the lesson or unit.

4\. \*\*Standards context\*\*    
   \- User-supplied standards (preferred), or    
   \- Request for AI-proposed standards, or    
   \- Permission to use placeholder standard descriptions.

5\. \*\*Desired output\*\*    
   \- Unit plan, single lesson, SAY-DO script, HTML, DOCX, JSON, etc.

6\. \*\*Lesson type\*\*    
   \- Critical inquiry, or    
   \- Disciplinary-practice-focused (craft, writing process, test-adjacent, aesthetic).

Record these parameters in a brief “Unit/Lesson Brief” document or note.

\---

\#\#\# 3.2 GENERATION: USING THE ENGINE

When generating a lesson or unit:

1\. \*\*Provide the context\*\*    
   \- Share the Unit/Lesson Brief with the engine.  
   \- Attach or reference any required texts, standards, or institutional documents.

2\. \*\*Specify constraints and preferences\*\*    
   \- Indicate any non-negotiables (e.g., no public sharing, specific texts, local policies).  
   \- Specify whether you want AI-proposed standards or will supply them.

3\. \*\*Request the full output contract\*\*    
   \- Ensure the engine includes all required sections: metadata, rationale, standards, EQ/CIQ, text set, perspective, targets, vocabulary, sequence, SAY/DO, differentiation, sensitivity, framing note, assessment, ethical limit, dossier artifact, Source Verification Table, next-lesson bridge, and QA report.

4\. \*\*Check for conflicts\*\*    
   \- If the output shows conflicting assumptions or authorities, resolve them before proceeding.

\---

\#\#\# 3.3 POST-GENERATION: TEACHER REVIEW AND ADAPTATION

After generation:

1\. \*\*Read for coherence and stance\*\*    
   \- Does the lesson align with your students, course, and local context?  
   \- Does it honor the engine’s non-negotiable stance (justice, inquiry, action, openness)?

2\. \*\*Check constructive alignment\*\*    
   \- Do the standard, objective, EQ, CIQ, instruction, artifact, and success criteria align?  
   \- Does the assessment directly measure the disciplinary action required by the standard?

3\. \*\*Review source integrity\*\*    
   \- Verify quotations, statistics, dates, and contextual claims against full, reliable sources.  
   \- Ensure the Source Verification Table is complete and accurate.  
   \- Remove or relabel any unverified or contested quotations in student-facing materials.

4\. \*\*Review critical lens discipline\*\*    
   \- Are the selected perspectives developmentally appropriate?  
   \- Are lenses defined, evidenced, and limited?  
   \- Are alternative interpretations structurally possible?

5\. \*\*Review access and care\*\*    
   \- Are differentiation pathways substantive and accessible?  
   \- Are sensitive content safeguards in place where needed?  
   \- Is personal disclosure optional?

6\. \*\*Review timing and feasibility\*\*    
   \- Can the lesson reasonably be completed in the declared period?  
   \- Are phase durations realistic?  
   \- Are materials and technology available?

7\. \*\*Adapt as needed\*\*    
   \- Adjust timing, texts, grouping, or artifacts to fit your context.  
   \- Preserve claim revision, source tension, and ethical limits when adapting.

\---

\#\#\# 3.4 QA REVIEW: USING THE CHECKLIST

Before classroom use:

1\. \*\*Run the QA Checklist v3.0\*\*    
   \- Complete all sections (Project Control, Constructive Alignment, Standards Alignment, Inquiry Quality, Source Integrity, Critical Lens Discipline, Access/Differentiation/Care, Instruction/Assessment, Say-Script Framing, Sensitivity/Safeguarding, Tactic Catalog Compliance).  
   \- Assign a status (\`PASS\`, \`WARNING\`, \`FAIL\`, \`NOT\_APPLICABLE\`) to each check.

2\. \*\*Resolve critical failures\*\*    
   \- Do not release the lesson if any critical failure remains unresolved.  
   \- Document required revisions and complete them.

3\. \*\*Address warnings\*\*    
   \- Make judgment-based revisions where needed.  
   \- Note any residual risks or assumptions.

4\. \*\*Complete the QA Decision Record\*\*    
   \- Record overall status, critical failures, warnings, required revisions, reviewer, date, plan version, and approval status.

5\. \*\*Approve for deployment\*\*    
   \- Only after all critical failures are resolved should the lesson be approved for classroom use.  
   \- Assign an approved version identifier (e.g., “Unit 2 Lesson 3 v3.0-approved-2026-08-25”).

\---

\#\#\# 3.5 CLASSROOM DEPLOYMENT

When teaching the lesson:

1\. \*\*Prepare materials\*\*    
   \- Print or share student-facing materials with verified quotations and sources.  
   \- Prepare any technology, VNPS surfaces, or groupings.

2\. \*\*Review SAY/DO scripts\*\*    
   \- Internalize key teacher moves and language frames.  
   \- Adapt scripts to your voice and context while preserving inquiry logic.

3\. \*\*Monitor inquiry and access\*\*    
   \- Listen for provisional claims, evidence use, counterclaims, and revisions.  
   \- Ensure all students have access to the intellectual target.

4\. \*\*Collect process evidence\*\*    
   \- Gather annotations, claim cards, discussion notes, drafts, revisions, and reflections.

5\. \*\*Note emergent issues\*\*    
   \- Record timing issues, access barriers, or sensitivity concerns for future revision.

\---

\#\#\# 3.6 POST-DEPLOYMENT: REFLECTION AND REVISION

After teaching:

1\. \*\*Reflect on inquiry quality\*\*    
   \- Did students form, test, and revise claims?  
   \- Did they engage meaningfully with power, craft, or practice?  
   \- Did they produce a meaningful next question?

2\. \*\*Reflect on access and care\*\*    
   \- Were all students able to participate meaningfully?  
   \- Were sensitivity safeguards effective?  
   \- Were differentiation pathways sufficient?

3\. \*\*Reflect on timing and feasibility\*\*    
   \- What took longer or shorter than expected?  
   \- What materials or supports were missing?

4\. \*\*Revise the plan\*\*    
   \- Update timing, texts, scaffolds, or assessments as needed.  
   \- Preserve core inquiry moves and ethical limits.

5\. \*\*Version the revision\*\*    
   \- Assign a new version identifier (e.g., “v3.1” or “v3.0-revised-2026-09”).  
   \- Update the QA Decision Record with post-deployment notes.

\---

\#\# 4\. VERSION CONTROL AND CHANGE MANAGEMENT

Maintain clear versioning for all core documents and curriculum artifacts.

\#\#\# 4.1 VERSION NUMBERING

Use a major.minor scheme:

\- \*\*Major version (v2.0 → v3.0)\*\*    
  \- Significant changes to stance, protocols, or architecture.  
  \- Changes that affect how lessons are designed or validated.

\- \*\*Minor version (v3.0 → v3.1)\*\*    
  \- Clarifications, examples, or incremental improvements.  
  \- Bug fixes or wording adjustments that do not change core logic.

\#\#\# 4.2 CHANGE LOG

For each core document, maintain a brief change log:

\- Version number.  
\- Date.  
\- Summary of changes.  
\- Rationale for changes.  
\- Author or reviewer.

Example:

\`\`\`text  
v3.0 – 2026-08-25  
\- Added Standards Resolution Protocol and Standards Alignment Record.  
\- Added Framing Transparency and leading-language rules.  
\- Added disciplinary-practice modules (craft, writing process, test-adjacent, aesthetic).  
\- Updated UDL language toward CAST 3.0.  
\- Added tactic schema fields (grade\_band, formative\_check, framing\_stance).  
\- Aligned with updated QA Checklist and Knowledge Base.  
\`\`\`

\#\#\# 4.3 DEPRECATION

When a new major version is released:

\- Mark the previous major version as “deprecated” but retain it for reference.  
\- Encourage users to migrate to the new version over a defined period.  
\- Document any breaking changes that require lesson redesign.

\---

\#\# 5\. USING THE NEW PROTOCOLS

\#\#\# 5.1 STANDARDS RESOLUTION PROTOCOL

When standards are involved:

1\. Prefer user-supplied standards.  
2\. If AI-proposed standards are requested, label them as \`unverified\`.  
3\. Use placeholder standard descriptions when no standards are provided or requested.  
4\. Complete a Standards Alignment Record for every lesson that references standards.  
5\. Resolve conflicts in favor of user-supplied standards.

\#\#\# 5.2 SOURCE VERIFICATION GATE

For every lesson or unit:

1\. Treat all AI-generated quotations, statistics, dates, and contextual claims as unverified until checked.  
2\. Complete a Source Verification Table for every anchor and secondary source.  
3\. Exclude unverified or contested quotations from student-facing materials.  
4\. Replace unverifiable quotations with verified excerpts or clearly labeled paraphrases.

\#\#\# 5.3 FRAMING TRANSPARENCY

When using explicitly critical frames:

1\. Name the frame or lens in the script or teacher notes.  
2\. State that alternative frames and interpretations are possible.  
3\. Invite students to use evidence to support, complicate, or challenge the frame.  
4\. Include a Framing Transparency Note in the lesson output.

\#\#\# 5.4 TACTIC SELECTION AND SCHEMA ENFORCEMENT

When selecting tactics:

1\. Use only tactics from the authorized catalog.  
2\. Ensure all required schema fields are present.  
3\. Match phase, text type, grade band, and time.  
4\. Ensure at least one formative check per 20-minute instructional window.  
5\. Translate instructional moves into explicit SAY/DO blocks.

\#\#\# 5.5 SENSITIVITY AND SAFEGUARDING

When sensitive content is present:

1\. Identify triggering content and assign a risk level.  
2\. Provide content notes (teacher-facing and student-facing).  
3\. Offer opt-in/opt-out pathways and alternative text options.  
4\. Specify response protocols (private, semi-public, public).  
5\. Follow local safeguarding and legal requirements.

\---

\#\# 6\. EXAMPLE DEPLOYMENT SEQUENCE

\*\*Scenario:\*\* A Grade 10 teacher wants a 90-minute critical inquiry lesson on a short story and a counter-narrative essay, aligned to CCSS.

1\. \*\*Pre-generation\*\*    
   \- Complete a Unit/Lesson Brief: Grade 10 English, 90 minutes, anchor short story \+ counter-narrative essay, CCSS alignment requested, critical inquiry lesson.  
   \- Share the brief with the engine.

2\. \*\*Generation\*\*    
   \- Engine generates a full lesson with all output contract sections, including AI-proposed CCSS (labeled \`unverified\`), Source Verification Table, Framing Transparency Note, and QA report.

3\. \*\*Teacher review\*\*    
   \- Teacher verifies quotations and source metadata.  
   \- Adjusts timing and grouping for their class.  
   \- Confirms that critical lens (e.g., cultural \+ gender) is developmentally appropriate.

4\. \*\*QA review\*\*    
   \- Teacher runs the QA Checklist v3.0.  
   \- Resolves one critical failure (unverified quotation in student handout) by replacing it with a verified excerpt.  
   \- Addresses two warnings (timing tightness, need for additional sentence frames).  
   \- Completes the QA Decision Record and approves version “v3.0-approved-2026-08-25”.

5\. \*\*Classroom deployment\*\*    
   \- Teacher implements the lesson, collects process evidence, and notes emergent issues.

6\. \*\*Post-deployment\*\*    
   \- Teacher revises timing and adds sentence frames.  
   \- Versions the lesson as “v3.1-revised-2026-09”.  
   \- Updates the QA Decision Record with post-deployment notes.

\---

\#\# 7\. CONTINUOUS IMPROVEMENT

The engine is designed for iterative improvement.

\- Collect feedback from teachers and students.  
\- Track recurring warnings or failures in the QA Checklist.  
\- Update tactics, examples, and protocols as needed.  
\- Version changes transparently and maintain a change log.

\---

\*Critical Inquiry AI Curriculum Engine | Core Foundations and Deployment Guide v3.0\*

