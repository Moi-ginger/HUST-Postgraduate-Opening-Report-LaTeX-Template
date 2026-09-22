# 硕士学位论文选题报告

## 论文题目

**工具调用型大语言模型智能体故障诊断的信息表征与交互设计研究**

## 一、选题依据

### 1.1 研究来源与背景

本课题来源于工具调用型大语言模型智能体的实际开发工作。智能体完成一项任务时，通常需要多次请求模型、调用外部工具并更新运行状态。任务失败后，开发者需要查阅提示、调用参数、工具返回、状态变化和错误信息，判断问题发生的环节及其对后续步骤的影响。这些材料分散在调用平台、日志、配置和代码中，增加了查找和理解的难度。

大语言模型（large language model，LLM）通过工具调用参与外部任务执行，形成大语言模型智能体（large language model agent）。Yao 等[1](https://arxiv.org/abs/2210.03629)提出的推理与行动协同方法（ReAct）将语言推理与环境操作相结合，使模型能够根据任务进展继续采取行动。在这种执行方式下，一次错误可能先改变工具参数或中间状态，经过后续处理才表现为最终失败。开发者需要解释跨步骤的影响，比较可能的原因，并决定继续检查什么。

近期研究开始提供这一问题的直接证据。Epperson 等[2](https://doi.org/10.1145/3706598.3713581)通过开发者访谈和用户研究发现，长对话检查、问题定位及运行调整存在困难，提供编辑和重执行功能后，使用者仍需判断修改位置和方式。van der Maden 等[3](https://doi.org/10.1145/3772318.3791069)对十九名大语言模型产品实践者的访谈揭示，发现评价问题与采取具体改进行动之间存在缺口。Kumar 等[4](https://arxiv.org/abs/2506.12347v3)对开发者与编程智能体协作的观察，也体现了持续评价、增量交互和人工干预在真实任务中的作用。

本课题研究开发者形成诊断判断的过程，重点关注运行材料的组织和使用。信息表征指运行事件及其属性、关系和来源在界面中的呈现方式；交互设计指开发者查找、关联、比较和核验这些信息的操作。研究将从实际诊断事件出发，确定具有共同性的困难，再形成和检验具体设计。

### 1.2 研究目的

本研究拟建立工具调用型智能体故障诊断的信息条件与开发者活动之间的经验联系，围绕一项经研究确认的核心困难，探索能够改善诊断判断的信息表征与交互方式，并提炼具有适用条件的设计原则。

具体目标包括：

1. 通过真实事件访谈和诊断任务观察，描述开发者查找材料、形成原因解释和检验判断的过程，识别反复出现的困难及其条件。
2. 根据经验研究确定设计问题，比较备选方案，形成能够表达和检验核心设计主张的原型。
3. 通过对照任务和新案例观察，评价设计对诊断判断、证据使用和操作成本的影响，明确原则的作用与适用范围。

### 1.3 研究意义

#### 1.3.1 理论意义

本研究预期在两个层级形成知识贡献。第一层为经验描述，说明在什么任务和信息条件下，开发者难以定位相关事件、建立事件关系、区分原因解释或决定后续检查。这些结果能够补充程序调试研究在自然语言记录、概率性输出和外部工具混合情境中的经验材料。

第二层为设计原则，概括针对共同诊断困难的设计操作、预期作用和适用条件。Höök 和 Löwgren[5](https://doi.org/10.1145/2362364.2362371)讨论的中层知识（intermediate-level knowledge）为这一贡献定位提供了参考。原则将联系具体实例和可迁移的设计认识，使其他设计者能够判断是否适用于类似任务，并在不同界面中实施。具体原则由形成性研究、方案比较及评价结果共同形成。

#### 1.3.2 实践意义

本研究将形成可复现的诊断案例、研究原型和评价材料，为智能体调试工具的设计提供依据。研究结果可帮助工具设计者判断哪些信息需要被记录，哪些关系需要被呈现，以及哪些操作有助于使用者检查自己的判断。案例与评分材料还可为开发团队评价调试界面和改进运行记录提供参考。

## 二、国内外研究现状

### 2.1 程序调试中的信息查找与原因理解

Ko 等[6](https://doi.org/10.1109/TSE.2006.116)观察开发者完成软件维护任务，发现其需要持续查找、关联和收集信息，线索不足和导航成本会妨碍理解。Lawrance 等[7](https://doi.org/10.1109/TSE.2010.111)通过信息觅食（information foraging）视角解释专业程序员的搜索行为，说明信息线索、预期价值和访问成本影响下一步检查位置。Starr 和 Storey[8](https://doi.org/10.1145/3800945)通过二十七名专业开发者的访谈，将排错中的困惑与系统理解、心理模型构建及认知疲劳联系起来。这些研究支持从具体活动和信息条件分析诊断困难。

信息表征的作用已有实验证据。Romero 等[9](https://doi.org/10.1016/j.ijhcs.2007.07.005)发现多表征环境中的调试行为与经验及表征知识有关；Cornelissen 等[10](https://doi.org/10.1109/TSE.2010.47)通过受控实验报告执行轨迹可视化对程序理解的帮助；Ko 和 Myers[11](https://doi.org/10.1145/1518701.1518942)通过面向原因问答的调试界面（Whyline）将程序输出问题连接到执行事件。Parnin 和 Orso[12](https://doi.org/10.1145/2001420.2001445)则发现，自动给出可疑位置之后，开发者仍需要上下文完成理解。

这些研究提示，本课题应同时考察找到相关材料和形成合理解释的过程。智能体运行中的自然语言内容、外部工具状态和观测缺失，会改变二者之间的联系，需要通过新的开发者资料具体分析。

### 2.2 大语言模型开发中的评价与改进

Barke 等[13](https://doi.org/10.1145/3586030)通过程序员使用代码生成工具的观察，描述加速既定实现和探索可能方案两种交互方式，揭示使用目的与知识状态对交互的影响。van der Maden 等[3](https://doi.org/10.1145/3772318.3791069)将研究推进到产品实践中的评价工作，指出评价结果与改进行动之间的衔接困难。Kumar 等[4](https://arxiv.org/abs/2506.12347v3)在真实仓库任务中观察开发者与智能体协作，提供了持续检查和人工干预的过程证据。

Arawjo 等[14](https://doi.org/10.1145/3613904.3642016)提出提示与输出比较工具（ChainForge），通过实验室研究和使用访谈展示输出探索、假设检验及评价迭代的工作方式。这些研究说明，生成结果需要在具体任务中被检查和解释。对于长链路智能体失败，仍需进一步明确开发者使用哪些跨步骤信息，以及怎样把观察转化为下一步检查。

### 2.3 智能体运行过程的可视分析与调试

Lu 等[15](https://doi.org/10.1109/TVCG.2024.3394053)提出智能体行为可视分析系统（AgentLens），利用层级结构和多粒度时间信息支持行为探索，并通过使用案例和用户研究进行评价。Epperson 等[2](https://doi.org/10.1145/3706598.3713581)提出交互调试工具（AGDebugger），分别开展诊断和运行引导研究，显示局部编辑和重执行的需求，也记录了选择干预位置的困难。Hutter 和 Pradel[16](https://arxiv.org/abs/2602.06593)提出软件开发智能体调试器（AgentStepper），以小规模研究考察暂停、检查与编辑功能。

近期工作扩展了事件关联和原始材料核验。Gao 等[17](https://aclanthology.org/2026.acl-demo.29/)通过科学智能体执行轨迹可视化工具（Graph of Trace）获得专家关于理解和使用价值的反馈。Wu 等[18](https://doi.org/10.1609/aaai.v40i48.42393)提出轨迹转图平台（AgentGraph），以类型化关系关联任务、工具、数据和人工干预，并将图元素连接到原始轨迹。

现有工具已经展示了多种设计实现。围绕开发者诊断活动，还需要补充三方面证据：哪些信息组织方式对应实际困难，设计改变了什么判断或检查行为，以及效果在不同任务和经验条件下如何变化。

### 2.4 运行记录、自动归因与判断边界

Sigelman 等[19](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/)总结大规模分布式追踪基础设施（Dapper）的部署经验，为跨组件记录的关联提供工程参考。Ragan 等[20](https://doi.org/10.1109/TVCG.2015.2467551)区分数据、操作、交互和分析理由等来源记录，提示执行历史与使用者的分析过程需要分别处理。

自动故障分析提供了案例与建议来源。Cemri 等[21](https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html)建立多智能体失败分类；Zhang 等[22](https://proceedings.mlr.press/v267/zhang25cq.html)评价自动定位责任主体和步骤的方法；Chen 等[23](https://arxiv.org/abs/2606.06324v2)将失败轨迹与运行框架实现联系起来，研究缺陷诊断和修复。它们分别提供失败类型、归因评价和实现关联的方法，人的诊断研究还需考察开发者怎样理解和核验这些结果。

本课题将区分实际故障原因和现有记录支持的判断。某些案例具有明确原因，参与者可根据材料识别；某些案例缺少关键观测，合理结果是列出尚未区分的解释，并提出能够区分它们的检查。该区分将同时用于案例构造、任务要求和评分。

### 2.5 解释呈现与判断质量

Liao 等[24](https://doi.org/10.1145/3313831.3376590)通过设计实践者访谈说明，解释需求与使用者角色、任务和问题有关。Kaur 等[25](https://doi.org/10.1145/3313831.3376219)研究数据科学家使用解释工具的过程，发现误解和过度依赖现象。Buçinca 等[26](https://doi.org/10.1145/3449287)通过对照实验发现，促使使用者独立思考的交互措施能够减少对错误建议的依赖，同时可能增加使用成本。Sieker 等[27](https://doi.org/10.18653/v1/2024.emnlp-main.1084)进一步研究解释对系统能力判断的影响，揭示主观理解与对系统局限的认识之间可能存在偏差。

这些结果支持将诊断表现、证据使用、信心和使用体验分别评价。Guo 等[28](https://doi.org/10.1109/TVCG.2015.2424872)关于图关系不确定性的实验也说明，视觉编码的效果受到任务及编码组合影响。若原型表达推断关系、缺失信息或自动建议，研究需要检查参与者是否正确理解其含义。

### 2.6 设计原则的形成与研究空间

国内相关研究强调智能时代人的能力、决策控制与交互设计之间的联系。范俊君等[29](https://doi.org/10.1360/N112017-00221)从交互模型和界面发展提出研究议题；许为、葛列众[30](https://doi.org/10.3724/SP.J.1042.2020.01409)提出以人为中心的人工智能及人机合作研究框架。具体设计原则需要进一步通过任务和使用情境获得支持。

Amershi 等[31](https://doi.org/10.1145/3290605.3300233)通过多轮评议和产品评价形成交互指南；Weisz 等[32](https://doi.org/10.1145/3613904.3642466)结合文献、实践者反馈、现有应用及实际设计过程形成生成式人工智能设计原则。两项研究展示了从多种材料中提炼和修订设计知识的路径。Sedlmair 等[33](https://doi.org/10.1109/TVCG.2012.213)以及 Meyer 和 Dykes[34](https://doi.org/10.1109/TVCG.2019.2934539)的方法研究，则支持在问题理解、设计实现和评价之间保留明确的论证关系。

综合以上文献，本课题的研究空间是：从工具调用型智能体开发者的诊断活动出发，说明信息条件与判断困难的关系，通过原型比较检验设计作用，并在新案例中考察其适用性。具体的时间线、关系图、摘要、比较或重执行功能，将依据研究发现选择。

## 三、研究问题、对象与分析框架

### 3.1 研究问题

本课题的核心问题是：**在工具调用型智能体故障诊断中，哪些信息条件使开发者难以形成和检验原因判断，怎样的信息表征与交互支持能够改善这些活动？**

围绕核心问题提出三个研究问题：

| 研究问题 | 需要取得的证据 | 预期回答形式 |
| --- | --- | --- |
| 研究问题一：开发者怎样使用运行材料诊断失败，反复出现的困难与哪些任务、信息条件有关？ | 真实事件回溯、任务观察、运行材料、判断与行动记录 | 跨案例活动描述及“条件—困难—行为后果”关系 |
| 研究问题二：针对一项核心困难，怎样的信息组织与交互操作能够支持开发者检查原因解释？ | 备选方案、任务式走查、设计理由、迭代观察 | 设计主张、备选方案的选择依据与研究原型 |
| 研究问题三：设计对诊断判断和证据使用产生什么影响，其作用在新案例中如何变化？ | 对照实验、过程资料、新案例任务与访谈 | 设计效果、使用成本、适用条件及修订后的原则 |

### 3.2 研究对象与范围

研究对象为具有实际开发或排错经验的工具调用型智能体开发者。目标系统包含一个主要智能体，能够通过多次模型请求和工具调用完成任务，并保留可供检查的运行记录。研究任务从失败结果出发，要求开发者解释异常、指出依据并提出下一步检查。

主要分析单位为一次具有明确任务目标、失败表现和诊断活动的事件。案例将覆盖跨步骤信息传递、工具交互及流程控制等运行条件。多智能体研究为相关工作和案例设计提供参考，正式研究范围集中在单个主要智能体，以保持责任关系和任务条件的可分析性。

研究关注对运行行为的诊断，包括工具参数、返回内容、状态更新和配置条件。模型内部表征、训练机制和参数级解释不构成本课题的研究对象。

### 3.3 分析框架与理论作用

本研究以任务活动和运行材料为分析起点，将诊断事件整理为“任务与症状、可见材料、参与者问题、原因假设、检查行动、判断变化”六类内容。这一结构用于组织资料，具体类别将依据分析结果调整。

信息觅食视角用于解释材料入口、搜索线索和访问成本。意义建构（sensemaking）视角用于分析分散材料如何被组织为原因解释，以及解释怎样随新材料改变。Pirolli 和 Card[35](https://www.e-education.psu.edu/geog885/sites/www.e-education.psu.edu.geog885/files/geog885q/file/Lesson_02/Sensemaking_206_Camera_Ready_Paper.pdf)的认知任务分析提供了信息搜集与解释形成的过程参照；Klein 等[36](https://doi.org/10.1109/MIS.2006.100)关于资料与解释框架相互作用的讨论，可用于识别假设维持与修订的条件。

两种视角承担具体分析任务。出现重复查找和无效导航时，重点检查线索与访问成本；出现忽略反例、难以比较原因或无法决定检查方向时，重点分析判断形成与修订。研究将保留不能由初始框架解释的资料，并据此调整分类。

## 四、研究内容与总体路径

研究按“诊断实践研究—设计探索—对照评价—新案例检验—知识提炼”推进。各阶段的产出作为后续阶段的输入。

| 阶段 | 核心工作 | 阶段产出 | 进入下一阶段的依据 |
| --- | --- | --- | --- |
| 诊断实践研究 | 关键事件访谈、任务观察、跨案例分析 | 困难与信息条件矩阵 | 核心困难有多个案例支持，能够通过设计进行比较 |
| 设计探索 | 提出备选方案、任务式走查、迭代原型 | 明确设计主张与原型 | 方案可用，设计差异可描述，评价材料能够回答问题 |
| 对照评价 | 冻结条件、开展正式任务、分析判断和过程 | 效果估计与行为解释 | 获得足以讨论核心主张的任务及过程资料 |
| 新案例检验 | 更换任务或工具条件，观察作用变化 | 支持案例、失效案例及修订依据 | 能够说明原则适用与不适用的条件 |
| 知识提炼 | 综合实证材料与设计记录 | 经验描述和设计原则 | 原则各项论断均有对应材料与证据范围 |

核心困难的选择综合考虑出现范围、诊断后果、材料可获得性、设计可介入性及实验可检验性。例如，研究可能发现困难主要来自跨步骤数据关联，也可能集中于多个原因解释之间的比较。原型将围绕最终选定的问题实现一组必要功能。

## 五、研究方法与实施方案

### 5.1 诊断实践研究

#### 5.1.1 招募与样本安排

形成性研究拟招募12—16名参与者，通过公司和领英（LinkedIn）等外部专业渠道招募，覆盖不同组织、开发经验和工具使用背景。纳入条件为：近六个月内实际搭建、修改或维护过工具调用型智能体，且能够描述至少一次亲自参与的排错事件。招募将记录开发年限、智能体经验、系统类型、排错频率和来源渠道，并针对已有样本的缺项补充参与者。

Malterud 等[37](https://doi.org/10.1177/1049732315617444)提出的信息力（information power）将定性样本充分性与目标、样本特征、访谈质量和分析方式联系起来。本研究据此评估资料是否足以回答研究问题，重点检查核心困难是否有跨参与者和跨任务的支持，反例是否得到解释，以及不同经验背景的材料是否充分。计划人数用于安排研究资源，实际招募根据资料质量和案例覆盖进行调整。

#### 5.1.2 数据收集

每次研究约60—90分钟，包括关键事件回溯和诊断任务观察。关键事件回溯围绕参与者亲历的故障展开，依次询问任务目标、最初症状、已取得的材料、曾怀疑的原因、采取的检查和最终判断。优先请参与者借助获得授权并脱敏的记录说明过程；无法提供记录时，以事件时间线和具体操作回忆补充，并标记资料来源。

任务观察使用初步构建的失败案例，让参与者查阅运行材料并完成诊断。研究记录屏幕、操作和同步口语报告（think-aloud），在自然停顿处询问当前判断及其依据。任务结束后回看关键片段，核对研究者对操作含义的理解。真实事件用于理解工作情境，统一任务便于比较不同参与者在相近条件下的活动。

资料包括访谈转录、事件概要、运行片段、操作时间线、参与者提出的假设及判断变化。研究将区分参与者回忆的经历、任务中直接观察的行为和研究者的解释。

#### 5.1.3 分析方法

研究采用框架法（framework method）。Gale 等[38](https://doi.org/10.1186/1471-2288-13-117)提出的案例—主题矩阵适合组织多名参与者的过程资料。分析先选取不同背景的案例开放编码，再结合初步分析框架形成编码表，随后在其余资料中应用和修订。

编码内容主要包括：当前诊断问题、所需与实际取得的信息、事件关系、原因解释、检查行动、判断变化及活动结果。跨案例比较重点识别同一困难是否出现于不同系统或任务，以及相似现象是否对应不同原因。例如，多次返回同一事件可能来自导航负担，也可能来自正在比较两种解释，需要结合口语和判断记录辨别。

研究拟邀请另一名研究人员复核约四分之一的资料，比较编码依据并记录分歧处理。分析保留反例和条件差异，形成核心困难、支持案例及适用条件的矩阵。结果进入设计阶段前，将邀请部分参与者核对事件解释是否符合其经历。

### 5.2 案例构建与答案标准

#### 5.2.1 案例来源和构造

研究以开源智能体框架自行构建可复现案例，并依据实践研究修订其任务和故障条件。初步考虑资料检索、结构化数据查询和多步骤工具处理等任务，最终选择取决于访谈结果及实现可行性。公司案例主要用于理解实际困难和核查任务真实性，正式实验材料以可公开或可授权复现的系统为主。

拟建立12—16个候选案例，经过专家核查和预实验后选取12个进入正式案例池。每个案例保存任务说明、系统版本、工具定义、正常运行材料、失败运行材料、配置及故障构造记录。保留完成诊断所需的背景和合理干扰事件，控制内容长度与领域知识要求。

案例差异围绕核心研究问题安排，可涉及异常发生位置与最终症状的距离、多个原因的表面相似性，以及关键材料是否充分。正式实验只选择其中一项作为主要案例条件，其余条件用于平衡难度和描述任务。

#### 5.2.2 实际原因与可见证据

每个案例建立两份记录。故障记录说明实际改变了哪些系统条件、故障如何发生，以及哪些复现或干预支持这一解释。任务记录说明参与者可看到哪些材料、能够据此作出什么判断，以及仍有哪些无法确定的内容。

材料充分的案例要求参与者指出与证据相符的原因及其作用过程。材料不足的案例允许保留多个解释，但要求说明具体缺少什么，以及哪项检查能够区分这些解释。研究将以有针对性的缺失构造后一类任务，并核查剩余线索是否意外泄露答案。

案例拟由两名具有相关开发经验的人员独立检查。核查内容包括情境合理性、故障可复现性、可见材料充分性、替代解释和评分规则。存在多个有效诊断路径时，将其纳入评分手册。构造时选定的故障只是实际原因记录，评分还需依据参与者可见材料判断答案是否合理。

### 5.3 设计探索与原型形成

研究围绕选定的核心困难提出至少两种备选方案。例如，针对跨步骤关联困难，可比较按诊断问题组织的访问入口与显式依赖关系导航；针对解释核验困难，可比较并列材料检查与逐项假设检查。具体方案将在实践研究后形成。

设计探索拟开展两轮任务式走查，共招募6—8名参与者，每轮约4—5人，部分参与者参与两轮以观察修改效果，并补充首次使用者检查学习成本。走查使用相同或难度相近的任务，收集理解错误、检查行为、未满足的信息需要和操作障碍。

原型分为通用功能和研究功能。通用功能包括任务说明、事件查看、必要搜索和材料展开；研究功能承载核心设计主张。每次迭代保存对应困难、设计意图、观察结果及修改理由，淘汰仅受偏好支持但未改善目标活动的方案。

最终原型优先使用保存的运行材料，以保证任务可复现。若形成性研究确认交互重执行对核心问题不可缺少，将为相关工具提供固定响应或受控执行，并记录每次修改和执行条件。正式评价前冻结原型版本。

### 5.4 对照评价设计

#### 5.4.1 比较条件与研究主张

正式研究采用被试内设计（within-subject design），比较基础界面与研究界面。基础界面提供可用的时间序列、事件详情、搜索和展开功能；研究界面在此基础上实现选定的信息组织或交互支持。训练使用独立练习案例，确保参与者能够操作两种界面。

比较前建立条件清单，逐项核对原始材料、派生内容、搜索能力、默认展开状态和访问步骤。若研究重点为信息组织，两种界面提供相同语义内容，差异集中于其呈现和操作。若选定方案引入新的派生信息，则把“派生信息及其呈现”的整体作用作为评价对象，并在研究主张和分析中保持一致。

主要待检验主张为：针对核心诊断困难形成的设计，在所覆盖的案例中提高有依据的诊断达成率。设计是否影响完成时间、材料核验、错误判断的信心和使用负担，作为次要问题考察。预实验之后确定并预注册具体主张、主要指标和评分规则。

#### 5.4.2 参与者与任务分配

正式实验初步按36名参与者安排，招募条件与形成性研究一致，并记录其经验。预实验拟招募4—6人，用于检查任务时长、理解难度、评分可操作性和测量流程。预实验参与者不进入正式实验；正式实验参与者不提前接触所用案例。

正式案例池拟包含12个案例，每人完成6个，每种界面各3个。通过平衡任务分配，使每个案例在两种界面下均获得评价，同一参与者只接触每个案例一次。界面顺序与案例分配交叉平衡，避免将某类故障固定给某一条件。全部任务预计约90—110分钟，具体时长依据预实验确定，并安排休息。

样本量依据主要指标、最小有实际意义的差异、参与者和案例的变异范围进行模拟论证。Lakens[39](https://doi.org/10.1525/collabra.33267)的样本量论证方法以及 Green 和 MacLeod[40](https://doi.org/10.1111/2041-210X.12504)的模拟方法为此提供依据。研究在正式招募前确定目标人数和分析计划，将预实验参数与保守参数范围共同纳入计算，避免仅依赖单一试测效应。

#### 5.4.3 任务流程与评价指标

每个任务要求参与者提交：对失败原因的判断、支持判断的运行事件、尚未排除的解释、下一步检查及判断信心。正式计时任务不要求持续口述，过程资料以操作记录为主，并在任务后进行简短回顾，减少口述对完成时间的影响。

主要指标为有依据的诊断达成率。每个答案依据预先确定的标准判断是否达成：

1. 原因或无法确定的判断符合案例可见材料允许的结论。
2. 引用的运行事件准确且能够支持关键判断。
3. 提出的下一步检查与剩余疑问相匹配；材料已经充分时，可提出有针对性的确认或修复检查。

三个条件分别评分，再按预注册规则形成达成判定，同时保留分项结果。承认无法判断需要指出具体缺口和可区分解释的检查，空泛保留意见不计为达成。

| 指标类别 | 具体测量 | 解释用途 |
| --- | --- | --- |
| 主要结果 | 有依据的诊断达成率 | 比较两种界面对诊断任务的支持 |
| 判断组成 | 原因或信息不足判断、引用依据、下一步检查的分项得分 | 识别改善发生的环节 |
| 时间与操作 | 完成时间、关键材料访问、比较与回查行为 | 描述获得结果所需的成本及过程 |
| 信心 | 作答后0—100分信心，与答案达成情况对应 | 检查错误判断是否伴随过高信心 |
| 使用体验 | 心智努力、操作困难及访谈反馈 | 解释使用负担和接受程度 |

任务达到时间上限时结束并保存当前判断；完成时间按未完成任务的截尾情况处理。两名评分者依据匿名化答案独立评分，评分材料隐藏界面条件，先报告一致性，再按评分手册讨论分歧。评分手册在正式数据分析前冻结。

#### 5.4.4 数据分析

主要结果拟使用广义线性混合模型（generalized linear mixed model），以界面条件为主要固定效应，纳入参与者与案例的随机效应，并按预注册计划处理顺序和经验因素。模型结构、参数估计及拟合异常的处理方式在预实验后确定。结果报告效应估计及置信区间。

时间、分项得分和使用体验分别分析。过程资料用于检查关键材料是否被发现、原因解释是否得到核验，以及错误判断如何形成。经验和案例条件的差异主要用于描述效果范围，探索性分析与主要检验分别呈现。

研究将把结果与预期作用联系起来。例如，诊断表现提高且关键关系的检查增加，可为相应设计主张提供支持；如果只有完成时间降低，则贡献集中在效率改善。效果解释依据实际结果形成。

### 5.5 新案例检验与设计原则提炼

对照评价后，拟另外构建3—4个未参与设计迭代的新案例，改变任务内容、工具组合或框架实现中的至少一项条件，保留待检验的共同诊断问题。招募6—8名具有相关经验的参与者完成任务，观察原则预期作用是否出现，以及是否需要额外前提。新案例研究重点分析迁移条件和失效情境。

研究同时尝试将一项核心原则用另一种低保真表现方式表达，并结合任务走查检查使用者能否完成相同检查活动。该步骤帮助区分原则依赖的操作与某个界面布局的偶然特征。结果将与正式实验一同用于修订原则。

每项原则按照以下结构整理：

| 内容 | 需要回答的问题 |
| --- | --- |
| 适用情境 | 哪类任务、信息条件或使用者困难需要这项原则？ |
| 设计操作 | 设计者应怎样组织信息或提供检查操作？ |
| 预期作用 | 该操作影响哪项诊断活动？ |
| 支持证据 | 哪些观察、比较结果和新案例支持这一判断？ |
| 实施条件与成本 | 需要哪些记录、背景知识和操作投入？ |
| 适用边界 | 哪些情况下效果减弱、无效或产生新的困难？ |

研究保留未得到支持的设计主张，并说明其结果。最终原则数量根据证据决定。

## 六、研究重点、难点与质量控制

### 6.1 研究重点

本研究重点是建立实践问题、设计选择与评价结论之间的对应关系。形成性研究确定可重复观察的困难，原型表达针对这一困难的设计主张，实验检查主张是否获得支持，新案例研究界定适用条件。

另一个重点是诊断答案的合理性。研究将区分实际故障、可见证据和参与者判断，避免只按最终原因名称评价任务表现。原始材料、派生信息和自动建议保留来源，使评分和过程分析具有可追溯依据。

### 6.2 主要难点与应对

| 难点 | 应对安排 |
| --- | --- |
| 实际案例包含公司或个人信息 | 以授权脱敏事件理解情境，用开源系统构建可复现任务 |
| 自建案例与真实困难脱节 | 依据访谈选择案例，由实践者核查背景、歧义和检查路径 |
| 多种原因符合表面症状 | 分别记录实际原因与可见材料支持的解释，允许多条合理诊断路径 |
| 原型同时改变过多因素 | 围绕一个核心问题设计条件，核对各条件的信息和操作差异 |
| 参与者经验与案例难度造成差异 | 记录经验，训练基础操作，平衡任务，联合分析人员与案例差异 |
| 专业参与者招募不足 | 提前开展公司与外部渠道招募，分阶段维护招募矩阵并调整计划 |
| 模型和工具更新影响重复评价 | 固定运行材料、版本与配置，保存构造记录及可复现环境 |

## 七、预期成果与创新点

### 7.1 预期成果

本研究拟形成以下成果：工具调用型智能体故障诊断的跨案例经验描述；围绕核心困难的研究原型及设计记录；包含运行材料、任务要求和评分手册的案例集；经对照评价与新案例检验支持的设计原则；完整学位论文及可在授权范围内共享的研究材料。

### 7.2 预期创新点

第一，围绕开发者完整诊断活动，研究运行信息条件与判断困难之间的联系，补充工具调用型智能体情境下的信息使用证据。

第二，针对经过经验研究确认的共同困难，将信息表征或交互操作转化为可比较的设计主张，考察其对判断依据、检查行为和诊断结果的作用。

第三，通过多案例评价及新案例检验形成具有适用条件的设计原则，使研究结论能够用于相似诊断工具的设计选择。创新的具体内容及范围将依据后续研究结果确定。

## 八、研究基础与可行性

课题来自实际开发工作中的问题观察，已完成相关文献调研和研究方案设计。访谈、案例收集、原型开发和实验尚未开展，本报告中的样本及研究安排均为计划。

研究者可通过公司渠道接触若干具有智能体开发经验的人员，并计划通过外部专业社群扩展招募。技术实现拟使用开源框架，研究原型主要处理保存的运行材料和必要的检查操作，开发范围与核心研究问题保持一致。

整体工作按阶段推进。先以访谈和轻量案例确认问题，再通过低保真方案和任务走查确定设计，正式实现集中于评价需要的功能。中期前完成形成性研究、原型和预实验，并争取取得正式评价的阶段性数据；中期后完成评价、迁移检验和论文写作。

## 九、研究伦理与数据管理

涉及参与者的研究将在完成学校要求的伦理程序后开展。知情同意材料说明研究目的、参与内容、录音及屏幕记录范围、补偿方式、退出权利和数据保存安排。公司渠道招募遵循自愿原则，参与情况不用于工作评价。

研究仅收集完成分析所需的材料。真实案例须取得授权并进行脱敏，排除密钥、个人信息及不可公开的业务内容。联系信息与研究编号分开保存，原始录音、屏幕记录和文本资料限制访问。论文使用匿名编号和必要摘录，公开材料遵守参与者授权及开源许可。

自动生成的摘要或建议保留生成配置与来源标记。案例、评分手册、原型版本和分析材料统一归档，以支持研究复核。

## 十、进度安排

| 时间 | 研究工作 | 阶段成果 |
| --- | --- | --- |
| 2026.09—2026.10 | 完成开题，细化研究协议，办理伦理程序，构建初始案例 | 研究协议、招募材料、案例模板 |
| 2026.11—2027.01 | 开展关键事件访谈与任务观察，同步整理资料 | 访谈及观察资料、初步编码 |
| 2027.02—2027.03 | 跨案例分析，补充样本，确定核心设计问题 | 困难与信息条件矩阵、设计要求 |
| 2027.03—2027.05 | 比较备选方案，完成两轮任务式走查 | 设计记录、核心主张、原型方案 |
| 2027.05—2027.06 | 实现研究原型，核查案例与评分规则 | 原型、正式案例池、评分手册 |
| 2027.06—2027.08 | 预实验、样本量论证与预注册，启动正式评价 | 预实验结果、正式研究计划、阶段数据 |
| 2027.09 | 中期答辩 | 形成性研究、设计依据、原型及评价进展 |
| 2027.09—2027.10 | 完成正式评价与新案例检验 | 完整研究数据、原则修订依据 |
| 2027.11—2028.02 | 综合分析并撰写论文 | 经验描述、设计原则、论文初稿 |
| 2028.03—2028.05 | 论文修改、送审与答辩准备 | 学位论文定稿、归档材料 |

## 十一、论文拟定结构

第一章为绪论，介绍研究问题、背景、对象和研究路径。第二章为相关研究，综述程序调试、智能体交互工具、解释与判断以及设计研究方法。第三章为诊断实践研究，报告参与者、资料收集、跨案例分析及核心困难。第四章为设计探索，说明设计主张、备选方案、迭代过程及原型。第五章为对照评价与新案例检验，报告任务设计、数据分析和研究结果。第六章提炼设计原则，讨论其证据、适用条件及与相关研究的联系。第七章总结研究贡献与后续研究方向。

## 参考文献

[1] [YAO S, ZHAO J, YU D, et al. ReAct: Synergizing Reasoning and Acting in Language Models[C]//International Conference on Learning Representations. 2023.](https://arxiv.org/abs/2210.03629)

[2] [EPPERSON W, BANSAL G, DIBIA V, et al. Interactive Debugging and Steering of Multi-Agent AI Systems[C]//Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems. 2025.](https://doi.org/10.1145/3706598.3713581)

[3] [VAN DER MADEN W, SADEK M, XIAO Z, et al. Results-Actionability Gap: Understanding How Practitioners Evaluate LLM Products in the Wild[C]//Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems. 2026: 1—17.](https://doi.org/10.1145/3772318.3791069)

[4] [KUMAR A, BAJPAI Y, GULWANI S, et al. Why AI Agents Still Need You: Findings from Developer-Agent Collaborations in the Wild[C]//Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering. 2025: 432—444.](https://arxiv.org/abs/2506.12347v3)

[5] [HÖÖK K, LÖWGREN J. Strong Concepts: Intermediate-Level Knowledge in Interaction Design Research[J]. ACM Transactions on Computer-Human Interaction, 2012, 19(3): 23:1—23:18.](https://doi.org/10.1145/2362364.2362371)

[6] [KO A J, MYERS B A, COBLENZ M J, et al. An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information during Software Maintenance Tasks[J]. IEEE Transactions on Software Engineering, 2006, 32(12): 971—987.](https://doi.org/10.1109/TSE.2006.116)

[7] [LAWRANCE J, BOGART C, BURNETT M, et al. How Programmers Debug, Revisited: An Information Foraging Theory Perspective[J]. IEEE Transactions on Software Engineering, 2013, 39(2): 197—215.](https://doi.org/10.1109/TSE.2010.111)

[8] [STARR A, STOREY M A. Theory of Troubleshooting: The Developer's Cognitive Experience of Overcoming Confusion[J/OL]. ACM Transactions on Software Engineering and Methodology, 2026[2026-09-22].](https://doi.org/10.1145/3800945)

[9] [ROMERO P, DU BOULAY B, COX R, et al. Debugging Strategies and Tactics in a Multi-Representation Software Environment[J]. International Journal of Human-Computer Studies, 2007, 65(12): 992—1009.](https://doi.org/10.1016/j.ijhcs.2007.07.005)

[10] [CORNELISSEN B, ZAIDMAN A, VAN DEURSEN A. A Controlled Experiment for Program Comprehension through Trace Visualization[J]. IEEE Transactions on Software Engineering, 2011, 37(3): 341—355.](https://doi.org/10.1109/TSE.2010.47)

[11] [KO A J, MYERS B A. Finding Causes of Program Output with the Java Whyline[C]//Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. 2009: 1569—1578.](https://doi.org/10.1145/1518701.1518942)

[12] [PARNIN C, ORSO A. Are Automated Debugging Techniques Actually Helping Programmers?[C]//Proceedings of the 2011 International Symposium on Software Testing and Analysis. 2011: 199—209.](https://doi.org/10.1145/2001420.2001445)

[13] [BARKE S, JAMES M B, POLIKARPOVA N. Grounded Copilot: How Programmers Interact with Code-Generating Models[J]. Proceedings of the ACM on Programming Languages, 2023, 7(OOPSLA1): 78:1—78:27.](https://doi.org/10.1145/3586030)

[14] [ARAWJO I, SWOOPES C, VAITHILINGAM P, et al. ChainForge: A Visual Toolkit for Prompt Engineering and LLM Hypothesis Testing[C]//Proceedings of the CHI Conference on Human Factors in Computing Systems. 2024.](https://doi.org/10.1145/3613904.3642016)

[15] [LU J, PAN B, CHEN J, et al. AgentLens: Visual Analysis for Agent Behaviors in LLM-Based Autonomous Systems[J]. IEEE Transactions on Visualization and Computer Graphics, 2025, 31(8): 4182—4197.](https://doi.org/10.1109/TVCG.2024.3394053)

[16] [HUTTER R, PRADEL M. AgentStepper: Interactive Debugging of Software Development Agents[EB/OL]. arXiv:2602.06593, 2026[2026-09-22].](https://arxiv.org/abs/2602.06593)

[17] [GAO T, LI H, LI J H, et al. Graph of Trace: Visualizing Execution Traces of Scientific Agents[C]//Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations). 2026: 297—306.](https://aclanthology.org/2026.acl-demo.29/)

[18] [WU Z, CHO S, VILLALOBOS C E M, et al. AgentGraph: Trace-to-Graph Platform for Interactive Analysis and Robustness Testing in Agentic AI Systems[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2026, 40(48): 41721—41723.](https://doi.org/10.1609/aaai.v40i48.42393)

[19] [SIGELMAN B H, BARROSO L A, BURROWS M, et al. Dapper, a Large-Scale Distributed Systems Tracing Infrastructure[R]. Google, 2010.](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/)

[20] [RAGAN E D, ENDERT A, SANYAL J, et al. Characterizing Provenance in Visualization and Data Analysis: An Organizational Framework of Provenance Types and Purposes[J]. IEEE Transactions on Visualization and Computer Graphics, 2016, 22(1): 31—40.](https://doi.org/10.1109/TVCG.2015.2467551)

[21] [CEMRI M, PAN M Z, YANG S, et al. Why Do Multi-Agent LLM Systems Fail?[C]//Advances in Neural Information Processing Systems. 2025, 38.](https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html)

[22] [ZHANG S, YIN M, ZHANG J, et al. Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems[C]//Proceedings of the 42nd International Conference on Machine Learning. PMLR, 2025, 267: 76583—76599.](https://proceedings.mlr.press/v267/zhang25cq.html)

[23] [CHEN M, WANG J, LIU Z, et al. From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws[EB/OL]. arXiv:2606.06324v2, 2026[2026-09-22].](https://arxiv.org/abs/2606.06324v2)

[24] [LIAO Q V, GRUEN D, MILLER S. Questioning the AI: Informing Design Practices for Explainable AI User Experiences[C]//Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems. 2020: 1—15.](https://doi.org/10.1145/3313831.3376590)

[25] [KAUR H, NORI H, JENKINS S, et al. Interpreting Interpretability: Understanding Data Scientists' Use of Interpretability Tools for Machine Learning[C]//Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems. 2020: 1—14.](https://doi.org/10.1145/3313831.3376219)

[26] [BUÇINCA Z, MALAYA M B, GAJOS K Z. To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making[J]. Proceedings of the ACM on Human-Computer Interaction, 2021, 5(CSCW1): 1—21.](https://doi.org/10.1145/3449287)

[27] [SIEKER J, JUNKER S, UTESCHER R, et al. The Illusion of Competence: Evaluating the Effect of Explanations on Users' Mental Models of Visual Question Answering Systems[C]//Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing. 2024: 19459—19475.](https://doi.org/10.18653/v1/2024.emnlp-main.1084)

[28] [GUO H, HUANG J, LAIDLAW D H. Representing Uncertainty in Graph Edges: An Evaluation of Paired Visual Variables[J]. IEEE Transactions on Visualization and Computer Graphics, 2015, 21(10): 1173—1186.](https://doi.org/10.1109/TVCG.2015.2424872)

[29] [范俊君, 田丰, 杜一, 等. 智能时代人机交互的一些思考[J]. 中国科学: 信息科学, 2018, 48(4): 361—375.](https://doi.org/10.1360/N112017-00221)

[30] [许为, 葛列众. 智能时代的工程心理学[J]. 心理科学进展, 2020, 28(9): 1409—1425.](https://doi.org/10.3724/SP.J.1042.2020.01409)

[31] [AMERSHI S, WELD D, VORVOREANU M, et al. Guidelines for Human-AI Interaction[C]//Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems. 2019: 1—13.](https://doi.org/10.1145/3290605.3300233)

[32] [WEISZ J D, HE J, MULLER M, et al. Design Principles for Generative AI Applications[C]//Proceedings of the CHI Conference on Human Factors in Computing Systems. 2024.](https://doi.org/10.1145/3613904.3642466)

[33] [SEDLMAIR M, MEYER M, MUNZNER T. Design Study Methodology: Reflections from the Trenches and the Stacks[J]. IEEE Transactions on Visualization and Computer Graphics, 2012, 18(12): 2431—2440.](https://doi.org/10.1109/TVCG.2012.213)

[34] [MEYER M, DYKES J. Criteria for Rigor in Visualization Design Study[J]. IEEE Transactions on Visualization and Computer Graphics, 2020, 26(1): 87—97.](https://doi.org/10.1109/TVCG.2019.2934539)

[35] [PIROLLI P, CARD S K. The Sensemaking Process and Leverage Points for Analyst Technology as Identified Through Cognitive Task Analysis[C]//Proceedings of the 2005 International Conference on Intelligence Analysis. 2005.](https://www.e-education.psu.edu/geog885/sites/www.e-education.psu.edu.geog885/files/geog885q/file/Lesson_02/Sensemaking_206_Camera_Ready_Paper.pdf)

[36] [KLEIN G, MOON B, HOFFMAN R R. Making Sense of Sensemaking 2: A Macrocognitive Model[J]. IEEE Intelligent Systems, 2006, 21(5): 88—92.](https://doi.org/10.1109/MIS.2006.100)

[37] [MALTERUD K, SIERSMA V D, GUASSORA A D. Sample Size in Qualitative Interview Studies: Guided by Information Power[J]. Qualitative Health Research, 2016, 26(13): 1753—1760.](https://doi.org/10.1177/1049732315617444)

[38] [GALE N K, HEATH G, CAMERON E, et al. Using the Framework Method for the Analysis of Qualitative Data in Multi-Disciplinary Health Research[J]. BMC Medical Research Methodology, 2013, 13: 117.](https://doi.org/10.1186/1471-2288-13-117)

[39] [LAKENS D. Sample Size Justification[J]. Collabra: Psychology, 2022, 8(1): 33267.](https://doi.org/10.1525/collabra.33267)

[40] [GREEN P, MACLEOD C J. SIMR: An R Package for Power Analysis of Generalized Linear Mixed Models by Simulation[J]. Methods in Ecology and Evolution, 2016, 7(4): 493—498.](https://doi.org/10.1111/2041-210X.12504)
