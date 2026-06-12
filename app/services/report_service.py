from sqlalchemy.orm import Session

from app.models.report import Report
from app.reports.markdown_generator import MarkdownReportGenerator


class ReportService:
    def __init__(self, db: Session):
        self.db = db
        self.generator = MarkdownReportGenerator()

    def create_report(self, repo_full_name: str, updates: list, period: str = "daily"):
        content = self.generator.generate(repo_full_name, updates)

        report = Report(
            repo_full_name=repo_full_name,
            period=period,
            content=content,
        )

        self.db.add(report)
        self.db.commit()
        self.db.refresh(report)

        return report

    def list_reports(self):
        return self.db.query(Report).order_by(Report.created_at.desc()).all()
