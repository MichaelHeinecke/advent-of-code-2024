def read_reports_from_file(file: str) -> list[list[int]]:
    parsed_reports = []
    with open(file) as f:
        for line in f:
            rep = line.split(r" ")
            parsed_reports.append([int(token) for token in rep])

    return parsed_reports


def calculate_number_of_safe_reports(reports: list[list[int]]) -> int:
    """Calculates the number of safe reports. A report consists of multiple numbers and
    is safe if all numbers are either ascending or descending, and adhere to a minimum
    and maximum distance from the next number in the report."""
    min_distance = 1
    max_distance = 3

    def is_safe(report: list[int]) -> bool:
        if all(min_distance <= report[i + 1] - report[i] <= max_distance for i in
               range(len(report) - 1)):
            return True
        if all(min_distance <= report[i] - report[i + 1] <= max_distance for i in
               range(len(report) - 1)):
            return True
        return False

    return sum(1 for report in reports if is_safe(report))


def calculate_number_of_safe_reports_with_single_unsafe_level_allowed(
        reports: list[list[int]]) -> int:
    """Calculates the number of safe reports. A report consists of multiple numbers and
    is safe if all numbers are either ascending or descending, and adhere to a minimum
    and maximum distance from the next number in the report. If a report can be made
    safe by removing a single number, it is also considered safe."""
    min_distance = 1
    max_distance = 3

    def is_safe(report: list[int]) -> bool:
        if all(min_distance <= report[i + 1] - report[i] <= max_distance for i in
               range(len(report) - 1)):
            return True
        if all(min_distance <= report[i] - report[i + 1] <= max_distance for i in
               range(len(report) - 1)):
            return True
        return False

    def can_be_made_safe(report: list[int]) -> bool:
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                return True
        return False

    return sum(1 for report in reports if is_safe(report) or can_be_made_safe(report))


if __name__ == '__main__':
    input_file = "input.txt"
    input_reports = read_reports_from_file(input_file)
    number_safe_reports = calculate_number_of_safe_reports(input_reports)
    print(f"The number of safe reports is: {number_safe_reports}")

    number_safe_reports = calculate_number_of_safe_reports_with_single_unsafe_level_allowed(
        input_reports)
    print(f"The number of safe reports with problem dampener is: {number_safe_reports}")
