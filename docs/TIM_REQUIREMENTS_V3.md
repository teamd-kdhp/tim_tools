# TIM REQUIREMENTS V3

## 0. Purpose
TIM's purpose is to serve as the user's dedicated strategic partner and achieve the following:

- provide ChatGPT-level natural conversation quality
- remember past context, policies, and decisions for continuous conversation
- access internal Google Drive, external APIs, internet information, and later SaaS systems when needed
- support discussion and analysis for business, finance, new business, planning, and practical execution
- later connect to execution systems such as OpenClaw

---

## 1. System Philosophy

### 1-1. TIM is the only dialogue interface
The user always talks only to TIM.
Internally there may be multiple modules, but externally TIM must behave as one consistent chief-of-staff partner.

### 1-2. LLM is the core intelligence
TIM's thinking, reasoning, explanation, and conversation quality must always be centered on LLM.
TIM itself must not become a fixed rule-based thinking engine.

### 1-3. TIM is “LLM + extensions”
TIM's value is not just conversation.
TIM combines:
- conversation
- memory
- state management
- external information access
- internal information access
- future execution ability

### 1-4. TIM must not become a bottleneck
TIM must not become a degraded wrapper around ChatGPT.
Therefore:
- conversation quality must be secured by high-performance LLM
- unnecessary custom rules must be minimized
- TIM's main role is to strengthen LLM using memory, state, and data access

### 1-5. Brain architecture is optional
TIM does not have to be implemented as a “Brain” architecture.
Any architecture is acceptable if:
- LLM remains the center
- memory/state/data are added cleanly
- natural conversation quality is preserved

---

## 2. High-level Architecture

