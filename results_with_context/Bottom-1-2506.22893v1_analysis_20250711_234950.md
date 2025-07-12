# Research Paper Analysis: Bottom-1-2506.22893v1.pdf

## Summary

| Metric | Value |
|--------|-------|
| **Paper** | Bottom-1-2506.22893v1.pdf |
| **Analysis Date** | 2025-07-11 23:49:50 |
| **Overall Score** | **7.62/10** |
| **Sections Analyzed** | 8 |
| **Processing Time** | 74.66 seconds |
| **Model Used** | claude-3-5-haiku-20241022 |

## Score Distribution

- **Ntroduction**: 7.0/10 🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜
- **Abstracting With Credit Is Permitted. To Copy Otherwise, Or Republish, To Post On Servers Or To Redistribute To Lists, Requires**: 7.0/10 🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜
- **Approach To Tasks. Enterprise Users Remain Accountable For Their Tasks And Sub-Tasks That Contribute**: 8.0/10 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜
- **Discussions With Other Companies And Tech Developers). No Llm Has Access To This Information**: 7.0/10 🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜
- **Analysis And Insights. These Two Analysts Differ In Their Agencies And User-Centric Ai Ought To**: 8.0/10 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜
- **Conclusion**: 8.0/10 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜
- **References**: 8.0/10 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜
- **Experimental Social Psychology. Vol. 30. Elsevier, 1–46.**: 8.0/10 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜

---

## Detailed Section Analysis

### 1. Ntroduction

**Score: 7.0/10**

**Evaluation:**
The introduction provides a compelling backdrop for the research by highlighting the recent advancements and challenges in AI. Strengths include: Clarity and Writing Quality (1.5/2): - Well-written and articulate - Clear progression of ideas - Highlights key technological developments Technical Depth (1.5/2): - Mentions specific AI technologies (transformers, diffusion models) - References current trends in AI assistants and agents - Identifies a critical problem space (AI-Centric User approach) Novelty and Originality (1/2): - Presents an interesting critique of current AI user interaction paradigms - Highlights a meaningful research problem - Could elaborate more on the unique contribution Methodology Rigor (1/2): - Limited methodology discussion (appropriate for an introduction) - Sets up the research problem effectively - Provides context for the subsequent research approach Evidence and Support (1/2): - Uses citations to support claims - References industry insights - Could benefit from more detailed supporting evidence

**Summary:**
The introduction discusses the rapid evolution of AI technologies, highlighting the proliferation of AI assistants and agents. It critically examines the current "AI-Centric User" paradigm, where users must adapt to inflexible AI systems, and sets the stage for exploring a more user-centric approach to AI interaction and design.

<details>
<summary>📄 View Section Content (1881 characters)</summary>

```
Introduction
The promise of Artificial Intelligence (AI) has been prognosticated for decades. The pace has
decidedly picked up over the last three years with apparent versatility of transformers [36] and
diffusion models [16] for text and image based data, respectively. There has been a proliferation of
AI Assistants–such as chatbots and co-pilots–in personal and professional domains, albeit yielding
mixed results for enterprises1. At the same time, discussions about Agents [7, 17, 31] have provided
a fillip for AI. However, lost in all this is the headwind coming from the current, widely practiced
regime of AI-Centric User, whereby humans do the heavy lift of adjusting to inflexible AI. For
example, (i) a typical user must learn to post queries in a specific manner to get appropriate and
useful responses from AI [9]; or, (ii) AI models, aligned with general purpose user preferences,
miss out on the needs for specific purpose, or for processes and workflows, or of specialists and
experienced users [33]. Moreover, most of the development focus of enterprises is on the AI itself,
less so on the expectations of users.
1https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage
Authors’ Contact Information: Arpit Narechania, arpit@ust.hk, The Hong Kong University of Science and Technology,
Hong Kong SAR, China; Alex Endert, Georgia Institute of Technology, Atlanta, USA, endert@gatech.edu; Atanu R Sinha,
Adobe Research, Bengaluru, India, atr@adobe.com.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee
provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the
full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored.
```

</details>

---

### 2. Abstracting With Credit Is Permitted. To Copy Otherwise, Or Republish, To Post On Servers Or To Redistribute To Lists, Requires

**Score: 7.0/10**

**Evaluation:**
The section demonstrates strong qualities while having some areas for improvement: Clarity and Writing Quality (1.5/2): - Well-written and articulate language - Clear exposition of key concepts - Introduces important terminological definitions Technical Depth (1.5/2): - Provides nuanced definitions of AI and Agents - Introduces a compelling conceptual framework of shifting from AI-Centric to User-Centric approaches - Establishes clear technological positioning Novelty and Originality (1.5/2): - Presents an innovative perspective on AI interaction paradigms - Proposes a novel conceptual shift in AI system design - Focuses on enterprise decision-making as a critical application domain Methodology Rigor (1/2): - Framework is conceptually sound but lacks explicit methodological details - More methodological elaboration would strengthen the argument Evidence and Support (1.5/2): - References existing literature - Uses clear citations - Provides theoretical grounding for proposed approach The section effectively builds upon the introduction's context, expanding the discussion of AI-user interactions and introducing the User-Centric AI concept.

**Summary:**
The section introduces a paradigm shift from AI-Centric to User-Centric AI, focusing on enterprise decision-making. It defines key terms like AI and Agents, critiques current AI interaction models, and proposes a new approach that emphasizes adapting AI systems to user needs and expectations.

<details>
<summary>📄 View Section Content (2029 characters)</summary>

```
Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires
prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2018 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM 1557-735X/2018/8-ART111
https://doi.org/XXXXXXX.XXXXXXX
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
111:2
Narechania, Endert, and Sinha
To wit, we refer to AI as the capability of a tool and the tool itself, including but not limited to
generative AI (GenAI). We posit that to realize the promise of AI, a shift away from the paradigm
of AI-Centric User to models of User-Centric AI is needed, wherein such AI adapt according
to users, their specific tasks, workflows, and processes. For enterprises, we assert that the shift
is attainable through task-specific Agents and their efficient and effective organization. We refer
to Agents as systems that independently accomplish tasks on a user’s behalf [27]. Hitherto, the
operational lens of industry views Agents through alternative agentic frameworks that pivot around
the paradigm of AI-Centric User [3, 10, 27]. In this paper, we take a step back and view the space
of AI and its delivery via Agents through the lens of users and beneficiaries (hereafter, users) with
focus on Enterprise Decision-Making, an important testbed and a milestone for progress in AI
and agentic thinking. We offer technological success criteria for efficient and effective impact of AI
on enterprises, toward a vision of User-Centric AI.
Embracing User-Centric AI in Enterprise Decision-Making
Our labeling of current efforts around GenAI as AI-Centric User stems from the heavy lift
enterprise users do trying to extract ever more from GenAI, as if, it is the ultimate repository,
whose yield is limited only by the incapability of users. Our proposed User-Centric AI shifts
the burden to AI itself, which must incorporate user’s agency, their expectations, and also their
```

