# 发布 DeepArchi Skill 到 OpenSkills

## 发布步骤

### 1. 准备 GitHub 仓库

#### 选项 A：创建新仓库

1. 在 GitHub 上创建新仓库（例如：`deeparchi-skill`）
2. 仓库设置为 Public（公开）
3. 添加仓库描述：`ArchiMate 3.2 compliant enterprise architecture diagrams using draw.io`

#### 选项 B：使用现有仓库

如果已有仓库，可以直接使用。

### 2. 初始化 Git 仓库（如果尚未初始化）

```bash
cd "EA Skills/deeparchi"
git init
git add .
git commit -m "Initial commit: DeepArchi ArchiMate skill v1.0.0"
```

### 3. 连接到 GitHub 仓库

```bash
# 替换为你的 GitHub 用户名和仓库名
git remote add origin https://github.com/YOUR_USERNAME/deeparchi-skill.git
git branch -M main
git push -u origin main
```

### 4. 创建 Release 标签（可选但推荐）

```bash
git tag -a v1.0.0 -m "DeepArchi Skill v1.0.0 - Initial release"
git push origin v1.0.0
```

### 5. 发布到 OpenSkills

#### 方法 1：通过 GitHub URL 安装

其他人可以通过以下命令安装你的技能：

```bash
npx openskills install https://github.com/YOUR_USERNAME/deeparchi-skill.git
```

或者如果仓库在根目录：

```bash
npx openskills install YOUR_USERNAME/deeparchi-skill
```

#### 方法 2：本地测试安装

在发布前，可以在本地测试：

```bash
# 从本地路径安装（用于测试）
npx openskills install ./EA\ Skills/deeparchi
```

### 6. 更新 AGENTS.md（可选）

如果技能已发布，可以在项目的 AGENTS.md 中更新技能位置：

```xml
<skill>
<name>deeparchi</name>
<description>Create ArchiMate 3.2 compliant enterprise architecture diagrams using draw.io...</description>
<location>global</location>
</skill>
```

然后运行：

```bash
npx openskills sync
```

## 发布检查清单

- [ ] 所有文件已创建并测试
- [ ] README.md 完整且清晰
- [ ] SKILL.md 包含正确的 YAML 前置元数据
- [ ] package.json 配置正确
- [ ] LICENSE 文件已添加
- [ ] .gitignore 已配置
- [ ] 代码和文档已审查
- [ ] GitHub 仓库已创建并推送
- [ ] Release 标签已创建（可选）
- [ ] 技能可以通过 GitHub URL 安装

## 发布后的维护

### 更新技能

1. 修改技能文件
2. 更新版本号（在 package.json 和 SKILL.md 中）
3. 提交更改：

```bash
git add .
git commit -m "Update: version 1.0.1 - Add new features"
git tag -a v1.0.1 -m "DeepArchi Skill v1.0.1"
git push origin main
git push origin v1.0.1
```

### 用户更新技能

用户可以通过以下命令更新已安装的技能：

```bash
npx openskills update deeparchi
```

## 推广技能

发布后，可以考虑：

1. 在技能描述中添加 GitHub 链接
2. 在相关社区分享（如 ArchiMate、TOGAF 社区）
3. 创建示例和教程
4. 收集用户反馈并持续改进

## 故障排除

### 问题：技能无法安装

- 检查 GitHub 仓库是否为 Public
- 确认 README.md 或 SKILL.md 存在于根目录
- 检查 package.json 配置是否正确

### 问题：技能内容无法读取

- 确认文件路径正确
- 检查文件编码（建议使用 UTF-8）
- 验证 Markdown 格式是否正确

## 相关资源

- [OpenSkills 文档](https://github.com/openskills/openskills)
- [Agent Skills 标准](https://agentskills.io)
- [GitHub 创建仓库指南](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
