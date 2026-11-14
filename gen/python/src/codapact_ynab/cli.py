"""Command line interface generated from the command model. Do not edit."""

# ruff: noqa: E501
from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import Any

from codapact.runtime.cli import (  # noqa: F401
    CliRuntime,
    compact,
    integer,
    json_value,
    number,
)

from .client import Client
from .client import _model as _api_model

RUNTIME = CliRuntime(program='ynab', env_prefix='YNAB', version='0.1.0', distribution='codapact-ynab', api_name='YNAB API Endpoints', api_version='1.91.0', model=_api_model, auth_plugin='', auth_config={})
RAW = argparse.RawDescriptionHelpFormatter



def _run_accounts_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.accounts.list(**kwargs)


def _run_accounts_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'name': args.p_name, 'type_': args.p_type, 'balance': args.p_balance})
    return client.accounts.create(**kwargs)


def _run_accounts_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_account_id', 'ACCOUNT_ID (or --account-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'account_id': getattr(args, 'p_account_id', None)})
    return client.accounts.get(**kwargs)


def _run_categories_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.categories.list(**kwargs)


def _run_categories_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'name': args.p_name, 'note': args.p_note, 'category_group_id': args.p_category_group_id, 'goal_target': args.p_goal_target, 'goal_target_date': args.p_goal_target_date, 'goal_needs_whole_amount': args.p_goal_needs_whole_amount, 'goal_frequency': args.p_goal_frequency})
    return client.categories.create(**kwargs)


def _run_categories_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_category_id', 'CATEGORY_ID (or --category-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'category_id': getattr(args, 'p_category_id', None)})
    return client.categories.get(**kwargs)


def _run_categories_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_category_id', 'CATEGORY_ID (or --category-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'category_id': getattr(args, 'p_category_id', None), 'name': args.p_name, 'note': args.p_note, 'category_group_id': args.p_category_group_id, 'goal_target': args.p_goal_target, 'goal_target_date': args.p_goal_target_date, 'goal_needs_whole_amount': args.p_goal_needs_whole_amount, 'goal_frequency': args.p_goal_frequency})
    return client.categories.update(**kwargs)


def _run_categories_get_month(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_month', 'YYYY-MM-DD (or --month)')
    RUNTIME.require(args, 'p_category_id', 'CATEGORY_ID (or --category-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'month': getattr(args, 'p_month', None), 'category_id': getattr(args, 'p_category_id', None)})
    return client.categories.get_month(**kwargs)


def _run_categories_update_month(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_month', 'YYYY-MM-DD (or --month)')
    RUNTIME.require(args, 'p_category_id', 'CATEGORY_ID (or --category-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'month': getattr(args, 'p_month', None), 'category_id': getattr(args, 'p_category_id', None), 'budgeted': args.p_budgeted})
    return client.categories.update_month(**kwargs)


def _run_categories_create_group(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'name': args.p_name})
    return client.categories.create_group(**kwargs)


def _run_categories_update_group(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_category_group_id', 'CATEGORY_GROUP_ID (or --category-group-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'category_group_id': getattr(args, 'p_category_group_id', None), 'name': args.p_name})
    return client.categories.update_group(**kwargs)


def _run_money_movements_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id})
    return client.money_movements.list(**kwargs)


def _run_money_movements_list_by_month(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_month', 'YYYY-MM-DD (or --month)')
    kwargs = compact({'plan_id': args.p_plan_id, 'month': getattr(args, 'p_month', None)})
    return client.money_movements.list_by_month(**kwargs)


def _run_money_movements_list_groups(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id})
    return client.money_movements.list_groups(**kwargs)


def _run_money_movements_list_groups_by_month(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_month', 'YYYY-MM-DD (or --month)')
    kwargs = compact({'plan_id': args.p_plan_id, 'month': getattr(args, 'p_month', None)})
    return client.money_movements.list_groups_by_month(**kwargs)


def _run_months_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.months.list(**kwargs)


def _run_months_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_month', 'YYYY-MM-DD (or --month)')
    kwargs = compact({'plan_id': args.p_plan_id, 'month': getattr(args, 'p_month', None)})
    return client.months.get(**kwargs)


def _run_payee_locations_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id})
    return client.payee_locations.list(**kwargs)


def _run_payee_locations_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_payee_location_id', 'PAYEE_LOCATION_ID (or --payee-location-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'payee_location_id': getattr(args, 'p_payee_location_id', None)})
    return client.payee_locations.get(**kwargs)


def _run_payee_locations_list_by_payee(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_payee_id', 'PAYEE_ID (or --payee-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'payee_id': getattr(args, 'p_payee_id', None)})
    return client.payee_locations.list_by_payee(**kwargs)


def _run_payees_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.payees.list(**kwargs)


def _run_payees_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'name': args.p_name})
    return client.payees.create(**kwargs)


def _run_payees_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_payee_id', 'PAYEE_ID (or --payee-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'payee_id': getattr(args, 'p_payee_id', None)})
    return client.payees.get(**kwargs)


def _run_payees_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_payee_id', 'PAYEE_ID (or --payee-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'payee_id': getattr(args, 'p_payee_id', None), 'name': args.p_name})
    return client.payees.update(**kwargs)


def _run_plans_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'include_accounts': args.p_include_accounts})
    return client.plans.list(**kwargs)


def _run_plans_get(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.plans.get(**kwargs)


def _run_plans_get_settings(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id})
    return client.plans.get_settings(**kwargs)


def _run_scheduled_transactions_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.scheduled_transactions.list(**kwargs)


def _run_scheduled_transactions_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'account_id': args.p_account_id, 'date': args.p_date, 'amount': args.p_amount, 'payee_id': args.p_payee_id, 'payee_name': args.p_payee_name, 'category_id': args.p_category_id, 'memo': args.p_memo, 'flag_color': args.p_flag_color, 'frequency': args.p_frequency})
    return client.scheduled_transactions.create(**kwargs)


def _run_scheduled_transactions_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_scheduled_transaction_id', 'SCHEDULED_TRANSACTION_ID (or --scheduled-transaction-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'scheduled_transaction_id': getattr(args, 'p_scheduled_transaction_id', None)})
    return client.scheduled_transactions.get(**kwargs)


def _run_scheduled_transactions_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_scheduled_transaction_id', 'SCHEDULED_TRANSACTION_ID (or --scheduled-transaction-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'scheduled_transaction_id': getattr(args, 'p_scheduled_transaction_id', None), 'account_id': args.p_account_id, 'date': args.p_date, 'amount': args.p_amount, 'payee_id': args.p_payee_id, 'payee_name': args.p_payee_name, 'category_id': args.p_category_id, 'memo': args.p_memo, 'flag_color': args.p_flag_color, 'frequency': args.p_frequency})
    return client.scheduled_transactions.update(**kwargs)


def _run_scheduled_transactions_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_scheduled_transaction_id', 'SCHEDULED_TRANSACTION_ID (or --scheduled-transaction-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'scheduled_transaction_id': getattr(args, 'p_scheduled_transaction_id', None)})
    RUNTIME.confirm(args, 'scheduled-transactions delete')
    return client.scheduled_transactions.delete(**kwargs)