</details>

---

### 3. Approach To Tasks. Enterprise Users Remain Accountable For Their Tasks And Sub-Tasks That Contribute

**Score: 8.0/10**

**Evaluation:**
The section demonstrates exceptional quality with a comprehensive and nuanced approach to user-centric AI in enterprise settings. Strong points include: Clarity and Writing Quality (2/2): - Extremely well-structured and articulate - Introduces complex concepts with clear explanations - Uses precise technical language - Provides concrete examples to illustrate abstract concepts Technical Depth (2/2): - Introduces sophisticated framework of user-agent-platform interactions - Provides detailed assumptions and tenets - Critically examines current AI paradigms - Offers a structured approach to enterprise AI adoption Novelty and Originality (1.5/2): - Proposes a groundbreaking shift from AI-centric to user-centric models - Introduces innovative concepts like market mechanism platforms and locally privacy-preserving learning - Provides a fresh perspective on AI's role in enterprise decision-making Methodology Rigor (1.5/2): - Establishes clear methodological assumptions - Defines precise tenets and primitives - Offers a structured approach to AI agent development Evidence and Support (1/2): - Includes multiple references and citations - Provides concrete examples - Could benefit from more empirical evidence

**Summary:**
The section presents a comprehensive framework for user-centric AI in enterprise settings, emphasizing user agency, process-orientation, and adaptable AI agents. It proposes six key tenets to guide AI development, focusing on flexibility, privacy, and user empowerment, while critically examining current AI interaction models.

<details>
<summary>📄 View Section Content (27801 characters)</summary>

