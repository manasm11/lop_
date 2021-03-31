from google.cloud import dialogflow_v2 as dialogflow

def create_entity(project_id, entity_type_id, entity_value, synonyms):
    """Create an entity of the given entity type."""
    # import dialogflow_v2 as dialogflow
    entity_types_client = dialogflow.EntityTypesClient()

    # Note: synonyms must be exactly [entity_value] if the
    # entity_type's kind is KIND_LIST
    synonyms = synonyms or [entity_value]

    entity_type_path = entity_types_client.entity_type_path(
        project_id, entity_type_id)

    entity = dialogflow.types.EntityType.Entity()
    entity.value = entity_value
    entity.synonyms.extend(synonyms)

    response = entity_types_client.batch_create_entities(parent=entity_type_path, entities=[entity])

    print('Entity created: {}'.format(response))


if __name__ == '__main__':
    entity_type_id = "8dc2ad9e-e452-4fa2-8c66-dbb0b01b6421"
    project_id = 'bot-test-303915'
    entity_value = 'Object Oriented Programming'
    synonyms = ['oop']
    create_entity(project_id, entity_type_id, entity_value, synonyms)
