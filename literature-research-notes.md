# 文献检索与核验记录

核验日期：2026年9月22日。

## 一、当前交付文件

- [文献综述](literature-review.md)：57篇正文实际引用的文献。
- [选题报告](selection-report.md)：40篇正文实际引用的文献，均包含在综述的57篇之中。
- 两份文件分别按首次引用顺序编号，便于独立阅读；合并为学校提交文档时需统一参考文献编号。
- 本次只编辑Markdown，未同步修改LaTeX、文献数据库或编译PDF。
- 修改前的Markdown保存在[备份目录](archive/2026-09-22-before-reference-revision/)。

对照材料为朱静文开题报告：参考文献61条，独立文献综述位于PDF第68—87页，另外包含较长的文献阅读卡。文献数量用于比较覆盖规模，本文依据主题相关性和证据作用选择57篇。

## 二、检索与核验方式

检索以程序调试、智能体诊断、运行追踪、分析历史、解释使用和设计知识为主线，结合核心论文的引用补充。优先核对出版方、会议论文集、作者与机构公开稿。正文保留可访问的论文链接，近期预印本注明引用日期或版本。

本次取得的材料深度包括论文全文及相关方法段、作者公开稿、出版方摘要和书目信息，并未把全部57篇都记为逐页全文精读。样本量、实验分组和具体结果只在所取得材料能够支持时写入；其他文献用于相应层级的技术、概念或方法说明。检索未实施可重复的全库筛选流程，正文采用主题综述，不声称系统综述。

代表性检索组合：

- 程序调试：developer debugging information seeking；program comprehension trace visualization。
- 智能体研究：LLM agent debugging user study；developer-agent collaboration；failure attribution。
- 解释与判断：explanations mental models；interpretability tools data scientists；overreliance。
- 分析活动：analytic provenance sensemaking；uncertainty visualization。
- 设计与研究方法：design principles generative AI；design study rigor；sample size justification。

## 三、重点文献的证据用途

以下编号对应文献综述。

| 文献 | 已核对的材料与研究类型 | 正文采用的结论范围 |
| --- | --- | --- |
| AGDebugger [22](https://doi.org/10.1145/3706598.3713581) | 论文方法与用户研究；5人形成性访谈、6人诊断研究、8人运行引导研究 | 分别描述研究部分，保留修改位置选择的困难；不用总体人数合并推断效果 |
| AgentStepper [24](https://arxiv.org/abs/2602.06593) | 预印本方法与结果；小规模学生参与者任务研究 | 采用初步交互证据，不把任务试次数的比例写成人员成功率 |
| ChainForge [18](https://doi.org/10.1145/3613904.3642016) | 论文实验与访谈；21人实验室研究、6次涉及8人的访谈 | 输出探索、比较及假设检验的使用方式 |
| AgentLens [19](https://doi.org/10.1109/TVCG.2024.3394053) | 系统论文、使用案例和14人用户研究 | 复杂行为探索；不据此断言故障诊断正确性提升 |
| Graph of Trace [20](https://aclanthology.org/2026.acl-demo.29/) | ACL正式论文页面及系统评价材料 | 专家对可理解性与使用价值的评价 |
| AgentGraph [32](https://doi.org/10.1609/aaai.v40i48.42393) | AAAI正式演示论文页面与摘要 | 类型化事件图、轨迹链接和分析能力 |
| LADYBUG [23](https://doi.org/10.48786/EDBT.2025.94) | EDBT会议公开稿 | 局部检查、干预和重执行能力；系统演示 |
| Results-Actionability Gap [12](https://doi.org/10.1145/3772318.3791069) | 正式发表信息、作者机构材料及研究摘要 | 19名实践者的评价与改进行动衔接问题 |
| Grounded Copilot [10](https://doi.org/10.1145/3586030) | 作者公开稿与正式发表信息 | 20人观察研究中的加速与探索模式 |
| Why AI Agents Still Need You [13](https://arxiv.org/abs/2506.12347v3) | 作者预印本、接收信息及作者履历 | 19名开发者、33项真实任务；行为关联与过程观察 |
| Pareek等 [14](https://doi.org/10.1145/3772318.3791157) | 作者全文，方法及任务段 | 12人、5种界面、两类任务，解释透明性与可靠性感受 |
| Sieker等 [40](https://doi.org/10.18653/v1/2024.emnlp-main.1084) | ACL权威作者名单、摘要与出版信息 | 解释提高能力评价，但未改善对系统限制的识别 |
| Kaur等 [38](https://doi.org/10.1145/3313831.3376219) | 论文方法与结果 | 数据科学家对解释工具的理解和误用 |
| Buçinca等 [39](https://doi.org/10.1145/3449287) | 论文研究设计与结果 | 认知强制措施对错误依赖及使用成本的影响 |
| AAR/AI [17](https://doi.org/10.1145/3487065) | 出版方论文材料，条件与结果描述 | 结构化复盘的作用；研究对象不是大语言模型智能体 |
| MAST [29](https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2025正式论文集与摘要 | 故障类型与案例采样依据；未混用预印本和正式版的数据量 |
| 自动失败归因 [30](https://proceedings.mlr.press/v267/zhang25cq.html) | ICML正式论文集与论文 | 自动定位任务；与人的诊断工具效果分别讨论 |
| 运行框架诊断与修复 [31](https://arxiv.org/abs/2606.06324v2) | 2026年预印本第二版 | 轨迹与实现关联的技术路径 |
| AgentSight [28](https://arxiv.org/abs/2508.02736v2) | 作者预印本及其正式发表关联信息 | 系统级观测能力；本稿链接实际查阅的预印本版本 |
| Dritsa与Houben [47](https://doi.org/10.1145/3685268) | 作者机构页面及公开稿 | 设计研究者解释可视化材料的经验，说明情境与不确定性的作用 |
| Guo等 [42](https://doi.org/10.1109/TVCG.2015.2424872) | 原始研究摘要与权威书目信息 | 配对视觉变量和任务影响图边不确定性表达 |
| Amershi等 [48](https://doi.org/10.1145/3290605.3300233)、Weisz等 [49](https://doi.org/10.1145/3613904.3642466) | 正式论文与作者稿中的原则形成过程 | 多轮反馈、多应用和设计实践对原则形成的支持 |

## 四、书目与引文检查结果

已依据权威来源修正Sieker等论文的作者信息，采用Pareek等和Dritsa与Houben论文的完整题名，修正AgentGraph的正式题名，并将MAST更新为NeurIPS 2025正式发表条目。Guo等论文的第二作者为Jeff Huang。未核实的卷期、页码和效果数值不补写。

已删除对同一理论的重复铺陈和与当前论证关系较弱的引用。综述按“问题—方法—结果—适用范围”组织经验研究，系统演示、自动评测和理论方法分别说明用途。

两份正文已检查引用编号、首次引用顺序、文末条目与链接的一致性；参考文献均在正文出现。研究计划统一为：形成性研究12—16人，两轮走查共6—8人，预实验4—6人，正式实验暂按36人安排，新案例研究6—8人。正式人数仍须在研究实施阶段依据主要指标和模拟论证确定。

## 五、提交与后续研究衔接

当前Markdown正文可独立审阅。工作区原有LaTeX和PDF仍保留此前版本；若学校要求合并排版，需以本次Markdown为内容来源统一编号和排版。

开题后的文献工作重点为：结合形成性研究确定的核心困难，继续精读最直接相关的实验方法；记录新增论文的样本、任务、比较条件和证据范围；在正式实验前更新同类智能体诊断工具的研究进展。