```
approach to tasks. Enterprise users remain accountable for their tasks and sub-tasks that contribute
to decision-making, whether strategic or tactical. In addition, these users’ tasks and decisions often
have different dependencies with and accountability to other users. Subsuming these user-centric
concepts in AI is an important step to attain its potential for Enterprise Decision-Making.
Enterprises, their Users, and Decision-Making. The long term viability of AI and its delivery
via Agents rides on capital expenditure by enterprises23, yet “only 1 percent of company executives
describe their GenAI rollouts as “mature”4.” As well, “despite the endless announcements about how
firms are ushering AI into their operations, few make much use of the technology for serious work5.”
The success of AI depends on the nature of expectations and net benefits that may accrue from
enterprises’ AI usage, which notably is qualitatively different from AI usage in the personal domain.
Enterprise users are accountable to someone else, making their behaviors different from their
individual self in personal situations. For example, many users may participate in a task; a user’s
task and solution may be customized; value of a tool is determined by repeated usage; the demand
for a tool has enterprise-specific dependencies on tasks and tools that others use; and so on6. All this
makes development of AI for enterprises challenging; but with a large upside if the challenges can
be overcome7. Agents can help, only if AI overcomes the lack of a deep understanding of enterprise
users. For enterprises, we particularly drill down on decision-making due to its omnipresent role, its
ambiguity and uncertainty, its time-consuming nature, and wider opportunity for impact-of-AI, by
moving from human decision-making to more automated decision-making. For AI, understanding
enterprise decision-making allows a discrete change from low-value-added AI Assistants to high-
value added Agents. We identify six tenets that can be infused in User-Centric AI, and contribute
2https://a16z.com/ai-enterprise-2025/
3https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-cost-of-compute-
a-7-trillion-dollar-race-to-scale-data-centers
4https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
5https://www.economist.com/finance-and-economics/2025/05/26/why-ai-hasnt-taken-your-job
6https://hbsp.harvard.edu/product/8145-PDF-ENG
7https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
Agentic Enterprise
111:3
substantively toward AI and organization of Agents into Platforms. Our vision complements
existing principles, practices, and lessons for successful adoption of AI in enterprises [3, 26, 29].
Notably, prior work on human-centered AI [34] and human-AI collaboration [30, 37], predating
large language models (LLMs) and GenAI, emphasize human values, ethics, and usability. In this
paper, we contribute by carving out such conceptual gaps in current AI research. We particularly
draw attention to the underexplored, albeit central role of users, their agency, and their contribution
to the ecosystems. We raise questions around the hidden labor of users who not only utilize AI, but
also contribute to it either directly during training or by providing explicit feedback to AI responses,
or indirectly through providing their data passively while using a system. Unlike general-purpose AI
frameworks, we advocate deep integration of AI with users’ beliefs, expectations, tasks, workflows
and decision-making contexts. Additionally, in a user’s Workflow involving AI, we try to foresee
points of commonality and conflict between Users and Agents, and propose coordination-aware,
market-mechanism-oriented Platforms of specialized AI agents to foster commonality and diffuse
conflict. This shift represents a major rethinking of Agents as incentive-compatible and responsive
partners which can even improve the user cognitively. Lastly, with traditional models proven in
many analytic tasks for enterprises, it is necessary to offer flexibility in AI to complement those.
Thus, the unique challenges and opportunities of AI in a user-centric paradigm may require thinking
beyond GenAI and Large Language Models (LLMs).
Six Tenets of User-Centric AI in Enterprises
1. Primacy of Process-Orientation in AI.
2. Forward Thinking AI.
3. Locally Privacy Preserving Agent-Learning.
4. Market Mechanism Platform for Agents and Users.
5. Agent Risk-Reward Diversity and Quality-Price Diversity.
6. Low Entry, Exit Barriers for Agents.
2
The Premise
As part of our premise, we consider three entities–Users, Agents, Platforms–and a Workflow.
Below, we define and clearly delineate a set of assumptions to be used as building blocks for the
rest of the paper. These assumptions work as boundary conditions for our propositions.
Users: A group which may benefit from AI. They could be performing tasks for an enterprise
collectively, or, individually. We make the following assumptions about users:
UA1 User’s Agency: Users seek agency and vary in skills from other users, and across tasks.
UA2 Discoverability: Users self-select whether to discover AI tools and not the other way round.
UA3 User Heterogeneity: For a given task, users are diverse in expectations and utilities from AI.
UA4 Task Heterogeneity: Across tasks, a user has diverse expectations and utilities from AI.
UA5 Utility: Users aim to maximize their own utility from AI.
UA6 Privacy: Users vary in expectations about degrees of protection of information they share.
Agents: “Agents are systems that independently accomplish tasks on your behalf” [27] by using a
language model to manage workflows, make decisions, correct errors, and dynamically interact
with external tools. Essentially, they are entities through which AI is delivered to users. These could
be a single entity or a collection of entities. We make the following assumptions about agents:
AA1 Agent Manifestation: An agent can be a user-assisting tool or an autonomous operator.
AA2 Task Specialization: An agent is specialized for a task.
AA3 Degree of Autonomy: An agent can be controlled or autonomous.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
111:4
Narechania, Endert, and Sinha
AA4 Communication Within: Autonomous agents may communicate directly with other agents.
AA5 Communication Outside: Autonomous agents may communicate directly with users.
AA6 Rewards: Agents are endowed with varying rewards by the platform.
AA7 Types of Models: Agents can represent GenAI or traditional models (we are agnostic to the
type) and depend on user demand and supply from the agent organization and platform.
AA8 Disclosure: Agents communicate their capabilities publicly, whether truthful or not.
Platform: A planner, which is an entity in charge of delivering benefits of AI to users. It can be
third-party or enterprise-governed. We make the following assumptions about the planner:
PA1 Accountability: The planner is accountable to users for delivering AI.
PA2 Organization: The planner uses a set of agents.
PA3 Discoverability: Planner needs to discover capabilities of agents.
PA4 Management: The planner manages the agents to maximize own utility.
PA5 Communication: Users communicate with the planner, which communicates with agents.
Planner can use a confederate, or orchestrator, which is then the conduit for communication.
PA6 Safety: The planner is responsible for degrees of safety in outputs. The degree depends on
the task and user’s stated appetite for risk.
Workflow: “A workflow is a sequence of steps that must be executed to meet the user’s goal” [27].
For expositional ease, consider users who perform data analytics as part of their work for an
enterprise–small, medium or large. We define the following simplified workflow–comprising four
discrete tasks common in an enterprise setting–as a running example for the rest of the paper. This
workflow is not meant to be exhaustive, but only an illustration.
1. Data (Preparation)
→2. Model (Selection, Application)
→3. Results (Evaluation, Verification)
→4. Presentation (Inference, Recommendation)
Each of the four tasks has several sub-tasks and lower-level analytic decisions contained within
it. For example, the model selection step consists of gathering a collection of models, ranking or
filtering them based on task criteria, and deciding on either a single model or an ensemble approach.
Having such discrete tasks makes it easier to assign an agent to it. Agents can also collaborate with
each other on a task. Agents can also plan [18, 38] and reason [5, 8] within this workflow to the
extent desired. Lastly, we let users freely choose agents to fit their workflow. For instance, one user
might only need help with model selection, while another might run a model, evaluate it, and then
return to data preparation to create more features.
3
Tenets of User-Centric AI
Under the premise in Section 2, we propose six tenets to guide AI toward an agentic enterprise.
First, we identify three necessary primitives for AI to recognize and endow agents with. Then, we
present the tenets as success factors for agentic platforms serving enterprise users.
3.1
Primitives
We first present three user-first primitives, emphasizing user-centrality.
I. User Agency.
II. Agent Foresight.
III. User Feedback and Agent Learning.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
Agentic Enterprise
111:5
In touting (I), drawing from formidable research in psychology [4], we recognize the importance
of incorporating the following user level criteria: (a) Users’ expectations and beliefs, since these
impact the realization of their experiences of interactions with AI [22, 24]; (b) Users’ tasks often
involve subjectivity, with no single correct answer; only the user fully understands their task and the
potential benefits from AI, making their ex post evaluation as important as any ex ante assessment
of AI; (c) Users are heterogeneous in tasks performed suggesting differences in expectations and
beliefs across tasks; (d) Users are heterogeneous in skill levels for a given task, suggesting differences
in expectations and beliefs for the task as well as benefits sought from the task; (e) Users want
to experiment with AI interactions for their own workflow [13], which only they know by (b),
suggesting expectation of flexibility and experimentation in tools.
In advocating (II), and to incorporate (a)–(d) above, AI needs to be imbued with Foresight, which
we define as “Looking ahead beyond the immediate next response, suggesting a degree of anticipation
of user’s reaction to its own response and interjecting for clarifications judiciously and with alternatives.”
Note that we do not reproduce other characteristics required of AI which are espoused in the extant
literature [1, 19]. We only highlight Foresight in addition to those.
In emphasizing (III), and to complement (I) and (III), incorporation of heterogeneous feedback for
a task and for heterogeneous tasks is necessary for AI to learn to meet and adapt to heterogeneous
users’ expectations and beliefs. Without an infrastructure for multi-user, multi-task, multi-agent
continuous feedback and learning, along with recognition of heterogeneities in users and tasks, no
framework can approach a degree of completeness. For example, incompleteness in user’s prompts
about tasks can be anticipated to build into the agents’ behaviors. These are especially pertinent
with the talk about AI having turned toward agents and agentic frameworks.
3.2
Tenets
Based on the primitives, we present six tenets as guidelines for enterprises and platforms, who serve
the former. Some apply broadly to enterprise users, others describe desired agent traits, and some
target platforms. Not all tenets are needed in every case; a subset may be enough. Each tenet is
stated with its rationale and illustrated by an example from the Workflow (introduced in Section 2).
3.2.1
Tenet 1: Primacy of Process-Orientation in AI.
Rationale: Broadly, value to users is of two types: (i) Outcome, and (ii) Process. Given UA1, UA3, and
UA4, the sample space of outcomes is not known, and thus, AI cannot meet all users’ expectations
on outcome-quality. Instead, steps or tasks of processes can be offered with respect to workflows,
where different users call in at different tasks in the workflow as and when needed (UA4, AA7, PA2).
Giving users easy-to-assemble tools to build their own workflows is beneficial. This requires AI to
have a deeper understanding of users’ workflows and learn how to improve their efficiency. In other
words, the focus shifts from training models on outcome data to training on process data. This
process-oriented approach shifts responsibility for outcome quality from the platform to the users,
and when focused on process, users retain agency [14, 20, 30] (UA1, UA5). For instance, users can
satisfy their agency through experimentation, trial and error, and achieve more self-actualization.
The platform reduces effort on excessive focus on outcome-quality, which is difficult to satisfy
under the various heterogeneities (UA3, UA4, PA6).
Example: An outcome orientation focuses on task specific response regardless of the user’s overall
need. An experienced enterprise user may need help with model selection and running, but does
not need help with other tasks. This user knows that model selection depends on both the task prior
to it, data preparation step, and the tasks the user wants after it; say, what type of presentation the
user wants. An outcome orientation is inadequate since it does not consider the user’s presentation
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
111:6
Narechania, Endert, and Sinha
need. A process orientation by AI allows users to plug in a task within their workflow, which knows
about the presentation need and can inform them about model selection.
3.2.2
Tenet 2: Forward Thinking AI.
Rationale: Enterprise users have diverse expectations and goals across tasks, many involving long-
term planning and complex workflows (UA3–5, AA2, PA2). Reactive AI platforms that respond
only to current user inputs lack the foresight needed for meaningful strategic support. This limits
AI’s ability to help users anticipate risks, plan ahead, or manage multi-step processes, leading to
fragmented and short-sighted assistance. Shifting to Forward Thinking AI that proactively forecasts
needs, warns of potential errors early, and guides users forward empowers better decisions and
broader goals (UA5, AA4–5, PA3).
Example: Forward Thinking AI within a workflow can occur for a task and for the workflow. In
response to a user’s ask about model selection, the AI can give the best response. A forward-looking
AI can determine additional follow-up questions from the user without her asking and frame the
response accordingly. It can offer the user alternative models with pros and cons rationale with
respect to her expected follow-up questions, which informs user’s selection. Furthermore, knowing
the user’s workflow a Forward Thinking AI can consider her presentation need as well.
3.2.3
Tenet 3: Locally Privacy Preserving Agent-Learning.
Rationale: AI platforms that treat user data uniformly and rely on one-size-fits-all agent learning fail
to meet the diverse skills and varied expectations of users across tasks (UA1, UA3–5, AA6–7, PA1).
While generalist agents work well for novices, experts benefit from integrating their specialized
knowledge to improve engagement and drive continuous agent improvement. Differentiating data
and feedback by user expertise and privacy preferences enables personalization and respects user
agency (UA1, UA5–6, AA7), encouraging experts to share valuable knowledge without risking
privacy or competitive concerns (AA7–AA8). To meet enterprise needs, platforms (PA1, PA3, PA6)
can use partitioned or federated learning that tags data by expertise and privacy, supports user-
specific agent training, lets users control AI learning contributions, and applies privacy safeguards
with incentives for expert participation. Without expert input, platform appeal drops. This privacy-
focused, on-demand approach builds reputation, improves personalization, and sustains a dynamic
ecosystem where novices and experts drive ongoing innovation and growth.
Example: Consider the data preparation step of our running example Workflow. While prior art
exists for feature selection from data, creating the feature that is most useful for a modeling task is as
much an art and depends on user experience and judgment. As any expert analyst knows, a feature
is important not only based on its contribution to model accuracy, but also on its actionability and
managerial meaningfulness. Those two latter aspects are private information to an expert who may
not want to share even with all users in the same enterprise in order to preserve their own worth.
If the AI Agent gleans and learns this expertise from the user, it can percolate to others, going
against the wishes of the user. Anticipating this, a user may not want to interact with the Agent AI,
reducing its learnability. Giving the user control of what enters into the AI’s learning maintains
locally privacy preserving agent learning. In other words, an AI can ‘think global, act local.’
3.2.4
Tenet 4: Market Mechanism Platform for Agents and Users.
Rationale: Given users’ diverse preferences and risk tolerances (UA1–5), and the uncertainty in AI
and agent quality relative to user needs (AA2, AA6, PA4), we propose a market mechanism [2, 23].
It features specialized agents offering varied skills, behaviors, and risk-reward profiles, enabling
users to choose agents that best fit their needs, promoting ownership and flexibility in AI outputs
(UA1, UA3, AA2, AA6, PA2, PA4). From the platform perspective, a decentralized agent organization
reduces the risk of reputation damage from any single poor-performing agent, boosting resilience
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
Agentic Enterprise
111:7
and encouraging innovation through competition and collaboration (AA6, PA4–5). While centralized
control eases management and ensures consistency, it limits user agency and adaptability (UA1, PA4).
Organizing agents as interoperable, loosely coupled entities in a market balances user autonomy
with quality and reputation safeguards, fostering experimentation, customization, and strong
process integration (UA1, UA5, AA2, PA2, PA4–5). Decentralized does not mean there are no checks
and balances on “underperforming” agents; it only means the planner’s role shifts to managing
agents through incentives to ensure user success rather than direct control (PA4, AA6).
Example: Each task-agent discloses its capabilities publicly so that users know what each can and
cannot do; each agent also receives feedback from users after task completion. All this renders
incentive compatible reward to the agent creator / developer to improve the agent. Without a
market mechanism such disclosure and feedback are rendered less effective.
3.2.5
Tenet 5: Agent Risk-Reward Diversity and Quality-Price Diversity.
Rationale: Diversity in agent offerings is necessary to address the heterogeneity of user tasks (UA4,
AA2, AA6). Given the heterogeneity in user expectations and utilities across tasks and the principle
that users aim to maximize their own utility (UA5), AI platforms should allow agents to self-select
their behavior styles and risk-reward profiles (UA1, AA2, AA6, PA6). Since agents cannot fully
eliminate undesirable behaviors due to task heterogeneity, supporting diverse agent behaviors
enables users to match risk profiles to their preferences (UA5, AA5–6, PA6). Users comfortable with
high-risk, high-reward outcomes can choose more exploratory agents, while others may prefer
safer, conservative ones. This flexibility preserves user agency and fosters innovation, while the
platform manages a diverse set of specialized agents to meet varying user needs, creating a dynamic
ecosystem that balances creativity and safety (UA1, UA5, AA2, PA2, PA6).
Example: Consider the model selection task in our example Workflow. A user with a penchant for
the latest may seek the newest model to showcase to the enterprise, only to be shot down in a
presentation by a senior since the latest model makes evaluation against historical benchmarks
difficult. In other cases, the risk may be worthwhile if the senior finds something useful for the
future from such a model. Another user may want to stay with tried and proven models. For a
single agent, serving both such types of user can be a challenge. Two agents with diverse skills
can address needs of two different users. These differences among agents can reflect in different
qualities as perceived by users and thus different willingness to pay for agent.
3.2.6
Tenet 6: Low Entry, Exit Barriers for Agents.
Rationale: Lower barriers to entry foster development of agents (AA6, AA8, PA5). Creating ease of
exit for poor performers maintains performance excellence that increases utility for users (UA5,
AA6, PA4–5). For entry, planner’s gatekeeping role is important, since unlike exit of existing agents,
less objective information about agent is expected (PA2, PA5). Moreover, Tenet 6 catalyzes Tenet 5
(AA8, PA5). We refrain from calling out “free or low” entry / exit since considerations of sanctity of
each enterprise’s data / information, that of switching cost for its users, and proclivity of agents
(developers) to overclaim their capability, along with planner’s imperfect verifiability of claims, all
pose restraints (UA6, PA1, PA6).
Example: A market mechanism works when an agent with low reward for, say model selection,
across a lot of users, falls below a certain threshold and is exited. This also suggests that other
qualified agents are ready to take its place, which lower barrier to entry ensures.
4
Toward User-Centric AI for Agentic Enterprise
Focusing on enterprise decision-making, we propose the type of AI evolution required to pay
persistent dividend for companies that use AI. Whether AI is up to the task, or, what form it will
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
111:8
Narechania, Endert, and Sinha
LEVEL OF DECISION-MAKING
LEVEL OF AUTOMATION
AGENTIC PARADIGM
Tactical
Strategic
AI-Centric User
User-Centric AI
Automated
User
AGENTIC
ENTERPRISE DECISION-MAKING
Future Opportunities
Underperforming Efforts
Successful Efforts
Fig. 1. Agentic Enterprise Decision-Making:
I cautions about intent since it remains difficult to ascertain
merely from data without user intervention.
II highlights the successes of automation for enterprise decision-
making in trading in stock market trading; revenue management for dynamic demand systems such as airlines
and hotels; recommendation systems for online businesses; and ad-bidding online market mechanism—all
with a combination of traditional, ML and AI models. III exemplifies gaps in common, big enterprise strategic
decisions, none of which is effectively addressable today with any AI. These decisions require enterprise
users’ breaking them down into atomic decisions issues. IV shows only a single atomic decision issue for
each of the three strategic decisions, as broken down by users.
V shows major information gaps, which are
germane for strategic decisions. Next, SOTA models use LLMs in attempts to address atomic issues but fall
short. To address atomic issues, VI shows the use of Decomposition, Planning, Reasoning (DPR), de rigueur
in strategic decision-making by users. VII shows that LLMs attempt to mimic DPR; but is emblematic of
AI-Centric User who tries everything to get the LLMs to perform better; yet not rising to a reliable level.
Finally, VIII highlights the conceptual gaps that are necessary for AI to fill for enterprise decision-making.
take is up for a debate8. For the rest of the paper, we refer to Figure 1. Broadly, decision-making
can be classified into Tactical or Strategic; and Automated or Human, where “automated” includes
human-in-the-loop automated decisions. Our premise is that enterprises’ preference is to push
more decision-making toward automation (including user-in-the-loop), subject to the decisions
8https://hbr.org/2024/12/the-irreplaceable-value-of-human-decision-making-in-the-age-of-ai
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
Agentic Enterprise
111:9
outperforming those by users. Favoring their preference is the strong evidence of success in tactical
decision-making such as Trading, Revenue Management (e.g., in hotels), Recommendation Systems
(RecSYS), Ad-Bidding, etc., where data based automation is de rigueur
II . Tactical decision-making
requiring knowledge of user intent
I , a difficult construct to infer from data alone or due to lack
of data [32], still benefits from human involvement. For example, solely based on a sequence of
clicks, it is difficult to tell if a new user is only looking for information or wants to make a purchase.
On the strategic decision side, we illustrate with three common examples of enterprise decision
problems. For each, the big question is shown in
III , while a corresponding atomic question is
shown in IV (only one atomic question among several is shown for each big question). The questions
in IV can be answered, in part, as follows by LLMs:
A. Regarding determining the maturity of a technology, an LLM can respond using its global
knowledge gathered from reports and commentaries (about the technology) on the web.
B. Regarding predicting next month’s buyers, an LLM’s generic global knowledge cannot answer
it. In a traditional setting, a business may follow a Workflow (akin to the one in Section 2)
to determine the answer. In an LLM setting, a business can provide data about the customer
segments it targets and their past purchase behaviors, along with how those segments are
defined. The LLM can then suggest a segment definition, though it may not be perfect.
C. Regarding determining unprofitable items, a business may follow a traditional Workflow like
B ’s above. In an LLM setting, the business can feed historical data tables about the different
products, unit sales, prices, and costs, for the LLM to provide an answer quickly. However, even
through a combination of decomposition, planning, and reasoning operations such as chain of
thought and tree of thought [21, 25, 28, 39, 40], LLMs can only partially address these questions.
These responses obtainable from GenAI are evidently restrictive and consistent with the paradigm
of AI-Centric User; thus, VII shows GenAI as a cautionary tale.
On the other hand, the user dependent big questions are more involved for an LLM to do
justice. For instance, in
III A, only the business knows its strength and weaknesses in developing
the technology and converting it into products. For example, does it have quality human capital
to leapfrog the tech beyond what is available or licensed? Does it have the compute and data
resources to develop it internally? How long will internal development take? What will it cost to
make versus buy, in the short and long term? This information depends on goals
V (defensive, to
retain current customers, or offensive, to attract new ones); judgment and subjectivity (different
executives may have different answers, as these are not objectively measurable); environment
(internal technologies and how they fit with the new technology, plus the company’s view of its
competition); and private knowledge (internal research and confidential insights from C-suite
```

