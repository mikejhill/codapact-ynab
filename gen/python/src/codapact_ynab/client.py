"""Client generated from the library surface. Do not edit."""

# ruff: noqa: E501
from __future__ import annotations

import builtins  # noqa: F401
from collections.abc import Iterator, Sequence
from functools import cache
from importlib.resources import files
from os import PathLike  # noqa: F401
from typing import Any, Literal, cast  # noqa: F401

from codapact.runtime import (
    AuthProvider,
    Middleware,
    RuntimeClient,
    Transport,
    load_model,
)
from codapact.runtime.arguments import UNSET, Unset, call_args

from codapact.runtime.arguments import fields as _fields  # noqa: F401

from . import types as _t


@cache
def _model() -> Any:
    return load_model(files(__package__).joinpath("_model.json"))


class _AccountsResource:
    """Operations under ``accounts``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, plan_id: str | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.AccountsResponse:
        """
        Get all accounts

        Returns all accounts
        """
        return cast('_t.AccountsResponse', self._runtime.call('get_accounts', call_args({'plan_id': plan_id, 'last_knowledge_of_server': last_knowledge_of_server})))

    def create(self, *, name: str, type_: _t.SaveAccountType, balance: int, plan_id: str | Unset = UNSET) -> _t.AccountResponse:
        """
        Create an account

        Creates a new account
        """
        return cast('_t.AccountResponse', self._runtime.call('create_account', call_args({'plan_id': plan_id}, {'body': {'account': _fields({'name': name, 'type': type_, 'balance': balance})}}, required=frozenset({'body'}))))

    def get(self, *, account_id: str, plan_id: str | Unset = UNSET) -> _t.AccountResponse:
        """
        Get an account

        Returns a single account
        """
        return cast('_t.AccountResponse', self._runtime.call('get_account_by_id', call_args({'plan_id': plan_id, 'account_id': account_id})))

class _CategoriesResource:
    """Operations under ``categories``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, plan_id: str | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.CategoriesResponse:
        """
        Get all categories

        Returns all categories grouped by category group.  Amounts (assigned, activity, available, etc.) are specific to the current plan month (UTC).
        """
        return cast('_t.CategoriesResponse', self._runtime.call('get_categories', call_args({'plan_id': plan_id, 'last_knowledge_of_server': last_knowledge_of_server})))

    def create(self, *, name: str | None, category_group_id: str, plan_id: str | Unset = UNSET, note: str | None | Unset = UNSET, goal_target: int | None | Unset = UNSET, goal_target_date: str | None | Unset = UNSET, goal_needs_whole_amount: bool | None | Unset = UNSET, goal_frequency: _t.SaveCategoryGoalFrequency | Unset = UNSET) -> _t.SaveCategoryResponse:
        """
        Create a category

        Creates a new category
        """
        return cast('_t.SaveCategoryResponse', self._runtime.call('create_category', call_args({'plan_id': plan_id}, {'body': {'category': _fields({'name': name, 'note': note, 'category_group_id': category_group_id, 'goal_target': goal_target, 'goal_target_date': goal_target_date, 'goal_needs_whole_amount': goal_needs_whole_amount, 'goal_frequency': goal_frequency})}}, required=frozenset({'body'}))))

    def get(self, *, category_id: str, plan_id: str | Unset = UNSET) -> _t.CategoryResponse:
        """
        Get a category

        Returns a single category.  Amounts (assigned, activity, available, etc.) are specific to the current plan month (UTC).
        """
        return cast('_t.CategoryResponse', self._runtime.call('get_category_by_id', call_args({'plan_id': plan_id, 'category_id': category_id})))

    def update(self, *, category_id: str, plan_id: str | Unset = UNSET, name: str | None | Unset = UNSET, note: str | None | Unset = UNSET, category_group_id: str | Unset = UNSET, goal_target: int | None | Unset = UNSET, goal_target_date: str | None | Unset = UNSET, goal_needs_whole_amount: bool | None | Unset = UNSET, goal_frequency: _t.SaveCategoryGoalFrequency | Unset = UNSET) -> _t.SaveCategoryResponse:
        """Update a category"""
        return cast('_t.SaveCategoryResponse', self._runtime.call('update_category', call_args({'plan_id': plan_id, 'category_id': category_id}, {'body': {'category': _fields({'name': name, 'note': note, 'category_group_id': category_group_id, 'goal_target': goal_target, 'goal_target_date': goal_target_date, 'goal_needs_whole_amount': goal_needs_whole_amount, 'goal_frequency': goal_frequency})}})))

    def get_month(self, *, month: str, category_id: str, plan_id: str | Unset = UNSET) -> _t.CategoryResponse:
        """
        Get a category for a specific plan month

        Returns a single category for a specific plan month.  Amounts (assigned, activity, available, etc.) are specific to the current plan month (UTC).
        """
        return cast('_t.CategoryResponse', self._runtime.call('get_month_category_by_id', call_args({'plan_id': plan_id, 'month': month, 'category_id': category_id})))

    def update_month(self, *, month: str, category_id: str, budgeted: int, plan_id: str | Unset = UNSET) -> _t.SaveCategoryResponse:
        """
        Update a category for a specific month

        Update a category for a specific month.  Only `budgeted` (assigned) amount can be updated.
        """
        return cast('_t.SaveCategoryResponse', self._runtime.call('update_month_category', call_args({'plan_id': plan_id, 'month': month, 'category_id': category_id}, {'body': {'category': _fields({'budgeted': budgeted})}}, required=frozenset({'body'}))))

    def create_group(self, *, name: str, plan_id: str | Unset = UNSET) -> _t.SaveCategoryGroupResponse:
        """
        Create a category group

        Creates a new category group
        """
        return cast('_t.SaveCategoryGroupResponse', self._runtime.call('create_category_group', call_args({'plan_id': plan_id}, {'body': {'category_group': _fields({'name': name})}}, required=frozenset({'body'}))))

    def update_group(self, *, category_group_id: str, name: str, plan_id: str | Unset = UNSET) -> _t.SaveCategoryGroupResponse:
        """Update a category group"""
        return cast('_t.SaveCategoryGroupResponse', self._runtime.call('update_category_group', call_args({'plan_id': plan_id, 'category_group_id': category_group_id}, {'body': {'category_group': _fields({'name': name})}}, required=frozenset({'body'}))))

