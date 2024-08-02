# R2Gen-Pad

该代码主要是用于训练Padchest数据集的R2Gen代码，主要的改动是在代码中加入了之前一篇论文中代码预训练好的padchest分类模型([2002.02582 (arxiv.org)](https://arxiv.org/pdf/2002.02582))，这个模型的表现在Cider和ROUGE_L上表现比较优秀，师兄说可能BLEU和METEOR不太适合评估西语的生成效果，更倾向于使用Cider和ROUGE_L去评估我们的报告生成(https://aclanthology.org/2023.findings-acl.104.pdf、https://arxiv.org/pdf/1708.04390、https://arxiv.org/pdf/2205.12522)，目前生成的效果比较好。
修改代码：
model文件夹中加入了分类模型的model文件，

visual_extractor.py中加入了调用model的代码，

dataset.py、dataloader.py中加入预处理的代码。

数据：
data中的数据都是根据论文处理过的，其中，

padchest_report.json是只有PA模态的报告，

padchest_report_joint.json是PA+L两个模态对应起来的报告，

padchest_label_joint+.json包括了处理后的label。



目前的工作：
师姐说可以把标签提取出embedding，然后输入到textdecoder中，辅助报告的生成，看看能不能在rouge和cider上继续提点。
第二个就是目前用的visual_extractor（即训练好的那个分类模型）的f1不是很高，在进行分类的时候，大部分预测对的结果都是标签比较少的，标签多的类很难预测对，这个可能也会影响生成效果。（预测效果详见labels_and_joint.csv）
