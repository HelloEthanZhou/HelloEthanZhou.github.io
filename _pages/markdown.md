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

脚注可用于澄清文本中的要点或引用信息。[^1]Markdown 支持数字脚注和文本脚注，只要数值是唯一的。[^note]

```markdown
这是一段文本[^1]这是另一段文本[^note]

[^1]: 这是一个脚注
[^note]: 这是另一个脚注。
```

[^1]: 例如这个脚注。
[^note]: 脚注标记使用文本时，名称中不允许有空格。

## HTML Tags

### Address Tag

<address>
  1 Infinite Loop<br /> Cupertino, CA 95014<br /> United States
</address>

### Anchor Tag (aka. Link)

This is an example of a [link](http://github.com "Github").

### Abbreviation Tag

The abbreviation CSS stands for "Cascading Style Sheets".

*[CSS]: Cascading Style Sheets

### Cite Tag

"Code is poetry." ---<cite>Automattic</cite>

### Code Tag

You will learn later on in these tests that `word-wrap: break-word;` will be your best friend.

You can also write larger blocks of code with syntax highlighting supported for some languages, such as Python:

```python
print('Hello World!')
```

or R:

```R
print("Hello World!", quote = FALSE)
```

### Strike Tag

This tag will let you <strike>strikeout text</strike>.

### Emphasize Tag

The emphasize tag should _italicize_ text.

### Insert Tag

This tag should denote <ins>inserted</ins> text.

### Keyboard Tag

This scarcely known tag emulates <kbd>keyboard text</kbd>, which is usually styled like the `<code>` tag.

### Preformatted Tag

This tag styles large blocks of code.

<pre>
.post-title {
  margin: 0 0 5px;
  font-weight: bold;
  font-size: 38px;
  line-height: 1.2;
  and here's a line of some really, really, really, really long text, just to see how the PRE tag handles it and to find out how it overflows;
}
</pre>

### Quote Tag

<q>Developers, developers, developers&#8230;</q> &#8211;Steve Ballmer

### Strong Tag

This tag shows **bold text**.

### Subscript Tag

Getting our science styling on with H<sub>2</sub>O, which should push the "2" down.

### Superscript Tag

Still sticking with science and Isaac Newton's E = MC<sup>2</sup>, which should lift the 2 up.

### Variable Tag

This allows you to denote <var>variables</var>.

***
**Footnotes**

The footnotes in the page will be returned following this line, return to the section on <a href="#footnotes">Markdown Footnotes</a>.

