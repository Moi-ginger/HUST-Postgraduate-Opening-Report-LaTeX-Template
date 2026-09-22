# 文献综述

## 工具调用型大语言模型智能体故障诊断的信息表征与交互设计

### 一、研究背景与综述范围

大语言模型智能体（large language model agent）通过模型推理、工具调用、状态更新和流程控制完成多步骤任务。Yao 等[1](https://arxiv.org/abs/2210.03629)提出推理与行动协同方法（ReAct），以交替生成推理文本和环境行动的方式连接语言模型与外部环境。工具调用使智能体能够检索信息、执行代码和操作业务系统，也使一次任务的结果同时受到模型输出、工具返回、上下文传递、状态管理与控制逻辑影响。

本文所称故障诊断，是开发者依据运行记录和实现材料，对失败现象进行定位、解释并决定后续检查的过程。诊断对象包括工具参数错误、返回结果误读、状态污染、上下文遗漏、终止条件错误和跨步骤传播等问题。运行轨迹（execution trace）是这一过程的主要材料，通常由模型请求与响应、工具调用与返回、时间信息、状态快照、错误信息以及相关配置组成。

现有研究分布在程序调试、分布式系统追踪、可视分析、可解释人工智能和智能体开发工具等领域。各领域分别研究了信息查找、事件关联、过程回溯、解释使用与交互干预，却较少共同回答一个设计问题：面对长链路、异构且可能不完整的智能体运行材料，开发者怎样形成可核验的诊断判断，界面可以在哪些环节提供帮助。

本综述以实证研究为主体，按照“研究问题—研究方法—主要发现—证据缺口”梳理相关工作。综述重点考察四类证据：开发者实际怎样调试；执行记录怎样被组织和关联；智能体开发工具怎样支持分析与干预；解释和不确定性呈现怎样影响人的判断。设计研究方法文献用于说明从具体原型提炼可复用知识的研究程序。

### 二、程序调试行为与信息表征研究

#### 2.1 程序调试中的信息搜寻行为

Katz 和 Anderson[2](https://doi.org/10.1207/s15327051hci0304_2)通过编程任务、口语报告和键盘操作记录分析程序员定位缺陷的策略。研究发现，调试者会依据错误输出向前追查，也会从程序结构向后推演；所采用的路径受到程序归属、经验和已有问题表征影响。错误表现提供诊断起点，原因定位还需要选择推理方向并持续修正问题表征。

Ko 等[3](https://doi.org/10.1109/TSE.2006.116)让十名开发者在陌生程序中完成调试与功能修改任务，观察其搜索、关联和收集信息的行为。参与者会在搜索相关代码、沿依赖关系导航和保存可能有用的内容之间反复切换。有限或误导性的线索会造成搜索失败，开发环境中的导航操作占用了大量时间，已经找到的相关位置也可能在后续操作中丢失。研究把调试困难具体化为线索质量、关联成本与工作空间记忆三个问题。

Lawrance 等[4](https://doi.org/10.1109/TSE.2010.111)观察十名专业程序员调试真实开源程序，并以信息觅食（information foraging）分析其导航选择。代码中的名称、结构和邻近内容构成信息气味，开发者依据预期收益与访问成本决定下一步查看位置。参与者在缺少有效线索时更容易进入低收益路径。该研究支持把界面入口和跳转关系作为调试工具的核心设计变量。

Rasmussen 和 Jensen[5](https://doi.org/10.1080/00140137408931355)对电子设备故障排查的现场活动进行分析，发现排查者会在症状识别、假设形成、测试和操作之间循环。虽然研究对象早于现代软件系统，其观察揭示了复杂故障诊断的一项稳定特征：当前检查由已有假设引导，新的证据又会改变假设。工具需要保留这一循环所需的材料和上下文。

这些研究均以确定性较强的程序或设备为对象。工具调用型智能体的运行记录包含自然语言、概率性生成和外部工具状态，同一症状可能来自不同环节，相同配置也可能产生不同执行路径。传统调试研究提供了查找和推理活动的分析单位，但智能体情境中的具体困难仍需通过实践者研究重新识别。

#### 2.2 程序调试中的信息表征方式

Romero 等[6](https://doi.org/10.1016/j.ijhcs.2007.07.005)研究多表征（multiple representations）软件环境中的调试策略，让参与者在代码、输出及相关图形或文本表示之间完成任务。研究发现，表征知识和编程经验都与表现有关；经验较丰富的参与者能够随呈现方式调整策略。多视图只有在对应关系明确、使用者理解其编码方式时才能发挥作用。

Cornelissen 等[7](https://doi.org/10.1109/TSE.2010.47)开展受控实验，比较普通集成开发环境与加入执行轨迹可视化的环境。实验设置八类程序理解任务，结果显示轨迹可视化组完成任务的时间减少，答案正确性提高。该研究为执行历史的可视组织提供了量化证据，也说明评价需要落到具体理解任务上。

Ko 和 Myers 围绕面向问题的调试界面（Whyline）连续开展设计与评价。早期研究[8](https://doi.org/10.1145/985692.985712)把用户对程序行为的“为什么”和“为什么没有”问题转化为可选择的界面入口；后续研究[9](https://doi.org/10.1145/1368088.1368130)将方法扩展到更复杂程序；Java 版本研究[10](https://doi.org/10.1145/1518701.1518942)进一步评价从输出现象进入相关执行事件的效果。三项工作共同表明，问题导向的访问方式可以缩小搜索范围，使使用者围绕可观察现象检查执行原因。

Parnin 和 Orso[11](https://doi.org/10.1145/2001420.2001445)通过开发者任务研究考察自动故障定位结果怎样被使用。即使系统提供可疑语句排序，参与者仍需阅读上下文、理解程序行为并判断可疑位置与错误之间的关系。仅提高排序指标不能保证调试者获得相同收益。该发现对智能体自动归因同样适用：系统建议的步骤需要配套证据和上下文，评价也要记录使用者如何核验建议。

Khanna 等[12](https://doi.org/10.1145/3487065)评价人工智能事后审查流程（After-Action Review for AI，AAR/AI），让具有领域知识的参与者检查智能体表现。使用该流程的参与者发现了更多缺陷，定位也更精确。研究还观察到，对问题进行标注可能帮助参与者从单个错误抽象出更高层类别。该结果说明，结构化审查既能支持个案诊断，也可能支持跨案例知识积累。

程序调试研究显示，诊断同时涉及时间顺序、症状入口、关系访问、多种表征之间的对应和问题结构保存。现有证据主要来自代码和确定性执行，对自然语言内容、工具返回和控制规则混合构成的智能体轨迹缺少直接研究。

### 三、运行追踪与过程来源研究

#### 3.1 分布式系统运行追踪

复杂智能体与分布式系统都面临记录分散的问题。Fonseca 等[13](https://www.usenix.org/conference/nsdi-07/x-trace-pervasive-network-tracing-framework)提出跨层追踪框架（X-Trace），以任务标识关联跨协议和跨组件事件，并在多个部署场景中验证其可行性。研究的核心贡献是让同一任务触发的操作能够被重新组合成整体路径。

Sigelman 等[14](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/)总结谷歌分布式追踪基础设施（Dapper）的设计与两年部署经验。系统通过统一插桩、采样和跨服务标识，在控制开销的同时为开发和运维团队提供端到端调用信息。实践经验显示，追踪数据的价值依赖于稳定的上下文传播和可在其上构建的分析工具。

Mace 等[15](https://doi.org/10.1145/2815400.2815415)提出动态因果监控方法（Pivot Tracing），将动态插桩与先发生连接结合，使使用者能够在运行时提出跨组件查询。研究在异构 Hadoop 集群中评价原型，展示其识别软件缺陷、错误配置和硬件异常的能力。相比预先固定日志字段，这一方法允许诊断问题驱动后续观测。

三项研究为智能体运行记录提供了工程基础：事件必须具有稳定标识，跨步骤上下文需要显式传播，采集内容要能够支持后续关联，必要时还要允许补充观测。它们的评价重点是系统能力、开销与故障案例，较少研究开发者怎样阅读由此形成的记录。智能体界面的研究对象因此应包含采集结构与人的使用过程。

#### 3.2 可视分析中的过程来源

Ragan 等[16](https://doi.org/10.1109/TVCG.2015.2467551)系统整理可视化与数据分析中的过程来源（provenance），区分数据来源、操作历史、分析理由等记录类型，并归纳回忆、复现、协作和质量检查等用途。这一框架提示，智能体轨迹中的“系统执行历史”和“开发者诊断历史”属于不同层次，二者需要分别记录。

Kadivar 等[17](https://doi.org/10.1109/VAST.2009.5333020)开发分析过程记录系统（CzSaw），捕获使用者的交互步骤，以历史、脚本和依赖视图支持回放与修改。该工作展示了分析历史如何成为继续探索和比较备选路径的材料。其评价以系统展示和分析场景为主，尚不能说明何种历史表示能稳定改善诊断表现。

Xu 等[18](https://doi.org/10.1109/MCG.2015.50)提出面向意义建构（sensemaking）的分析过程来源研究议程，强调采集、可视化、协作使用和不确定性传播。作者区分操作记录与推理记录，并提出自动捕获与人工补充相结合的方向。对智能体诊断而言，点击轨迹反映材料访问过程，原因判断的形成依据还需要口语报告、答案和回访资料加以解释。

Sacha 等[19](https://doi.org/10.1109/TVCG.2015.2467591)分析可视分析中的不确定性、觉察和信任关系，指出不确定性会从数据来源、处理过程传播到视觉输出，使用者是否意识到这些不确定性会影响最终知识判断。Hullman[20](https://doi.org/10.1109/TVCG.2019.2934287)对可视化作者的研究发现，不确定性表达受到受众预期、传播目标和设计成本影响，作者可能因担心混淆或削弱信息而省略相关内容。两项研究说明，缺失记录、派生关系和模型生成摘要都需要清楚表达来源与限制。

过程来源研究提供了记录类型与用途的框架，其主要场景是数据分析。智能体故障诊断还包含发现关键事件、排除竞争解释和提出后续检查等实现任务。本研究据此将过程来源信息与诊断判断、证据使用和后续行动共同评价。

### 四、大语言模型与智能体开发工具研究

#### 4.1 大语言模型输出比较与智能体行为分析

Arawjo 等[21](https://doi.org/10.1145/3613904.3642016)开发提示与模型输出比较工具（ChainForge），开展二十一人的实验室研究，并通过六次访谈了解八名实际使用者的工作。参与者会根据任务目标选择比较标准，在探索性试验、有限范围评价和迭代改进之间转换。研究显示，比较视图的价值取决于使用者当时需要回答的问题。

van der Maden 等[22](https://doi.org/10.1145/3772318.3791069)访谈十九名大语言模型产品实践者，分析团队如何评价产品并把结果转化为改进。研究发现，团队即使拥有评价结果，也可能难以判断应该修改什么；评价数据、产品目标和行动责任之间缺少连接。该“结果—行动缺口”与故障诊断直接相关，输出异常、原因位置和后续操作构成连续的判断过程。

Lu 等[23](https://doi.org/10.1109/TVCG.2024.3394053)提出智能体行为可视分析系统（AgentLens），以层级时间结构和行为追踪支持自主智能体分析。作者结合应用案例与十四人对照研究，记录任务正确率、完成时间和访谈反馈。研究报告行为分析任务表现得到改善，同时观察到复杂分析仍要求一定技术知识。其任务侧重行为模式与涌现现象，对参数、状态和控制逻辑的实现诊断涉及较少。

Dibia 等[24](https://doi.org/10.18653/v1/2024.emnlp-demo.8)提出多智能体开发工具（AutoGen Studio），通过声明式配置、流程搭建、执行查看和组件复用支持原型开发与调试。论文总结了工具设计原则并提供使用案例，其评价主要来自部署使用和示例流程，缺少对诊断表现的受控比较。该工作证明开发与调试可以被整合到同一工具链，也暴露出需要用户研究验证的设计主张。

#### 4.2 交互调试与运行干预

Epperson 等[25](https://doi.org/10.1145/3706598.3713581)先访谈五名智能体开发者，再设计多智能体交互调试系统（AGDebugger）。系统支持查看消息、修改内容和重置执行。评价包括六人的错误识别比较和八人的交互干预研究。参与者偏好可编辑和可重置的界面，但决定修改位置、确定修改内容和判断修改效果仍有困难。研究说明，提供操作入口不能替代原因理解。

Hutter 和 Pradel[26](https://arxiv.org/abs/2602.06593)提出软件开发智能体分步调试工具（AgentStepper），把模型、智能体程序与工具交互组织为结构化会话，并提供断点、现场编辑和中间代码变化查看。十二名计算机专业学生与博士生参加分组任务研究，轨迹理解和实现缺陷识别任务呈现不同幅度的改善。样本以高校参与者为主，信息内容增加与组织方式变化同时发生，其适用条件仍需由实践者研究补充。

现有用户研究覆盖了输出比较、行为概览、消息检查和执行干预。研究样本通常较小，且常由学生或研究人员构成；任务聚焦单次识别或工具使用，较少追踪“异常发现—证据收集—原因判断—下一步检查”的完整过程。界面中加入更多信息后取得的改善，也难以直接归因于某一种组织方式。

#### 4.3 失败分类、自动归因与修复

Cemri 等[27](https://arxiv.org/abs/2503.13657)收集多智能体失败执行，通过轨迹标注归纳多智能体系统失败分类（Multi-Agent System Failure Taxonomy，MAST），覆盖系统设计、智能体间协调、验证与终止等问题。分类为跨案例比较提供了编码框架，也能帮助案例抽样覆盖不同故障环节。

Zhang 等[28](https://proceedings.mlr.press/v267/zhang25cq.html)建立失败归因基准（Who&When），以一百二十七个多智能体系统的失败日志评价责任智能体与关键步骤定位。最佳方法识别责任智能体的准确率为 53.5%，定位责任步骤的准确率为 14.2%。结果说明自动归因尚不足以直接代替人工诊断，界面需要支持使用者核验候选位置和相关证据。

Chen 等[29](https://arxiv.org/abs/2606.06324v2)研究智能体运行框架缺陷，提出连接数据流、控制流和实现位置的中间表征，并据此完成归因与修复。研究结合开源仓库开发记录与基准实验，展示由失败轨迹进入实现检查的技术路径。该方法的评价集中于自动修复结果，其中部分中间信息由模型生成；人如何理解和校验这些信息仍是开放问题。

失败分类、自动归因和修复研究能够为人机交互研究提供案例类型、候选关系和机器基线。开发者在证据不完备或候选原因冲突时的判断过程仍缺少实证材料。自动建议的界面应用还需要评价使用者的核验行为及高信心误诊风险。

### 五、解释工具与判断质量

#### 5.1 面向任务的解释需求

Miller[30](https://doi.org/10.1016/j.artint.2018.07.007)综合社会科学中的解释研究，指出人类解释通常具有选择性、对比性和社会性。该综述为解释形式提供理论依据。智能体诊断中的具体解释需求仍需根据开发者提出的问题和所需执行证据开展用户研究。

Liao 等[31](https://doi.org/10.1145/3313831.3376590)访谈二十名人工智能产品的用户体验与设计实践者，并以问题库作为研究探针，整理使用者可能询问的解释问题。研究发现，实践中的解释需求覆盖系统能力、具体输出原因、数据使用和改进方式，不同角色与任务关注的问题不同。对诊断工具而言，解释入口需要对应开发者的当前任务，固定的全局摘要难以覆盖全部需求。

Amershi 等[32](https://doi.org/10.1145/3290605.3300233)从既有资料汇总人智交互建议，经过多轮专家评价，并由四十九名设计实践者在二十个产品上验证，形成十八项设计指南。与本课题直接相关的内容包括说明系统能力、支持纠错、解释行为原因、传达用户操作后果和提供全局控制。该研究证明设计原则可以通过系统综述和跨产品评价形成，也提示原则需要在具体任务中检验适用性。

Wang 等[33](https://doi.org/10.1145/3290605.3300831)提出以用户目标和解释任务组织可解释人工智能设计，强调解释设计应明确使用者、使用情境和预期行为。Abdul 等[34](https://doi.org/10.1145/3173574.3174156)通过文献分析梳理可解释与可问责系统的人机交互研究轨迹，指出大量工作偏重算法与模型，人的理解和实际使用证据不足。两项研究共同支持以诊断任务为中心选择理论和变量。

#### 5.2 解释使用与判断质量

Kaur 等[35](https://doi.org/10.1145/3313831.3376219)通过十一名数据科学家的情境调查和一百九十七人的问卷研究专业使用者如何使用机器学习解释工具。参与者可能误读图形，也可能在理解不足时信任解释。研究表明，可用性评价、主观信任和理解正确性应分别测量。

Buçinca 等[36](https://doi.org/10.1145/3449287)开展一百九十九人的实验，比较三种认知促发设计、简单解释条件与无人工智能条件。要求参与者在查看建议前作出初步判断等设计降低了对错误建议的过度依赖，却获得较低的主观评价，且效果受到认知动机影响。该结果说明，增加核验步骤可能改善判断质量并提高操作成本，实验需要同时测量收益与代价。

Sieker 等[37](https://doi.org/10.18653/v1/2024.emnlp-main.1084)研究解释对视觉问答系统心智模型的影响，发现使用者对自身理解的感受与实际能力可能不一致。解释能够提升“觉得自己理解”的程度，却未必形成准确心智模型。这一发现直接支持在诊断实验中加入原因说明、证据引用和迁移任务。

Ehsan 等[38](https://doi.org/10.1145/3411764.3445188)访谈组织中的人工智能使用者，提出社会透明度（social transparency）视角，把“谁在何种情境下对系统作出过什么判断”纳入解释。其结果说明，专业判断不仅依赖模型信息，还依赖组织经验与既有处置。Ehsan 等[39](https://doi.org/10.1145/3637396)随后通过四十三名参与者的情境式协同设计研究接缝显化的可解释人工智能（Seamful XAI），探索怎样呈现系统边界与不完备性以支持质疑和行动。两项工作拓展了解释内容的范围，但其设计主张仍需在真实诊断任务中评价。

解释研究对本课题形成三项方法要求。第一，记录参与者结论所引用的具体证据。第二，把诊断正确性、信心、任务负担和主观偏好分开测量。第三，设置材料不足与自动建议错误的案例，观察使用者能否识别结论边界。这样才能判断界面是在支持核验，还是仅提升了表面上的可理解感。

### 六、意义建构理论及其研究应用

Klein 等[40](https://doi.org/10.1109/MIS.2006.88)比较多种意义建构研究传统，指出人在信息模糊、矛盾或超出预期时需要形成并修正解释。Klein 等[41](https://doi.org/10.1109/MIS.2006.100)进一步提出数据—框架循环，描述人怎样以既有框架寻找数据，又怎样根据新数据调整框架。Klein 等[42](https://doi.org/10.1017/CBO9780511612062.006)在数据—框架理论中将活动细化为构建、质疑、比较和重构框架。

Pirolli 和 Card[43](https://www.e-education.psu.edu/geog885/sites/www.e-education.psu.edu.geog885/files/geog885q/file/Lesson_02/Sensemaking_206_Camera_Ready_Paper.pdf)通过认知任务分析提出意义建构的过程模型，将信息搜寻、信息组织、结构形成和呈现联系起来。该模型常用于解释分析者如何从大量材料形成可交流的判断。

意义建构可以描述智能体诊断中的动态活动：开发者从失败现象形成初步解释，依据解释查找运行材料，再用新材料确认、区分或修正原因。本课题以其组织访谈编码和过程指标，包括初始框架、证据搜寻、竞争解释与框架修正。界面形式依据形成性研究资料和方案比较确定。

### 七、设计研究中的知识形成

Zimmerman 等[44](https://doi.org/10.1145/1240624.1240704)将通过设计开展研究（research through design）界定为以设计实践生成研究知识的方法，强调设计产物、研究过程和知识主张之间的联系。Höök 和 Löwgren[45](https://doi.org/10.1145/2362364.2362371)提出中层知识（intermediate-level knowledge）与强概念（strong concepts），用于表达高于单个作品、又能够指导设计实践的知识形式。

Sedlmair 等[46](https://doi.org/10.1109/TVCG.2012.213)总结可视化设计研究的方法，强调问题理解、与领域人员协作、方案形成、评价和反思之间的连续关系。Meyer 和 Dykes[47](https://doi.org/10.1109/TVCG.2019.2934539)提出设计研究严谨性标准，要求研究说明证据来源、设计选择、评价过程与研究者反思。这些方法适合约束本课题的知识提炼过程。

定性研究的样本与分析也需要明确依据。Malterud 等[48](https://doi.org/10.1177/1049732315617444)提出信息力（information power），主张样本量取决于研究目标、样本特异性、理论使用、对话质量和分析策略。Gale 等[49](https://doi.org/10.1186/1471-2288-13-117)介绍框架分析法（framework method），通过逐案与跨案矩阵保持原始材料、编码和主题之间的可追溯关系。两项方法为本课题的招募停止、跨案例比较和审计记录提供操作依据。

本课题可能形成的知识位于中层层级：描述一类诊断情境中的共同困难，提出相应的信息组织与交互原则，并通过任务评价说明这些原则的作用条件和代价。原型是产生和检验知识的研究工具。知识主张应能够追溯到形成性研究、设计比较和评价结果，也应明确适用的智能体类型、故障结构和使用者经验范围。

### 八、现有研究述评

现有研究已经提供四组相互补充的证据。程序调试研究说明，开发者需要从症状出发搜寻、关联和保存材料；分布式追踪与过程来源研究说明，跨组件标识、因果关联、历史回放和信息来源是组织复杂执行记录的基础；智能体工具研究提供输出比较、行为概览、消息检查、执行修改和自动归因方法；解释研究证明主观信任与实际理解可能分离，界面需要支持核验和边界判断。

仍有三项证据缺口。第一，缺少对具有实际智能体开发经验者的完整诊断过程研究，尚不清楚困难出现在哪些活动、信息条件和故障结构中。第二，现有工具通常同时改变信息数量、组织方式和交互能力，难以判断核心设计作用于查找、关联、假设比较还是后续检查。第三，自动归因与解释可能带来高信心错误，现有评价较少要求参与者引用证据并识别材料不足。

因此，本研究以工具调用型大语言模型智能体的失败执行为对象，研究开发者从失败现象形成可核验诊断判断的过程。研究先通过关键事件访谈和任务观察识别跨案例困难，再围绕一个核心困难比较信息表征与交互方案，最后以对照任务和新案例检验设计作用及适用范围。预期成果包括诊断活动与信息条件的经验描述，以及具有证据链和适用条件的设计原则。

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
