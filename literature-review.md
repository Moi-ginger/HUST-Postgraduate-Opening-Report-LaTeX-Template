# 文献综述

**工具调用型大语言模型智能体故障诊断的信息表征与交互设计研究**

## 一、研究背景与文献范围

### 1.1 从任务执行到故障诊断

大语言模型（large language model，LLM）能够根据自然语言目标生成操作方案，并通过工具调用访问外部数据、执行计算和改变环境状态。Yao 等[1](https://arxiv.org/abs/2210.03629)提出的推理与行动协同方法（ReAct）将语言推理与环境操作组织为交替进行的任务过程，为大语言模型智能体（large language model agent）的研究提供了一种基本实现方式。一个任务的结果由多次模型输出、工具返回和状态更新共同形成，其失败原因也可能分布在这些环节之中。

工具调用型智能体的开发者需要解释运行过程中的偏差。例如，最终回答使用了错误数据，可能涉及检索参数、工具返回、上下文保留或模型对材料的解释；工具调用持续重复，可能涉及失败恢复、状态更新或结束条件。诊断需要将最终症状与相关运行事件联系起来，再通过比较、补充检查或重新执行检验原因判断。本课题关注的信息表征，是运行事件及其属性、关系和来源在界面中的组织与呈现；交互设计则涉及开发者如何进入、查找、比较和核验这些材料。

国内人机交互研究为这一问题提供了学科背景。范俊君等[2](https://doi.org/10.1360/N112017-00221)讨论了智能时代交互模型、界面与设计原则的发展，强调人的能力与机器能力在交互中的结合；许为、葛列众[3](https://doi.org/10.3724/SP.J.1042.2020.01409)将人机合作、决策控制和以人为中心的人工智能纳入工程心理学研究框架。这些工作提出了研究方向。具体到智能体排错，仍需通过开发者的实际诊断行为，说明界面应支持什么活动，以及设计效果如何被观察和评价。

### 1.2 综述的组织与证据类型

本综述围绕“开发者怎样利用运行信息形成并检验故障判断”组织文献，检索与核验范围包括计算机协会数字图书馆、计算语言学协会文献库、主要计算机系统会议论文集、期刊官网、作者机构存档及预印本平台，文献更新至2026年9月22日。检索主题包括程序调试行为、智能体调试、运行追踪、分析过程记录、可解释人工智能、意义建构及交互设计研究方法，并结合核心论文的前向与后向引用补充相关研究。

纳入文献承担三类作用。开发者观察、访谈和用户实验用于说明人的活动、困难及设计效果；系统论文与自动归因评测用于说明可获得的数据、技术能力和故障分析方法；理论与方法文献用于建立分析视角和研究程序。综述分别说明各类研究的对象和评价方式，以便判断结论能够支持的范围。近期预印本保留版本信息，其结论结合样本、任务和评价条件使用。

## 二、开发者如何理解和诊断异常行为

### 2.1 从可疑位置搜索到原因判断

程序调试研究较早就把搜索位置与理解原因作为两个相互联系的活动。Katz 和 Anderson[4](https://doi.org/10.1207/s15327051hci0304_2)通过四项程序调试实验分析学习者的缺陷定位策略，发现搜索策略会影响检查路径，而定位到某一位置之后，仍然需要判断局部行为是否正确。该研究的对象是程序学习者，其价值在于把“查到哪里”和“如何判断”分开考察。对于智能体运行记录，快速到达一次异常调用只是诊断过程的一部分，开发者还需解释该调用与任务失败之间的联系。

Ko 等[5](https://doi.org/10.1109/TSE.2006.116)观察十名开发者完成软件维护任务，将其活动概括为查找、关联和收集相关信息。开发者需要在代码位置、依赖关系和临时收集的材料之间往返，信息线索不足及导航成本会妨碍理解。研究提示，材料分散所造成的问题既包括访问成本，也包括已经发现的内容难以在后续推理中保持可用。智能体轨迹中的提示、参数、工具返回和状态快照同样可能需要被联合查看，这一共同点构成可进一步检验的研究起点。

Lawrance 等[6](https://doi.org/10.1109/TSE.2010.111)以信息觅食（information foraging）视角分析专业程序员的调试行为，研究信息线索、预期价值和获取成本如何影响下一步搜索。其解释重点在于开发者为何沿某条路径继续查找，以及什么时候离开当前材料。由此可将界面中的标签、摘要和跳转关系视为影响搜索决策的具体设计因素，并观察它们是否把使用者引向相关材料。一个醒目的错误标签可能有助于定位，也可能使使用者过早集中于末端症状；效果取决于标签与诊断任务的关系。

这些研究共同建立了一组可观察的行为：进入材料、选择线索、建立关联、保留发现和判断原因。相应的评价需要同时记录搜索过程与诊断结果。访问事件数量较少可能意味着导航高效，也可能意味着调查过早结束；停留时间较长可能来自困难，也可能来自必要的核验。行为数据需要与参与者当时的问题及最终判断结合分析。

### 2.2 系统理解、经验与困惑

Starr 和 Storey[7](https://doi.org/10.1145/3800945)通过对二十七名专业开发者的访谈，运用建构主义扎根理论（constructivist grounded theory）研究排错中的认知经历。他们将理解异常行为的过程与困惑、心理模型构建以及认知疲劳联系起来。研究说明，开发者的困难可以来自对系统行为缺乏连贯解释，即使相关技术信息已经存在，也仍需将其组织为能够指导下一步检查的理解。

这一发现对研究对象的选择具有直接影响。熟悉自身系统的开发者可能知道哪些行为值得怀疑，而首次接触某个框架的参与者还需要学习其正常运行方式。两类任务同时包含诊断，但前置理解成本有明显差异。研究应记录参与者的编程经验、智能体开发经验和案例熟悉程度，并为正式任务提供必要的系统背景。否则，观察到的界面差异可能主要反映学习陌生系统的难度。

经验也会影响多种表征的使用。Romero 等[8](https://doi.org/10.1016/j.ijhcs.2007.07.005)研究多表征软件环境中的调试策略，发现表征使用与编程经验、表征知识及具体任务有关。由此可见，关系图、代码和输出窗口之间的协调本身就是需要学习的操作。为智能体增加更多视图之前，应识别开发者需要联合判断的对象、已有知识以及视图切换的代价。

### 2.3 自动定位结果如何进入人的诊断

Parnin 和 Orso[9](https://doi.org/10.1145/2001420.2001445)通过用户研究考察自动故障定位技术对程序员的实际帮助，指出提供可疑代码排序之后，开发者仍需要上下文才能理解和修复问题。该研究把算法提供的线索与人完成的诊断工作联系起来，也表明评价自动定位工具时，需要观察使用者能否把提示转化为可执行的检查。

在工具调用型智能体中，自动生成的原因解释同样只是诊断输入之一。开发者可能需要检查建议引用的运行事件、比较其他解释，或判断现有记录是否足够。因此，本课题可将“取得线索—解释异常—检验判断”作为初步观察线索，再由实际材料修订。尚需通过经验研究确认的，是这些活动在智能体任务中怎样连接，哪些环节最易受运行信息组织方式影响。

## 三、大语言模型开发与智能体协作的实证研究

### 3.1 生成结果的理解与评价

Barke 等[10](https://doi.org/10.1145/3586030)观察二十名程序员使用代码生成工具，并通过扎根分析描述加速既定实现和探索可能方案两种交互方式。当开发者已有明确意图时，生成结果可以加快实现；当其探索陌生任务时，需要通过阅读、试用和修改来建立理解。该研究提示，人使用生成系统的目标和知识状态会改变其信息需要。

Zamfirescu-Pereira 等[11](https://doi.org/10.1145/3544548.3581388)研究非人工智能专家设计提示的过程，发现参与者会基于有限输出进行机会式修改，并将日常人际交流经验带入对模型的判断。研究对象主要是非专家提示设计者，其发现可用于提醒研究者关注评价依据的充分性。在专业开发者群体中，是否存在类似的局部试验和过早概括，需要结合实际开发任务重新观察。

van der Maden 等[12](https://doi.org/10.1145/3772318.3791069)访谈十九名大语言模型产品实践者，分析评价工作如何连接产品改进。研究揭示，发现质量问题、解释问题来源和决定采取何种修改之间存在可行动性缺口。对本课题而言，这一结果把研究焦点推进到评价之后：使用者已经知道某次运行失败，却可能缺乏将失败转化为诊断和修复决策的支持。

以上研究分别涉及代码生成、提示设计和产品评价，共同指向一种持续存在的工作：使用者需要判断生成结果的含义及其对下一步行动的影响。智能体增加了多步骤执行和外部工具反馈，因此需要进一步研究，开发者究竟依据哪些事件建立解释，如何排除相似原因，以及何时决定补充观测。

### 3.2 开发者与编程智能体的实际协作

Kumar 等[13](https://arxiv.org/abs/2506.12347v3)研究十九名开发者与编程智能体协作处理三十三个真实仓库问题的过程。参与者处理自己曾贡献过的仓库任务，研究观察到增量交互、主动干预和持续评价在协作中的作用。该研究将人类参与放在真实开发工作中考察，提供了比单纯任务成功率更细致的过程资料。其观察性设计能够揭示行为模式及关联，具体交互方式的因果效果还需要控制条件下的比较。

这类现场研究也揭示了实验材料设计的重要性。真实问题包含任务意图、仓库约束和已有知识，单一的人工报错很难覆盖这些条件。在智能体诊断研究中，可通过真实事件回溯提取具有代表性的困难，再用可复现系统构造能够保持这些困难的任务。案例的真实性应体现在事件关系、合理歧义和诊断行动之中。

### 3.3 智能体过程展示与使用者理解

Pareek 等[14](https://doi.org/10.1145/3772318.3791157)结合文献分析与实验室研究，考察使用者如何解读多智能体界面中的透明性和可信赖性线索。研究让十二名参与者使用五种界面完成信息查找与逻辑推理任务，并通过访谈和卡片排序了解其对透明性、帮助程度和可靠性的判断。其结果关注过程展示如何进入使用者对系统的理解和评价，为运行信息的呈现提供了经验材料。

该研究同时明确了本课题需要进一步测量的内容：透明性感受、可信赖性感受与具体故障判断属于不同的评价对象。开发者可能认为界面解释充分，却仍未识别造成失败的条件；也可能在确认信息缺失后降低信心，形成更符合材料的判断。诊断界面的主要效果应通过任务表现和证据使用来评价，主观感受用于解释接受程度和使用体验。

## 四、支持诊断的信息表征与交互工具

### 4.1 执行轨迹与面向问题的导航

Cornelissen 等[15](https://doi.org/10.1109/TSE.2010.47)通过受控实验研究执行轨迹可视化对程序理解的影响，在其任务设置下观察到正确性和完成时间方面的改善。实验支持了运行过程表征对程序理解的价值，也表明效果需要与特定理解任务相联系。轨迹可视化应帮助使用者回答某些问题，例如某个对象如何被创建、一个行为由哪些调用触发，而其整体视觉复杂度本身不能说明诊断价值。

Ko 和 Myers[16](https://doi.org/10.1145/1518701.1518942)开发面向原因问答的调试界面（Whyline），让开发者从可见程序输出提出“为什么发生”与“为什么没有发生”的问题，再进入相关执行事件。该工作的设计贡献在于连接使用者的问题与系统记录中的可回答材料。对智能体而言，任务失败常以自然语言结果或外部操作表现出来，是否能够建立从症状到相关记录的有效入口，是值得研究的设计问题。

两项研究采用的执行记录和程序语义较为明确。智能体事件可能包含模型生成的解释、工具返回和不完整上下文，界面需要进一步说明链接关系来自调用结构、实际数据传递，还是分析工具的推断。可以在设计中借鉴面向问题的入口与关系导航，但具体关系的依据应成为研究材料的一部分。

### 4.2 结构化复盘与输出比较

Khanna 等[17](https://doi.org/10.1145/3487065)通过人工智能复盘工具（AAR/AI）的实证研究，考察结构化反思如何帮助使用者发现人工智能系统的缺陷。研究将相同解释材料置于不同组织条件下，以“发生了什么、为什么、需要改变什么”等问题支持复盘，并测量故障回忆和描述。结果为信息组织方式影响缺陷理解提供了证据。其研究对象和任务具有特定背景，应用于大语言模型智能体时，需要检验结构化问题是否符合开发者的诊断活动。

Arawjo 等[18](https://doi.org/10.1145/3613904.3642016)提出提示与输出比较工具（ChainForge），通过可视化流程支持提示、模型和输入的组合试验。其评价包括二十一人的实验室研究，以及六次涉及八名使用者的访谈，揭示了工具在输出探索、假设检验和评价迭代中的使用方式。该工作说明，将多个输出放在可比较的结构中，可以支持对模型行为的考察。

上述研究分别强调复盘的组织方式和比较的操作空间。对于一次智能体失败，比较对象可以是预期与实际参数、成功与失败运行、修改前后的状态，或两种原因解释所依赖的事件。选择哪一种比较，取决于诊断任务中实际存在的判断困难。研究需要观察比较是否帮助使用者发现关键差异，以及是否引入额外的信息筛选成本。

### 4.3 智能体行为的层级呈现

Lu 等[19](https://doi.org/10.1109/TVCG.2024.3394053)提出智能体行为可视分析系统（AgentLens），通过层级结构和多粒度时间信息支持对自主智能体行为的探索。论文报告了使用案例和十四名参与者的用户研究，体现了从概览进入局部行为的设计价值。该系统主要处理行为分析问题，研究材料能够说明使用者如何理解复杂运行过程；其结果还需要结合具体故障答案，才能支持关于诊断正确性的结论。

Gao 等[20](https://aclanthology.org/2026.acl-demo.29/)提出科学智能体执行轨迹可视化工具（Graph of Trace），将运行过程组织为可交互的事件图，并请相关领域专家评价系统。专家反馈提供了可理解性和使用价值方面的证据。科学任务中，领域知识会影响对中间结果的解释，工具对专业使用者的帮助需要结合其任务背景理解。

这些工作展示了概览、分层和关系连接的可行实现。对故障诊断而言，还需进一步区分几类连接：时间先后、调用包含、数据依赖和原因假设。若不同关系在视觉上被赋予相同含义，使用者可能把“先发生”理解为“导致了”。本课题因此需要把关系语义的理解纳入观察和评价，同时记录使用者怎样从整体运行进入需要检查的局部材料。

### 4.4 可编辑执行与交互调试

Dibia 等[21](https://doi.org/10.18653/v1/2024.emnlp-demo.8)提出多智能体开发工具（AutoGen Studio），整合组件配置、执行过程查看和调试功能。该系统论文展示了开发流程与工具能力，为案例组织和基础界面提供了参考。其部署经验有助于识别常见操作需求，具体设计对人的诊断效果仍需相应用户任务数据。

Epperson 等[22](https://doi.org/10.1145/3706598.3713581)通过五名开发者的形成性访谈提出交互调试工具（AGDebugger），随后分别开展诊断和运行引导研究。诊断研究涉及六名参与者，运行引导研究涉及八名参与者。参与者对编辑、重置和局部重执行等功能表现出偏好，但研究也记录了判断修改位置和修改方式的困难。两部分研究说明，提供操作能力之后，使用者仍需建立足以指导操作的理解。

Rorseth 等[23](https://doi.org/10.48786/EDBT.2025.94)提出面向数据应用的智能体调试器（LADYBUG），展示逐步追踪、局部干预及受影响环节重新执行的实现。Hutter 和 Pradel[24](https://arxiv.org/abs/2602.06593)提出软件开发智能体调试器（AgentStepper），提供暂停、检查和编辑等功能，并报告小规模学生参与者研究。前者属于系统演示，后者提供了初步任务评价；它们共同扩展了交互调试的实现空间，专业开发者在多类故障上的使用效果仍值得进一步检验。

局部重执行可以成为核验假设的手段，但修改多个条件、随机生成差异和外部环境变化都会影响解释。诊断研究应记录干预内容、保持条件和结果变化，使使用者能够判断一次成功是否支持此前的原因解释。若课题聚焦静态材料中的理解与判断，可首先研究查找、关联和比较；是否纳入运行干预，应由形成性研究确认其必要性。

### 4.5 现有工具证据的综合比较

| 研究 | 主要研究对象与方法 | 已提供的证据 | 对本课题仍需检验的内容 |
| --- | --- | --- | --- |
| Whyline[16](https://doi.org/10.1145/1518701.1518942) | 程序输出原因查询与用户任务评价 | 问题入口与执行事件连接的价值 | 自然语言记录及不完整观测中的关系理解 |
| AAR/AI[17](https://doi.org/10.1145/3487065) | 结构化复盘的对照研究 | 相同解释材料的组织方式影响缺陷描述 | 结构化复盘在专业智能体排错中的作用 |
| ChainForge[18](https://doi.org/10.1145/3613904.3642016) | 实验室研究与实际使用访谈 | 输出比较、假设检验和评价迭代的使用方式 | 跨步骤故障解释与下一步检查 |
| AgentLens[19](https://doi.org/10.1109/TVCG.2024.3394053) | 使用案例与用户研究 | 层级轨迹支持复杂行为探索 | 诊断正确性、原因判断及证据使用 |
| AGDebugger[22](https://doi.org/10.1145/3706598.3713581) | 开发者访谈、诊断与运行引导研究 | 编辑和重执行的需求及使用困难 | 哪种信息支持使用者选择干预位置 |
| AgentStepper[24](https://arxiv.org/abs/2602.06593) | 小规模任务研究 | 单步检查与编辑的初步可用性证据 | 经验差异及多类案例上的效果 |
| Graph of Trace[20](https://aclanthology.org/2026.acl-demo.29/) | 科学智能体案例与专家评价 | 事件图的可理解性与使用价值 | 主观理解和客观诊断表现之间的关系 |

现有研究已经提供了丰富的设计资源。进一步的研究任务是选择一项与开发者困难对应的设计主张，明确它改变的内容，并通过可比较的任务检验其效果。单个原型可以同时提供多种功能，但知识贡献需要能够说明，哪些设计选择在什么情况下发挥了作用。

## 五、运行追踪、自动归因与诊断材料

### 5.1 分散事件的采集与关联

分布式追踪（distributed tracing）研究为跨组件运行信息的关联提供了技术基础。Fonseca 等[25](https://www.usenix.org/conference/nsdi-07/x-trace-pervasive-network-tracing-framework)提出跨层任务追踪框架（X-Trace），通过传播任务信息重建请求经过的组件与操作。Sigelman 等[26](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/)总结大规模追踪基础设施（Dapper）的部署经验，讨论追踪开销、采样及跨服务关联。Mace 等[27](https://doi.org/10.1145/2815400.2815415)提出动态因果监测系统（Pivot Tracing），通过动态插桩和查询支持跨组件分析。这些工作说明，统一标识与关系记录能够将分散事件组织为可查询的执行过程。

对智能体研究而言，这些成果首先影响案例材料能否回答诊断问题。若工具参数、返回值与后续模型输入之间缺乏对应关系，界面只能展示相邻事件；若保留了数据传递关系，则能够支持更具体的检查。设计研究应先列出任务所需材料，再核查记录能力。记录无法支持的关系需要通过补充观测获得，或在界面中标明其推断性质。

Zheng 等[28](https://arxiv.org/abs/2508.02736v2)提出系统级智能体观测工具（AgentSight），关联模型交互与底层系统活动，并在异常行为和性能分析场景中展示其作用。该研究补充了应用层对话记录之外的信息来源。采集层级的扩展能够帮助解释某些运行问题，同时也会增加材料种类；开发者怎样选择和组合这些信息，仍然是交互研究需要回答的问题。

### 5.2 故障分类与自动责任归因

Cemri 等[29](https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html)分析多智能体系统的失败运行并建立分类，涉及系统设计、智能体间协调以及任务验证等问题。该分类有助于理解智能体失败并不限于单次模型输出，也可作为案例采样的参考。多智能体协作中的协调和责任分配包含额外变量，因此借鉴其故障类型时，应逐项判断是否适用于单个工具调用型智能体。

Zhang 等[30](https://proceedings.mlr.press/v267/zhang25cq.html)围绕“哪个智能体在何时导致失败”构建自动失败归因任务，并比较不同归因方法。研究表明，在已有轨迹中定位责任主体和责任步骤仍具有挑战。这类评测回答机器方法能否接近标注答案；对于人使用诊断工具的研究，还需检查参与者是否理解建议依据、是否能够识别错误建议，以及是否会把局部责任步骤视为完整原因。

Chen 等[31](https://arxiv.org/abs/2606.06324v2)研究智能体运行框架缺陷的诊断和修复，将失败轨迹与数据流、控制流及实现位置联系起来。研究提供了从运行表现追查框架问题的技术路径，其评价重点是自动诊断和修复。轨迹与实现的关联可以成为界面候选功能，但其必要性需要根据开发者的具体任务判断：有些问题可以在工具输入输出层面解释，有些则需要继续进入配置或实现细节。

上述研究对本课题的主要作用有两点。第一，辅助构建故障案例，避免只选择明显报错或单一错误类型。第二，明确自动建议的来源、可靠性和可检查性。研究中若使用自动归因结果，应保存模型、输入与生成版本，并将其与原始运行事实区分，便于分析使用者何时接受、质疑或放弃建议。

### 5.3 图结构的语义与可核验性

Wu 等[32](https://doi.org/10.1609/aaai.v40i48.42393)提出轨迹转图分析平台（AgentGraph），将智能体、任务、工具、输入输出和人工干预组织为具有类型的节点与关系，并将图元素链接到原始轨迹片段。系统还展示了失败分析和扰动测试。该工作说明，图结构可以同时承载运行对象、关联信息和原始出处。

在故障诊断中，图是否有帮助取决于其关系是否可理解，以及使用者能否据此完成检查。调用关系、数据使用关系和自动生成的原因关系具有不同依据。来源标识、关系说明和返回原始材料的操作，因而构成值得比较的设计因素。图的完整程度也需要服从任务要求：过多无关关系可能增加查找成本，过度压缩则可能隐藏判断所需的条件。

### 5.4 分析历史与推理依据

来源追溯（provenance）研究关注数据与分析结果从何而来。Ragan 等[33](https://doi.org/10.1109/TVCG.2015.2467551)提出可视化和数据分析中的来源类型与用途框架，区分数据、操作、交互、洞见和理由等记录。该区分提示，智能体执行历史与开发者的分析历史承担不同作用：前者描述系统发生的事件，后者描述使用者如何形成判断。研究过程需要同时保留两者，才能将界面操作与诊断解释联系起来。

Kadivar 等[34](https://doi.org/10.1109/VAST.2009.5333020)提出可编辑和可回放分析历史的可视分析系统（CzSaw），支持使用者回顾、调整和复用分析过程。Xu 等[35](https://doi.org/10.1109/MCG.2015.50)进一步讨论分析来源如何服务于理解、审计和协作，并提出将操作记录与推理活动连接的研究议程。这些工作为记录已检查材料、保留暂定假设和比较分析分支提供了设计资源。

对本课题而言，执行记录与分析记录的结合也关系到研究数据的解释。屏幕上出现某条日志不能证明参与者已经使用它；一次点击也不能直接表示接受了某种解释。研究需要在适当时点采集参与者的判断和理由，再与操作记录对应。通过这种方式，可以分析某项设计是否帮助发现了关键材料，还是仅改变了浏览方式。

## 六、解释、透明性与判断质量

### 6.1 解释需求来自任务和角色

可解释人工智能（explainable artificial intelligence，XAI）研究将解释放在人使用系统的情境中考察。Liao 等[36](https://doi.org/10.1145/3313831.3376590)访谈二十名相关设计实践者，并借助问题提示讨论解释需求，形成面向用户问题的设计资源。研究显示，使用者需要的解释与其角色、任务及所处环节有关。对开发者而言，解释可能用于理解一次失败、选择修改位置或决定是否需要更多观测，这些用途对应不同的信息要求。

Ehsan 等[37](https://doi.org/10.1145/3411764.3445188)以情境化设计材料访谈二十九名人工智能使用者与实践者，研究社会透明性（social transparency），将其他人的使用情境、行动和结果纳入解释。该研究揭示，解释需求可以扩展到技术输出之外的工作背景。公司中的智能体诊断也可能涉及配置责任、已尝试的修改和历史处理经验，这些内容适合在事件回溯中调查，再根据研究范围决定是否进入原型。

这类研究的启示是，形成性研究应从具体诊断事件提问。例如，参与者当时试图确认什么，哪些材料影响了判断，以及最终凭什么采取行动。单纯询问“希望界面有什么功能”容易获得脱离任务的偏好，具体事件则更有利于发现信息、解释和行动之间的关系。

### 6.2 解释的可用性与正确使用

Kaur 等[38](https://doi.org/10.1145/3313831.3376219)结合十一名数据科学家的情境研究与一百九十七人的调查，考察解释工具在机器学习分析中的实际使用。研究观察到使用者可能误解或过度依赖解释结果。该发现表明，解释功能的存在、使用者的熟悉程度和解释的正确运用之间，需要经验性检验。

Buçinca 等[39](https://doi.org/10.1145/3449287)在一百九十九名参与者的人工智能辅助决策实验中比较多种交互条件，发现促使使用者独立思考的认知强制措施（cognitive forcing functions）可以减少对错误建议的过度依赖，但也伴随接受度和使用成本方面的变化。研究说明，提高判断质量可能需要增加必要的核验活动；界面偏好、操作时间和正确性应分别测量。

Sieker 等[40](https://doi.org/10.18653/v1/2024.emnlp-main.1084)在视觉问答任务中操纵系统可见的图像信息，考察解释是否帮助使用者理解系统能力与局限。研究中，提供解释提高了使用者对系统能力的评价，却未帮助其更准确地识别系统限制。使用者是否感觉“理解了”，需要与其能否识别系统限制及错误结果一起评价。

三项研究支持本课题在实验中区分任务表现、证据使用和信心。一个清晰的摘要可能加快作答，却使参与者忽略反例；一个补充检查入口可能增加时间，但提高对原因的辨别能力。研究应先确定主要诊断目标，再解释各指标之间的变化，不能用满意度概括全部效果。

### 6.3 不确定性如何被表达和使用

Hullman[41](https://doi.org/10.1109/TVCG.2019.2934287)调查九十名可视化作者并访谈十三名设计者，研究实际传播中为何常省略不确定性。其结果揭示了信息简洁性、沟通目标、受众预期和表达成本之间的张力。研究对象是可视化作者，结论主要解释不确定性表达的实践选择，对诊断工具的启示是需要调查哪些不确定性真正影响后续检查，以及怎样以可使用的方式呈现。

Guo 等[42](https://doi.org/10.1109/TVCG.2015.2424872)通过用户实验比较图边不确定性与其他边属性的配对视觉编码，发现编码效果受到视觉变量组合和任务类型影响。这一结果说明，透明度、模糊或线型等表现方式需要在具体任务中验证。若智能体界面使用虚线表示推断关系，需要检查使用者是否理解这种含义、是否能区分数据缺失和关系不确定，以及是否会错误理解其强弱。

Sacha 等[43](https://doi.org/10.1109/TVCG.2015.2467591)从可视分析过程讨论不确定性、意识与信任的关系，为分析不确定性在处理和理解环节中的传播提供概念框架。Ehsan 等[44](https://doi.org/10.1145/3637396)通过四十三名参与者的情境化协同设计，研究如何在解释中显露系统接缝、限制和工作条件。前者提供分析视角，后者提供设计探索的经验材料，共同支持把系统限制作为可供判断的信息。

在智能体诊断中，至少需要区分三类情况：运行事实已被记录，但含义尚有争议；关键事实缺失，现有记录无法区分多个原因；工具生成了原因建议，但其正确性尚未核验。三类情况所需的行动分别可能是比较解释、补充观测和检查建议依据。这一划分是本课题的初步分析工具，其适用性还需通过参与者任务资料修订。

## 七、从诊断活动到可复用设计知识

### 7.1 意义建构的解释作用

意义建构（sensemaking）关注人如何把分散信息组织为能够理解情境和指导行动的解释。Pirolli 和 Card[45](https://www.e-education.psu.edu/geog885/sites/www.e-education.psu.edu.geog885/files/geog885q/file/Lesson_02/Sensemaking_206_Camera_Ready_Paper.pdf)基于认知任务分析与口语报告，描述情报分析中的信息搜集和解释形成活动，并讨论技术介入的位置。其研究提供了从材料选择到解释形成的过程视角，但具体活动结构需要结合智能体诊断资料确定。

Klein 等[46](https://doi.org/10.1109/MIS.2006.100)提出的宏观认知模型强调资料与解释框架之间的相互作用：已有理解影响人注意哪些信息，新信息又可能促使人保留、补充或调整理解。这个视角适合用于分析诊断中原因假设如何改变。例如，开发者最初怀疑工具返回错误，在发现返回内容正确后，可能转而检查状态传递。分析重点应落在触发判断变化的材料和行动上。

Dritsa 和 Houben[47](https://doi.org/10.1145/3685268)通过设计研究者使用健康相关数据可视化的经验研究，提出关注不确定性的意义建构模型，讨论数据、表征和使用者背景如何影响洞见形成。该工作展示了从具体实践资料修订过程描述的路径，也说明意义建构模型的价值来自其对特定活动的解释能力。

本课题可据此观察假设提出、材料选择、解释修订和后续检查，但不预先规定参与者必须经历固定阶段。若形成性研究发现主要困难集中在访问成本或术语理解，信息觅食和任务分析可能提供更直接的解释；若反复出现假设维持与修订问题，意义建构视角可用于组织过程资料。理论的选择应服务于已经观察到的现象。

### 7.2 设计原则如何获得经验支持

Amershi 等[48](https://doi.org/10.1145/3290605.3300233)通过多轮形成、评议和验证提出十八条人机交互指南，评价涉及四十九名设计实践者和二十种产品。该研究展示了通用指导如何通过多种产品和使用情境检验其清晰性与适用性。原则的价值既体现在表述，也体现在其能否帮助设计者识别问题和作出设计决策。

Weisz 等[49](https://doi.org/10.1145/3613904.3642466)结合文献、设计实践者反馈、现有生成式人工智能应用以及两个应用的设计过程，迭代形成六项设计原则及相应策略。研究把原则的抽象表述与具体实施方式联系起来，并通过多种来源修订其内容。这为本课题提供了原则形成的参照：经验问题、设计操作、任务结果和应用条件需要相互对应。

Zimmerman 等[50](https://doi.org/10.1145/1240624.1240704)讨论通过设计开展研究（research through design）的知识生产方式，将设计实践与研究贡献联系起来。Höök 和 Löwgren[51](https://doi.org/10.1145/2362364.2362371)以强概念（strong concepts）讨论交互设计中的中层知识（intermediate-level knowledge），说明知识可以位于单个实例与宏观理论之间。两项工作支持设计研究提炼可迁移认识，同时要求研究者明确其知识形态及依据。

本课题适宜争取的贡献是具有条件的设计原则，以及支撑这些原则的跨案例经验描述。原则应说明面对哪类诊断困难，设计者可以怎样组织信息或提供操作，预期影响什么活动，现有证据来自哪些参与者和任务，以及何时效果减弱或成本增加。原则可以借助一个原型检验，但其表述需要让其他设计者在另一种界面中实施。

### 7.3 设计研究中的过程质量

Sedlmair 等[52](https://doi.org/10.1109/TVCG.2012.213)总结可视化设计研究的方法，将问题理解、抽象、设计实现和验证联系起来，并讨论各阶段可能出现的偏差。Meyer 和 Dykes[53](https://doi.org/10.1109/TVCG.2019.2934539)进一步从可视化设计研究的经验出发讨论严谨性，强调研究过程的反思、论证和材料呈现。这些方法工作提示，本课题需要保留设计选择的依据及其变化，而不仅记录最终界面。

具体而言，一项候选原则应能够追溯到跨案例困难、至少两种可比较方案及其评价结果。若研究界面同时增加原始数据、自动摘要和关系导航，整体表现改善只能首先支持这组设计的综合效果；进一步声称某个组成部分独立有效，需要相应比较或过程证据。清楚界定评价对象，有助于使贡献范围与研究证据一致。

### 7.4 样本与分析如何支撑结论

Malterud 等[54](https://doi.org/10.1177/1049732315617444)提出信息力（information power），将定性样本的充分性与研究目标、样本特征、理论使用、访谈质量和分析方式联系起来。该观点支持以研究问题和资料质量决定招募，而不是仅以访谈人数判断充分性。对于本课题，关键在于是否获得不同开发背景下可分析的诊断事件，以及这些事件能否支持跨案例比较。

Gale 等[55](https://doi.org/10.1186/1471-2288-13-117)介绍框架法（framework method），通过编码和矩阵组织案例与主题，适用于需要系统比较多名参与者经验的研究。本课题可按“诊断任务—运行材料—判断困难—采取行动—结果”建立矩阵，同时保留不符合主要模式的案例。矩阵有助于区分广泛出现的困难、某类任务特有的困难和个别人的使用偏好。

对照实验中的样本量需要另行论证。Lakens[56](https://doi.org/10.1525/collabra.33267)讨论最小有意义效应、估计精度和研究资源等样本量依据；Green 和 MacLeod[57](https://doi.org/10.1111/2041-210X.12504)提供广义线性混合模型的模拟功效分析方法。参与者反复处理多个案例时，人员和案例都可能造成差异，样本论证应纳入这种结构。预实验适合用于检查任务难度、测量流程和参数范围，正式比较应在明确主要指标和分析计划之后开展。

## 八、研究评述与课题定位

### 8.1 已有研究形成的认识

现有文献形成了四方面认识。第一，调试包含材料搜索、关系理解、假设形成与检查，自动提供可疑位置仍需要人的解释工作。第二，生成式系统的实践者持续面临结果评价和改进行动之间的衔接问题，智能体增加了跨步骤执行、工具反馈和干预选择。第三，轨迹可视化、问题式入口、输出比较和局部重执行提供了多种设计资源，效果与任务、使用者经验及信息条件有关。第四，清晰解释和透明性感受需要与客观判断分别评价，不确定性和系统限制会影响使用者的检查行为。

国内研究在智能时代人机协作与工程心理学方面形成了重要议题，国际相关文献积累了程序调试、生成式工具使用和智能体可视分析的具体经验。现阶段，工具调用型智能体的专业开发者诊断行为，尤其是运行材料怎样影响原因判断和下一步检查，仍需要更直接的经验研究。

### 8.2 尚需补充的研究证据

首先，需要补充从真实诊断事件出发的过程证据。现有工具评价揭示了使用需求和部分任务表现，但关于开发者如何在工具参数、返回内容、状态变化和配置之间寻找原因，仍缺少足以支撑设计选择的细致描述。研究应确定困难出现的条件，并区分材料未被记录、材料难以访问以及材料虽已取得但难以解释。

其次，需要补充针对核心设计选择的比较证据。多种功能组合可以改善工具体验，但研究还需说明设计改变了哪项诊断活动。可在控制材料与基础功能的情况下比较信息组织方式，也可明确研究“新增信息及其呈现”的整体效果。评价对象的界定决定结论能否解释具体设计的作用。

再次，需要补充对判断依据和材料边界的评价。最终答案可能出现猜测正确、证据使用错误或合理承认无法判断等情况。研究需要区分故障的实际实现原因与可见材料允许作出的判断，并将二者用于任务设计和评分。

最后，需要补充设计知识在新案例中的适用证据。新案例可以改变工具组合、任务内容、故障传播方式或记录完整性，研究据此检查某项原则是否依赖具体案例或界面实现。跨案例验证能够逐步明确知识适用的情境，支持后续设计者判断能否借鉴。

### 8.3 本课题的研究定位

本课题聚焦具有工具调用和状态更新过程的单个主要智能体，研究开发者在任务失败后如何利用运行材料形成并检验诊断判断。研究首先通过访谈和任务观察建立跨案例描述，再选择一项具有共同性且能够通过设计改善的困难，形成可比较的原型方案，随后开展对照评价与新案例检验。

核心研究问题为：在工具调用型智能体故障诊断中，哪些信息条件使开发者难以建立和检验原因判断，以及怎样的信息表征与交互支持能够改善这些活动？预期知识包括诊断困难与信息条件的经验联系，以及由研究支持的设计原则。原型承载并检验设计主张，实验说明其作用与代价，新案例研究界定其可迁移范围。这样的研究过程能够把具体开发问题转化为适用于一类相似情境的设计知识。

## 参考文献

[1] [YAO S, ZHAO J, YU D, et al. ReAct: Synergizing Reasoning and Acting in Language Models[C]//International Conference on Learning Representations. 2023.](https://arxiv.org/abs/2210.03629)

[2] [范俊君, 田丰, 杜一, 等. 智能时代人机交互的一些思考[J]. 中国科学: 信息科学, 2018, 48(4): 361—375.](https://doi.org/10.1360/N112017-00221)

[3] [许为, 葛列众. 智能时代的工程心理学[J]. 心理科学进展, 2020, 28(9): 1409—1425.](https://doi.org/10.3724/SP.J.1042.2020.01409)

[4] [KATZ I R, ANDERSON J R. Debugging: An Analysis of Bug-Location Strategies[J]. Human-Computer Interaction, 1987, 3(4): 351—399.](https://doi.org/10.1207/s15327051hci0304_2)

[5] [KO A J, MYERS B A, COBLENZ M J, et al. An Exploratory Study of How Developers Seek, Relate, and Collect Relevant Information during Software Maintenance Tasks[J]. IEEE Transactions on Software Engineering, 2006, 32(12): 971—987.](https://doi.org/10.1109/TSE.2006.116)

[6] [LAWRANCE J, BOGART C, BURNETT M, et al. How Programmers Debug, Revisited: An Information Foraging Theory Perspective[J]. IEEE Transactions on Software Engineering, 2013, 39(2): 197—215.](https://doi.org/10.1109/TSE.2010.111)

[7] [STARR A, STOREY M A. Theory of Troubleshooting: The Developer's Cognitive Experience of Overcoming Confusion[J/OL]. ACM Transactions on Software Engineering and Methodology, 2026[2026-09-22].](https://doi.org/10.1145/3800945)

[8] [ROMERO P, DU BOULAY B, COX R, et al. Debugging Strategies and Tactics in a Multi-Representation Software Environment[J]. International Journal of Human-Computer Studies, 2007, 65(12): 992—1009.](https://doi.org/10.1016/j.ijhcs.2007.07.005)

[9] [PARNIN C, ORSO A. Are Automated Debugging Techniques Actually Helping Programmers?[C]//Proceedings of the 2011 International Symposium on Software Testing and Analysis. 2011: 199—209.](https://doi.org/10.1145/2001420.2001445)

[10] [BARKE S, JAMES M B, POLIKARPOVA N. Grounded Copilot: How Programmers Interact with Code-Generating Models[J]. Proceedings of the ACM on Programming Languages, 2023, 7(OOPSLA1): 78:1—78:27.](https://doi.org/10.1145/3586030)

[11] [ZAMFIRESCU-PEREIRA J D, WONG R Y, HARTMANN B, et al. Why Johnny Can't Prompt: How Non-AI Experts Try (and Fail) to Design LLM Prompts[C]//Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems. 2023.](https://doi.org/10.1145/3544548.3581388)

[12] [VAN DER MADEN W, SADEK M, XIAO Z, et al. Results-Actionability Gap: Understanding How Practitioners Evaluate LLM Products in the Wild[C]//Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems. 2026: 1—17.](https://doi.org/10.1145/3772318.3791069)

[13] [KUMAR A, BAJPAI Y, GULWANI S, et al. Why AI Agents Still Need You: Findings from Developer-Agent Collaborations in the Wild[C]//Proceedings of the 40th IEEE/ACM International Conference on Automated Software Engineering. 2025: 432—444.](https://arxiv.org/abs/2506.12347v3)

[14] [PAREEK S, GOVERS J, KOLLERUP N K, et al. Sensemaking in Multi-Agent LLM Interfaces: How Users Interpret Transparency and Trustworthiness Cues[C]//Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems. 2026.](https://doi.org/10.1145/3772318.3791157)

[15] [CORNELISSEN B, ZAIDMAN A, VAN DEURSEN A. A Controlled Experiment for Program Comprehension through Trace Visualization[J]. IEEE Transactions on Software Engineering, 2011, 37(3): 341—355.](https://doi.org/10.1109/TSE.2010.47)

[16] [KO A J, MYERS B A. Finding Causes of Program Output with the Java Whyline[C]//Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. 2009: 1569—1578.](https://doi.org/10.1145/1518701.1518942)

[17] [KHANNA R, DODGE J, ANDERSON A, et al. Finding AI's Faults with AAR/AI: An Empirical Study[J]. ACM Transactions on Interactive Intelligent Systems, 2022, 12(1): 1—33.](https://doi.org/10.1145/3487065)

[18] [ARAWJO I, SWOOPES C, VAITHILINGAM P, et al. ChainForge: A Visual Toolkit for Prompt Engineering and LLM Hypothesis Testing[C]//Proceedings of the CHI Conference on Human Factors in Computing Systems. 2024.](https://doi.org/10.1145/3613904.3642016)

[19] [LU J, PAN B, CHEN J, et al. AgentLens: Visual Analysis for Agent Behaviors in LLM-Based Autonomous Systems[J]. IEEE Transactions on Visualization and Computer Graphics, 2025, 31(8): 4182—4197.](https://doi.org/10.1109/TVCG.2024.3394053)

[20] [GAO T, LI H, LI J H, et al. Graph of Trace: Visualizing Execution Traces of Scientific Agents[C]//Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations). 2026: 297—306.](https://aclanthology.org/2026.acl-demo.29/)

[21] [DIBIA V, CHEN J, BANSAL G, et al. AutoGen Studio: A No-Code Developer Tool for Building and Debugging Multi-Agent Systems[C]//Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: System Demonstrations. 2024: 72—79.](https://doi.org/10.18653/v1/2024.emnlp-demo.8)

[22] [EPPERSON W, BANSAL G, DIBIA V, et al. Interactive Debugging and Steering of Multi-Agent AI Systems[C]//Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems. 2025.](https://doi.org/10.1145/3706598.3713581)

[23] [RORSETH J, GODFREY P, GOLAB L, et al. LADYBUG: An LLM Agent DeBUGger for Data-Driven Applications[C]//Proceedings of the 28th International Conference on Extending Database Technology. 2025: 1082—1085.](https://doi.org/10.48786/EDBT.2025.94)

[24] [HUTTER R, PRADEL M. AgentStepper: Interactive Debugging of Software Development Agents[EB/OL]. arXiv:2602.06593, 2026[2026-09-22].](https://arxiv.org/abs/2602.06593)

[25] [FONSECA R, PORTER G, KATZ R H, et al. X-Trace: A Pervasive Network Tracing Framework[C]//Proceedings of the 4th USENIX Symposium on Networked Systems Design and Implementation. 2007: 271—284.](https://www.usenix.org/conference/nsdi-07/x-trace-pervasive-network-tracing-framework)

[26] [SIGELMAN B H, BARROSO L A, BURROWS M, et al. Dapper, a Large-Scale Distributed Systems Tracing Infrastructure[R]. Google, 2010.](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/)

[27] [MACE J, ROELKE R, FONSECA R. Pivot Tracing: Dynamic Causal Monitoring for Distributed Systems[C]//Proceedings of the 25th ACM Symposium on Operating Systems Principles. 2015: 378—393.](https://doi.org/10.1145/2815400.2815415)

[28] [ZHENG Y, HU Y, YU T, et al. AgentSight: System-Level Observability for AI Agents Using eBPF[EB/OL]. arXiv:2508.02736v2, 2025[2026-09-22].](https://arxiv.org/abs/2508.02736v2)

[29] [CEMRI M, PAN M Z, YANG S, et al. Why Do Multi-Agent LLM Systems Fail?[C]//Advances in Neural Information Processing Systems. 2025, 38.](https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html)

[30] [ZHANG S, YIN M, ZHANG J, et al. Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems[C]//Proceedings of the 42nd International Conference on Machine Learning. PMLR, 2025, 267: 76583—76599.](https://proceedings.mlr.press/v267/zhang25cq.html)

[31] [CHEN M, WANG J, LIU Z, et al. From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws[EB/OL]. arXiv:2606.06324v2, 2026[2026-09-22].](https://arxiv.org/abs/2606.06324v2)

[32] [WU Z, CHO S, VILLALOBOS C E M, et al. AgentGraph: Trace-to-Graph Platform for Interactive Analysis and Robustness Testing in Agentic AI Systems[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2026, 40(48): 41721—41723.](https://doi.org/10.1609/aaai.v40i48.42393)

[33] [RAGAN E D, ENDERT A, SANYAL J, et al. Characterizing Provenance in Visualization and Data Analysis: An Organizational Framework of Provenance Types and Purposes[J]. IEEE Transactions on Visualization and Computer Graphics, 2016, 22(1): 31—40.](https://doi.org/10.1109/TVCG.2015.2467551)

[34] [KADIVAR N, CHEN V, DUNSMUIR D, et al. Capturing and Supporting the Analysis Process[C]//Proceedings of the IEEE Symposium on Visual Analytics Science and Technology. 2009: 131—138.](https://doi.org/10.1109/VAST.2009.5333020)

[35] [XU K, ATTFIELD S, JANKUN-KELLY T J, et al. Analytic Provenance for Sensemaking: A Research Agenda[J]. IEEE Computer Graphics and Applications, 2015, 35(3): 56—64.](https://doi.org/10.1109/MCG.2015.50)

[36] [LIAO Q V, GRUEN D, MILLER S. Questioning the AI: Informing Design Practices for Explainable AI User Experiences[C]//Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems. 2020: 1—15.](https://doi.org/10.1145/3313831.3376590)

[37] [EHSAN U, LIAO Q V, MULLER M, et al. Expanding Explainability: Towards Social Transparency in AI Systems[C]//Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems. 2021: 1—19.](https://doi.org/10.1145/3411764.3445188)

[38] [KAUR H, NORI H, JENKINS S, et al. Interpreting Interpretability: Understanding Data Scientists' Use of Interpretability Tools for Machine Learning[C]//Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems. 2020: 1—14.](https://doi.org/10.1145/3313831.3376219)

[39] [BUÇINCA Z, MALAYA M B, GAJOS K Z. To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making[J]. Proceedings of the ACM on Human-Computer Interaction, 2021, 5(CSCW1): 1—21.](https://doi.org/10.1145/3449287)

[40] [SIEKER J, JUNKER S, UTESCHER R, et al. The Illusion of Competence: Evaluating the Effect of Explanations on Users' Mental Models of Visual Question Answering Systems[C]//Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing. 2024: 19459—19475.](https://doi.org/10.18653/v1/2024.emnlp-main.1084)

[41] [HULLMAN J. Why Authors Don't Visualize Uncertainty[J]. IEEE Transactions on Visualization and Computer Graphics, 2020, 26(1): 130—139.](https://doi.org/10.1109/TVCG.2019.2934287)

[42] [GUO H, HUANG J, LAIDLAW D H. Representing Uncertainty in Graph Edges: An Evaluation of Paired Visual Variables[J]. IEEE Transactions on Visualization and Computer Graphics, 2015, 21(10): 1173—1186.](https://doi.org/10.1109/TVCG.2015.2424872)

[43] [SACHA D, SENARATNE H, KWON B C, et al. The Role of Uncertainty, Awareness, and Trust in Visual Analytics[J]. IEEE Transactions on Visualization and Computer Graphics, 2016, 22(1): 240—249.](https://doi.org/10.1109/TVCG.2015.2467591)

[44] [EHSAN U, LIAO Q V, PASSI S, et al. Seamful XAI: Operationalizing Seamful Design in Explainable AI[J]. Proceedings of the ACM on Human-Computer Interaction, 2024, 8(CSCW1): 1—29.](https://doi.org/10.1145/3637396)

[45] [PIROLLI P, CARD S K. The Sensemaking Process and Leverage Points for Analyst Technology as Identified Through Cognitive Task Analysis[C]//Proceedings of the 2005 International Conference on Intelligence Analysis. 2005.](https://www.e-education.psu.edu/geog885/sites/www.e-education.psu.edu.geog885/files/geog885q/file/Lesson_02/Sensemaking_206_Camera_Ready_Paper.pdf)

[46] [KLEIN G, MOON B, HOFFMAN R R. Making Sense of Sensemaking 2: A Macrocognitive Model[J]. IEEE Intelligent Systems, 2006, 21(5): 88—92.](https://doi.org/10.1109/MIS.2006.100)

[47] [DRITSA D, HOUBEN S. How Design Researchers Make Sense of Data Visualizations in Data-Driven Design: An Uncertainty-Aware Sensemaking Model[J]. ACM Transactions on Computer-Human Interaction, 2024, 31(6): 72:1—72:53.](https://doi.org/10.1145/3685268)

[48] [AMERSHI S, WELD D, VORVOREANU M, et al. Guidelines for Human-AI Interaction[C]//Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems. 2019: 1—13.](https://doi.org/10.1145/3290605.3300233)

[49] [WEISZ J D, HE J, MULLER M, et al. Design Principles for Generative AI Applications[C]//Proceedings of the CHI Conference on Human Factors in Computing Systems. 2024.](https://doi.org/10.1145/3613904.3642466)

[50] [ZIMMERMAN J, FORLIZZI J, EVENSON S. Research through Design as a Method for Interaction Design Research in HCI[C]//Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. 2007: 493—502.](https://doi.org/10.1145/1240624.1240704)

[51] [HÖÖK K, LÖWGREN J. Strong Concepts: Intermediate-Level Knowledge in Interaction Design Research[J]. ACM Transactions on Computer-Human Interaction, 2012, 19(3): 23:1—23:18.](https://doi.org/10.1145/2362364.2362371)

[52] [SEDLMAIR M, MEYER M, MUNZNER T. Design Study Methodology: Reflections from the Trenches and the Stacks[J]. IEEE Transactions on Visualization and Computer Graphics, 2012, 18(12): 2431—2440.](https://doi.org/10.1109/TVCG.2012.213)

[53] [MEYER M, DYKES J. Criteria for Rigor in Visualization Design Study[J]. IEEE Transactions on Visualization and Computer Graphics, 2020, 26(1): 87—97.](https://doi.org/10.1109/TVCG.2019.2934539)

[54] [MALTERUD K, SIERSMA V D, GUASSORA A D. Sample Size in Qualitative Interview Studies: Guided by Information Power[J]. Qualitative Health Research, 2016, 26(13): 1753—1760.](https://doi.org/10.1177/1049732315617444)

[55] [GALE N K, HEATH G, CAMERON E, et al. Using the Framework Method for the Analysis of Qualitative Data in Multi-Disciplinary Health Research[J]. BMC Medical Research Methodology, 2013, 13: 117.](https://doi.org/10.1186/1471-2288-13-117)

[56] [LAKENS D. Sample Size Justification[J]. Collabra: Psychology, 2022, 8(1): 33267.](https://doi.org/10.1525/collabra.33267)

[57] [GREEN P, MACLEOD C J. SIMR: An R Package for Power Analysis of Generalized Linear Mixed Models by Simulation[J]. Methods in Ecology and Evolution, 2016, 7(4): 493—498.](https://doi.org/10.1111/2041-210X.12504)
