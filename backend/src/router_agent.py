def route_query(query):

    query = query.lower()

    hr_keywords = [
        "leave",
        "attendance",
        "salary",
        "employee",
        "policy"
    ]

    project_keywords = [
        "project",
        "requirement",
        "module",
        "milestone"
    ]

    technical_keywords = [
        "python",
        "fastapi",
        "docker",
        "api",
        "programming"
    ]

    for word in hr_keywords:
        if word in query:
            return "hr"

    for word in project_keywords:
        if word in query:
            return "project"

    for word in technical_keywords:
        if word in query:
            return "technical"

    return "technical"