class _MoneyMovementsResource:
    """Operations under ``money_movements``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, plan_id: str | Unset = UNSET) -> _t.MoneyMovementsResponse:
        """
        Get all money movements

        Returns all money movements
        """
        return cast('_t.MoneyMovementsResponse', self._runtime.call('get_money_movements', call_args({'plan_id': plan_id})))

    def list_by_month(self, *, month: str, plan_id: str | Unset = UNSET) -> _t.MoneyMovementsResponse:
        """
        Get money movements for a plan month

        Returns all money movements for a specific month
        """
        return cast('_t.MoneyMovementsResponse', self._runtime.call('get_money_movements_by_month', call_args({'plan_id': plan_id, 'month': month})))

    def list_groups(self, *, plan_id: str | Unset = UNSET) -> _t.MoneyMovementGroupsResponse:
        """
        Get all money movement groups

        Returns all money movement groups
        """
        return cast('_t.MoneyMovementGroupsResponse', self._runtime.call('get_money_movement_groups', call_args({'plan_id': plan_id})))

    def list_groups_by_month(self, *, month: str, plan_id: str | Unset = UNSET) -> _t.MoneyMovementGroupsResponse:
        """
        Get money movement groups for a plan month

        Returns all money movement groups for a specific month
        """
        return cast('_t.MoneyMovementGroupsResponse', self._runtime.call('get_money_movement_groups_by_month', call_args({'plan_id': plan_id, 'month': month})))

class _MonthsResource:
    """Operations under ``months``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, plan_id: str | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.MonthSummariesResponse:
        """
        Get all plan months

        Returns all plan months
        """
        return cast('_t.MonthSummariesResponse', self._runtime.call('get_plan_months', call_args({'plan_id': plan_id, 'last_knowledge_of_server': last_knowledge_of_server})))

    def get(self, *, month: str, plan_id: str | Unset = UNSET) -> _t.MonthDetailResponse:
        """
        Get a plan month

        Returns a single plan month
        """
        return cast('_t.MonthDetailResponse', self._runtime.call('get_plan_month', call_args({'plan_id': plan_id, 'month': month})))

