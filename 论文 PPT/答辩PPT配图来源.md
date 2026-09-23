# 开题答辩 PPT 配图来源

按 [《开题答辩PPT内容构思》](开题答辩PPT内容构思.md) 的页码筛选。优先使用**论文作者或会议发布的原图**，图号和位置已核对。图片已保存到 [答辩PPT配图](答辩PPT配图) 文件夹；论文配图从 PDF 中裁出。

| 建议页码 | 图 | 直接入口 | 建议取用部分 |
| --- | --- | --- | --- |
| 03—04 研究来源、背景 | ReAct 的推理与行动示意 | [作者项目页原图](https://react-lm.github.io/files/diagram.png) · [项目页](https://react-lm.github.io/) | 用于解释模型推理、行动和外部观察交替出现。它是 ReAct 的方法图，不宜标成所有工具调用型智能体的统一架构。 |
| 08 程序调试信息行为 | Whyline：从输出提出“为什么”问题，再进入执行事件 | [Ko 与 Myers 2009 论文 PDF，第 1 页 Fig. 1、第 3 页 Fig. 2](https://faculty.washington.edu/ajko/papers/Ko2009JavaWhylineUI.pdf#page=1) | Fig. 1 展示选择异常输出并提出问题；Fig. 2 展示回查执行原因。建议两图并列、各裁出关键区域。 |
| 09 大模型开发与故障诊断 | AGDebugger 的“识别错误—尝试修复”循环 | [作者论文 PDF，第 6 页 Fig. 2](https://willepperson.com/papers/agdebugger-chi25.pdf#page=6) | 适合说明开发者的调试活动；这是已有研究的模型，不是本课题发现。 |
| 10 运行轨迹 | AgentLens 的三视图界面 | [作者网页上的图片](https://yingchaojiefeng.github.io/images/agentLens.png) · [作者主页](https://yingchaojiefeng.github.io/) | 保留概览、单个智能体细节、监视视图三部分，突出从全局到局部的查看方式。 |
| 10—12 事件关系与证据来源 | AgentGraph 的图关系与原始轨迹联动 | [AAAI 论文 PDF，第 2 页 Fig. 1，重点看 B 区](https://ojs.aaai.org/index.php/AAAI/article/download/42393/46354#page=2) | 裁出“知识图谱 + Trace 原文高亮”部分，适合讲证据如何回连原始记录。 |
| 11 检查与干预 | AGDebugger 的消息界面、编辑与回退 | [作者论文 PDF，第 7 页 Fig. 3、Fig. 4](https://willepperson.com/papers/agdebugger-chi25.pdf#page=7) · [作者概览图](https://willepperson.com/images/papers/25-agdebugger.png) | Fig. 3 展示完整界面；Fig. 4 展示修改此前消息后继续运行。选其中一张即可。 |
| 11 检查与干预 | AgentStepper 的断点、逐步执行和状态检查界面 | [作者论文 PDF，第 6 页 Fig. 2](https://arxiv.org/pdf/2602.06593#page=6) | 可与 AGDebugger 并列，对应“消息重置/编辑”和“断点/逐步检查”两种交互。 |
| 12 运行追踪 | Graph of Trace 的对话、轨迹图、节点详情三栏 | [ACL Anthology PDF，第 4 页 Fig. 2](https://aclanthology.org/2026.acl-demo.29.pdf#page=4) | 用于展示一次执行如何从对话进入结构化轨迹，再检查单个节点。 |

## 最值得先放进 Figma 的四张

1. **ReAct 原图**：第 03 页，建立“多次行动与观察”的研究场景。
2. **Whyline Fig. 1**：第 08 页，说明从症状回查原因的交互思路。
3. **AgentLens 界面图**：第 10 页，展示轨迹的多层次查看。
4. **AGDebugger Fig. 3 或 Fig. 4**：第 11 页，展示编辑与重执行。

## 放图时注意

- **AgentLens、AgentGraph、AGDebugger 主要涉及多智能体或特定应用场景**。它们适合放在“相关研究”中，不要用作本课题单个主要智能体的真实案例或未来原型截图。
- 背景页的**具体故障、证据充分/不足、研究框架**最好根据选题报告在 Figma 自绘；现有论文图不能替代尚未开展的研究结果。
- 论文原图的页脚至少保留“作者，年份，图号”；裁切或翻译后标“据……改绘”。完整文献条目见 `ref/report.bib`。
