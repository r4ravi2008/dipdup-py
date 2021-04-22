import demo_tezos_domains.models as models
from demo_tezos_domains.types.name_registry.parameter.execute import Execute
from demo_tezos_domains.types.name_registry_update_record.parameter.update_record import UpdateRecord
from dipdup.models import HandlerContext, OperationContext


async def on_update_registry(
    ctx: HandlerContext,
    update_record: OperationContext[UpdateRecord],
    execute: OperationContext[Execute],
) -> None:
    try:
        label = update_record.parameter.name
        domain = await models.Domain.filter(label=label).get()
        address, _ = await models.Address.get_or_create(address=update_record.parameter.address)
        owner, _ = await models.Address.get_or_create(address=update_record.parameter.owner)
        domain.address = address
        domain.owner = owner
        await domain.save()
    # FIXME: Object does not exist, some entrypoints are not covered
    except Exception as exc:
        print(exc)