class _PayeeLocationsResource:
    """Operations under ``payee_locations``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, plan_id: str | Unset = UNSET) -> _t.PayeeLocationsResponse:
        """
        Get all payee locations

        Returns all payee locations
        """
        return cast('_t.PayeeLocationsResponse', self._runtime.call('get_payee_locations', call_args({'plan_id': plan_id})))

    def get(self, *, payee_location_id: str, plan_id: str | Unset = UNSET) -> _t.PayeeLocationResponse:
        """
        Get a payee location

        Returns a single payee location
        """
        return cast('_t.PayeeLocationResponse', self._runtime.call('get_payee_location_by_id', call_args({'plan_id': plan_id, 'payee_location_id': payee_location_id})))

    def list_by_payee(self, *, payee_id: str, plan_id: str | Unset = UNSET) -> _t.PayeeLocationsResponse:
        """
        Get all locations for a payee

        Returns all payee locations for a specified payee
        """
        return cast('_t.PayeeLocationsResponse', self._runtime.call('get_payee_locations_by_payee', call_args({'plan_id': plan_id, 'payee_id': payee_id})))

class _PayeesResource:
    """Operations under ``payees``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, plan_id: str | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.PayeesResponse:
        """
        Get all payees

        Returns all payees
        """
        return cast('_t.PayeesResponse', self._runtime.call('get_payees', call_args({'plan_id': plan_id, 'last_knowledge_of_server': last_knowledge_of_server})))

    def create(self, *, name: str, plan_id: str | Unset = UNSET) -> _t.SavePayeeResponse:
        """
        Create a payee

        Creates a new payee
        """
        return cast('_t.SavePayeeResponse', self._runtime.call('create_payee', call_args({'plan_id': plan_id}, {'body': {'payee': _fields({'name': name})}}, required=frozenset({'body'}))))

    def get(self, *, payee_id: str, plan_id: str | Unset = UNSET) -> _t.PayeeResponse:
        """
        Get a payee

        Returns a single payee
        """
        return cast('_t.PayeeResponse', self._runtime.call('get_payee_by_id', call_args({'plan_id': plan_id, 'payee_id': payee_id})))

    def update(self, *, payee_id: str, plan_id: str | Unset = UNSET, name: str | Unset = UNSET) -> _t.SavePayeeResponse:
        """Update a payee"""
        return cast('_t.SavePayeeResponse', self._runtime.call('update_payee', call_args({'plan_id': plan_id, 'payee_id': payee_id}, {'body': {'payee': _fields({'name': name})}})))

