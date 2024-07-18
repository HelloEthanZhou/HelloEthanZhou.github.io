---
permalink: /markdown/
title: "个人主页指南"
author_profile: true
redirect_from: 
  - /md/
  - /markdown.html
---

## 关键文件

* 基本配置选项：_config.yml
* 顶部导航栏配置：_data/navigation.yml
* 单页：_pages/
* 页面为 .md 或 .html 文件，见如下文件夹：
  * _publications/
  * _portfolio/
  * _posts/
  * _teaching/
  * _talks/
* 页脚：_includes/footer.html
* 静态文件（如 PDF）：/files/
* 个人形象（在 _config.yml 中设置）：images/profile.png

## 技巧和提示

* 将文件命名为“.md”，就能以 markdown 格式显示；命名为“.html”，就能以 HTML 格式显示。
* 访问 [commit list](https://github.com/academicpages/academicpages.github.io/commits/master)（在你的 repo 上），查找 Github 使用 Jekyll 构建的最后一个版本。
  * Green check: successful build
  * Orange circle: building
  * Red X: error
  * No icon: not built

## 资源
 * [Liquid syntax guide](https://shopify.github.io/liquid/tags/control-flow/)
 * [MathJax Documentation](https://docs.mathjax.org/en/latest/)

## MathJax 

该模板支持 MathJax 3.0 版本：

$$
\mathrm{e}^{i \pi} + 1 = 0
$$

**注意**：由于 Academic Pages 使用 Markdown，因此在转义字符和新行方面会对 MathJax 和 LaTeX 产生一些干扰，不过存在一些[变通方法](https://math.codidact.com/posts/278763/278772#answer-278772)。

## Markdown 指南

Academic Pages 使用 [kramdown](https://kramdown.gettalong.org/index.html) 进行 Markdown 渲染，这与其他 Markdown 实现（如 GitHub 的实现）存在一些差异。除本指南外，请参阅 [kramdown 语法页面](https://kramdown.gettalong.org/syntax.html)获取完整文档。 

## 小标题

单行楷体引号：

> 引语很酷。

## 表格

### 表格1

| Entry            | Item   |                                                              |
| --------         | ------ | ------------------------------------------------------------ |
| [John Doe](#)    | 2016   | Description of the item in the list                          |
| [Jane Doe](#)    | 2019   | Description of the item in the list                          |
| [Doe Doe](#)     | 2022   | Description of the item in the list                          |

### 表格2

| Header1 | Header2 | Header3 |
|:--------|:-------:|--------:|
| cell1   | cell2   | cell3   |
| cell4   | ce
ll5   | cell6   |
|-----------------------------|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|=============================|
| Foot1   | Foot2   | Foot3   |

## 定义列表

定义列表标题
:   定义列表划分

启动
:  创业公司或初创企业是指旨在寻找可重复、可扩展商业模式的公司或临时组织。

#“干得漂亮”
:  由 Rob Dyrdek 和他的贴身保镖 Christopher "Big Black" Boykins 共同提出的 “干得漂亮”，既可以激励自己，也可以激励朋友。

Do It Live
:  我会让Bill O'Reilly [解释](https://www.youtube.com/watch?v=O_HyZ5aW76c “We'll Do It Live”)这个问题。

## 无序列表（嵌套）

  * 无序列表1
      * 无序列表1.1
          * 无序列表1.1.1
          * 无序列表1.1.2
          * 无序列表1.1.3
          * 无序列表1.1.4
      * 无序列表1.2
      * 无序列表1.3
      * 无序列表1.4
  * 无序列表2
  * 无序列表3
  * 无序列表4

## 有序列表（嵌套）

  1. 有序列表1
      1. 有序列表1.1
          1. 有序列表1.1.1
          2. 有序列表1.1.2
          3. 有序列表1.1.3
          4. 有序列表1.1.4
      2. 有序列表1.2
      3. 有序列表1.3
      4. 有序列表1.4
  2. 有序列表2
  3. 有序列表3
  4. 有序列表4

## 突出

应用 `.btn` 时，可使任何链接更加突出。

## 强调

使用以下语法支持基本强调或呼出：

```markdown
**注意！** 您还可以通过在段落后一行添加 `{: .notice}` 来添加强调。
{: .notice}
```

将显示为

**注意！** 您还可以通过在段落后一行添加 `{: .notice}` 来添加强调。
{: .notice}

### 脚注

脚注可用于澄清文本中的要点或引用信息[^1]。Markdown 支持数字脚注和文本脚注，只要数值是唯一的[^note]。

```markdown
这是一段文本[^1]。这是另一段文本[^note]。

[^1]: 这是一个脚注
[^note]: 这是另一个脚注。
```

[^1]: 例如这个脚注。
[^note]: 脚注标记使用文本时，名称中不允许有空格。

## HTML 标签

### 地址标签

<address>
  1 Infinite Loop<br /> Cupertino, CA 95014<br /> United States
</address>

### 锚标签（又称链接）

这是一个[链接](http://github.com "Github")的例子。

### 缩写标签

CSS 是 “层叠样式表 ”的缩写。

*[CSS]: 层叠样式表

### 引用标签

"Code is poetry." ---<cite>Automattic</cite>

### 代码标签

在稍后的测试中，您将了解到 `word-wrap: break-word;` 将是您最好的朋友。

您还可以编写较大的代码块，某些语言（如 Python）支持语法高亮显示：

```python
print('Hello World!')
```

或 R ：

```R
print("Hello World!", quote = FALSE)
```

### 删除标签

删除标签可以<strike>删除文本</strike>。

### 强调标签

强调标签可以使文本_斜体化_。

### 插入标签

强调标签可以<ins>插入</ins>文本。

### 键盘标签

这个鲜为人知的标记模拟<kbd>键盘文本</kbd>,，其样式通常与 `代码` 标记相似。

### 预格式化标签

该标签为大的代码块设置样式。

<pre>
.post-title {
  margin: 0 0 5px;
  font-weight: bold;
  font-size: 38px;
  line-height: 1.2;
  and here's a line of some really, really, really, really long text, just to see how the PRE tag handles it and to find out how it overflows;
}
</pre>

### 引用标签

<q>Developers, developers, developers&#8230;</q> &#8211;Steve Ballmer

### 黑体标签

强调标签可以使文本**黑体**。

### 下划标签

水的化学式为 H<sub>2</sub>O 。

### 上划标签

质能方程为 E = MC<sup>2</sup> 。

### 变量标签

变量标签可以标记 <var>变量</var>。

***

**脚注**

页面中的脚注将在这一行之后返回，请返回<a href=“#footnotes”>Markdown脚注</a>部分。