def _run_transactions_list(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'since_date': args.p_since_date, 'until_date': args.p_until_date, 'type_': args.p_type, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.transactions.list(**kwargs)


def _run_transactions_create(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'transaction': args.p_transaction, 'transactions': args.p_transactions})
    return client.transactions.create(**kwargs)


def _run_transactions_update_many(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id, 'transactions': args.p_transactions})
    return client.transactions.update_many(**kwargs)


def _run_transactions_import(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({'plan_id': args.p_plan_id})
    return client.transactions.import_(**kwargs)


def _run_transactions_get(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_transaction_id', 'TRANSACTION_ID (or --transaction-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'transaction_id': getattr(args, 'p_transaction_id', None)})
    return client.transactions.get(**kwargs)


def _run_transactions_update(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_transaction_id', 'TRANSACTION_ID (or --transaction-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'transaction_id': getattr(args, 'p_transaction_id', None), 'account_id': args.p_account_id, 'date': args.p_date, 'amount': args.p_amount, 'payee_id': args.p_payee_id, 'payee_name': args.p_payee_name, 'category_id': args.p_category_id, 'memo': args.p_memo, 'cleared': args.p_cleared, 'approved': args.p_approved, 'flag_color': args.p_flag_color, 'subtransactions': args.p_subtransactions})
    return client.transactions.update(**kwargs)


def _run_transactions_delete(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_transaction_id', 'TRANSACTION_ID (or --transaction-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'transaction_id': getattr(args, 'p_transaction_id', None)})
    RUNTIME.confirm(args, 'transactions delete')
    return client.transactions.delete(**kwargs)


def _run_transactions_list_by_account(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_account_id', 'ACCOUNT_ID (or --account-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'account_id': getattr(args, 'p_account_id', None), 'since_date': args.p_since_date, 'until_date': args.p_until_date, 'type_': args.p_type, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.transactions.list_by_account(**kwargs)


def _run_transactions_list_by_category(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_category_id', 'CATEGORY_ID (or --category-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'category_id': getattr(args, 'p_category_id', None), 'since_date': args.p_since_date, 'until_date': args.p_until_date, 'type_': args.p_type, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.transactions.list_by_category(**kwargs)


def _run_transactions_list_by_payee(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_payee_id', 'PAYEE_ID (or --payee-id)')
    kwargs = compact({'plan_id': args.p_plan_id, 'payee_id': getattr(args, 'p_payee_id', None), 'since_date': args.p_since_date, 'until_date': args.p_until_date, 'type_': args.p_type, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.transactions.list_by_payee(**kwargs)


def _run_transactions_list_by_month(client: Client, args: argparse.Namespace) -> Any:
    RUNTIME.require(args, 'p_month', 'MONTH (or --month)')
    kwargs = compact({'plan_id': args.p_plan_id, 'month': getattr(args, 'p_month', None), 'since_date': args.p_since_date, 'until_date': args.p_until_date, 'type_': args.p_type, 'last_knowledge_of_server': args.p_last_knowledge_of_server})
    return client.transactions.list_by_month(**kwargs)


def _run_user_get(client: Client, args: argparse.Namespace) -> Any:
    kwargs = compact({})
    return client.user.get(**kwargs)

def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    common = argparse.ArgumentParser(add_help=False)
    RUNTIME.add_global_options(common, hidden=True)
    parser = RUNTIME.parser(
        description='Our API uses a REST based design, leverages the JSON data format, and relies\nupon HTTPS for transport. We respond with meaningful HTTP response codes and\nif an error occurs, we include error details in the response body.\n\nRead the [API Documentation](https://api.ynab.com) for more information about\nthe API, including how to obtain an access token and how to use it to make\nrequests.',
        epilog="credentials:\n  bearer: set YNAB_BEARER, YNAB_BEARER_COMMAND, or run 'ynab auth login'",
        examples=['ynab accounts get ACCOUNT_ID'],
    )
    commands = parser.add_subparsers(dest="command", metavar="COMMAND", required=True)
    g_accounts = commands.add_parser('accounts', help='create, get, list', description="Run 'ynab accounts COMMAND --help' for a command's options and examples.")
    g_accounts_commands = g_accounts.add_subparsers(dest="g_accounts", metavar="COMMAND", required=True)
    c = g_accounts_commands.add_parser('list', parents=[common], help='Get all accounts', description='Returns all accounts', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab accounts list']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_accounts_list, flags={'plan_id': '--plan-id', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_accounts'})
    c = g_accounts_commands.add_parser('create', parents=[common], help='Create an account', description='Creates a new account', usage='%(prog)s --name NAME --type {checking,savings,cash,creditCard,otherAsset,otherLiability} --balance BALANCE [options]', epilog=RUNTIME.command_epilog(['ynab accounts create --name NAME --type checking --balance BALANCE', 'ynab accounts create --name NAME --type checking --balance BALANCE --dry-run']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan ("last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan) (default: last-used)')
    c.add_argument('--name', dest='p_name', metavar='NAME', required=True, help='The name of the account')
    c.add_argument('--type', dest='p_type', choices=['checking', 'savings', 'cash', 'creditCard', 'otherAsset', 'otherLiability'], required=True)
    c.add_argument('--balance', dest='p_balance', type=integer, metavar='BALANCE', required=True, help='The current balance of the account in milliunits format')
    c.set_defaults(handler=_run_accounts_create, flags={'plan_id': '--plan-id', 'body.account.name': '--name', 'body.account.type': '--type', 'body.account.balance': '--balance'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_account'})
    c = g_accounts_commands.add_parser('get', parents=[common], help='Get an account', description='Returns a single account', usage='%(prog)s ACCOUNT_ID [options]', epilog=RUNTIME.command_epilog(['ynab accounts get ACCOUNT_ID']), formatter_class=RAW)
    c.add_argument('p_account_id', metavar='ACCOUNT_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the account')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--account-id', dest='p_account_id', default=argparse.SUPPRESS, metavar='ACCOUNT_ID', help='same as ACCOUNT_ID')
    c.set_defaults(handler=_run_accounts_get, flags={'plan_id': '--plan-id', 'account_id': '--account-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_account_by_id'})
    g_categories = commands.add_parser('categories', help='create, create-group, get, … (8 commands)', description="Run 'ynab categories COMMAND --help' for a command's options and examples.")
    g_categories_commands = g_categories.add_subparsers(dest="g_categories", metavar="COMMAND", required=True)
    c = g_categories_commands.add_parser('list', parents=[common], help='Get all categories', description='Returns all categories grouped by category group. Amounts (assigned, activity,\navailable, etc.) are specific to the current plan month (UTC).', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab categories list']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_categories_list, flags={'plan_id': '--plan-id', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_categories'})
    c = g_categories_commands.add_parser('create', parents=[common], help='Create a category', description='Creates a new category', usage='%(prog)s --name NAME --category-group-id CATEGORY_GROUP_ID [options]', epilog=RUNTIME.command_epilog(['ynab categories create --name NAME --category-group-id CATEGORY_GROUP_ID', 'ynab categories create --name NAME --category-group-id CATEGORY_GROUP_ID --dry-run']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan ("last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan) (default: last-used)')
    c.add_argument('--name', dest='p_name', metavar='NAME', required=True)
    c.add_argument('--note', dest='p_note', metavar='NOTE')
    c.add_argument('--category-group-id', dest='p_category_group_id', metavar='CATEGORY_GROUP_ID', required=True, help='The id of the category group to which this category belongs.  An internal category group may not be specified.')
    c.add_argument('--goal-target', dest='p_goal_target', type=integer, metavar='GOAL_TARGET', help="The goal target amount in milliunits format.  If value is specified and goal has not already been configured for category, a monthly goal will be created for the category with this target amount.  If goal_type is not specified, it will default to 'NEED', or to 'MF' for Credit Card Payment categories and 'DEBT' for categories paired to a loan account. Must not be negative. When updating a category, passing null removes any existing target. Passing 0 does too, except for a Credit Card Payment category's 'TBD' (Pay Off Balance by Date) target, where 0 is a valid amount because the card's balance sets it. Use null to remove that target.")
    c.add_argument('--goal-target-date', dest='p_goal_target_date', metavar='YYYY-MM-DD', help="The goal target date in ISO format (e.g. 2016-12-01). Not supported for categories paired to a loan account. When combined with a goal_frequency of 'monthly' or 'yearly', this is the date the recurring target is next due. Required for yearly targets, so it cannot be removed from one.")
    c.add_argument('--goal-needs-whole-amount', dest='p_goal_needs_whole_amount', action=argparse.BooleanOptionalAction, help="Whether the goal requires the full target amount each period. Only supported for 'NEED' goals, and not supported for Credit Card Payment categories or categories paired to a loan account. When true, the goal is configured as 'Set aside another...'. When false, the goal is configured as 'Refill up to...'.")
    c.add_argument('--goal-frequency', dest='p_goal_frequency', choices=['monthly', 'weekly', 'yearly'], help="When specified, configures a recurring 'NEED' target of goal_target that repeats at this frequency, replacing any existing target. Requires goal_target. 'yearly' also requires goal_target_date, the date the target is next due. 'monthly' accepts an optional goal_target_date, and 'weekly' cannot be combined with goal_target_date. Not supported for Credit Card Payment categories or categories paired to a loan account. Omit to leave an existing target's cadence unchanged.")
    c.set_defaults(handler=_run_categories_create, flags={'plan_id': '--plan-id', 'body.category.name': '--name', 'body.category.note': '--note', 'body.category.category_group_id': '--category-group-id', 'body.category.goal_target': '--goal-target', 'body.category.goal_target_date': '--goal-target-date', 'body.category.goal_needs_whole_amount': '--goal-needs-whole-amount', 'body.category.goal_frequency': '--goal-frequency'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_category'})
    c = g_categories_commands.add_parser('get', parents=[common], help='Get a category', description='Returns a single category. Amounts (assigned, activity, available, etc.) are\nspecific to the current plan month (UTC).', usage='%(prog)s CATEGORY_ID [options]', epilog=RUNTIME.command_epilog(['ynab categories get CATEGORY_ID']), formatter_class=RAW)
    c.add_argument('p_category_id', metavar='CATEGORY_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the category')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--category-id', dest='p_category_id', default=argparse.SUPPRESS, metavar='CATEGORY_ID', help='same as CATEGORY_ID')
    c.set_defaults(handler=_run_categories_get, flags={'plan_id': '--plan-id', 'category_id': '--category-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_category_by_id'})
    c = g_categories_commands.add_parser('update', parents=[common], help='Update a category', description='Update a category', usage='%(prog)s CATEGORY_ID [options]', epilog=RUNTIME.command_epilog(['ynab categories update CATEGORY_ID', 'ynab categories update CATEGORY_ID --dry-run']), formatter_class=RAW)
    c.add_argument('p_category_id', metavar='CATEGORY_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the category')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--category-id', dest='p_category_id', default=argparse.SUPPRESS, metavar='CATEGORY_ID', help='same as CATEGORY_ID')
    c.add_argument('--name', dest='p_name', metavar='NAME')
    c.add_argument('--note', dest='p_note', metavar='NOTE')
    c.add_argument('--category-group-id', dest='p_category_group_id', metavar='CATEGORY_GROUP_ID', help='The id of the category group to which this category belongs.  An internal category group may not be specified.')
    c.add_argument('--goal-target', dest='p_goal_target', type=integer, metavar='GOAL_TARGET', help="The goal target amount in milliunits format.  If value is specified and goal has not already been configured for category, a monthly goal will be created for the category with this target amount.  If goal_type is not specified, it will default to 'NEED', or to 'MF' for Credit Card Payment categories and 'DEBT' for categories paired to a loan account. Must not be negative. When updating a category, passing null removes any existing target. Passing 0 does too, except for a Credit Card Payment category's 'TBD' (Pay Off Balance by Date) target, where 0 is a valid amount because the card's balance sets it. Use null to remove that target.")
    c.add_argument('--goal-target-date', dest='p_goal_target_date', metavar='YYYY-MM-DD', help="The goal target date in ISO format (e.g. 2016-12-01). Not supported for categories paired to a loan account. When combined with a goal_frequency of 'monthly' or 'yearly', this is the date the recurring target is next due. Required for yearly targets, so it cannot be removed from one.")
    c.add_argument('--goal-needs-whole-amount', dest='p_goal_needs_whole_amount', action=argparse.BooleanOptionalAction, help="Whether the goal requires the full target amount each period. Only supported for 'NEED' goals, and not supported for Credit Card Payment categories or categories paired to a loan account. When true, the goal is configured as 'Set aside another...'. When false, the goal is configured as 'Refill up to...'.")
    c.add_argument('--goal-frequency', dest='p_goal_frequency', choices=['monthly', 'weekly', 'yearly'], help="When specified, configures a recurring 'NEED' target of goal_target that repeats at this frequency, replacing any existing target. Requires goal_target. 'yearly' also requires goal_target_date, the date the target is next due. 'monthly' accepts an optional goal_target_date, and 'weekly' cannot be combined with goal_target_date. Not supported for Credit Card Payment categories or categories paired to a loan account. Omit to leave an existing target's cadence unchanged.")
    c.set_defaults(handler=_run_categories_update, flags={'plan_id': '--plan-id', 'category_id': '--category-id', 'body.category.name': '--name', 'body.category.note': '--note', 'body.category.category_group_id': '--category-group-id', 'body.category.goal_target': '--goal-target', 'body.category.goal_target_date': '--goal-target-date', 'body.category.goal_needs_whole_amount': '--goal-needs-whole-amount', 'body.category.goal_frequency': '--goal-frequency'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_category', 'requires_one_of': [['--name', '--note', '--category-group-id', '--goal-target', '--goal-target-date', '--goal-needs-whole-amount', '--goal-frequency']]})
    c = g_categories_commands.add_parser('get-month', parents=[common], help='Get a category for a specific plan month', description='Returns a single category for a specific plan month. Amounts (assigned,\nactivity, available, etc.) are specific to the current plan month (UTC).', usage='%(prog)s YYYY-MM-DD CATEGORY_ID [options]', epilog=RUNTIME.command_epilog(['ynab categories get-month YYYY-MM-DD CATEGORY_ID']), formatter_class=RAW)
    c.add_argument('p_month', metavar='YYYY-MM-DD', nargs='?', default=argparse.SUPPRESS, help='The plan month in ISO format (e.g. 2016-12-01) ("current" can also be used to specify the current calendar month (UTC))')
    c.add_argument('p_category_id', metavar='CATEGORY_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the category')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--month', dest='p_month', default=argparse.SUPPRESS, metavar='YYYY-MM-DD', help='same as YYYY-MM-DD')
    c.add_argument('--category-id', dest='p_category_id', default=argparse.SUPPRESS, metavar='CATEGORY_ID', help='same as CATEGORY_ID')
    c.set_defaults(handler=_run_categories_get_month, flags={'plan_id': '--plan-id', 'month': '--month', 'category_id': '--category-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_month_category_by_id'})
    c = g_categories_commands.add_parser('update-month', parents=[common], help='Update a category for a specific month', description='Update a category for a specific month. Only `budgeted` (assigned) amount can\nbe updated.', usage='%(prog)s YYYY-MM-DD CATEGORY_ID --budgeted BUDGETED [options]', epilog=RUNTIME.command_epilog(['ynab categories update-month YYYY-MM-DD CATEGORY_ID --budgeted BUDGETED', 'ynab categories update-month YYYY-MM-DD CATEGORY_ID --budgeted BUDGETED --dry-run']), formatter_class=RAW)
    c.add_argument('p_month', metavar='YYYY-MM-DD', nargs='?', default=argparse.SUPPRESS, help='The plan month in ISO format (e.g. 2016-12-01) ("current" can also be used to specify the current calendar month (UTC))')
    c.add_argument('p_category_id', metavar='CATEGORY_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the category')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--month', dest='p_month', default=argparse.SUPPRESS, metavar='YYYY-MM-DD', help='same as YYYY-MM-DD')
    c.add_argument('--category-id', dest='p_category_id', default=argparse.SUPPRESS, metavar='CATEGORY_ID', help='same as CATEGORY_ID')
    c.add_argument('--budgeted', dest='p_budgeted', type=integer, metavar='BUDGETED', required=True, help='Assigned (budgeted) amount in milliunits format')
    c.set_defaults(handler=_run_categories_update_month, flags={'plan_id': '--plan-id', 'month': '--month', 'category_id': '--category-id', 'body.category.budgeted': '--budgeted'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_month_category'})
    c = g_categories_commands.add_parser('create-group', parents=[common], help='Create a category group', description='Creates a new category group', usage='%(prog)s --name NAME [options]', epilog=RUNTIME.command_epilog(['ynab categories create-group --name NAME', 'ynab categories create-group --name NAME --dry-run']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan ("last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan) (default: last-used)')
    c.add_argument('--name', dest='p_name', metavar='NAME', required=True, help='The name of the category group. The name must be a maximum of 50 characters.')
    c.set_defaults(handler=_run_categories_create_group, flags={'plan_id': '--plan-id', 'body.category_group.name': '--name'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_category_group'})
    c = g_categories_commands.add_parser('update-group', parents=[common], help='Update a category group', description='Update a category group', usage='%(prog)s CATEGORY_GROUP_ID --name NAME [options]', epilog=RUNTIME.command_epilog(['ynab categories update-group CATEGORY_GROUP_ID --name NAME', 'ynab categories update-group CATEGORY_GROUP_ID --name NAME --dry-run']), formatter_class=RAW)
    c.add_argument('p_category_group_id', metavar='CATEGORY_GROUP_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the category group')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--category-group-id', dest='p_category_group_id', default=argparse.SUPPRESS, metavar='CATEGORY_GROUP_ID', help='same as CATEGORY_GROUP_ID')
    c.add_argument('--name', dest='p_name', metavar='NAME', required=True, help='The name of the category group. The name must be a maximum of 50 characters.')
    c.set_defaults(handler=_run_categories_update_group, flags={'plan_id': '--plan-id', 'category_group_id': '--category-group-id', 'body.category_group.name': '--name'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_category_group'})
    g_money_movements = commands.add_parser('money-movements', help='list, list-by-month, list-groups, list-groups-by-month', description="Run 'ynab money-movements COMMAND --help' for a command's options and examples.")
    g_money_movements_commands = g_money_movements.add_subparsers(dest="g_money_movements", metavar="COMMAND", required=True)
    c = g_money_movements_commands.add_parser('list', parents=[common], help='Get all money movements', description='Returns all money movements', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab money-movements list']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.set_defaults(handler=_run_money_movements_list, flags={'plan_id': '--plan-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_money_movements'})
    c = g_money_movements_commands.add_parser('list-by-month', parents=[common], help='Get money movements for a plan month', description='Returns all money movements for a specific month', usage='%(prog)s YYYY-MM-DD [options]', epilog=RUNTIME.command_epilog(['ynab money-movements list-by-month YYYY-MM-DD']), formatter_class=RAW)
    c.add_argument('p_month', metavar='YYYY-MM-DD', nargs='?', default=argparse.SUPPRESS, help='The plan month in ISO format (e.g. 2016-12-01) ("current" can also be used to specify the current calendar month (UTC))')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--month', dest='p_month', default=argparse.SUPPRESS, metavar='YYYY-MM-DD', help='same as YYYY-MM-DD')
    c.set_defaults(handler=_run_money_movements_list_by_month, flags={'plan_id': '--plan-id', 'month': '--month'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_money_movements_by_month'})
    c = g_money_movements_commands.add_parser('list-groups', parents=[common], help='Get all money movement groups', description='Returns all money movement groups', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab money-movements list-groups']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.set_defaults(handler=_run_money_movements_list_groups, flags={'plan_id': '--plan-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_money_movement_groups'})
    c = g_money_movements_commands.add_parser('list-groups-by-month', parents=[common], help='Get money movement groups for a plan month', description='Returns all money movement groups for a specific month', usage='%(prog)s YYYY-MM-DD [options]', epilog=RUNTIME.command_epilog(['ynab money-movements list-groups-by-month YYYY-MM-DD']), formatter_class=RAW)
    c.add_argument('p_month', metavar='YYYY-MM-DD', nargs='?', default=argparse.SUPPRESS, help='The plan month in ISO format (e.g. 2016-12-01) ("current" can also be used to specify the current calendar month (UTC))')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--month', dest='p_month', default=argparse.SUPPRESS, metavar='YYYY-MM-DD', help='same as YYYY-MM-DD')
    c.set_defaults(handler=_run_money_movements_list_groups_by_month, flags={'plan_id': '--plan-id', 'month': '--month'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_money_movement_groups_by_month'})
    g_months = commands.add_parser('months', help='get, list', description="Run 'ynab months COMMAND --help' for a command's options and examples.")
    g_months_commands = g_months.add_subparsers(dest="g_months", metavar="COMMAND", required=True)
    c = g_months_commands.add_parser('list', parents=[common], help='Get all plan months', description='Returns all plan months', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab months list']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_months_list, flags={'plan_id': '--plan-id', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_plan_months'})
    c = g_months_commands.add_parser('get', parents=[common], help='Get a plan month', description='Returns a single plan month', usage='%(prog)s YYYY-MM-DD [options]', epilog=RUNTIME.command_epilog(['ynab months get YYYY-MM-DD']), formatter_class=RAW)
    c.add_argument('p_month', metavar='YYYY-MM-DD', nargs='?', default=argparse.SUPPRESS, help='The plan month in ISO format (e.g. 2016-12-01) ("current" can also be used to specify the current calendar month (UTC))')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--month', dest='p_month', default=argparse.SUPPRESS, metavar='YYYY-MM-DD', help='same as YYYY-MM-DD')
    c.set_defaults(handler=_run_months_get, flags={'plan_id': '--plan-id', 'month': '--month'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_plan_month'})
    g_payee_locations = commands.add_parser('payee-locations', help='get, list, list-by-payee', description="Run 'ynab payee-locations COMMAND --help' for a command's options and examples.")
    g_payee_locations_commands = g_payee_locations.add_subparsers(dest="g_payee_locations", metavar="COMMAND", required=True)
    c = g_payee_locations_commands.add_parser('list', parents=[common], help='Get all payee locations', description='Returns all payee locations', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab payee-locations list']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.set_defaults(handler=_run_payee_locations_list, flags={'plan_id': '--plan-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_payee_locations'})
    c = g_payee_locations_commands.add_parser('get', parents=[common], help='Get a payee location', description='Returns a single payee location', usage='%(prog)s PAYEE_LOCATION_ID [options]', epilog=RUNTIME.command_epilog(['ynab payee-locations get PAYEE_LOCATION_ID']), formatter_class=RAW)
    c.add_argument('p_payee_location_id', metavar='PAYEE_LOCATION_ID', nargs='?', default=argparse.SUPPRESS, help='id of payee location')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--payee-location-id', dest='p_payee_location_id', default=argparse.SUPPRESS, metavar='PAYEE_LOCATION_ID', help='same as PAYEE_LOCATION_ID')
    c.set_defaults(handler=_run_payee_locations_get, flags={'plan_id': '--plan-id', 'payee_location_id': '--payee-location-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_payee_location_by_id'})
    c = g_payee_locations_commands.add_parser('list-by-payee', parents=[common], help='Get all locations for a payee', description='Returns all payee locations for a specified payee', usage='%(prog)s PAYEE_ID [options]', epilog=RUNTIME.command_epilog(['ynab payee-locations list-by-payee PAYEE_ID']), formatter_class=RAW)
    c.add_argument('p_payee_id', metavar='PAYEE_ID', nargs='?', default=argparse.SUPPRESS, help='id of payee')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--payee-id', dest='p_payee_id', default=argparse.SUPPRESS, metavar='PAYEE_ID', help='same as PAYEE_ID')
    c.set_defaults(handler=_run_payee_locations_list_by_payee, flags={'plan_id': '--plan-id', 'payee_id': '--payee-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_payee_locations_by_payee'})
    g_payees = commands.add_parser('payees', help='create, get, list, update', description="Run 'ynab payees COMMAND --help' for a command's options and examples.")
    g_payees_commands = g_payees.add_subparsers(dest="g_payees", metavar="COMMAND", required=True)
    c = g_payees_commands.add_parser('list', parents=[common], help='Get all payees', description='Returns all payees', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab payees list']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_payees_list, flags={'plan_id': '--plan-id', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_payees'})
    c = g_payees_commands.add_parser('create', parents=[common], help='Create a payee', description='Creates a new payee', usage='%(prog)s --name NAME [options]', epilog=RUNTIME.command_epilog(['ynab payees create --name NAME', 'ynab payees create --name NAME --dry-run']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--name', dest='p_name', metavar='NAME', required=True, help='The name of the payee.')
    c.set_defaults(handler=_run_payees_create, flags={'plan_id': '--plan-id', 'body.payee.name': '--name'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_payee'})
    c = g_payees_commands.add_parser('get', parents=[common], help='Get a payee', description='Returns a single payee', usage='%(prog)s PAYEE_ID [options]', epilog=RUNTIME.command_epilog(['ynab payees get PAYEE_ID']), formatter_class=RAW)
    c.add_argument('p_payee_id', metavar='PAYEE_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the payee')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--payee-id', dest='p_payee_id', default=argparse.SUPPRESS, metavar='PAYEE_ID', help='same as PAYEE_ID')
    c.set_defaults(handler=_run_payees_get, flags={'plan_id': '--plan-id', 'payee_id': '--payee-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_payee_by_id'})
    c = g_payees_commands.add_parser('update', parents=[common], help='Update a payee', description='Update a payee', usage='%(prog)s PAYEE_ID [options]', epilog=RUNTIME.command_epilog(['ynab payees update PAYEE_ID', 'ynab payees update PAYEE_ID --dry-run']), formatter_class=RAW)
    c.add_argument('p_payee_id', metavar='PAYEE_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the payee')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--payee-id', dest='p_payee_id', default=argparse.SUPPRESS, metavar='PAYEE_ID', help='same as PAYEE_ID')
    c.add_argument('--name', dest='p_name', metavar='NAME', help='The name of the payee.')
    c.set_defaults(handler=_run_payees_update, flags={'plan_id': '--plan-id', 'payee_id': '--payee-id', 'body.payee.name': '--name'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_payee', 'requires_one_of': [['--name']]})
    g_plans = commands.add_parser('plans', help='get, get-settings, list', description="Run 'ynab plans COMMAND --help' for a command's options and examples.")
    g_plans_commands = g_plans.add_subparsers(dest="g_plans", metavar="COMMAND", required=True)
    c = g_plans_commands.add_parser('list', parents=[common], help='Get all plans', description='Returns plans list with summary information', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab plans list']), formatter_class=RAW)
    c.add_argument('--include-accounts', dest='p_include_accounts', action=argparse.BooleanOptionalAction, help='Whether to include the list of plan accounts')
    c.set_defaults(handler=_run_plans_list, flags={'include_accounts': '--include-accounts'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_plans'})
    c = g_plans_commands.add_parser('get', parents=[common], help='Get a plan', description='Returns a single plan with all related entities. This resource is effectively\na full plan export.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab plans get']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_plans_get, flags={'plan_id': '--plan-id', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_plan_by_id'})
    c = g_plans_commands.add_parser('get-settings', parents=[common], help='Get plan settings', description='Returns settings for a plan', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab plans get-settings']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.set_defaults(handler=_run_plans_get_settings, flags={'plan_id': '--plan-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_plan_settings_by_id'})
    g_scheduled_transactions = commands.add_parser('scheduled-transactions', help='create, delete, get, … (5 commands)', description="Run 'ynab scheduled-transactions COMMAND --help' for a command's options and examples.")
    g_scheduled_transactions_commands = g_scheduled_transactions.add_subparsers(dest="g_scheduled_transactions", metavar="COMMAND", required=True)
    c = g_scheduled_transactions_commands.add_parser('list', parents=[common], help='Get all scheduled transactions', description='Returns all scheduled transactions', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab scheduled-transactions list']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_scheduled_transactions_list, flags={'plan_id': '--plan-id', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_scheduled_transactions'})
    c = g_scheduled_transactions_commands.add_parser('create', parents=[common], help='Create a scheduled transaction', description='Creates a single scheduled transaction (a transaction with a future date).', usage='%(prog)s --account-id ACCOUNT_ID --date YYYY-MM-DD [options]', epilog=RUNTIME.command_epilog(['ynab scheduled-transactions create --account-id ACCOUNT_ID --date YYYY-MM-DD', 'ynab scheduled-transactions create --account-id ACCOUNT_ID --date YYYY-MM-DD --dry-run']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--account-id', dest='p_account_id', metavar='ACCOUNT_ID', required=True)
    c.add_argument('--date', dest='p_date', metavar='YYYY-MM-DD', required=True, help='The scheduled transaction date in ISO format (e.g. 2016-12-01).  This should be a future date no more than 5 years into the future.')
    c.add_argument('--amount', dest='p_amount', type=integer, metavar='AMOUNT', help='The scheduled transaction amount in milliunits format.')
    c.add_argument('--payee-id', dest='p_payee_id', metavar='PAYEE_ID', help='The payee for the scheduled transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as `transfer_payee_id` on the account resource.')
    c.add_argument('--payee-name', dest='p_payee_name', metavar='PAYEE_NAME', help='The payee name for the the scheduled transaction.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a payee with the same name or (2) creation of a new payee.')
    c.add_argument('--category-id', dest='p_category_id', metavar='CATEGORY_ID', help='The category for the scheduled transaction. Credit Card Payment categories are not permitted. Creating a split scheduled transaction is not currently supported.')
    c.add_argument('--memo', dest='p_memo', metavar='MEMO')
    c.add_argument('--flag-color', dest='p_flag_color', choices=['red', 'orange', 'yellow', 'green', 'blue', 'purple', ''])
    c.add_argument('--frequency', dest='p_frequency', choices=['never', 'daily', 'weekly', 'everyOtherWeek', 'twiceAMonth', 'every4Weeks', 'monthly', 'everyOtherMonth', 'every3Months', 'every4Months', 'twiceAYear', 'yearly', 'everyOtherYear'])
    c.set_defaults(handler=_run_scheduled_transactions_create, flags={'plan_id': '--plan-id', 'body.scheduled_transaction.account_id': '--account-id', 'body.scheduled_transaction.date': '--date', 'body.scheduled_transaction.amount': '--amount', 'body.scheduled_transaction.payee_id': '--payee-id', 'body.scheduled_transaction.payee_name': '--payee-name', 'body.scheduled_transaction.category_id': '--category-id', 'body.scheduled_transaction.memo': '--memo', 'body.scheduled_transaction.flag_color': '--flag-color', 'body.scheduled_transaction.frequency': '--frequency'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_scheduled_transaction'})
    c = g_scheduled_transactions_commands.add_parser('get', parents=[common], help='Get a scheduled transaction', description='Returns a single scheduled transaction', usage='%(prog)s SCHEDULED_TRANSACTION_ID [options]', epilog=RUNTIME.command_epilog(['ynab scheduled-transactions get SCHEDULED_TRANSACTION_ID']), formatter_class=RAW)
    c.add_argument('p_scheduled_transaction_id', metavar='SCHEDULED_TRANSACTION_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the scheduled transaction')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--scheduled-transaction-id', dest='p_scheduled_transaction_id', default=argparse.SUPPRESS, metavar='SCHEDULED_TRANSACTION_ID', help='same as SCHEDULED_TRANSACTION_ID')
    c.set_defaults(handler=_run_scheduled_transactions_get, flags={'plan_id': '--plan-id', 'scheduled_transaction_id': '--scheduled-transaction-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_scheduled_transaction_by_id'})
    c = g_scheduled_transactions_commands.add_parser('update', parents=[common], help='Update a scheduled transaction', description='Updates a single scheduled transaction', usage='%(prog)s SCHEDULED_TRANSACTION_ID --account-id ACCOUNT_ID --date YYYY-MM-DD [options]', epilog=RUNTIME.command_epilog(['ynab scheduled-transactions update SCHEDULED_TRANSACTION_ID --account-id ACCOUNT_ID --date YYYY-MM-DD', 'ynab scheduled-transactions update SCHEDULED_TRANSACTION_ID --account-id ACCOUNT_ID --date YYYY-MM-DD --dry-run']), formatter_class=RAW)
    c.add_argument('p_scheduled_transaction_id', metavar='SCHEDULED_TRANSACTION_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the scheduled transaction')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--scheduled-transaction-id', dest='p_scheduled_transaction_id', default=argparse.SUPPRESS, metavar='SCHEDULED_TRANSACTION_ID', help='same as SCHEDULED_TRANSACTION_ID')
    c.add_argument('--account-id', dest='p_account_id', metavar='ACCOUNT_ID', required=True)
    c.add_argument('--date', dest='p_date', metavar='YYYY-MM-DD', required=True, help='The scheduled transaction date in ISO format (e.g. 2016-12-01).  This should be a future date no more than 5 years into the future.')
    c.add_argument('--amount', dest='p_amount', type=integer, metavar='AMOUNT', help='The scheduled transaction amount in milliunits format.')
    c.add_argument('--payee-id', dest='p_payee_id', metavar='PAYEE_ID', help='The payee for the scheduled transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as `transfer_payee_id` on the account resource.')
    c.add_argument('--payee-name', dest='p_payee_name', metavar='PAYEE_NAME', help='The payee name for the the scheduled transaction.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a payee with the same name or (2) creation of a new payee.')
    c.add_argument('--category-id', dest='p_category_id', metavar='CATEGORY_ID', help='The category for the scheduled transaction. Credit Card Payment categories are not permitted. Creating a split scheduled transaction is not currently supported.')
    c.add_argument('--memo', dest='p_memo', metavar='MEMO')
    c.add_argument('--flag-color', dest='p_flag_color', choices=['red', 'orange', 'yellow', 'green', 'blue', 'purple', ''])
    c.add_argument('--frequency', dest='p_frequency', choices=['never', 'daily', 'weekly', 'everyOtherWeek', 'twiceAMonth', 'every4Weeks', 'monthly', 'everyOtherMonth', 'every3Months', 'every4Months', 'twiceAYear', 'yearly', 'everyOtherYear'])
    c.set_defaults(handler=_run_scheduled_transactions_update, flags={'plan_id': '--plan-id', 'scheduled_transaction_id': '--scheduled-transaction-id', 'body.scheduled_transaction.account_id': '--account-id', 'body.scheduled_transaction.date': '--date', 'body.scheduled_transaction.amount': '--amount', 'body.scheduled_transaction.payee_id': '--payee-id', 'body.scheduled_transaction.payee_name': '--payee-name', 'body.scheduled_transaction.category_id': '--category-id', 'body.scheduled_transaction.memo': '--memo', 'body.scheduled_transaction.flag_color': '--flag-color', 'body.scheduled_transaction.frequency': '--frequency'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_scheduled_transaction'})
    c = g_scheduled_transactions_commands.add_parser('delete', parents=[common], help='Delete a scheduled transaction', description='Deletes a scheduled transaction', usage='%(prog)s SCHEDULED_TRANSACTION_ID [options]', epilog=RUNTIME.command_epilog(['ynab scheduled-transactions delete SCHEDULED_TRANSACTION_ID --dry-run', 'ynab scheduled-transactions delete SCHEDULED_TRANSACTION_ID --yes']), formatter_class=RAW)
    c.add_argument('p_scheduled_transaction_id', metavar='SCHEDULED_TRANSACTION_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the scheduled transaction')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--scheduled-transaction-id', dest='p_scheduled_transaction_id', default=argparse.SUPPRESS, metavar='SCHEDULED_TRANSACTION_ID', help='same as SCHEDULED_TRANSACTION_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_scheduled_transactions_delete, flags={'plan_id': '--plan-id', 'scheduled_transaction_id': '--scheduled-transaction-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_scheduled_transaction'})
    g_transactions = commands.add_parser('transactions', help='create, delete, get, … (11 commands)', description="Run 'ynab transactions COMMAND --help' for a command's options and examples.")
    g_transactions_commands = g_transactions.add_subparsers(dest="g_transactions", metavar="COMMAND", required=True)
    c = g_transactions_commands.add_parser('list', parents=[common], help='Get transactions', description='Returns plan transactions, excluding any pending transactions', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab transactions list']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--since-date', dest='p_since_date', metavar='YYYY-MM-DD', help='If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). Defaults to one year ago when not specified.')
    c.add_argument('--until-date', dest='p_until_date', metavar='YYYY-MM-DD', help='If specified, only transactions on or before this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).')
    c.add_argument('--type', dest='p_type', choices=['uncategorized', 'unapproved'], help='If specified, only transactions of the specified type will be included. "uncategorized" and "unapproved" are currently supported.')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_transactions_list, flags={'plan_id': '--plan-id', 'since_date': '--since-date', 'until_date': '--until-date', 'type': '--type', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_transactions'})
    c = g_transactions_commands.add_parser('create', parents=[common], help='Create a single transaction or multiple transactions', description='Creates a single transaction or multiple transactions. If you provide a body\ncontaining a `transaction` object, a single transaction will be created and if\nyou provide a body containing a `transactions` array, multiple transactions\nwill be created. Scheduled transactions (transactions with a future date)\ncannot be created on this endpoint.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab transactions create', 'ynab transactions create --dry-run']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--transaction', dest='p_transaction', type=json_value, metavar="JSON")
    c.add_argument('--transactions', dest='p_transactions', type=json_value, metavar="JSON")
    c.set_defaults(handler=_run_transactions_create, flags={'plan_id': '--plan-id', 'body.transaction': '--transaction', 'body.transactions': '--transactions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'create_transaction', 'requires_one_of': [['--transaction', '--transactions']]})
    c = g_transactions_commands.add_parser('update-many', parents=[common], help='Update multiple transactions', description='Updates multiple transactions, by `id` or `import_id`.', usage='%(prog)s --transactions @transactions.json [options]', epilog=RUNTIME.command_epilog(['ynab transactions update-many --transactions @transactions.json', 'ynab transactions update-many --transactions @transactions.json --dry-run']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--transactions', dest='p_transactions', type=json_value, metavar="JSON", required=True)
    c.set_defaults(handler=_run_transactions_update_many, flags={'plan_id': '--plan-id', 'body.transactions': '--transactions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_transactions'})
    c = g_transactions_commands.add_parser('import', parents=[common], help='[deprecated] Import transactions', description='DEPRECATED: This endpoint is no longer needed because YNAB now automatically\nimports transactions on linked accounts. Requests are still accepted for\nbackwards compatibility but no import is performed and the response will\nalways contain an empty list of transaction ids.', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab transactions import', 'ynab transactions import --dry-run']), formatter_class=RAW)
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.set_defaults(handler=_run_transactions_import, flags={'plan_id': '--plan-id'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': True, 'operation': 'import_transactions'})
    c = g_transactions_commands.add_parser('get', parents=[common], help='Get a transaction', description='Returns a single transaction', usage='%(prog)s TRANSACTION_ID [options]', epilog=RUNTIME.command_epilog(['ynab transactions get TRANSACTION_ID']), formatter_class=RAW)
    c.add_argument('p_transaction_id', metavar='TRANSACTION_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the transaction')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--transaction-id', dest='p_transaction_id', default=argparse.SUPPRESS, metavar='TRANSACTION_ID', help='same as TRANSACTION_ID')
    c.set_defaults(handler=_run_transactions_get, flags={'plan_id': '--plan-id', 'transaction_id': '--transaction-id'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_transaction_by_id'})
    c = g_transactions_commands.add_parser('update', parents=[common], help='Update a transaction', description='Updates a single transaction', usage='%(prog)s TRANSACTION_ID [options]', epilog=RUNTIME.command_epilog(['ynab transactions update TRANSACTION_ID', 'ynab transactions update TRANSACTION_ID --dry-run']), formatter_class=RAW)
    c.add_argument('p_transaction_id', metavar='TRANSACTION_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the transaction')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--transaction-id', dest='p_transaction_id', default=argparse.SUPPRESS, metavar='TRANSACTION_ID', help='same as TRANSACTION_ID')
    c.add_argument('--account-id', dest='p_account_id', metavar='ACCOUNT_ID')
    c.add_argument('--date', dest='p_date', metavar='YYYY-MM-DD', help='The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied it will be ignored.')
    c.add_argument('--amount', dest='p_amount', type=integer, metavar='AMOUNT', help='The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a different amount is supplied it will be ignored.')
    c.add_argument('--payee-id', dest='p_payee_id', metavar='PAYEE_ID', help='The payee for the transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as `transfer_payee_id` on the account resource.')
    c.add_argument('--payee-name', dest='p_payee_name', metavar='PAYEE_NAME', help='The payee name.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only if `import_id` is also specified) or (2) a payee with the same name or (3) creation of a new payee.')
    c.add_argument('--category-id', dest='p_category_id', metavar='CATEGORY_ID', help='The category for the transaction.  To configure a split transaction, you can specify null for `category_id` and provide a `subtransactions` array as part of the transaction object.  If an existing transaction is a split, the `category_id` cannot be changed.  Credit Card Payment categories are not permitted and will be ignored if supplied.')
    c.add_argument('--memo', dest='p_memo', metavar='MEMO')
    c.add_argument('--cleared', dest='p_cleared', choices=['cleared', 'uncleared', 'reconciled'])
    c.add_argument('--approved', dest='p_approved', action=argparse.BooleanOptionalAction, help='Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default.')
    c.add_argument('--flag-color', dest='p_flag_color', choices=['red', 'orange', 'yellow', 'green', 'blue', 'purple', ''])
    c.add_argument('--subtransactions', dest='p_subtransactions', type=json_value, metavar="JSON", help='An array of subtransactions to configure a transaction as a split. Updating `subtransactions` on an existing split transaction is not supported and will return an error.  Splits are not allowed on tracking accounts or on transfers between on-budget accounts; a transfer to a tracking account can be a split.')
    c.set_defaults(handler=_run_transactions_update, flags={'plan_id': '--plan-id', 'transaction_id': '--transaction-id', 'body.transaction.account_id': '--account-id', 'body.transaction.date': '--date', 'body.transaction.amount': '--amount', 'body.transaction.payee_id': '--payee-id', 'body.transaction.payee_name': '--payee-name', 'body.transaction.category_id': '--category-id', 'body.transaction.memo': '--memo', 'body.transaction.cleared': '--cleared', 'body.transaction.approved': '--approved', 'body.transaction.flag_color': '--flag-color', 'body.transaction.subtransactions': '--subtransactions'}, meta={'read_only': False, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'update_transaction', 'requires_one_of': [['--account-id', '--date', '--amount', '--payee-id', '--payee-name', '--category-id', '--memo', '--cleared', '--approved', '--flag-color', '--subtransactions']]})
    c = g_transactions_commands.add_parser('delete', parents=[common], help='Delete a transaction', description='Deletes a transaction', usage='%(prog)s TRANSACTION_ID [options]', epilog=RUNTIME.command_epilog(['ynab transactions delete TRANSACTION_ID --dry-run', 'ynab transactions delete TRANSACTION_ID --yes']), formatter_class=RAW)
    c.add_argument('p_transaction_id', metavar='TRANSACTION_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the transaction')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--transaction-id', dest='p_transaction_id', default=argparse.SUPPRESS, metavar='TRANSACTION_ID', help='same as TRANSACTION_ID')
    RUNTIME.add_confirm_option(c)
    c.set_defaults(handler=_run_transactions_delete, flags={'plan_id': '--plan-id', 'transaction_id': '--transaction-id'}, meta={'read_only': False, 'destructive': True, 'paginated': False, 'deprecated': False, 'operation': 'delete_transaction'})
    c = g_transactions_commands.add_parser('list-by-account', parents=[common], help='Get account transactions', description='Returns all transactions for a specified account, excluding any pending\ntransactions', usage='%(prog)s ACCOUNT_ID [options]', epilog=RUNTIME.command_epilog(['ynab transactions list-by-account ACCOUNT_ID']), formatter_class=RAW)
    c.add_argument('p_account_id', metavar='ACCOUNT_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the account')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--account-id', dest='p_account_id', default=argparse.SUPPRESS, metavar='ACCOUNT_ID', help='same as ACCOUNT_ID')
    c.add_argument('--since-date', dest='p_since_date', metavar='YYYY-MM-DD', help='If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). Defaults to one year ago when not specified.')
    c.add_argument('--until-date', dest='p_until_date', metavar='YYYY-MM-DD', help='If specified, only transactions on or before this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).')
    c.add_argument('--type', dest='p_type', choices=['uncategorized', 'unapproved'], help='If specified, only transactions of the specified type will be included. "uncategorized" and "unapproved" are currently supported.')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_transactions_list_by_account, flags={'plan_id': '--plan-id', 'account_id': '--account-id', 'since_date': '--since-date', 'until_date': '--until-date', 'type': '--type', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_transactions_by_account'})
    c = g_transactions_commands.add_parser('list-by-category', parents=[common], help='Get category transactions', description='Returns all transactions for a specified category, excluding any pending\ntransactions', usage='%(prog)s CATEGORY_ID [options]', epilog=RUNTIME.command_epilog(['ynab transactions list-by-category CATEGORY_ID']), formatter_class=RAW)
    c.add_argument('p_category_id', metavar='CATEGORY_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the category')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--category-id', dest='p_category_id', default=argparse.SUPPRESS, metavar='CATEGORY_ID', help='same as CATEGORY_ID')
    c.add_argument('--since-date', dest='p_since_date', metavar='YYYY-MM-DD', help='If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). Defaults to one year ago when not specified.')
    c.add_argument('--until-date', dest='p_until_date', metavar='YYYY-MM-DD', help='If specified, only transactions on or before this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).')
    c.add_argument('--type', dest='p_type', choices=['uncategorized', 'unapproved'], help='If specified, only transactions of the specified type will be included. "uncategorized" and "unapproved" are currently supported.')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_transactions_list_by_category, flags={'plan_id': '--plan-id', 'category_id': '--category-id', 'since_date': '--since-date', 'until_date': '--until-date', 'type': '--type', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_transactions_by_category'})
    c = g_transactions_commands.add_parser('list-by-payee', parents=[common], help='Get payee transactions', description='Returns all transactions for a specified payee, excluding any pending\ntransactions', usage='%(prog)s PAYEE_ID [options]', epilog=RUNTIME.command_epilog(['ynab transactions list-by-payee PAYEE_ID']), formatter_class=RAW)
    c.add_argument('p_payee_id', metavar='PAYEE_ID', nargs='?', default=argparse.SUPPRESS, help='The id of the payee')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--payee-id', dest='p_payee_id', default=argparse.SUPPRESS, metavar='PAYEE_ID', help='same as PAYEE_ID')
    c.add_argument('--since-date', dest='p_since_date', metavar='YYYY-MM-DD', help='If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30). Defaults to one year ago when not specified.')
    c.add_argument('--until-date', dest='p_until_date', metavar='YYYY-MM-DD', help='If specified, only transactions on or before this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).')
    c.add_argument('--type', dest='p_type', choices=['uncategorized', 'unapproved'], help='If specified, only transactions of the specified type will be included. "uncategorized" and "unapproved" are currently supported.')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_transactions_list_by_payee, flags={'plan_id': '--plan-id', 'payee_id': '--payee-id', 'since_date': '--since-date', 'until_date': '--until-date', 'type': '--type', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_transactions_by_payee'})
    c = g_transactions_commands.add_parser('list-by-month', parents=[common], help='Get plan month transactions', description='Returns all transactions for a specified month, excluding any pending\ntransactions', usage='%(prog)s MONTH [options]', epilog=RUNTIME.command_epilog(['ynab transactions list-by-month MONTH']), formatter_class=RAW)
    c.add_argument('p_month', metavar='MONTH', nargs='?', default=argparse.SUPPRESS, help='The plan month in ISO format (e.g. 2016-12-01) ("current" can also be used to specify the current calendar month (UTC))')
    c.add_argument('--plan-id', dest='p_plan_id', metavar='PLAN_ID', help='The id of the plan. "last-used" can be used to specify the last used plan and "default" can be used if default plan selection is enabled (see: https://api.ynab.com/#oauth-default-plan). (default: last-used)')
    c.add_argument('--month', dest='p_month', default=argparse.SUPPRESS, metavar='MONTH', help='same as MONTH')
    c.add_argument('--since-date', dest='p_since_date', metavar='YYYY-MM-DD', help='If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).')
    c.add_argument('--until-date', dest='p_until_date', metavar='YYYY-MM-DD', help='If specified, only transactions on or before this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).')
    c.add_argument('--type', dest='p_type', choices=['uncategorized', 'unapproved'], help='If specified, only transactions of the specified type will be included. "uncategorized" and "unapproved" are currently supported.')
    c.add_argument('--last-knowledge-of-server', dest='p_last_knowledge_of_server', type=integer, metavar='LAST_KNOWLEDGE_OF_SERVER', help='The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.')
    c.set_defaults(handler=_run_transactions_list_by_month, flags={'plan_id': '--plan-id', 'month': '--month', 'since_date': '--since-date', 'until_date': '--until-date', 'type': '--type', 'last_knowledge_of_server': '--last-knowledge-of-server'}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_transactions_by_month'})
    g_user = commands.add_parser('user', help='get', description="Run 'ynab user COMMAND --help' for a command's options and examples.")
    g_user_commands = g_user.add_subparsers(dest="g_user", metavar="COMMAND", required=True)
    c = g_user_commands.add_parser('get', parents=[common], help='Get user', description='Returns authenticated user information', usage='%(prog)s [options]', epilog=RUNTIME.command_epilog(['ynab user get']), formatter_class=RAW)
    c.set_defaults(handler=_run_user_get, flags={}, meta={'read_only': True, 'destructive': False, 'paginated': False, 'deprecated': False, 'operation': 'get_user'})
    RUNTIME.add_builtins(commands)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Parse arguments, run one command, and return the exit code."""
    return RUNTIME.main(
        build_parser, lambda options: Client(**options), _api_model, argv
    )
