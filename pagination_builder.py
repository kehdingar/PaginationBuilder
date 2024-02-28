
def pagination_builder(current_page, total_pages, boundaries, around):
    """Creates pagination for website """

    # validate input
    if not isinstance(current_page, int) or not isinstance(total_pages, int):
        raise TypeError("current_page and total_pages must be integers")
    if current_page < 0 or total_pages < 0:
        raise ValueError("current_page and total_pages cannot be negative")
    if current_page > total_pages:
        raise ValueError("current_page cannot be greater than total_pages")
    if boundaries < 0 or around < 0:
        raise ValueError("boundaries and around cannot be negative")

    # handle cases where current page == 0
    if total_pages == 0:
        return ""

    # build first section of pagination ensuring only valid page numbers
    results = []
    for i in range(1, boundaries + 1):
        if i <= total_pages:
            # prevent duplicates
            if str(i) not in results:
                results.append(str(i))

    # verify if elipse "..." is needed before current page
    if current_page > boundaries + around + 2:
        results.append("...")

    for i in range(max(boundaries + 1, current_page - around), min(current_page + around + 1, total_pages - boundaries + 1)):
        if str(i) not in results:
            results.append(str(i))

    # verify if elipse is needed after current page
    if current_page < total_pages - boundaries - around - 1: 
        results.append("...")

    # handle the building of the last section of pagination
    for i in range(total_pages - boundaries + 1, total_pages + 1):
        if i > 0:
            if str(i) not in results:
                results.append(str(i))

    return " ".join(results)
