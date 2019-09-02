# flake8: noqa
import logging
logger = logging.getLogger(__name__)

from .supervised import SupervisedRunner

try:
    import wandb
    from .wandb import WandbRunner, SupervisedWandbRunner
except ImportError:
    logger.warning(
        "wandb not available, switching to pickle. "
        "To install wandb, run `pip install wandb`."
    )