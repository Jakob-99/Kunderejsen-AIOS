"""Fetch a basic traffic report from Google Analytics 4.

Usage:
    python ga4_report.py --start-date 30daysAgo --end-date today
"""

import argparse
import os

from dotenv import load_dotenv
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from google.oauth2 import service_account

load_dotenv()


def build_client() -> BetaAnalyticsDataClient:
    key_file = os.environ["GA4_SERVICE_ACCOUNT_FILE"]
    credentials = service_account.Credentials.from_service_account_file(
        key_file, scopes=["https://www.googleapis.com/auth/analytics.readonly"]
    )
    return BetaAnalyticsDataClient(credentials=credentials)


def run_report(client: BetaAnalyticsDataClient, property_id: str, start_date: str, end_date: str):
    request = RunReportRequest(
        property=f"properties/{property_id}",
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
        dimensions=[Dimension(name="date")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="activeUsers"),
            Metric(name="conversions"),
        ],
        order_bys=[{"dimension": {"dimension_name": "date"}}],
    )
    return client.run_report(request)


def print_report(response) -> None:
    header = [dim.name for dim in response.dimension_headers] + [
        metric.name for metric in response.metric_headers
    ]
    print("\t".join(header))
    for row in response.rows:
        values = [dv.value for dv in row.dimension_values] + [mv.value for mv in row.metric_values]
        print("\t".join(values))


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a GA4 traffic report")
    parser.add_argument("--start-date", default="30daysAgo")
    parser.add_argument("--end-date", default="today")
    args = parser.parse_args()

    property_id = os.environ["GA4_PROPERTY_ID"]
    client = build_client()
    response = run_report(client, property_id, args.start_date, args.end_date)
    print_report(response)


if __name__ == "__main__":
    main()
