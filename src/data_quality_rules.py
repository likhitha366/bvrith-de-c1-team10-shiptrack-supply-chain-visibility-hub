"""
ShipTrack - Data Quality Rules

Week: 6
Layer: Trusted Silver
Purpose:
    Reusable PySpark data quality helper functions for the ShipTrack project.

These rules can be used to validate:
    - Shipment data
    - Package data
    - Hub / Zone reference data
    - Carrier data
    - Delivery data
"""


def required_field_rule(df, field_name):
    """
    Return records where a required field is NULL.

    Example:
        invalid_shipments = required_field_rule(
            silver_df,
            "shipment_id"
        )
    """
    return df.filter(df[field_name].isNull())


def non_negative_rule(df, field_name):
    """
    Return records where a numeric field is negative.

    Useful for:
        - package_weight
        - shipping_cost
        - delivery_days
        - package_quantity
    """
    return df.filter(df[field_name] < 0)


def duplicate_key_rule(df, key_field):
    """
    Return duplicate business keys and their counts.

    Example:
        duplicate_shipments = duplicate_key_rule(
            silver_df,
            "shipment_id"
        )
    """
    return (
        df.groupBy(key_field)
        .count()
        .filter("count > 1")
    )


def valid_reference_rule(
    fact_df,
    reference_df,
    fact_key,
    reference_key
):
    """
    Return records from fact_df where the reference key
    does not exist in the reference table.

    Useful for validating:
        - shipment zone_id against zone reference
        - shipment carrier_id against carrier reference
        - shipment hub_id against hub reference

    Example:
        invalid_zones = valid_reference_rule(
            silver_shipments,
            silver_zones,
            "zone_id",
            "zone_id"
        )
    """
    return fact_df.join(
        reference_df,
        fact_df[fact_key] == reference_df[reference_key],
        "left_anti"
    )


def valid_status_rule(df, field_name, valid_statuses):
    """
    Return records having an invalid shipment/delivery status.

    Example:
        valid_statuses = [
            "Booked",
            "In Transit",
            "Out for Delivery",
            "Delivered",
            "Cancelled"
        ]

        invalid_records = valid_status_rule(
            silver_df,
            "status",
            valid_statuses
        )
    """
    return df.filter(~df[field_name].isin(valid_statuses))


def valid_weight_rule(df, field_name="package_weight"):
    """
    Return records where package weight is zero or negative.
    """
    return df.filter(df[field_name] <= 0)


def valid_delivery_days_rule(df, field_name="delivery_days"):
    """
    Return records where delivery days are negative.
    """
    return df.filter(df[field_name] < 0)


def date_order_rule(
    df,
    pickup_date="pickup_date",
    delivery_date="delivery_date"
):
    """
    Return records where delivery date occurs
    before pickup date.
    """
    return df.filter(
        df[delivery_date] < df[pickup_date]
    )


def null_identifier_rule(df, identifier_fields):
    """
    Return records where any important identifier is NULL.

    Example:
        invalid_records = null_identifier_rule(
            silver_df,
            ["shipment_id", "customer_id", "carrier_id"]
        )
    """
    condition = None

    for field in identifier_fields:
        current_condition = df[field].isNull()

        if condition is None:
            condition = current_condition
        else:
            condition = condition | current_condition

    return df.filter(condition)
