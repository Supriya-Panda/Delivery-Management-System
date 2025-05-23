from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DispatchLog

@api_view(['GET'])
def compliance_report(request):
    logs = DispatchLog.objects.filter(compliance_flag=True).select_related('agent')
    report = [{
        'agent': log.agent.name,
        'warehouse': log.agent.warehouse.name,
        'orders': log.orders_assigned,
        'distance': log.total_distance,
        'time': log.total_time,
        'earnings': log.earnings
    } for log in logs]

    return Response(report)




