from .models import Urban

def write(urban: Urban):
    Urban.model_validate(urban)
    return True