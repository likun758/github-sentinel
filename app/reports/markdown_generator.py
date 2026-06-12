class MarkdownReportGenerator:
    def generate(self, repo_full_name: str, updates: list) -> str:
        lines = [
            "# GitHub Sentinel Report",
            "",
            f"Repository: {repo_full_name}",
            f"Update Count: {len(updates)}",
            "",
        ]

        for item in updates:
            lines.append(f"- {item}")

        return "\n".join(lines)
