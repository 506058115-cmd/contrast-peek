# contrast-peek

在本地终端计算两种 HEX 颜色的对比度，并按 WCAG 2.2 AA 的文字阈值显示结果。不联网，不需要第三方依赖。

## 使用

需要 Python 3.8+。

```sh
python contrast_peek.py '#25364a' '#f5f0e6'
```

支持 `#RGB` 与 `#RRGGBB`。普通文字阈值为 4.5:1；大号文字阈值为 3:1（一般指至少 18pt 常规字重，或至少 14pt 粗体）。工具只检查颜色对比度，不能代表完整的 WCAG 合规结论。

计算依据：[WCAG 2.2 对比度（最低）](https://www.w3.org/TR/WCAG22/#contrast-minimum) 与 [W3C 相对亮度和对比度技术说明](https://www.w3.org/WAI/WCAG22/Techniques/general/G145)。

## 许可

MIT，见 [LICENSE](LICENSE)。
## Linux x86_64 下载

- [单文件版](https://github.com/506058115-cmd/contrast-peek/releases/download/v1.0.0/contrast-peek-linux-x86_64-onefile.tar.gz)
- [目录版](https://github.com/506058115-cmd/contrast-peek/releases/download/v1.0.0/contrast-peek-linux-x86_64-onedir.tar.gz)
- [v1.0.0 Release 页面](https://github.com/506058115-cmd/contrast-peek/releases/tag/v1.0.0)

压缩包附带构建信息和依赖许可证；Release 另附 SHA-256 校验文件。产物在 WSL Ubuntu 24.04（Python 3.12.3、PyInstaller 6.22.2）中构建，目标为 GNU/Linux x86_64。较旧的发行版可能需要兼容的 glibc。