</details>

---

### 4. Discussions With Other Companies And Tech Developers). No Llm Has Access To This Information

**Score: 7.0/10**

**Evaluation:**
This section demonstrates a nuanced exploration of AI challenges in enterprise settings, with strong points in technical depth and critical analysis. The strengths include: 1. Clarity and Writing Quality (1.5/2): - Well-structured discussion of AI limitations in enterprise contexts - Clear articulation of challenges with LLM integration - Technical language is precise and sophisticated 2. Technical Depth (1.8/2): - Sophisticated discussion of Decomposition, Planning, and Reasoning (DPR) - Identifies specific gaps in current AI enterprise applications - Highlights complex interaction between AI systems and user motivations 3. Novelty and Originality (1.5/2): - Introduces novel perspective on user motivation types (prevention vs. promotion) - Critically examines current AI-enterprise interaction models - Proposes user-centric AI as a potential solution 4. Methodology Rigor (1.2/2): - References multiple academic sources - Discusses methodological limitations - Slightly lacks detailed methodological explanation 5. Evidence and Support (1/2): - Cites academic references - Provides conceptual illustrations - Could benefit from more empirical evidence

**Summary:**
The section explores the challenges of integrating AI, particularly Large Language Models (LLMs), into enterprise settings. It critically examines current limitations, including data confidentiality, goal misalignment, and incomplete user inputs. The discussion emphasizes the need for a user-centric AI approach that respects human agency and understands contextual motivations.

