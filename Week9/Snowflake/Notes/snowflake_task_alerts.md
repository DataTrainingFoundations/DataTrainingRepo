# Snowflake Task Monitoring & Alerting Guide

## Question 1: How can I be notified when a Snowflake task completes or fails?

### Answer

Snowflake provides several ways to monitor task execution and receive
notifications.

### 1. Check Task Status (Built-in Monitoring)

Use system views:

``` sql
SELECT *
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY(
    TASK_NAME => 'MY_TASK',
    RESULT_LIMIT => 10
))
ORDER BY SCHEDULED_TIME DESC;
```

Key columns: - STATE → SUCCEEDED, FAILED, CANCELLED - ERROR_MESSAGE →
failure reason - COMPLETED_TIME

------------------------------------------------------------------------

### 2. Snowflake Alerts (Best Native Option)

``` sql
CREATE OR REPLACE ALERT task_failure_alert
  WAREHOUSE = MY_WH
  SCHEDULE = '5 MINUTE'
AS
SELECT *
FROM SNOWFLAKE.ACCOUNT_USAGE.TASK_HISTORY
WHERE STATE = 'FAILED'
  AND COMPLETED_TIME > DATEADD('minute', -5, CURRENT_TIMESTAMP());
```

------------------------------------------------------------------------

### 3. Email Notifications

``` sql
CALL SYSTEM$SEND_EMAIL(
  'my_email_integration',
  'you@example.com',
  'Snowflake Task Failed',
  'Your task MY_TASK has failed.'
);
```

------------------------------------------------------------------------

### 4. Stored Procedure Wrapper

``` sql
CREATE OR REPLACE PROCEDURE run_task_wrapper()
RETURNS STRING
LANGUAGE SQL
AS
$$
BEGIN
    RETURN 'SUCCESS';
EXCEPTION
    WHEN OTHER THEN
        CALL SYSTEM$SEND_EMAIL(...);
        RETURN 'FAILED';
END;
$$;
```

------------------------------------------------------------------------

### 5. Snowsight UI

Use UI to monitor task runs and failures visually.

------------------------------------------------------------------------

## Question 2: How else can I receive alerts besides email?

### Answer

### 1. Webhooks (Slack, Teams, PagerDuty)

Call external APIs using procedures or external functions.

------------------------------------------------------------------------

### 2. Slack / Teams Integration

Send JSON payloads via webhook.

------------------------------------------------------------------------

### 3. Event Streaming / Queues

Push failures to systems like Kafka, SNS, or Pub/Sub.

------------------------------------------------------------------------

### 4. Cloud Integrations

Use AWS Lambda, Azure Functions, or GCP Cloud Functions.

------------------------------------------------------------------------

### 5. Logging Table + Polling

Insert failures into a table and poll externally.

------------------------------------------------------------------------

## Recommended Architecture

Snowflake Task → Alert → Stored Procedure → Webhook (Slack/PagerDuty)

------------------------------------------------------------------------

-   Use TASK_HISTORY for monitoring
-   Use Alerts for automation
-   Use Webhooks for modern alerting
