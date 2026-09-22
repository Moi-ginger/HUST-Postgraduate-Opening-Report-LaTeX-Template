# 硕士学位论文选题报告

## 论文题目

**工具调用型大语言模型智能体故障诊断的信息表征与交互设计研究**

## 一、选题依据

### 1.1 研究来源

本课题来源于工具调用型大语言模型智能体的实际开发工作。智能体在执行多步骤任务时会留下模型请求与响应、工具调用与返回、状态变化、错误信息和重试记录。一次失败的表现可能出现在链路末端，实际问题却产生于较早的参数传递、工具返回解释、上下文更新或控制判断。运行信息分散在日志、调用平台、配置和代码中，开发者需要在多个位置之间查找并重新建立事件关系。

本研究以开发者形成诊断判断的过程为研究对象，通过经验研究识别跨案例问题，再形成和检验相应的信息表征与交互设计。时间线、关系图、摘要、搜索、比较和运行干预构成待研究的设计方案，其选择依据来自开发者在诊断过程中遇到的具体困难。

### 1.2 研究背景

大语言模型智能体（large language model agent）通过模型推理、工具调用、状态更新和流程控制完成任务。Yao 等[1](https://arxiv.org/abs/2210.03629)提出推理与行动协同方法（ReAct），将语言推理与环境操作组织在同一执行过程中。工具调用扩展了模型能力，也使系统结果同时受到模型、外部服务、运行框架和上下文管理影响。

智能体的故障具有跨步骤传播和多来源耦合特征。错误参数可以产生形式正常的工具返回，返回内容可能被后续模型误读，错误状态又可能经过多次调用后才表现为最终失败。相似症状可能对应工具异常、提示缺陷、状态污染或终止条件错误。运行记录还可能受到采样、截断、异步执行和隐私处理影响，现有材料有时不足以支持唯一原因判断。

分布式系统追踪已经建立跨组件事件关联的工程方法。Fonseca 等[13](https://www.usenix.org/conference/nsdi-07/x-trace-pervasive-network-tracing-framework)以任务标识关联跨层操作；Sigelman 等[14](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/)总结大规模追踪基础设施的部署经验；Mace 等[15](https://doi.org/10.1145/2815400.2815415)通过动态插桩支持跨组件因果查询。这些研究能够回答记录如何采集与连接，尚未充分解释开发者怎样使用长链路材料完成诊断。

近期智能体工具研究开始关注开发者工作。Epperson 等[25](https://doi.org/10.1145/3706598.3713581)访谈五名智能体开发者，发现检查长对话、定位问题和调整配置构成明显困难；其后续用户研究显示，可编辑与重置功能受到偏好，参与者仍难以决定修改位置和修改方式。van der Maden 等[22](https://doi.org/10.1145/3772318.3791069)对十九名大语言模型产品实践者的访谈表明，评价结果与具体改进行动之间存在缺口。两项研究共同说明，从看见异常到决定怎样修复，中间存在尚未解决的理解与证据组织问题。

现有系统提供了多种界面形态。Arawjo 等[21](https://doi.org/10.1145/3613904.3642016)通过提示和输出比较支持大语言模型试验；Lu 等[23](https://doi.org/10.1109/TVCG.2024.3394053)通过层级时间结构支持智能体行为分析；Dibia 等[24](https://doi.org/10.18653/v1/2024.emnlp-demo.8)将流程搭建、执行查看和调试整合到多智能体开发工具中；Hutter 和 Pradel[26](https://arxiv.org/abs/2602.06593)提供断点、编辑和中间产物查看。上述研究证实轨迹能够被组织为可操作界面，现有评价常同时改变信息内容与交互方式，难以解释具体设计为什么有效以及适用于什么故障。

自动失败分析也在快速发展。Cemri 等[27](https://arxiv.org/abs/2503.13657)建立多智能体失败分类；Zhang 等[28](https://proceedings.mlr.press/v267/zhang25cq.html)以一百二十七个系统的失败日志评价自动归因，最佳方法定位责任步骤的准确率仍然较低；Chen 等[29](https://arxiv.org/abs/2606.06324v2)通过连接数据流、控制流和实现位置支持运行框架缺陷诊断与修复。这些成果可以提供案例类型和机器建议，当前性能决定了开发者仍需核验自动结果。

本课题聚焦这一人机协同诊断环节：开发者怎样从失败现象进入相关运行材料，怎样形成并比较原因解释，怎样识别证据缺口，以及信息表征与交互设计能否提高诊断判断的质量。

### 1.3 研究目的

本研究拟完成三个相互衔接的目标。

1. 描述具有实际开发经验的使用者诊断工具调用型智能体失败时的活动、困难与信息需求，明确困难出现的任务条件和材料条件。
2. 围绕一项经形成性研究确认的核心困难，形成可实现、可比较的信息表征与交互方案，并说明设计选择的经验依据。
3. 通过任务实验和新案例观察，检验设计对诊断判断、过程理解、证据使用与操作成本的影响，提炼具有适用条件的设计原则。

### 1.4 研究意义

#### 理论意义

本研究计划形成工具调用型智能体故障诊断活动的经验描述，说明跨步骤异常、相似症状和材料缺失怎样影响开发者的查找、关联、假设形成和核验。该描述能够补充现有程序调试研究在概率性生成、自然语言记录与外部工具混合情境中的证据。

研究预期形成中层知识（intermediate-level knowledge）。Höök 和 Löwgren[45](https://doi.org/10.1145/2362364.2362371)将中层知识用于表达高于单个设计实例、能够迁移到相似设计情境的知识。本研究的原则将同时说明适用情境、设计操作、预期作用、经验依据和限制，使其能够用于相似智能体调试工具的设计决策。原则是否成立由后续研究结果决定，开题阶段不预先声明具体原则内容。

#### 实践意义

研究将形成一套可复现的故障案例、诊断任务、评分标准和原型评价方法。其结果可帮助智能体工具设计者选择记录内容、组织事件关系、呈现派生信息，并评价界面是否真正支持开发者判断。对开发团队而言，研究还可为运行记录规范和诊断工作流程提供参考。

## 二、国内外研究现状

### 2.1 程序调试行为与信息表征

Katz 和 Anderson[2](https://doi.org/10.1207/s15327051hci0304_2)通过编程任务与口语报告分析缺陷定位策略，发现调试者会在由输出回溯和由程序结构前向推演之间选择。Ko 等[3](https://doi.org/10.1109/TSE.2006.116)观察十名开发者完成维护任务，发现其持续进行搜索、依赖导航和信息收集，有限线索与界面导航成本会造成重复查找。Lawrance 等[4](https://doi.org/10.1109/TSE.2010.111)以信息觅食（information foraging）分析专业程序员的调试过程，说明信息线索与访问成本共同影响下一步查看位置。

信息组织会改变调试表现。Romero 等[6](https://doi.org/10.1016/j.ijhcs.2007.07.005)发现多表征环境的效果受到表征知识和编程经验影响。Cornelissen 等[7](https://doi.org/10.1109/TSE.2010.47)通过受控实验报告轨迹可视化对程序理解时间和正确性的改善。Ko 和 Myers[8](https://doi.org/10.1145/985692.985712)[9](https://doi.org/10.1145/1368088.1368130)[10](https://doi.org/10.1145/1518701.1518942)以面向问题的调试界面支持使用者从“为什么发生”或“为什么没有发生”进入相关执行事件。Parnin 和 Orso[11](https://doi.org/10.1145/2001420.2001445)发现，提供自动故障排序后，开发者仍需结合上下文理解可疑位置。

上述研究确立了本课题的基本分析单位：信息入口、导航路径、事件关系、问题解释和后续检查。其对象主要是代码与确定性执行，智能体轨迹中的自然语言信息、外部工具状态和概率性输出需要新的经验研究。

### 2.2 分布式运行追踪与过程来源

跨组件追踪研究解决了分散记录的关联问题。X-Trace[13](https://www.usenix.org/conference/nsdi-07/x-trace-pervasive-network-tracing-framework)、Dapper[14](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/)和 Pivot Tracing[15](https://doi.org/10.1145/2815400.2815415)分别展示任务标识传播、规模化采样和动态因果查询。它们为智能体记录的事件标识、父子关系和补充观测提供工程参考。

可视分析中的过程来源（provenance）研究关注分析历史怎样被记录和再利用。Ragan 等[16](https://doi.org/10.1109/TVCG.2015.2467551)区分数据来源、操作历史和分析理由等类型。Kadivar 等[17](https://doi.org/10.1109/VAST.2009.5333020)以可编辑历史支持分析回放。Xu 等[18](https://doi.org/10.1109/MCG.2015.50)指出操作记录与推理记录需要区分。Sacha 等[19](https://doi.org/10.1109/TVCG.2015.2467591)讨论不确定性在数据处理与知识形成中的传播，Hullman[20](https://doi.org/10.1109/TVCG.2019.2934287)则揭示不确定性表达受到沟通目标与设计成本制约。

这些研究能够指导运行材料的采集与表示。它们较少以故障诊断为最终任务，也缺少从界面操作到原因判断的证据。因此，本研究需要把过程来源的设计与诊断结果联系起来。

### 2.3 智能体工具与失败分析

现有智能体工具覆盖比较、概览、调试与干预。ChainForge[21](https://doi.org/10.1145/3613904.3642016)的用户研究显示，实践者会根据不同目标采用不同评价标准。AgentLens[23](https://doi.org/10.1109/TVCG.2024.3394053)通过层级时间结构支持行为分析，并以十四人对照研究评价任务表现。AutoGen Studio[24](https://doi.org/10.18653/v1/2024.emnlp-demo.8)提供声明式流程编辑和运行查看。AGDebugger[25](https://doi.org/10.1145/3706598.3713581)允许使用者查看、修改和重置多智能体消息，用户研究发现操作机会与有效干预之间仍有理解障碍。AgentStepper[26](https://arxiv.org/abs/2602.06593)把软件开发智能体的中间步骤组织为可检查会话，初步实验显示不同任务上的收益存在差异。

失败分类与自动归因研究为案例组织提供技术依据。MAST[27](https://arxiv.org/abs/2503.13657)覆盖系统设计、协调、验证和终止问题；Who&When[28](https://proceedings.mlr.press/v267/zhang25cq.html)把责任智能体与责任步骤分别评价；HarnessFix[29](https://arxiv.org/abs/2606.06324v2)把失败轨迹与实现材料关联。上述研究重点评价算法或系统能力，面向人的证据集中在小规模、特定任务的用户研究中。

### 2.4 解释工具与判断质量

Miller[30](https://doi.org/10.1016/j.artint.2018.07.007)指出人的解释具有选择性和对比性。Liao 等[31](https://doi.org/10.1145/3313831.3376590)访谈二十名人工智能产品实践者，发现解释问题随角色和任务变化。Amershi 等[32](https://doi.org/10.1145/3290605.3300233)通过资料综合、多轮专家评价和四十九名设计实践者验证，形成十八项人智交互设计指南。Wang 等[33](https://doi.org/10.1145/3290605.3300831)强调解释设计需要明确使用者目标和任务。

实证研究还显示解释可能制造理解错觉。Kaur 等[35](https://doi.org/10.1145/3313831.3376219)发现数据科学家会误读解释工具并在理解不足时信任结果。Buçinca 等[36](https://doi.org/10.1145/3449287)的实验显示，要求使用者先行思考的交互能够降低对错误建议的过度依赖，同时增加主观成本。Sieker 等[37](https://doi.org/10.18653/v1/2024.emnlp-main.1084)发现主观理解感与实际心智模型可能不一致。Ehsan 等[38](https://doi.org/10.1145/3411764.3445188)[39](https://doi.org/10.1145/3637396)分别从组织经验和系统边界拓展解释内容。

这些研究要求本课题把主观偏好、信心和诊断质量分开测量，并检查参与者能否引用证据、识别替代解释和发现材料不足。

### 2.5 研究述评

已有研究提供了三类基础。第一，程序调试研究解释了开发者怎样搜索、关联和保存信息。第二，运行追踪和过程来源研究建立了跨组件关联、历史回放与来源表达方法。第三，智能体与解释工具研究展示了可视分析、交互干预和自动归因的可能性，并揭示主观理解与实际判断之间的差异。

现有证据尚未充分回答工具调用型智能体故障诊断中的三个问题：开发者在完整诊断过程中遇到哪些跨案例困难；信息表征与交互设计分别作用于哪些诊断活动；设计效果在材料不完整、症状相似和框架变化时能否保持。上述问题构成本研究的经验起点。

## 三、研究问题与研究范围

### 3.1 研究问题

本研究的核心问题是：**如何通过信息表征与交互设计，支持开发者依据复杂运行材料形成可核验的工具调用型大语言模型智能体故障诊断判断？**

核心问题分解为三个研究问题。

1. **研究问题一：**开发者诊断工具调用型智能体失败时，会进行哪些信息查找、事件关联、原因解释和后续检查活动；其中反复出现的困难及其信息条件是什么？
2. **研究问题二：**针对形成性研究识别的核心困难，怎样组织运行信息并设计交互，使开发者更有效地找到关键材料、比较原因解释和识别证据边界？
3. **研究问题三：**所形成的设计在什么任务和材料条件下改善诊断判断、过程理解与证据使用，其操作成本和适用范围是什么？

### 3.2 核心概念

**工具调用型大语言模型智能体**指以大语言模型为决策或生成组件，能够调用外部工具并根据返回结果继续执行多步骤任务的系统。研究包含单智能体与多智能体工作流，要求案例中存在可检查的工具调用和状态传递。

**故障**指系统实际执行与任务要求、实现约束或预期流程不一致的情形。研究关注可通过运行材料和实现检查分析的故障，不研究模型参数层面的内部机理。

**诊断判断**包括故障发生位置、可能原因、支持该判断的证据、仍存在的替代解释和下一步检查。材料不足时，指出无法区分的原因及所需补充信息属于合理判断。

**信息表征与交互设计**包括运行事件的分组、层级、关系、来源和缺失状态表达，以及搜索、展开、跳转、比较、标注和回放等操作。具体设计形式由研究问题一和方案比较决定。

### 3.3 研究范围

研究对象为具有编程基础和智能体开发、集成或调试经验的使用者。研究任务聚焦开发阶段的失败诊断，不覆盖终端用户使用智能体时的信任形成，也不把在线生产事故处置作为主要场景。

案例以可公开复现的开源智能体为主，覆盖模型调用、工具执行、上下文或状态和流程控制。研究原型使用保存的运行材料支持诊断，需要观察运行变化的任务加入受控回放。原型范围集中于诊断所需的信息组织和核心交互。

## 四、理论与分析框架

### 4.1 意义建构

Klein 等[40](https://doi.org/10.1109/MIS.2006.88)[41](https://doi.org/10.1109/MIS.2006.100)提出的数据—框架循环描述人怎样以已有解释寻找信息，又怎样根据新信息修正解释。Klein 等[42](https://doi.org/10.1017/CBO9780511612062.006)进一步把活动分为框架形成、质疑、比较和重构。Pirolli 和 Card[43](https://www.e-education.psu.edu/geog885/sites/www.e-education.psu.edu.geog885/files/geog885q/file/Lesson_02/Sensemaking_206_Camera_Ready_Paper.pdf)通过认知任务分析描述信息搜寻、组织和结构形成之间的联系。

本研究将意义建构用作过程分析框架。形成性研究编码关注参与者从什么症状形成初步解释、依据解释查找什么材料、怎样处理反证和竞争解释，以及何时修改判断。该框架帮助连接操作日志、口语材料和最终答案，不预先规定设计形式。

### 4.2 过程来源与不确定性

Ragan 等[16](https://doi.org/10.1109/TVCG.2015.2467551)对过程来源类型和用途的整理用于区分原始运行事件、系统派生关系、模型生成内容与开发者诊断记录。Sacha 等[19](https://doi.org/10.1109/TVCG.2015.2467591)关于不确定性传播的分析用于检查材料来源、缺失和派生过程怎样影响判断。

这一框架指导研究材料和界面标注：原始采集内容保留事件标识与来源；规则计算结果说明计算方式；模型生成的摘要或候选原因明确标识；缺失记录说明缺失位置和可支持的判断范围。评价时记录参与者是否使用和正确理解这些信息。

### 4.3 设计知识的形成

Zimmerman 等[44](https://doi.org/10.1145/1240624.1240704)提出通过设计开展研究（research through design），强调设计产物与知识主张的关系。Höök 和 Löwgren[45](https://doi.org/10.1145/2362364.2362371)提出中层知识，为从具体设计提炼可迁移概念提供表达层级。Sedlmair 等[46](https://doi.org/10.1109/TVCG.2012.213)与 Meyer 和 Dykes[47](https://doi.org/10.1109/TVCG.2019.2934539)提出的设计研究过程与严谨性要求，用于组织问题理解、方案形成、评价和反思。

本研究为每项设计主张维护“问题条件—观察证据—设计操作—预期作用—评价结果—适用限制”的对应记录。只有获得多阶段材料支持的主张才提炼为主要原则。

## 五、研究内容与研究方法

### 5.1 总体研究路径

研究采用序列式混合方法，共分三个阶段。第一阶段研究实际诊断活动并确定核心设计问题；第二阶段通过备选方案和任务式走查形成研究原型；第三阶段通过对照任务和新案例观察评价设计作用与适用范围。各阶段按照研究问题、设计主张和评价证据的顺序衔接。

| 阶段 | 主要问题 | 研究材料与方法 | 阶段产出 | 对下一阶段的约束 |
| --- | --- | --- | --- | --- |
| 形成性研究 | 困难发生在什么活动和信息条件中 | 关键事件访谈、真实材料回溯、诊断任务观察、框架分析 | 活动模型、困难类型、核心设计问题 | 决定原型解决什么问题和需要哪些材料 |
| 设计探索 | 哪些信息组织与交互方式能够作用于核心困难 | 备选概念、低保真原型、两轮任务式走查、设计记录 | 核心设计主张、研究原型、评价协议 | 决定实验条件和过程指标 |
| 效果与边界评价 | 设计改善什么、成本如何、何时失效 | 被试内对照任务、操作日志、任务后访谈、新案例观察 | 效果估计、机制解释、适用条件、设计原则 | 形成论文知识贡献 |

### 5.2 诊断活动形成性研究

#### 参与者招募

研究计划从公司开发团队和外部开发者社群招募参与者。纳入条件包括：近一年参与过大语言模型应用或智能体开发；实际处理过工具调用或多步骤执行问题；能够说明一次具体失败事件。招募时记录从业年限、智能体项目经验、主要框架、任务类型和调试频率。

样本采用目的抽样，覆盖单智能体与多智能体、不同工具类型和不同经验水平。以 15—20 名作为初始招募范围，每完成一组访谈即更新样本矩阵。Malterud 等[48](https://doi.org/10.1177/1049732315617444)提出的信息力（information power）用于判断停止条件：当新增样本不再增加关键活动、困难条件或反例，且主要类型已具有足够材料时停止。公司来源与外部来源分别标记，以检查组织环境造成的偏差。

#### 资料收集

每位参与者先完成约 60—90 分钟的关键事件访谈。访谈要求围绕一至两个实际事件，按时间顺序说明异常怎样被发现、查看过哪些材料、形成过哪些解释、采取过哪些检查、何时改变判断以及最终怎样确认原因。参与者可使用获得授权并脱敏的运行记录、截图或代码片段进行回溯。

为补充回忆资料，参与者再完成一个 30—45 分钟的诊断任务。任务材料来自公开案例池，提供基础日志、事件详情和必要实现片段。研究者采用口语报告与屏幕记录，重点观察起始位置、跳转顺序、搜索词、证据摘录、竞争解释和停止条件。任务后进行回放访谈，询问关键操作所依据的判断。

无法提供真实材料的参与者仍可参加访谈，其内容在分析中标记为回忆资料。研究不收集公司机密、用户个人信息或未经授权的生产数据。

#### 分析方法

资料转写后采用框架分析法（framework method）。Gale 等[49](https://doi.org/10.1186/1471-2288-13-117)提出的逐案与跨案矩阵用于保持原始材料和主题之间的联系。初始编码包含失败现象、诊断目标、信息入口、查找路径、事件关系、原因假设、反证、信息缺口、检查动作和判断结果；研究过程中允许增加由资料产生的编码。

两名研究者共同编码首批资料，讨论代码定义与边界，再由主研究者完成其余材料，并对至少四分之一资料进行双人复核。分析分别比较公司与外部来源、经验水平、单智能体与多智能体案例，寻找共同模式和反例。

每项困难以“任务情境—触发条件—可观察行为—所需信息—后果”的结构记录。核心设计问题依据出现范围、影响程度、可设计性和研究可行性选择。第一阶段结束时确定第二阶段的设计范围，开题时不预先指定时间线、关系图或自动摘要为主方案。

### 5.3 交互方案设计与原型开发

#### 设计输入与备选方案

设计输入包括第一阶段的活动模型、困难类型、典型案例和反例，以及程序调试、追踪和解释工具中的相关设计。围绕核心困难形成至少三种备选概念，每种概念明确：使用者需要完成的诊断活动、信息组织方式、交互操作、预期帮助和可能成本。

若核心困难是跨步骤关系难以建立，备选方案可比较层级时间组织、按问题展开的关系路径和可查询依赖视图；若核心困难是多个原因难以区分，备选方案可比较证据矩阵、竞争假设记录和差异化检查提示。上述示例仅说明方案空间，实际选择依据第一阶段资料。

#### 两轮任务式走查

第一轮使用纸面或低保真交互原型，计划招募 5—6 名具有相关经验的参与者。参与者用同一组案例完成定位、解释和下一步检查任务。研究记录误解、遗漏、无效跳转和额外信息需求，淘汰不能对应核心困难的方案。

第二轮使用中保真原型，计划招募 5—6 名未参加第一轮的参与者，比较保留方案的使用过程。评价包含任务答案、关键证据命中、操作路径、访谈和简短任务负担。此阶段用于选择与完善设计，不进行确证性显著性检验。

#### 研究原型

原型提供两层能力。基础层包括运行列表、事件时间顺序、搜索、事件详情和相关实现材料访问。研究层实现第二轮选定的核心设计。两层使用相同原始案例数据，以控制信息数量并比较组织方式与交互设计的作用。

派生信息按照来源区分。确定性规则产生的关系保留计算依据和源事件入口；模型生成的摘要或候选解释明确标识生成方式，并允许返回原始记录；缺失内容以可观察的采集状态表示。每项主要设计决定记录备选方案、选择理由和预期作用。

### 5.4 原型评价与适用范围检验

#### 案例构建

正式评价计划建立约 12 个案例，案例来源以两个开源智能体框架和可公开复现任务为主。故障通过修改工具返回、参数传递、上下文更新、状态写入或流程控制构造，保留完整配置和运行记录。每个案例只设置一个主要原因，可以包含由主要原因引发的多个表面异常。

案例池覆盖三种诊断结构：问题在较早步骤产生并在较晚步骤表现；不同环节能够产生相似症状；关键记录缺失导致部分原因无法区分。材料中保留正常事件、失败重试和与任务无关的记录，使任务接近实际排查环境。

每个案例建立两份说明。故障说明记录构造方式、实际原因和复现步骤；评分说明只依据参与者可见材料，列出可支持的结论、合理替代解释、关键证据和必要检查。两名具有相关经验的开发者独立核查案例，争议案例修改后再次核查。

#### 实验条件

正式研究设置基础界面与研究界面。基础界面提供常见的时间记录、搜索、事件详情和实现材料；研究界面在相同数据基础上加入核心设计。若核心设计必须依赖派生信息，实验协议列出新增内容、生成方式和可能误差，并将其视为完整设计条件的一部分。

采用被试内设计（within-subjects design）。每位参与者完成练习和 6 个正式案例，在两个条件下各完成 3 个不同案例。条件顺序、案例分配和任务顺序采用平衡安排，避免同一参与者重复处理相同案例。正式参与者不得参加原型走查或接触正式案例。

预实验计划招募 4—6 人，检查任务时长、难度、界面学习成本、评分规则和记录完整性。正式研究以 36 名合格参与者作为招募预算起点。最终样本量在预实验后依据主要结果的最小有意义差异、案例间方差和统计功效模拟确定，正式分析只使用独立于预实验的数据。

#### 评价指标

主要结果为诊断判断质量。材料充分的案例要求参与者指出合理原因范围并引用关键证据；材料不足的案例要求指出尚不能区分的原因和必要检查。评分允许多条合理证据路径，不要求参与者复述预设答案。

| 评价方面 | 记录内容 | 与研究问题的关系 |
| --- | --- | --- |
| 诊断判断质量 | 原因范围、关键证据、替代解释、必要检查 | 检验设计是否支持可核验判断 |
| 过程理解 | 执行顺序、输入来源、状态变化和传播关系 | 识别设计作用于哪个理解环节 |
| 证据使用 | 查看和引用的事件、反证、缺失信息识别 | 解释正确或错误判断怎样形成 |
| 判断信心 | 每个任务后的信心评分及其与判断质量的关系 | 识别高信心错误和过度谨慎 |
| 使用成本 | 完成时间、操作数量、回访困难与任务负担 | 估计设计收益与交互代价 |

开放答案由不了解实验条件的评分者依据手册评价。至少四分之一答案进行双人独立评分，报告一致性和分歧处理。操作日志以事件标识记录访问、搜索、展开、比较和提交行为；任务后访谈结合操作回放追问关键判断。

#### 定量与定性分析

主要结果根据评分分布选择广义线性混合效应模型（generalized linear mixed-effects model）或线性混合效应模型，以参与者和案例处理重复观测。模型报告条件效应、区间估计和效应量。经验、条件顺序和案例类型作为预先确定的调整因素。完成时间分析保留超时信息，并进行适合其分布的稳健分析。

正式收集前进行预注册（preregistration），明确主要结果、假设、样本停止规则、条件差异、排除标准、评分手册和模型。次要指标与探索性分析明确标记。

定性资料围绕错误路径和成功路径分析，包括未发现关键材料、误解事件关系、忽略反证、过早收敛、识别材料不足和提出有效补充检查。定量结果说明设计是否产生变化，过程资料用于解释变化发生在哪一环节。

#### 跨案例适用性检验

主要实验后选取 3—4 个未参与方案形成的新案例，优先来自第二种开源框架或不同工具组合。邀请 6—8 名开发者完成任务观察与访谈，检查设计在新事件结构、命名方式和故障类型中的使用情况。

该阶段记录哪些信息关系仍然必要、哪些界面元素需要调整、出现了哪些新困难。结果用于说明设计原则的适用范围，并区分跨案例稳定的主张与依赖特定原型的做法。

### 5.5 研究问题与研究方法对应关系

| 研究问题 | 样本与材料 | 方法 | 回答形式 |
| --- | --- | --- | --- |
| 研究问题一 | 15—20 名实践者；真实事件回溯与公开案例任务 | 关键事件访谈、任务观察、框架分析 | 诊断活动、困难类型及其信息条件 |
| 研究问题二 | 两轮各 5—6 名参与者；备选设计与典型案例 | 任务式走查、方案比较、设计记录 | 核心设计主张及其形成依据 |
| 研究问题三 | 正式样本量由功效模拟确定；约 12 个案例 | 被试内对照、混合效应模型、回放访谈 | 效果、作用环节、成本与边界 |
| 迁移检查 | 6—8 名开发者；3—4 个新案例 | 任务观察与访谈 | 设计原则的适用范围和修订依据 |

## 六、研究重点与难点

### 6.1 研究重点

研究重点是建立从实践问题到知识贡献的完整证据链。形成性研究要识别跨案例困难，原型要对应其中一个核心问题，实验要检验设计影响的具体活动，最终原则要包含适用条件和限制。各阶段使用统一的案例标识、设计记录和分析矩阵保持可追溯性。

另一个重点是区分信息增加与信息组织。基础界面和研究界面尽量使用相同原始数据；新增派生信息时明确其生成方式和误差。这样可以判断改善来自材料本身、访问方式还是自动建议。

### 6.2 实施难点

第一，实际智能体故障包含组织机密和个人信息，难以直接共享。研究通过授权脱敏的事件回溯理解工作情境，以开源系统构建可复现实验案例。

第二，诊断答案可能存在多个合理层级。研究在每个案例中区分实际实现原因与可见材料支持的判断，评分接受不同证据路径，并把识别信息不足作为有效结果。

第三，专业开发者招募成本较高。研究采用公司与外部社群双渠道，分阶段复用招募基础，同时避免正式实验参与者提前接触案例。

第四，设计效果可能受到案例和经验影响。研究通过多案例平衡、混合效应模型、过程资料和新案例观察说明变化范围。

## 七、预期知识贡献与创新点

### 7.1 预期知识贡献

本研究预期形成两个层级的知识。

第一层为经验知识：工具调用型智能体诊断活动、困难与信息条件的跨案例描述。它回答开发者在什么情况下难以定位、关联、比较或判断，并说明可观察行为和后果。

第二层为设计知识：针对核心困难的信息表征与交互原则。每项原则包含适用情境、设计操作、预期作用、支持证据、使用成本和适用限制。原则的数量和具体内容由研究资料决定。

### 7.2 预期创新点

1. 以完整诊断过程为单位研究工具调用型智能体故障，建立运行材料条件与开发者诊断困难之间的经验联系。
2. 形成一套从症状、证据、原因解释到后续检查的界面评价方法，把诊断正确性、证据使用、信心和操作成本共同纳入评价。
3. 通过形成性研究、方案比较、对照评价和新案例检验提炼设计原则，说明设计作用与适用范围。

## 八、研究基础与可行性

### 8.1 已有基础

课题来自实际工作中观察到的智能体排错问题，已完成相关领域的初步文献调研和研究方案设计。访谈、案例收集、原型和实验尚未开始，开题报告中的样本和结果均为研究计划。

研究者能够通过公司渠道招募若干具有智能体开发经验的参与者，并计划通过 LinkedIn 等外部社群补充样本。案例以开源工具自行搭建为主，能够控制故障构造、运行记录与实验条件。

### 8.2 技术与实施可行性

研究原型范围集中于保存的运行材料、信息组织和核心交互。开源智能体框架能够提供工具调用、状态传递和流程控制案例。冻结运行材料可以降低模型服务变化对正式实验的影响。

研究按阶段推进。形成性研究先确定问题范围，低保真走查用于淘汰无效方案，中保真原型确认交互，正式实现只包含评价需要的功能。该安排能够控制开发工作量。

### 8.3 实施风险及应对措施

| 风险 | 应对安排 |
| --- | --- |
| 招募来源集中 | 记录来源与经验矩阵，定向补充外部参与者并进行分组比较 |
| 自建案例缺少真实复杂度 | 由实践者核查案例，保留正常事件、重试和合理歧义，加入新框架案例 |
| 设计范围扩大 | 只实现一个核心设计问题，使用基础层承载通用功能 |
| 评分争议 | 区分实际原因与可见证据，建立评分手册并进行双人复核 |
| 模型或框架更新 | 冻结实验材料、版本和配置，记录复现环境 |
| 样本量不足 | 提前开展多渠道招募，依据预实验和功效模拟调整正式计划 |

## 九、研究伦理与数据管理

参与者研究将在完成学校要求的伦理审查后开展。招募与知情同意材料说明研究目的、记录范围、补偿、退出权利和数据保留期限。公司渠道招募遵循自愿原则，研究参与和工作绩效评价分开。

真实案例仅使用获得授权并完成脱敏的材料。公开或合成案例在发布前检查密钥、个人信息、内部地址和许可条件。身份联系信息与研究编号分开保存，录音、屏幕记录和操作日志限制访问。论文与共享材料使用匿名编号和必要摘录。

模型生成内容在研究材料中标明来源，不将其视为事实答案。研究案例、评分说明、分析脚本和可公开的匿名材料按学校与参与者授权范围归档。

## 十、进度安排

| 时间 | 工作内容 | 阶段成果 |
| --- | --- | --- |
| 2026.09—2026.10 | 完成开题，细化协议，办理伦理审查，搭建初始案例 | 研究协议、招募材料、案例模板 |
| 2026.11—2027.01 | 开展关键事件访谈与诊断任务观察 | 访谈资料、活动模型、困难矩阵 |
| 2027.02—2027.03 | 完成跨案例分析，确定核心设计问题 | 形成性研究结果与设计要求 |
| 2027.03—2027.05 | 形成备选方案，完成两轮任务式走查 | 方案比较记录与核心设计主张 |
| 2027.05—2027.06 | 实现研究原型，核查案例和评分标准 | 原型、正式案例池、评分手册 |
| 2027.06—2027.08 | 进行预实验、功效模拟和预注册，启动正式评价 | 预实验结果、预注册方案、阶段数据 |
| 2027.09 | 中期答辩 | 形成性研究、设计依据、原型和评价进展 |
| 2027.09—2027.10 | 完成正式评价与新案例检验 | 完整研究数据与原则修订依据 |
| 2027.11—2028.02 | 综合分析，提炼设计原则，撰写论文 | 学位论文初稿 |
| 2028.03—2028.05 | 修改、送审与答辩准备 | 学位论文与归档材料 |

## 十一、预期成果

预期形成一篇设计学研究型硕士学位论文，内容包括开发者诊断活动与困难分析、方案形成过程、交互原型、实证评价和具有适用条件的设计原则。

配套成果包括可运行的研究原型、可复现或回放的故障案例、案例评分说明、实验协议和分析材料。研究结果成熟且授权条件允许时，整理为学术论文投稿。

## 参考文献

[1] [YAO S, ZHAO J, YU D, et al. ReAct: Synergizing Reasoning and Acting in Language Models[C]//International Conference on Learning Representations. 2023.](https://arxiv.org/abs/2210.03629)

[2] [KATZ I R, ANDERSON J R. Debugging: An Analysis of Bug-Location Strategies[J]. Human-Computer Interaction, 1987—1988, 3(4): 351—399.](https://doi.org/10.1207/s15327051hci0304_2)

[3] [KO A J, MYERS B A, COBLENZ M J, et al. An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information during Software Maintenance Tasks[J]. IEEE Transactions on Software Engineering, 2006, 32(12): 971—987.](https://doi.org/10.1109/TSE.2006.116)

[4] [LAWRANCE J, BOGART C, BURNETT M, et al. How Programmers Debug, Revisited: An Information Foraging Theory Perspective[J]. IEEE Transactions on Software Engineering, 2013, 39(2): 197—215.](https://doi.org/10.1109/TSE.2010.111)

[5] [RASMUSSEN J, JENSEN A. Mental Procedures in Real-Life Tasks: A Case Study of Electronic Trouble Shooting[J]. Ergonomics, 1974, 17(3): 293—307.](https://doi.org/10.1080/00140137408931355)

[6] [ROMERO P, DU BOULAY B, COX R, et al. Debugging Strategies and Tactics in a Multi-Representation Software Environment[J]. International Journal of Human-Computer Studies, 2007, 65(12): 992—1009.](https://doi.org/10.1016/j.ijhcs.2007.07.005)

[7] [CORNELISSEN B, ZAIDMAN A, VAN DEURSEN A. A Controlled Experiment for Program Comprehension through Trace Visualization[J]. IEEE Transactions on Software Engineering, 2011, 37(3): 341—355.](https://doi.org/10.1109/TSE.2010.47)

[8] [KO A J, MYERS B A. Designing the Whyline: A Debugging Interface for Asking Questions about Program Behavior[C]//Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. 2004: 151—158.](https://doi.org/10.1145/985692.985712)

[9] [KO A J, MYERS B A. Debugging Reinvented: Asking and Answering Why and Why Not Questions about Program Behavior[C]//Proceedings of the 30th International Conference on Software Engineering. 2008: 301—310.](https://doi.org/10.1145/1368088.1368130)

[10] [KO A J, MYERS B A. Finding Causes of Program Output with the Java Whyline[C]//Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. 2009: 1569—1578.](https://doi.org/10.1145/1518701.1518942)

[11] [PARNIN C, ORSO A. Are Automated Debugging Techniques Actually Helping Programmers?[C]//Proceedings of the 2011 International Symposium on Software Testing and Analysis. 2011: 199—209.](https://doi.org/10.1145/2001420.2001445)

[12] [KHANNA R, DODGE J, ANDERSON A, et al. Finding AI's Faults with AAR/AI: An Empirical Study[J]. ACM Transactions on Interactive Intelligent Systems, 2022, 12(1): 1—33.](https://doi.org/10.1145/3487065)

[13] [FONSECA R, PORTER G, KATZ R H, et al. X-Trace: A Pervasive Network Tracing Framework[C]//Proceedings of the 4th USENIX Symposium on Networked Systems Design and Implementation. 2007: 271—284.](https://www.usenix.org/conference/nsdi-07/x-trace-pervasive-network-tracing-framework)

[14] [SIGELMAN B H, BARROSO L A, BURROWS M, et al. Dapper, a Large-Scale Distributed Systems Tracing Infrastructure[R]. Google, 2010.](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/)

[15] [MACE J, ROELKE R, FONSECA R. Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems[C]//Proceedings of the 25th ACM Symposium on Operating Systems Principles. 2015: 378—393.](https://doi.org/10.1145/2815400.2815415)

[16] [RAGAN E D, ENDERT A, SANYAL J, et al. Characterizing Provenance in Visualization and Data Analysis: An Organizational Framework of Provenance Types and Purposes[J]. IEEE Transactions on Visualization and Computer Graphics, 2016, 22(1): 31—40.](https://doi.org/10.1109/TVCG.2015.2467551)

[17] [KADIVAR N, CHEN V, DUNSMUIR D, et al. Capturing and Supporting the Analysis Process[C]//Proceedings of the IEEE Symposium on Visual Analytics Science and Technology. 2009: 131—138.](https://doi.org/10.1109/VAST.2009.5333020)

[18] [XU K, ATTFIELD S, JANKUN-KELLY T J, et al. Analytic Provenance for Sensemaking: A Research Agenda[J]. IEEE Computer Graphics and Applications, 2015, 35(3): 56—64.](https://doi.org/10.1109/MCG.2015.50)

[19] [SACHA D, SENARATNE H, KWON B C, et al. The Role of Uncertainty, Awareness, and Trust in Visual Analytics[J]. IEEE Transactions on Visualization and Computer Graphics, 2016, 22(1): 240—249.](https://doi.org/10.1109/TVCG.2015.2467591)

[20] [HULLMAN J. Why Authors Don't Visualize Uncertainty[J]. IEEE Transactions on Visualization and Computer Graphics, 2020, 26(1): 130—139.](https://doi.org/10.1109/TVCG.2019.2934287)

[21] [ARAWJO I, SWOOPES C, VAITHILINGAM P, et al. ChainForge: A Visual Toolkit for Prompt Engineering and LLM Hypothesis Testing[C]//Proceedings of the CHI Conference on Human Factors in Computing Systems. 2024.](https://doi.org/10.1145/3613904.3642016)

[22] [VAN DER MADEN W, SADEK M, XIAO Z, et al. Results-Actionability Gap: Understanding How Practitioners Evaluate LLM Products in the Wild[C]//Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems. 2026: 1—17.](https://doi.org/10.1145/3772318.3791069)

[23] [LU J, PAN B, CHEN J, et al. AgentLens: Visual Analysis for Agent Behaviors in LLM-Based Autonomous Systems[J]. IEEE Transactions on Visualization and Computer Graphics, 2025, 31(8): 4182—4197.](https://doi.org/10.1109/TVCG.2024.3394053)

[24] [DIBIA V, CHEN J, BANSAL G, et al. AutoGen Studio: A No-Code Developer Tool for Building and Debugging Multi-Agent Systems[C]//Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations. 2024: 72—79.](https://doi.org/10.18653/v1/2024.emnlp-demo.8)

[25] [EPPERSON W, BANSAL G, DIBIA V, et al. Interactive Debugging and Steering of Multi-Agent AI Systems[C]//Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems. 2025.](https://doi.org/10.1145/3706598.3713581)

[26] [HUTTER R, PRADEL M. AgentStepper: Interactive Debugging of Software Development Agents[EB/OL]. arXiv:2602.06593, 2026[2026-09-22].](https://arxiv.org/abs/2602.06593)

[27] [CEMRI M, PAN M Z, YANG S, et al. Why Do Multi-Agent LLM Systems Fail?[EB/OL]. arXiv:2503.13657, 2025[2026-09-22].](https://arxiv.org/abs/2503.13657)

[28] [ZHANG S, YIN M, ZHANG J, et al. Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems[C]//Proceedings of the 42nd International Conference on Machine Learning. PMLR, 2025, 267: 76583—76599.](https://proceedings.mlr.press/v267/zhang25cq.html)

[29] [CHEN M, WANG J, LIU Z, et al. From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws[EB/OL]. arXiv:2606.06324v2, 2026[2026-09-22].](https://arxiv.org/abs/2606.06324v2)

[30] [MILLER T. Explanation in Artificial Intelligence: Insights from the Social Sciences[J]. Artificial Intelligence, 2019, 267: 1—38.](https://doi.org/10.1016/j.artint.2018.07.007)

[31] [LIAO Q V, GRUEN D, MILLER S. Questioning the AI: Informing Design Practices for Explainable AI User Experiences[C]//Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems. 2020: 1—15.](https://doi.org/10.1145/3313831.3376590)

[32] [AMERSHI S, WELD D, VORVOREANU M, et al. Guidelines for Human-AI Interaction[C]//Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems. 2019: 1—13.](https://doi.org/10.1145/3290605.3300233)

[33] [WANG D, YANG Q, ABDUL A, et al. Designing Theory-Driven User-Centric Explainable AI[C]//Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems. 2019: 1—15.](https://doi.org/10.1145/3290605.3300831)

[34] [ABDUL A, VERMEULEN J, WANG D, et al. Trends and Trajectories for Explainable, Accountable and Intelligible Systems: An HCI Research Agenda[C]//Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems. 2018: 1—18.](https://doi.org/10.1145/3173574.3174156)

[35] [KAUR H, NORI H, JENKINS S, et al. Interpreting Interpretability: Understanding Data Scientists' Use of Interpretability Tools for Machine Learning[C]//Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems. 2020: 1—14.](https://doi.org/10.1145/3313831.3376219)

[36] [BUÇINCA Z, MALAYA M B, GAJOS K Z. To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making[J]. Proceedings of the ACM on Human-Computer Interaction, 2021, 5(CSCW1): 1—21.](https://doi.org/10.1145/3449287)

[37] [SIEKER J, KRAMER M, ESCOFFIER T, et al. The Illusion of Competence: Evaluating the Effect of Explanations on Users' Mental Models of Visual Question Answering Systems[C]//Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing. 2024: 19459—19475.](https://doi.org/10.18653/v1/2024.emnlp-main.1084)

[38] [EHSAN U, LIAO Q V, MULLER M, et al. Expanding Explainability: Towards Social Transparency in AI Systems[C]//Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems. 2021: 1—19.](https://doi.org/10.1145/3411764.3445188)

[39] [EHSAN U, LIAO Q V, PASSI S, et al. Seamful XAI: Operationalizing Seamful Design in Explainable AI[J]. Proceedings of the ACM on Human-Computer Interaction, 2024, 8(CSCW1): 1—29.](https://doi.org/10.1145/3637396)

[40] [KLEIN G, MOON B, HOFFMAN R R. Making Sense of Sensemaking 1: Alternative Perspectives[J]. IEEE Intelligent Systems, 2006, 21(4): 70—73.](https://doi.org/10.1109/MIS.2006.88)

[41] [KLEIN G, MOON B, HOFFMAN R R. Making Sense of Sensemaking 2: A Macrocognitive Model[J]. IEEE Intelligent Systems, 2006, 21(5): 88—92.](https://doi.org/10.1109/MIS.2006.100)

[42] [KLEIN G, PHILLIPS J K, RALL E L, et al. A Data-Frame Theory of Sensemaking[M]//HOFFMAN R R. Expertise Out of Context. New York: Lawrence Erlbaum Associates, 2007: 113—155.](https://doi.org/10.1017/CBO9780511612062.006)

[43] [PIROLLI P, CARD S K. The Sensemaking Process and Leverage Points for Analyst Technology as Identified Through Cognitive Task Analysis[C]//Proceedings of the 2005 International Conference on Intelligence Analysis. 2005.](https://www.e-education.psu.edu/geog885/sites/www.e-education.psu.edu.geog885/files/geog885q/file/Lesson_02/Sensemaking_206_Camera_Ready_Paper.pdf)

[44] [ZIMMERMAN J, FORLIZZI J, EVENSON S. Research through Design as a Method for Interaction Design Research in HCI[C]//Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. 2007: 493—502.](https://doi.org/10.1145/1240624.1240704)

[45] [HÖÖK K, LÖWGREN J. Strong Concepts: Intermediate-Level Knowledge in Interaction Design Research[J]. ACM Transactions on Computer-Human Interaction, 2012, 19(3): 1—18.](https://doi.org/10.1145/2362364.2362371)

[46] [SEDLMAIR M, MEYER M, MUNZNER T. Design Study Methodology: Reflections from the Trenches and the Stacks[J]. IEEE Transactions on Visualization and Computer Graphics, 2012, 18(12): 2431—2440.](https://doi.org/10.1109/TVCG.2012.213)

[47] [MEYER M, DYKES J. Criteria for Rigor in Visualization Design Study[J]. IEEE Transactions on Visualization and Computer Graphics, 2020, 26(1): 87—97.](https://doi.org/10.1109/TVCG.2019.2934539)

[48] [MALTERUD K, SIERSMA V D, GUASSORA A D. Sample Size in Qualitative Interview Studies: Guided by Information Power[J]. Qualitative Health Research, 2016, 26(13): 1753—1760.](https://doi.org/10.1177/1049732315617444)

[49] [GALE N K, HEATH G, CAMERON E, et al. Using the Framework Method for the Analysis of Qualitative Data in Multi-Disciplinary Health Research[J]. BMC Medical Research Methodology, 2013, 13: 117.](https://doi.org/10.1186/1471-2288-13-117)