<details>
<summary>📄 View Section Content (1973 characters)</summary>

```
discussions with other companies and tech developers). No LLM has access to this information
V .
Moreover, a business may be reluctant to share confidential data with an LLM without an iron-clad
leakage prevention or developing its own local GenAI model.
Recent advances in decomposition, planning and reasoning (or, DPR) [21, 25, 28, 39, 40] foster
hopes of improved automation, with user-in-the-loop. Currently, utility of DPR to enterprises is
limited VII due to a host of factors including misalignment of goals between AI or Platform and
enterprise users, lack of training of finetuning data that capture the complex and involved nature
of enterprise decisions, incomplete and imperfect input from enterprise users, and dearth of models
that incorporate these gaps. The severe gaps
V with respect to strategic decisions include lack
of information about decision makers’ goals, lack of data (codified information) about human-
judgment, subjectivity (which could also be situational), private knowledge, and environment
(within firm, within industry, etc.). To deal with this ambiguous situation, technology turns to
LLMs to fill in the gaps. Users exert effort to extract as much as they can from LLMs, as if the yield
from LLMs is stymied only by users’ inability.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
111:10
Narechania, Endert, and Sinha
Enterprises can benefit from Agents that are endowed with User-Centric AI VIII . This kind of AI
appreciates human agency, namely, that enterprise users prefer to learn how to do their job, instead
of being told an answer for a specific question. Users motivation plays a role where motivation is one
of two types: prevention or promotion [15], and they are situational and contextual. As illustration,
for an analyst with prevention focus, not making an error in presenting results to a large team is
more important, while one with a promotion focus may want to surprise the team with a very new
```