class _PlansResource:
    """Operations under ``plans``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, include_accounts: bool | Unset = UNSET) -> _t.PlanSummaryResponse:
        """
        Get all plans

        Returns plans list with summary information
        """
        return cast('_t.PlanSummaryResponse', self._runtime.call('get_plans', call_args({'include_accounts': include_accounts})))

    def get(self, *, plan_id: str | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.PlanDetailResponse:
        """
        Get a plan

        Returns a single plan with all related entities.  This resource is effectively a full plan export.
        """
        return cast('_t.PlanDetailResponse', self._runtime.call('get_plan_by_id', call_args({'plan_id': plan_id, 'last_knowledge_of_server': last_knowledge_of_server})))

    def get_settings(self, *, plan_id: str | Unset = UNSET) -> _t.PlanSettingsResponse:
        """
        Get plan settings

        Returns settings for a plan
        """
        return cast('_t.PlanSettingsResponse', self._runtime.call('get_plan_settings_by_id', call_args({'plan_id': plan_id})))

class _ScheduledTransactionsResource:
    """Operations under ``scheduled_transactions``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, plan_id: str | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.ScheduledTransactionsResponse:
        """
        Get all scheduled transactions

        Returns all scheduled transactions
        """
        return cast('_t.ScheduledTransactionsResponse', self._runtime.call('get_scheduled_transactions', call_args({'plan_id': plan_id, 'last_knowledge_of_server': last_knowledge_of_server})))

    def create(self, *, account_id: str, date: str, plan_id: str | Unset = UNSET, amount: int | Unset = UNSET, payee_id: str | None | Unset = UNSET, payee_name: str | None | Unset = UNSET, category_id: str | None | Unset = UNSET, memo: str | None | Unset = UNSET, flag_color: _t.TransactionFlagColor | None | Unset = UNSET, frequency: _t.ScheduledTransactionFrequency | Unset = UNSET) -> _t.ScheduledTransactionResponse:
        """
        Create a scheduled transaction

        Creates a single scheduled transaction (a transaction with a future date).
        """
        return cast('_t.ScheduledTransactionResponse', self._runtime.call('create_scheduled_transaction', call_args({'plan_id': plan_id}, {'body': {'scheduled_transaction': _fields({'account_id': account_id, 'date': date, 'amount': amount, 'payee_id': payee_id, 'payee_name': payee_name, 'category_id': category_id, 'memo': memo, 'flag_color': flag_color, 'frequency': frequency})}}, required=frozenset({'body'}))))

    def get(self, *, scheduled_transaction_id: str, plan_id: str | Unset = UNSET) -> _t.ScheduledTransactionResponse:
        """
        Get a scheduled transaction

        Returns a single scheduled transaction
        """
        return cast('_t.ScheduledTransactionResponse', self._runtime.call('get_scheduled_transaction_by_id', call_args({'plan_id': plan_id, 'scheduled_transaction_id': scheduled_transaction_id})))

    def update(self, *, scheduled_transaction_id: str, account_id: str, date: str, plan_id: str | Unset = UNSET, amount: int | Unset = UNSET, payee_id: str | None | Unset = UNSET, payee_name: str | None | Unset = UNSET, category_id: str | None | Unset = UNSET, memo: str | None | Unset = UNSET, flag_color: _t.TransactionFlagColor | None | Unset = UNSET, frequency: _t.ScheduledTransactionFrequency | Unset = UNSET) -> _t.ScheduledTransactionResponse:
        """
        Update a scheduled transaction

        Updates a single scheduled transaction
        """
        return cast('_t.ScheduledTransactionResponse', self._runtime.call('update_scheduled_transaction', call_args({'plan_id': plan_id, 'scheduled_transaction_id': scheduled_transaction_id}, {'body': {'scheduled_transaction': _fields({'account_id': account_id, 'date': date, 'amount': amount, 'payee_id': payee_id, 'payee_name': payee_name, 'category_id': category_id, 'memo': memo, 'flag_color': flag_color, 'frequency': frequency})}}, required=frozenset({'body'}))))

    def delete(self, *, scheduled_transaction_id: str, plan_id: str | Unset = UNSET) -> _t.ScheduledTransactionResponse:
        """
        Delete a scheduled transaction

        Deletes a scheduled transaction
        """
        return cast('_t.ScheduledTransactionResponse', self._runtime.call('delete_scheduled_transaction', call_args({'plan_id': plan_id, 'scheduled_transaction_id': scheduled_transaction_id})))

