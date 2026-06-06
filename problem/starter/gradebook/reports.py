"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


from problem.starter.gradebook.stats import average_per_student, passing_students, subjects_offered, top_scorer


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass

    averages = average_per_student(records)
    subjects = sorted(subjects_offered(records))
    top_name, top_avg = top_scorer(records)
    passed = passing_students(records)

    report = "=== Gradebook Report ===\n"
    report += f"Total records: {len(records)}\n"
    report += f"Subjects offered: {', '.join(subjects)}\n\n"

    report += "Averages:\n"
    for name in sorted(averages):
        report += f"  {name}: {averages[name]}\n"

    report += f"\nTop scorer: {top_name} ({top_avg})\n"
    report += f"Passing students (>= 60.0): {', '.join(passed)}"

    return report