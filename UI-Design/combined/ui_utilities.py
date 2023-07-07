

###
# FILE IS BROKEN DO NOT USE
###


from database_utilites import execute_query, execute_insert_query

def resizeEvent(event):
    if event:
        event.accept()
    if hasattr('dashBoardChartView'):
        dashBoardChartView.resize(dashboard_frame_left.size())
        dashBoardChartView.show()
        
    if hasattr('topChartview'):
        topChartview.resize(chart_top.size())
        topChartview.show()
        
    if hasattr('bottomChartview'):
        bottomChartview.resize(chart_bottom.size())
        bottomChartview.show()
        
    super().resizeEvent(event)

def set_priority_counts():
    query = "SELECT priority, COUNT(*) FROM workorders GROUP BY priority"
    result = execute_query(query)

    # Store the counts
    priority_totals = {}
    for priority_count in result:
        priority = priority_count[0]
        count = priority_count[1]
        priority_totals[priority] = count

    pri_1_count.setText(str(priority_totals[1]))
    pri_2_count.setText(str(priority_totals[2]))
    pri_3_count.setText(str(priority_totals[3]))