</details>

---

### 5. Analysis And Insights. These Two Analysts Differ In Their Agencies And User-Centric Ai Ought To

**Score: 8.0/10**

**Evaluation:**
The section demonstrates strong technical depth and originality in addressing AI integration challenges in enterprise environments. The analysis shows nuanced understanding of complex organizational dynamics, particularly: 1. Clarity and Writing Quality (1.8/2): Well-structured writing with clear articulation of complex concepts around AI agency and enterprise interactions. 2. Technical Depth (1.9/2): Sophisticated exploration of cooperative/competitive dynamics in enterprise AI, considering nuanced aspects like cognitive bias detection and inter-agent information flow. 3. Novelty and Originality (1.7/2): Introduces innovative "Walled-Garden Platform" concept with market mechanism governance, representing a novel approach to enterprise AI deployment. 4. Methodology Rigor (1.6/2): Provides a conceptual framework with references to economic literature, demonstrating methodological grounding. Acknowledges potential implementation challenges. 5. Evidence and Support (1/2): Uses academic citations, but could benefit from more empirical evidence supporting proposed platform model. The section builds logically on previous sections' discussions about user-centric AI, extending the framework with pragmatic organizational considerations.

**Summary:**
The section explores how enterprise AI agents should navigate complex cooperative and competitive organizational landscapes. It proposes a "Walled-Garden Platform" with agent autonomy governed by market mechanisms, emphasizing user agency, information control, and adaptive decision-making support. The analysis critically examines AI deployment challenges while offering a structured approach to mitigating potential risks.

<details>
<summary>📄 View Section Content (2380 characters)</summary>

```
analysis and insights. These two analysts differ in their agencies and User-Centric AI ought to
take the difference into account. It is common in enterprises that users cooperate on some work
and compete on others [12, 35]. This has ramifications for Agentic AI, with which all users interact,
in that the AI should foster improved cooperation with smoother flow of information among users,
but for the latter curtail information flow between users perhaps with sandboxes. Moreover, a firm
cooperates with some partner-firms and competes with rival-firms. This understanding, some of
which can come from firm-specific information, is crucial for AI to offer decision-making advice
and input or make automated decisions on many aspects. Last but not the least, the omnipresence
of cognitive biases in managerial judgment and decision-making is well received wisdom [6]. In
offering advice to users for decision-making, where users provide input to the AI, detecting such
biases in the input affords AI to perform mitigation in advice giving.
What kind of Agentic Platform to benefit Enterprises? We propose a Walled-Garden Platform
with agent autonomy, governed by a market mechanism. Enterprises have data and knowledge
repositories that need firewall. Without a degree of control exerted over agents, enterprises may find
inadequate protection for all their repositories and reduce adoption. At the same time, a centralized
planner through which users must access services of agents can be costly in communication (say,
planner seeking too many clarifications), poor user experience in not being able to communicate
with an agent she specifically needs help from, wrong interpretation of user intent, direction
of query to wrong agent, mis-attribution of user’s feedback to agents, among others. A walled
garden platform with direct communication between users and agents, where users beware of
their own actions, planners supervise agents, and agents are rewarded based on–their own claim
of performance, planner’s observance of their performance and users’ feedback–is worthy of
strong consideration. Borrowing from the large market mechanism literature in Economics [11, 23],
different mechanisms can be designed for different situations. For instance, an ad-bidding platform
is a highly successful market mechanism, though it differs significantly from an agentic platform.
5
```

</details>

---

### 6. Conclusion

**Score: 8.0/10**

**Evaluation:**
The Conclusion section effectively synthesizes the key themes from previous sections and provides a forward-looking perspective on user-centric AI in enterprise settings. It scores strongly in several areas: Clarity and Writing Quality (2/2): The text is well-written, clear, and concise, effectively summarizing the paper's core contributions. Technical Depth (1.5/2): The section demonstrates substantive technical insight by articulating a clear framework and proposing specific, nuanced research questions that extend the paper's core arguments. Novelty and Originality (1.5/2): The conclusion builds on previous discussions by highlighting innovative research directions, particularly around privacy-preserving agent learning and diverse user needs. Methodology Rigor (1/2): While not deeply methodological, the section outlines a structured approach to future research with specific, actionable questions. Evidence and Support (2/2): The conclusion is well-grounded in the context of previous sections, showing a coherent narrative about user-centric AI development.

**Summary:**
The conclusion proposes a framework for AI-human collaboration in enterprise settings, emphasizing user agency and adaptability. It identifies key research questions around privacy, learning strategies, and simulation environments, positioning the work as a foundational contribution to developing more responsive, user-centric AI ecosystems.

<details>
<summary>📄 View Section Content (1443 characters)</summary>

```
Conclusion
The vision of people and AI working together to perform tasks can transition to reality with agents.
This transition requires taking conceptual notions of how such ecosystems of agents and people
will co-exist, and implementing them in specific ways. In this paper, we propose a framework to
reason about the core principles that such ecosystems should exemplify. We present these as tenets,
focused on balancing user agency and value as a core principle. Through these, we posit that future
agentic ecosystems can better serve users in enterprises for their decision-making.
Building on this foundation, several key research questions arise: How can we advance locally
privacy-preserving agent learning beyond current federated and distributed approaches? Specif-
ically, how can we enable fine-grained user control over which specific information is used for
general or targeted learning? Next, what strategies can create a diversity of risk-reward and quality-
price trade-offs in both processes and outputs to better meet varied user needs? Lastly, how can we
develop simulation environments that test different agent organizations and support diverse user
profiles for more effective platform evaluation and refinement? Addressing these questions will
pave the way from AI-Centric User towards User-Centric AI in Agentic Enterprises.
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
Agentic Enterprise
111:11
```

