# Academic Pages

![pages-build-deployment](https://github.com/academicpages/academicpages.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)

Academic Pages 是一款适用于学术网站的 Github 网页模板。

# 入门

1. 注册一个 GitHub 账户（如果没有）并确认电子邮件（必填！）。
2. 点击右上角的 “Use this template ”按钮。
3. 在 “New repository ”页面，输入版本库名称“[您的 GitHub 用户名].github.io”，这也将是您网站的 URL。
4. 设置全站配置并添加内容。
5. 上传任何文件（如 PDF、.zip 文件等）到 `files/` 目录。它们将出现在 https://[您的 GitHub 用户名].github.io/files/example.pdf。
6. 进入仓库设置，在 “GitHub 页面 ”部分查看状态
7. （可选）使用 `markdown_generator`文件夹中的 Jupyter 笔记本或 python 脚本从 TSV 文件为出版物和j讲座生成 markdown 文件。

更多信息，请访问 https://academicpages.github.io/。

## 本地运行

当您初步开发网站时，在将更改推送到 GitHub 之前，在本地预览更改是非常有用的。要在本地工作，您需要

1. 克隆版本库，并按上文所述进行更新。
1. 确保已安装 ruby-dev、bundler 和 nodejs
   
    在大多数 Linux 发行版和 [Windows 子系统 Linux](https://learn.microsoft.com/en-us/windows/wsl/about)上，该命令为
    ```bash
    sudo apt install ruby-dev ruby-bundler nodejs
    ```
    在 MacOS 上，这些命令是
    ```bash
    brew install ruby
    brew install node
    gem install bundler
    ```
1. 运行 `bundle install` 安装 Ruby 依赖项。如果出现错误，请删除 Gemfile.lock，然后重试。
1. 运行 `jekyll serve -l -H localhost` 生成 HTML，并从 `localhost:4000` 发送。

如果在 Linux 上运行，可能需要安装一些额外的依赖项，然后才能在本地运行：`sudo apt install build-essential gcc make`。

# 维护

有关模板的错误报告和功能请求应[通过 GitHub 提交](https://github.com/academicpages/academicpages.github.io/issues/new/choose)。有关模板样式的问题，请随时在 [GitHub](https://github.com/academicpages/academicpages.github.io/discussions) 上发起[新讨论]。

本版本库由 [Stuart Geiger](https://github.com/staeiou) 从 [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/) 分支（然后分离）而来，后者是 © 2016 Michael Rose 根据 MIT 许可发布的（参见 LICENSE.md）。目前由 [Robert Zupko](https://github.com/rjzupkoii) 维护，欢迎更多维护者加入。

## 修正和增强功能

如果您想以 pull request 的形式提交错误修正和增强功能，则需要 [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) 此版本库，而不是将其用作模板。这也将允许你把模板的 [同步副本](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) 同步到你的 fork 中。

遗憾的是，像 Academic Pages 这样的模板主题存在一个后勤问题，即核心主题的错误修复和更新有点麻烦。如果使用该模板并对其进行自定义，那么在尝试同步时很可能会出现合并冲突。如果你想保存你的各种 .yml 配置文件和 markdown 文件，可以删除该版本库，然后重新 fork。或者也可以手动打补丁。
