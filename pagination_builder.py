def pagination_builder(current_page, total_pages, boundaries, around):
    """Creates pagination for website """

    for parameter in [current_page, total_pages, boundaries, around]:
        if not isinstance(parameter, int) or isinstance(parameter, bool):
            raise TypeError('Parameter must be an integer')
        elif parameter < 0:
            raise ValueError('Parameter cannot be negative')
    
    if total_pages == 0:
        return ""    
    
    if current_page > total_pages:
        raise ValueError("current_page cannot be greater than total_pages")
    if current_page == 0:
        raise ValueError("current_page should not be 0") 

    # Adjust boundaries and around if they exceed total_pages
    boundaries = min(boundaries, total_pages)
    around = min(around, total_pages)
        
    current_page_neighbors = [current_page]

    for page_number in range(1, around + 1):
        neighbor_page_forward = current_page + page_number
        neighbor_page_backward = current_page - page_number 
        if neighbor_page_forward <= total_pages:
            current_page_neighbors.append(neighbor_page_forward)
        if neighbor_page_backward >= 1:
            current_page_neighbors.append(neighbor_page_backward)

    # Order current_page_neighbors
    start_range = min(current_page_neighbors)
    stop_range = max(current_page_neighbors) + 1
    ordered_current_page_neighbors = list(range(start_range, stop_range))

    if boundaries != 0:
        first_page = 1
        # Order boundary_left and right
        boundary_left = list(range(first_page, first_page + boundaries))
        boundary_right = list(range(total_pages - boundaries + 1, total_pages + 1))

        unique_ordered_pages = boundary_left
        if (ordered_current_page_neighbors[0] < boundary_right[0]):
            smaller_list = ordered_current_page_neighbors
            bigger_list = boundary_right
        else:
            smaller_list = boundary_right
            bigger_list = ordered_current_page_neighbors
        # The order of extending the list matters so that result should be ordered and unique
        unique_ordered_pages.extend(
            page_number for page_number in smaller_list 
            if page_number not in unique_ordered_pages
        )
        unique_ordered_pages.extend(
            page_number for page_number in bigger_list 
            if page_number not in unique_ordered_pages
        )
    else:
        unique_ordered_pages = ordered_current_page_neighbors
 
    output = ""
    if min(unique_ordered_pages) != 1:
        output += "... "

    for page in range(len(unique_ordered_pages)):
        if page > 0 and unique_ordered_pages[page] != unique_ordered_pages[page-1] + 1:
            output += "... "
        output += str(unique_ordered_pages[page]) + " "

    if total_pages not in unique_ordered_pages:
        output += "... "
    return output.strip()