</details>

---

### 7. References

**Score: 8.0/10**

**Evaluation:**
The References section demonstrates high quality and relevance to the paper's core themes of user-centric AI, agent autonomy, and enterprise AI systems. Key strengths include: Clarity and Writing Quality (2/2): - Professionally formatted references - Clear, consistent citation style - Recent and forward-looking sources (many from 2024-2025) Technical Depth (2/2): - Comprehensive range of sources covering AI agents, market mechanisms, organizational psychology, and human-machine interaction - Sources directly support the paper's key arguments about agency, autonomy, and multi-agent systems - Includes academic, industry, and technical publications Novelty and Originality (1/2): - Good mix of sources, but slightly deducted for relying on survey/review papers - References demonstrate emerging research landscape in agent-based AI Methodology Rigor (1/2): - References provide methodological context - Includes theoretical and empirical sources - Slight deduction for not having more primary research citations Evidence and Support (2/2): - Sources comprehensively support paper's theoretical framework - Covers psychological, technological, and organizational perspectives - Includes both academic research and industry documentation

**Summary:**
The References section provides a robust scholarly foundation for the paper's exploration of user-centric AI and agent autonomy. It draws from diverse sources spanning AI technology, organizational psychology, and market mechanisms, offering a comprehensive intellectual backdrop for the research's innovative approach to enterprise AI systems.

<details>
<summary>📄 View Section Content (2454 characters)</summary>

```
References
[1] Deepak Bhaskar Acharya, Karthigeyan Kuppan, and B Divya. 2025. Agentic AI: Autonomous Intelligence for Complex
Goals–A Comprehensive Survey. IEEE Access (2025).
[2] George A Akerlof. 1978. The Market for “Lemons”: Quality Uncertainty and the Market Mechanism. In Uncertainty in
Economics. Elsevier, 235–251.
[3] Anthropic. 2025. How We Built Our Multi-Agent Research System. https://www.anthropic.com/engineering/built-
multi-agent-research-system Accessed: 2025-06-14.
[4] Albert Bandura. 2006. Toward a Psychology of Human Agency. Perspectives on Psychological Science 1, 2 (2006),
164–180.
[5] Dibyanayan Bandyopadhyay, Soham Bhattacharjee, and Asif Ekbal. 2025. Thinking Machines: A Survey of LLM Based
Reasoning Strategies. arXiv preprint arXiv:2503.10814 (2025).
[6] Max H Bazerman and Don A Moore. 2012. Judgment in Managerial Decision Making. John Wiley & Sons.
[7] Zane Durante, Qiuyuan Huang, Naoki Wake, Ran Gong, Jae Sung Park, Bidipta Sarkar, Rohan Taori, Yusuke Noda,
Demetri Terzopoulos, Yejin Choi, et al. 2024. Agent AI: Surveying the Horizons of Multimodal Interaction. arXiv
preprint arXiv:2401.03568 (2024).
[8] Mohamed Amine Ferrag, Norbert Tihanyi, and Merouane Debbah. 2025. From LLM Reasoning to Autonomous AI
Agents: A Comprehensive Review. arXiv preprint arXiv:2504.19678 (2025).
[9] Google LLC. 2024. Prompting Guide 101. https://services.google.com/fh/files/misc/gemini-for-google-workspace-
prompting-guide-101.pdf
[10] Google LLC. 2025. Google Agentspace Enterprise Overview. https://cloud.google.com/agentspace/agentspace-enterprise/
docs/overview Accessed: 2025-06-14.
[11] Oliver D Hart. 1983. The Market Mechanism as an Incentive Scheme. The Bell Journal of Economics (1983), 366–382.
[12] Chad A Hartnell, Amy Yi Ou, and Angelo Kinicki. 2011. Organizational Culture and Organizational Effectiveness:
A Meta-analytic Investigation of the Competing Values Framework’s Theoretical Suppositions. Journal of Applied
Psychology 96, 4 (2011), 677.
[13] Harvard Business Review. 2023. The New Human-Machine Relationship. https://store.hbr.org/product/the-new-
human-machine-relationship/R2302B Accessed: 2025-06-14.
[14] Jeffrey Heer. 2019. Agency Plus Automation: Designing Artificial Intelligence into Interactive Systems. Proceedings of
the National Academy of Sciences 116, 6 (2019), 1844–1850.
[15] E Tory Higgins. 1998. Promotion and Prevention: Regulatory Focus as a Motivational Principle. In Advances in
```

</details>

---

### 8. Experimental Social Psychology. Vol. 30. Elsevier, 1–46.

**Score: 8.0/10**

**Evaluation:**
This section appears to be a comprehensive reference list for a research paper on AI agents, enterprise AI, and human-AI collaboration. The references demonstrate strong scholarly rigor and contemporary relevance: Clarity and Writing Quality (2/2): - Well-organized bibliographic entries - Covers recent publications (2017-2025) - Includes diverse sources from technical conferences, journals, and preprint platforms Technical Depth (2/2): - Highly technical references spanning AI, machine learning, social psychology, and organizational systems - Includes cutting-edge publications on AI agent design, language models, and human-AI interaction - Covers theoretical and practical perspectives on AI system development Novelty and Originality (1/2): - Many references are very recent (2023-2025) - Captures emerging discourse on AI agent design and governance - Slightly lower originality score as many are preprint/emerging research Methodology Rigor (1/2): - Strong methodological references from reputable conferences/journals - Includes technical and theoretical methodological approaches - Some references lack full peer-review validation Evidence and Support (2/2): - Comprehensive range of citations - Includes technical reports, academic publications, and conference proceedings - Provides robust scholarly foundation for the research

**Summary:**
This reference section presents a curated collection of sources exploring AI agent design, human-AI collaboration, and enterprise AI strategies. The references span technical, organizational, and theoretical domains, offering a comprehensive scholarly backdrop for understanding contemporary AI system development and governance.

<details>
<summary>📄 View Section Content (5988 characters)</summary>

