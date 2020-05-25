from datetime import datetime


def get_datetime_by_formats(value):
    format_date = "%Y-%m-%dT%H:%M:%S.%f"
    try:
        result = datetime.strptime(value, format_date)
        return result
    except:
        try:
            format_date = format_date + 'Z'
            result = datetime.strptime(value, format_date)
            return result
        except:
            return None


def date_from_model(body, att_name):
    if "created_at" == att_name or "updated_at" == att_name:
        result = get_datetime_by_formats(
            body[att_name]
        )

        return result

    return None


def deserialize_body_to_model(body, model, custom_deserialize=None):
    for att_name, att_value in body.items():
        result = None
        if custom_deserialize:
            result = custom_deserialize(
                body=body,
                att_name=att_name
            )

        result = date_from_model(body, att_name) if not result else result
        if result:
            model[att_name] = result
            continue

        try:
            setattr(model, att_name, att_value)
        except Exception:
            print(
                'Error when add value into model: {}={}'.format(
                    att_name, att_value
                )
            )


    return model