class _TransactionsResource:
    """Operations under ``transactions``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def list(self, *, plan_id: str | Unset = UNSET, since_date: str | Unset = UNSET, until_date: str | Unset = UNSET, type_: _t.GetTransactionsType | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.TransactionsResponse:
        """
        Get transactions

        Returns plan transactions, excluding any pending transactions
        """
        return cast('_t.TransactionsResponse', self._runtime.call('get_transactions', call_args({'plan_id': plan_id, 'since_date': since_date, 'until_date': until_date, 'type': type_, 'last_knowledge_of_server': last_knowledge_of_server})))

    def create(self, *, plan_id: str | Unset = UNSET, transaction: _t.NewTransaction | Unset = UNSET, transactions: builtins.list[_t.NewTransaction] | Unset = UNSET) -> _t.SaveTransactionsResponse:
        """
        Create a single transaction or multiple transactions

        Creates a single transaction or multiple transactions.  If you provide a body containing a `transaction` object, a single transaction will be created and if you provide a body containing a `transactions` array, multiple transactions will be created.  Scheduled transactions (transactions with a future date) cannot be created on this endpoint.
        """
        return cast('_t.SaveTransactionsResponse', self._runtime.call('create_transaction', call_args({'plan_id': plan_id}, {'body': {'transaction': transaction, 'transactions': transactions}})))

    def update_many(self, *, transactions: builtins.list[_t.SaveTransactionWithIdOrImportId], plan_id: str | Unset = UNSET) -> _t.SaveTransactionsResponse:
        """
        Update multiple transactions

        Updates multiple transactions, by `id` or `import_id`.
        """
        return cast('_t.SaveTransactionsResponse', self._runtime.call('update_transactions', call_args({'plan_id': plan_id}, {'body': {'transactions': transactions}}, required=frozenset({'body'}))))

    def import_(self, *, plan_id: str | Unset = UNSET) -> _t.TransactionsImportResponse:
        """
        Import transactions

        DEPRECATED: This endpoint is no longer needed because YNAB now automatically imports transactions on linked accounts.  Requests are still accepted for backwards compatibility but no import is performed and the response will always contain an empty list of transaction ids.

        Deprecated.
        """
        return cast('_t.TransactionsImportResponse', self._runtime.call('import_transactions', call_args({'plan_id': plan_id})))

    def get(self, *, transaction_id: str, plan_id: str | Unset = UNSET) -> _t.TransactionResponse:
        """
        Get a transaction

        Returns a single transaction
        """
        return cast('_t.TransactionResponse', self._runtime.call('get_transaction_by_id', call_args({'plan_id': plan_id, 'transaction_id': transaction_id})))

    def update(self, *, transaction_id: str, plan_id: str | Unset = UNSET, account_id: str | Unset = UNSET, date: str | Unset = UNSET, amount: int | Unset = UNSET, payee_id: str | None | Unset = UNSET, payee_name: str | None | Unset = UNSET, category_id: str | None | Unset = UNSET, memo: str | None | Unset = UNSET, cleared: _t.TransactionClearedStatus | Unset = UNSET, approved: bool | Unset = UNSET, flag_color: _t.TransactionFlagColor | None | Unset = UNSET, subtransactions: builtins.list[_t.SaveSubTransaction] | Unset = UNSET) -> _t.TransactionResponse:
        """
        Update a transaction

        Updates a single transaction
        """
        return cast('_t.TransactionResponse', self._runtime.call('update_transaction', call_args({'plan_id': plan_id, 'transaction_id': transaction_id}, {'body': {'transaction': _fields({'account_id': account_id, 'date': date, 'amount': amount, 'payee_id': payee_id, 'payee_name': payee_name, 'category_id': category_id, 'memo': memo, 'cleared': cleared, 'approved': approved, 'flag_color': flag_color, 'subtransactions': subtransactions})}})))

    def delete(self, *, transaction_id: str, plan_id: str | Unset = UNSET) -> _t.TransactionResponse:
        """
        Delete a transaction

        Deletes a transaction
        """
        return cast('_t.TransactionResponse', self._runtime.call('delete_transaction', call_args({'plan_id': plan_id, 'transaction_id': transaction_id})))

    def list_by_account(self, *, account_id: str, plan_id: str | Unset = UNSET, since_date: str | Unset = UNSET, until_date: str | Unset = UNSET, type_: _t.GetTransactionsByAccountType | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.TransactionsResponse:
        """
        Get account transactions

        Returns all transactions for a specified account, excluding any pending transactions
        """
        return cast('_t.TransactionsResponse', self._runtime.call('get_transactions_by_account', call_args({'plan_id': plan_id, 'account_id': account_id, 'since_date': since_date, 'until_date': until_date, 'type': type_, 'last_knowledge_of_server': last_knowledge_of_server})))

    def list_by_category(self, *, category_id: str, plan_id: str | Unset = UNSET, since_date: str | Unset = UNSET, until_date: str | Unset = UNSET, type_: _t.GetTransactionsByCategoryType | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.HybridTransactionsResponse:
        """
        Get category transactions

        Returns all transactions for a specified category, excluding any pending transactions
        """
        return cast('_t.HybridTransactionsResponse', self._runtime.call('get_transactions_by_category', call_args({'plan_id': plan_id, 'category_id': category_id, 'since_date': since_date, 'until_date': until_date, 'type': type_, 'last_knowledge_of_server': last_knowledge_of_server})))

    def list_by_payee(self, *, payee_id: str, plan_id: str | Unset = UNSET, since_date: str | Unset = UNSET, until_date: str | Unset = UNSET, type_: _t.GetTransactionsByPayeeType | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.HybridTransactionsResponse:
        """
        Get payee transactions

        Returns all transactions for a specified payee, excluding any pending transactions
        """
        return cast('_t.HybridTransactionsResponse', self._runtime.call('get_transactions_by_payee', call_args({'plan_id': plan_id, 'payee_id': payee_id, 'since_date': since_date, 'until_date': until_date, 'type': type_, 'last_knowledge_of_server': last_knowledge_of_server})))

    def list_by_month(self, *, month: str, plan_id: str | Unset = UNSET, since_date: str | Unset = UNSET, until_date: str | Unset = UNSET, type_: _t.GetTransactionsByMonthType | Unset = UNSET, last_knowledge_of_server: int | Unset = UNSET) -> _t.TransactionsResponse:
        """
        Get plan month transactions

        Returns all transactions for a specified month, excluding any pending transactions
        """
        return cast('_t.TransactionsResponse', self._runtime.call('get_transactions_by_month', call_args({'plan_id': plan_id, 'month': month, 'since_date': since_date, 'until_date': until_date, 'type': type_, 'last_knowledge_of_server': last_knowledge_of_server})))

class _UserResource:
    """Operations under ``user``."""

    def __init__(self, runtime: RuntimeClient) -> None:
        self._runtime = runtime

    def get(self) -> _t.UserResponse:
        """
        Get user

        Returns authenticated user information
        """
        return cast('_t.UserResponse', self._runtime.call('get_user', call_args({})))


class Client:
    """
    YNAB API Endpoints client.

    Default base URL: https://api.ynab.com/v1
    """

    def __init__(
        self,
        *,
        base_url: str | None = None,
        auth: AuthProvider | None = None,
        transport: Transport | None = None,
        middleware: Sequence[Middleware] | None = None,
        validate: bool = True,
        timeout: float = 30.0,
        allow_private: bool = False,
        response_validation: str = "strict",
        proxy: str | None = None,
    ) -> None:
        self._runtime = RuntimeClient(
            _model(),
            base_url=base_url,
            auth=auth,
            transport=transport,
            middleware=middleware,
            validate=validate,
            timeout=timeout,
            allow_private=allow_private,
            response_validation=response_validation,
            proxy=proxy,
        )
        self.accounts = _AccountsResource(self._runtime)
        self.categories = _CategoriesResource(self._runtime)
        self.money_movements = _MoneyMovementsResource(self._runtime)
        self.months = _MonthsResource(self._runtime)
        self.payee_locations = _PayeeLocationsResource(self._runtime)
        self.payees = _PayeesResource(self._runtime)
        self.plans = _PlansResource(self._runtime)
        self.scheduled_transactions = _ScheduledTransactionsResource(self._runtime)
        self.transactions = _TransactionsResource(self._runtime)
        self.user = _UserResource(self._runtime)