```
Experimental Social Psychology. Vol. 30. Elsevier, 1–46.
[16] Jonathan Ho, Ajay Jain, and Pieter Abbeel. 2020. Denoising Diffusion Probabilistic Models. Advances in Neural
Information Processing Systems 33 (2020), 6840–6851.
[17] Qiuyuan Huang, Naoki Wake, Bidipta Sarkar, Zane Durante, Ran Gong, Rohan Taori, Yusuke Noda, Demetri Terzopoulos,
Noboru Kuno, Ade Famoti, et al. 2024. Position Paper: Agent AI Towards a Holistic Intelligence. arXiv preprint
arXiv:2403.00833 (2024).
[18] Xu Huang, Weiwen Liu, Xiaolong Chen, Xingmei Wang, Hao Wang, Defu Lian, Yasheng Wang, Ruiming Tang, and
Enhong Chen. 2024. Understanding the Planning of LLM agents: A Survey. arXiv preprint arXiv:2402.02716 (2024).
[19] Laurie Hughes, Yogesh K Dwivedi, Tegwen Malik, Mazen Shawosh, Mousa Ahmed Albashrawi, Il Jeon, Vincent Dutot,
Mandanna Appanderanda, Tom Crick, Rahul De’, et al. 2025. AI Agents and Agentic Systems: a Multi-Expert Analysis.
Journal of Computer Information Systems (2025), 1–29.
[20] Sebastian Krakowski. 2025. Human-AI Agency in the Age of Generative AI. Information and Organization 35, 1 (2025),
100560.
[21] Vishwajeet Kumar, Yash Gupta, Saneem Chemmengath, Jaydeep Sen, Soumen Chakrabarti, Samarth Bharadwaj, and
Feifei Pan. 2023. Multi-Row, Multi-Span Distant Supervision For Table+Text Question Answering. In Proceedings of
the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Anna Rogers, Jordan
Boyd-Graber, and Naoaki Okazaki (Eds.). Association for Computational Linguistics, Toronto, Canada, 8080–8094.
doi:10.18653/v1/2023.acl-long.449
[22] Doris Läpple and Bradford L Barham. 2019. How do Learning Ability, Advice from Experts and Peers Shape Decision
Making? Journal of Behavioral and Experimental Economics 80 (2019), 92–107.
[23] Roger B Myerson. 2008. Perspectives on Mechanism Design in Economic Theory. American Economic Review 98, 3
(2008), 586–603.
[24] Arpit Narechania, Alex Endert, and Atanu R Sinha. 2025. Guidance Source Matters: How Guidance from AI, Expert, or
a Group of Analysts Impacts Visual Data Preparation and Analysis. In Proceedings of the 30th International Conference
on Intelligent User Interfaces. 789–809.
[25] Giang Nguyen, Ivan Brugere, Shubham Sharma, Sanjay Kariyappa, Anh Totti Nguyen, and Freddy Lecue. 2024.
Interpretable Table Question Answering via Plans of Atomic Table Transformations. https://openreview.net/forum?
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
111:12
Narechania, Endert, and Sinha
id=mDV36U4d6u
[26] OpenAI. 2024. AI in the Enterprise. Technical Report. OpenAI. https://cdn.openai.com/business-guides-and-resources/
ai-in-the-enterprise.pdf Accessed: 2025-06-17.
[27] OpenAI. 2025. A Practical Guide to Building Agents. https://cdn.openai.com/business-guides-and-resources/a-practical-
guide-to-building-agents.pdf Accessed: 2025-06-14.
[28] Ansh Radhakrishnan, Karina Nguyen, Anna Chen, Carol Chen, Carson Denison, Danny Hernandez, Esin Durmus,
Evan Hubinger, Jackson Kernion, Kamil˙e Lukoši¯ut˙e, et al. 2023. Question Decomposition Improves the Faithfulness of
Model-Generated Reasoning. arXiv preprint arXiv:2307.11768 (2023).
[29] Ashay Satav. 2025. Enterprise API & Platform Strategy in the Era of Agentic AI. Journal of Computer Science and
Technology Studies 7, 1 (2025), 380–385.
[30] Yijia Shao, Humishka Zope, Yucheng Jiang, Jiaxin Pei, David Nguyen, Erik Brynjolfsson, and Diyi Yang. 2025. Future
of Work with AI Agents: Auditing Automation and Augmentation Potential across the US Workforce. arXiv preprint
arXiv:2506.06576 (2025).
[31] Shavit, Yonadav and Agarwal, Sandhini and Brundage, Miles and Adler, Steven and O’Keefe, Cullen and Campbell,
Rosie and Lee, Teddy and Mishkin, Pamela and Eloundou, Tyna and Hickey, Alan and others. 2023. Practices for
Governing Agentic AI Systems. Technical Report. OpenAI. https://cdn.openai.com/papers/practices-for-governing-
agentic-ai-systems.pdf Accessed: 2025-06-17.
[32] Paschal Sheeran. 2002. Intention—Behavior Relations: a Conceptual and Empirical Review. European Review of Social
Psychology 12, 1 (2002), 1–36.
[33] Chufan Shi, Yixuan Su, Cheng Yang, Yujiu Yang, and Deng Cai. 2023. Specialist or Generalist? Instruction Tuning for
Specific NLP Tasks. arXiv preprint arXiv:2310.15326 (2023).
[34] Ben Shneiderman. 2022. Human-Centered AI. Oxford University Press.
[35] George J Stigler. 1974. Free Riders and Collective Action: An Appendix to Theories of Economic Regulation. The Bell
Journal of Economics and Management Science (1974), 359–365.
[36] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia
Polosukhin. 2017. Attention is All You Need. Advances in Neural Information Processing Systems 30 (2017).
[37] Dakuo Wang, Elizabeth Churchill, Pattie Maes, Xiangmin Fan, Ben Shneiderman, Yuanchun Shi, and Qianying Wang.
2020. From Human-Human Collaboration to Human-AI Collaboration: Designing AI Systems that Can Work Together
with People. In Extended Abstracts of the 2020 CHI Conference on Human Factors in Computing Systems. 1–6.
[38] Hui Wei, Zihao Zhang, Shenghua He, Tian Xia, Shijia Pan, and Fei Liu. 2025. PlanGenLLMs: A Modern Survey of LLM
Planning Capabilities. arXiv preprint arXiv:2502.11221 (2025).
[39] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Tom Griffiths, Yuan Cao, and Karthik Narasimhan. 2023. Tree
of Thoughts: Deliberate Problem Solving with Large Language Models. Advances in Neural Information Processing
Systems 36 (2023), 11809–11822.
[40] Kun Zhang, Jiali Zeng, Fandong Meng, Yuanzhuo Wang, Shiqi Sun, Long Bai, Huawei Shen, and Jie Zhou. 2024.
Tree-of-Reasoning Question Decomposition for Complex Question Answering with Large Language Models Authors.
In Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38. 19560–19568.
Received 20 February 2007; revised 12 March 2009; accepted 5 June 2009
J. ACM, Vol. 37, No. 4, Article 111. Publication date: August 2018.
```

</details>

---

## Technical Details

- **PDF Path**: `papers/Bottom-1-2506.22893v1.pdf`
- **Processing Configuration**:
  - max_chunk_size: 4000
  - min_chunk_size: 100
  - delay_between_requests: 1.0

*Analysis generated by Research Paper Scorer v0.1.0*
