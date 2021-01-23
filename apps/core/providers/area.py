from typing import List, Dict, Any

from apps.core.uc.area_uc import GetStateAreaUC

from apps.core.models import Area


def get_area_state_by_area(area: Area) -> List[Dict[str, Any]]:
    return GetStateAreaUC(area).execute()


def get_area_instance(area_id: int) -> Area:
    return Area.objects.get(id=area_id)