```text
User
 ↓
TIM (only dialogue interface / LLM-first orchestrator)
 ├ Conversation Core (LLM)
 ├ Memory Layer
 ├ State Layer
 ├ Context Builder
 ├ Data Layer
 │   ├ Web Connector
 │   ├ Drive Connector
 │   ├ Internal DB Connector
 │   └ SaaS Connector
 └ Executor Connector (future)
3. TIM Core Requirements
3-1. Responsibilities

TIM must:

have natural conversation with the user
interpret user intent
determine what information is needed
call Memory / State / Data layers when needed
build context for LLM
integrate LLM output
suggest next actions when helpful
later serve as the origin point for execution instructions
3-2. Personality requirements

TIM should behave like an internal strategic partner.

Required qualities:

natural conversation
understands rough or abstract input
management perspective
organizes situations clearly
can become concrete when needed
maintains continuity across time
helps move work forward

Avoid:

starting from zero every time
overly fixed templates
generic consultant-like responses
visibly rule-based behavior
lack of awareness of internal context
4. Conversation Core Requirements
4-1. Goal

Provide ChatGPT-level conversation quality.

4-2. Required abilities
natural language understanding
interpretation of ambiguous consultation
context-aware response
brainstorming
issue structuring
hypothesis generation
decision support
expression adjustment
natural movement from chat to practical work
4-3. Modes

At minimum:

A. Conversation Mode

Examples:

What do you think?
Something feels off
Organize this
How do you see the direction?
B. Command Mode

Examples:

Compare these
Give me next steps
Draft a business plan
Review past documents and summarize
4-4. Quality requirements
close to ChatGPT in naturalness
follows abrupt topic changes
connects to past projects
understands the user's executive role
neither too stiff nor too casual
feels like talking leads to progress
5. Memory Layer Requirements
5-1. Goal

Store long-term important information.

5-2. What to store
user policies
decision tendencies
important preferences
business/project basics
background of ongoing projects
important past decisions
reusable discussion points
internal structure and stakeholder information
standing rules
5-3. What not to store
one-off small talk
temporary emotions
low-confidence hypotheses
trivial one-time topics
important numbers not yet confirmed
5-4. Memory types

At minimum:

A. Personal Memory
preferences
thinking style
priorities
management stance
B. Project Memory
project/business background
current situation
recurring issues
past discussion history
C. Decision Memory
what was decided
why it was decided
what remains pending
D. Relationship Memory
internal/external stakeholders
counterpart characteristics
roles
5-5. Requirements
retrieve only relevant memories during conversation
do not pass all memories every time
support update history
allow memory correction
support importance hierarchy
6. State Layer Requirements
6-1. Goal

Track “where things are now” for active work.

6-2. What state includes
current projects
phases
progress
pending items
blocked items
next actions
current hypotheses
recent discussion points
unresolved items
6-3. Difference from Memory

Memory is long-term.
State is current working status.
They must not be mixed.

6-4. Requirements
project-level state tracking
state updates
current-position awareness
next-action storage
blocked-reason storage
priority management
7. Context Builder Requirements
7-1. Goal

Prepare the right context before sending to LLM.

7-2. Inputs
latest user input
relevant memory
relevant state
relevant Drive materials
relevant external information
relevant past decisions
7-3. Requirements
identify project/topic
select relevant information
remove noise
control information volume
prioritize useful context
7-4. Forbidden
sending all data every time
mixing irrelevant projects
automatically prioritizing old information
8. Data Layer Requirements
8-1. Goal

Allow TIM to retrieve needed information from external and internal sources.

8-2. Components
Web Connector
Drive Connector
Internal DB Connector
SaaS Connector
History Connector
8-3. Principle
retrieval and judgment must be separated
retrieval alone does not equal conclusion
final interpretation must come from LLM
9. Connector Requirements
9-1. Web Connector

Targets:

news
policy/regulation
market information
competitors
similar cases
official site information

Required:

search query generation
URL retrieval
content extraction
source retention
latest information retrieval
summarization material preparation
9-2. Drive Connector

Targets:

Google Drive
docs
sheets
PDFs
proposals
contracts
minutes
business plans
internal memos

Operational assumptions:

create a dedicated TIM Google account
share only needed folders
start read-only
minimize edit/delete permissions

Required:

file search
folder-limited search
file content retrieval
docx / pdf / sheet / text reading
related file listing
metadata retrieval
citation/source retention
9-3. Internal DB Connector

Targets:

sales
customer information
behavioral logs
contract information
usage data
finance data

Required:

SQL / API retrieval
predefined query support
table summarization
project-level data access
extraction for numeric comparisons
9-4. SaaS Connector

Targets:

Money Forward
CRM
attendance
accounting
invoicing
task management SaaS

Priority:

API integration
official connector
MCP / function-calling style connection
browser automation later

Initial policy:

read/reference first
updates/sending later
9-5. History Connector

Targets:

past consultation logs
past decisions
past TODOs
previous conclusions
comparison histories

Required:

project-based history retrieval
topic-based history retrieval
chronological summary
important conversation extraction
10. LLM Usage Requirements
10-1. Principle

Use LLM broadly.
TIM must not become the bottleneck.

10-2. Role of LLM
thinking
reasoning
expression
hypothesis generation
issue structuring
summarization
comparison
decision support
natural conversation generation
10-3. What LLM should do
final judgment
integrated answer
natural explanation
interpretation across multiple sources
executive-facing structuring
clarification of ambiguous consultation
10-4. What LLM should not mainly do
simple fixed retrieval
authentication itself
purely mechanical transformations
strict calculation-only work
access permission management
10-5. Requirements
LLM always participates in final thinking
TIM logic must not interfere with LLM quality
provide high-quality context before inference
output should be natural conversation
structured internal data can still be maintained
11. Response Requirements
11-1. Surface response

Responses may be natural conversation.
They should not be forced into the same template every time.

11-2. Internal structure

Internally TIM should be able to hold at least:

current_context
key_points
hypothesis
judgment
next_actions
missing_info
memory_updates
11-3. Response quality
executive-friendly
organized points
balance between abstract and concrete
next actions when helpful
missing information when necessary
11-4. By mode

Brainstorming:

soft natural conversation

Practical work:

organized response

Direct instruction:

concrete steps or deliverables
12. Permissions Requirements
12-1. Principle

TIM is treated like internal staff, but with only necessary permissions.

12-2. Google Drive
dedicated TIM account
limited sharing scope
read-focused initially
ideally log what TIM accessed
12-3. SaaS
reference first
updates only with explicit permission
secure credential storage
operation logs
12-4. Future
grant execution rights gradually
sending/deleting/updating may require approval
13. Audit / Logging Requirements
13-1. Goal

If TIM is truly internal staff-like, it should be possible to trace what it looked at and what it based its response on.

13-2. Logs to keep
user input
invoked layers
referenced data sources
retrieved files / URLs
summary of LLM input context
summary of response
memory/state updates
13-3. Notes
scope of sensitive raw logs should be controlled
raw and summary logs may be separated
14. Executor Connector Requirements
14-1. Goal

Allow future execution through systems such as OpenClaw.

14-2. Example execution
file creation
draft creation
comparison table generation
report generation
routine operations
browser operations
SaaS operations
14-3. Initial policy

Can remain unimplemented for now.
But architecture must allow later addition.

14-4. Principle
approval if needed before execution
keep audit logs
prevent erroneous operations
15. Multi-project Management Requirements
15-1. TIM must handle multiple projects

Examples:

どこでも社食
Visa連携
こどハピTV
行政連携
新規事業
財務
契約
YouTube
15-2. Required abilities
identify projects
project-specific memory
project-specific state
cross-project priority organization
switch among multiple projects
follow topic jumps naturally
16. UX Requirements
16-1. Ideal

TIM should feel like an internal chief-of-staff.

16-2. Good experience
same partner over time
knows internal context
remembers prior discussion
retrieves needed documents
checks outside information too
talking to TIM moves work forward
16-3. Bad experience
repeated re-explaining
no awareness of internal materials
generic judgments
forgetting ongoing work
not going to retrieve information
17. Initial Development Scope
Phase 1
TIM conversation interface
LLM Gateway
Memory Layer
State Layer
minimal Context Builder
Phase 2
Drive Connector
past document search
Drive-grounded conversation
Phase 3
Web Connector
web-grounded conversation
Phase 4
Internal DB Connector
numeric/business data access
Phase 5
SaaS Connector
Money Forward and similar references
Phase 6
Executor Connector
OpenClaw integration
18. Success Conditions

TIM is successful if:

it is usable with ChatGPT-level natural conversation
the user thinks “ask TIM” by default
it preserves past context
it can look at internal Drive and answer
it can incorporate web information
it is practical for business, finance, and new business consultation
it feels stronger than plain ChatGPT alone
19. One-line Definition

TIM is an LLM-first strategic partner system that extends ChatGPT-class intelligence with memory, state management, internal Drive access, web/API/SaaS connectivity, and future execution capability.
