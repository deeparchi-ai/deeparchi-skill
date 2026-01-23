# 快速发布指南

## 一键发布（推荐）

在 PowerShell 中运行：

```powershell
cd "EA Skills/deeparchi"
.\publish.ps1
```

脚本会自动：
1. 检查 Git 环境
2. 初始化 Git 仓库（如需要）
3. 添加所有文件
4. 提交更改
5. 配置远程仓库
6. 创建版本标签
7. 推送到 GitHub

## 手动发布步骤

### 1. 初始化 Git 仓库

```powershell
cd "EA Skills/deeparchi"
git init
git add .
git commit -m "Initial commit: DeepArchi Skill v1.0.0"
```

### 2. 在 GitHub 上创建仓库

1. 访问 https://github.com/new
2. 仓库名称：`deeparchi-skill`（或你喜欢的名称）
3. 设置为 Public（公开）
4. 不要初始化 README、.gitignore 或 LICENSE（我们已经有了）
5. 点击 "Create repository"

### 3. 连接到 GitHub

```powershell
# 替换 YOUR_USERNAME 为你的 GitHub 用户名
git remote add origin https://github.com/YOUR_USERNAME/deeparchi-skill.git
git branch -M main
git push -u origin main
```

### 4. 创建 Release 标签

```powershell
git tag -a v1.0.0 -m "DeepArchi Skill v1.0.0 - Initial release"
git push origin v1.0.0
```

### 5. 验证发布

其他人现在可以通过以下命令安装你的技能：

```bash
npx openskills install YOUR_USERNAME/deeparchi-skill
```

## 文件结构

发布前确保以下文件存在：

```
deeparchi/
├── README.md                    ✓ 主要文档
├── SKILL.md                     ✓ 技能元数据（YAML格式）
├── EXAMPLES.md                  ✓ 使用示例
├── package.json                 ✓ NPM 包配置
├── LICENSE                      ✓ MIT 许可证
├── .gitignore                   ✓ Git 忽略文件
├── PUBLISH.md                   ✓ 详细发布指南
├── references/                  ✓ 参考文档
│   ├── archimate-relationships-guide.md
│   └── drawio-archimate-tutorial.md
├── scripts/                     ✓ 工具脚本
│   └── validate-archimate.js
└── assets/                      ✓ 资源文件
    └── archimate-color-palette.json
```

## 常见问题

### Q: 如何更新已发布的技能？

A: 修改文件后，更新版本号并推送：

```powershell
# 更新 package.json 和 SKILL.md 中的版本号
git add .
git commit -m "Update: version 1.0.1"
git tag -a v1.0.1 -m "DeepArchi Skill v1.0.1"
git push origin main
git push origin v1.0.1
```

### Q: 技能安装失败怎么办？

A: 检查：
- GitHub 仓库是否为 Public
- README.md 或 SKILL.md 是否在根目录
- package.json 配置是否正确

### Q: 如何测试本地技能？

A: 使用本地路径安装：

```bash
npx openskills install ./EA\ Skills/deeparchi
```

## 需要帮助？

查看 `PUBLISH.md` 获取更详细的发布指南和故障排除信息。
