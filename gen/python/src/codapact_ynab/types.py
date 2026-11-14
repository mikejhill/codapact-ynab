"""Types generated from the semantic model. Do not edit."""

# ruff: noqa: E501, F401, UP013
from __future__ import annotations

from typing import Any, Literal, NotRequired, TypedDict

__all__ = ['Account', 'AccountBase', 'AccountResponse', 'AccountResponseData', 'AccountType', 'AccountsResponse', 'AccountsResponseData', 'BulkResponse', 'BulkResponseData', 'BulkResponseDataBulk', 'BulkTransactions', 'CategoriesResponse', 'CategoriesResponseData', 'Category', 'CategoryBase', 'CategoryBaseGoalType', 'CategoryGroup', 'CategoryGroupWithCategories', 'CategoryResponse', 'CategoryResponseData', 'CurrencyFormat', 'DateFormat', 'ErrorDetail', 'ErrorResponse', 'ExistingCategory', 'ExistingTransaction', 'GetTransactionsByAccountType', 'GetTransactionsByCategoryType', 'GetTransactionsByMonthType', 'GetTransactionsByPayeeType', 'GetTransactionsType', 'HybridTransaction', 'HybridTransactionType', 'HybridTransactionsResponse', 'HybridTransactionsResponseData', 'LoanAccountPeriodicValue', 'MoneyMovement', 'MoneyMovementBase', 'MoneyMovementGroup', 'MoneyMovementGroupsResponse', 'MoneyMovementGroupsResponseData', 'MoneyMovementsResponse', 'MoneyMovementsResponseData', 'MonthDetail', 'MonthDetailBase', 'MonthDetailResponse', 'MonthDetailResponseData', 'MonthSummariesResponse', 'MonthSummariesResponseData', 'MonthSummary', 'MonthSummaryBase', 'NewCategory', 'NewTransaction', 'PatchCategoryGroupWrapper', 'PatchCategoryWrapper', 'PatchMonthCategoryWrapper', 'PatchPayeeWrapper', 'PatchTransactionsWrapper', 'Payee', 'PayeeLocation', 'PayeeLocationResponse', 'PayeeLocationResponseData', 'PayeeLocationsResponse', 'PayeeLocationsResponseData', 'PayeeResponse', 'PayeeResponseData', 'PayeesResponse', 'PayeesResponseData', 'PlanDetail', 'PlanDetailResponse', 'PlanDetailResponseData', 'PlanSettings', 'PlanSettingsResponse', 'PlanSettingsResponseData', 'PlanSummary', 'PlanSummaryResponse', 'PlanSummaryResponseData', 'PostAccountWrapper', 'PostCategoryGroupWrapper', 'PostCategoryWrapper', 'PostPayee', 'PostPayeeWrapper', 'PostScheduledTransactionWrapper', 'PostTransactionsWrapper', 'PutScheduledTransactionWrapper', 'PutTransactionWrapper', 'SaveAccount', 'SaveAccountType', 'SaveCategory', 'SaveCategoryGoalFrequency', 'SaveCategoryGroup', 'SaveCategoryGroupResponse', 'SaveCategoryGroupResponseData', 'SaveCategoryResponse', 'SaveCategoryResponseData', 'SaveMonthCategory', 'SavePayee', 'SavePayeeResponse', 'SavePayeeResponseData', 'SaveScheduledTransaction', 'SaveSubTransaction', 'SaveTransactionWithIdOrImportId', 'SaveTransactionWithOptionalFields', 'SaveTransactionsResponse', 'SaveTransactionsResponseData', 'ScheduledSubTransaction', 'ScheduledSubTransactionBase', 'ScheduledTransactionDetail', 'ScheduledTransactionFrequency', 'ScheduledTransactionResponse', 'ScheduledTransactionResponseData', 'ScheduledTransactionSummary', 'ScheduledTransactionSummaryBase', 'ScheduledTransactionSummaryBaseFrequency', 'ScheduledTransactionsResponse', 'ScheduledTransactionsResponseData', 'SubTransaction', 'SubTransactionBase', 'TransactionClearedStatus', 'TransactionDetail', 'TransactionFlagColor', 'TransactionFlagName', 'TransactionResponse', 'TransactionResponseData', 'TransactionSummary', 'TransactionSummaryBase', 'TransactionSummaryBaseDebtTransactionType', 'TransactionsImportResponse', 'TransactionsImportResponseData', 'TransactionsResponse', 'TransactionsResponseData', 'User', 'UserResponse', 'UserResponseData']

Account = TypedDict(
    'Account',
    {
    'id': "str",
    'name': "str",
    'type': "AccountType",
    'on_budget': "bool",
    'closed': "bool",
    'note': NotRequired["str | None"],
    'balance': "int",
    'cleared_balance': "int",
    'uncleared_balance': "int",
    'transfer_payee_id': "str | None",
    'direct_import_linked': NotRequired["bool"],
    'direct_import_in_error': NotRequired["bool"],
    'last_reconciled_at': NotRequired["str | None"],
    'debt_original_balance': NotRequired["int | None"],
    'debt_interest_rates': NotRequired["LoanAccountPeriodicValue | None"],
    'debt_minimum_payments': NotRequired["LoanAccountPeriodicValue | None"],
    'debt_escrow_amounts': NotRequired["LoanAccountPeriodicValue | None"],
    'deleted': "bool",
    'balance_formatted': NotRequired["str"],
    'balance_currency': NotRequired["float"],
    'cleared_balance_formatted': NotRequired["str"],
    'cleared_balance_currency': NotRequired["float"],
    'uncleared_balance_formatted': NotRequired["str"],
    'uncleared_balance_currency': NotRequired["float"],
    },
)

AccountBase = TypedDict(
    'AccountBase',
    {
    'id': "str",
    'name': "str",
    'type': "AccountType",
    'on_budget': "bool",
    'closed': "bool",
    'note': NotRequired["str | None"],
    'balance': "int",
    'cleared_balance': "int",
    'uncleared_balance': "int",
    'transfer_payee_id': "str | None",
    'direct_import_linked': NotRequired["bool"],
    'direct_import_in_error': NotRequired["bool"],
    'last_reconciled_at': NotRequired["str | None"],
    'debt_original_balance': NotRequired["int | None"],
    'debt_interest_rates': NotRequired["LoanAccountPeriodicValue | None"],
    'debt_minimum_payments': NotRequired["LoanAccountPeriodicValue | None"],
    'debt_escrow_amounts': NotRequired["LoanAccountPeriodicValue | None"],
    'deleted': "bool",
    },
)

AccountResponse = TypedDict(
    'AccountResponse',
    {
    'data': "AccountResponseData",
    },
)

AccountResponseData = TypedDict(
    'AccountResponseData',
    {
    'account': "Account",
    },
)

type AccountType = Literal['checking', 'savings', 'cash', 'creditCard', 'lineOfCredit', 'otherAsset', 'otherLiability', 'mortgage', 'autoLoan', 'studentLoan', 'personalLoan', 'medicalDebt', 'otherDebt']
"""The type of account"""

AccountsResponse = TypedDict(
    'AccountsResponse',
    {
    'data': "AccountsResponseData",
    },
)

AccountsResponseData = TypedDict(
    'AccountsResponseData',
    {
    'accounts': "list[Account]",
    'server_knowledge': "int",
    },
)

BulkResponse = TypedDict(
    'BulkResponse',
    {
    'data': "BulkResponseData",
    },
)

BulkResponseData = TypedDict(
    'BulkResponseData',
    {
    'bulk': "BulkResponseDataBulk",
    },
)

BulkResponseDataBulk = TypedDict(
    'BulkResponseDataBulk',
    {
    'transaction_ids': "list[str]",
    'duplicate_import_ids': "list[str]",
    },
)

BulkTransactions = TypedDict(
    'BulkTransactions',
    {
    'transactions': "list[SaveTransactionWithOptionalFields]",
    },
)

CategoriesResponse = TypedDict(
    'CategoriesResponse',
    {
    'data': "CategoriesResponseData",
    },
)

CategoriesResponseData = TypedDict(
    'CategoriesResponseData',
    {
    'category_groups': "list[CategoryGroupWithCategories]",
    'server_knowledge': "int",
    },
)

Category = TypedDict(
    'Category',
    {
    'id': "str",
    'category_group_id': "str",
    'category_group_name': NotRequired["str"],
    'name': "str",
    'hidden': "bool",
    'internal': "bool",
    'original_category_group_id': NotRequired["str | None"],
    'note': NotRequired["str | None"],
    'budgeted': "int",
    'activity': "int",
    'balance': "int",
    'goal_type': NotRequired["CategoryBaseGoalType | None"],
    'goal_needs_whole_amount': NotRequired["bool | None"],
    'goal_day': NotRequired["int | None"],
    'goal_cadence': NotRequired["int | None"],
    'goal_cadence_frequency': NotRequired["int | None"],
    'goal_creation_month': NotRequired["str | None"],
    'goal_target': NotRequired["int | None"],
    'goal_target_month': NotRequired["str | None"],
    'goal_target_date': NotRequired["str | None"],
    'goal_percentage_complete': NotRequired["int | None"],
    'goal_months_to_budget': NotRequired["int | None"],
    'goal_under_funded': NotRequired["int | None"],
    'goal_overall_funded': NotRequired["int | None"],
    'goal_overall_left': NotRequired["int | None"],
    'goal_snoozed_at': NotRequired["str | None"],
    'deleted': "bool",
    'balance_formatted': NotRequired["str"],
    'balance_currency': NotRequired["float"],
    'activity_formatted': NotRequired["str"],
    'activity_currency': NotRequired["float"],
    'budgeted_formatted': NotRequired["str"],
    'budgeted_currency': NotRequired["float"],
    'goal_target_formatted': NotRequired["str | None"],
    'goal_target_currency': NotRequired["float | None"],
    'goal_under_funded_formatted': NotRequired["str | None"],
    'goal_under_funded_currency': NotRequired["float | None"],
    'goal_overall_funded_formatted': NotRequired["str | None"],
    'goal_overall_funded_currency': NotRequired["float | None"],
    'goal_overall_left_formatted': NotRequired["str | None"],
    'goal_overall_left_currency': NotRequired["float | None"],
    },
)

CategoryBase = TypedDict(
    'CategoryBase',
    {
    'id': "str",
    'category_group_id': "str",
    'category_group_name': NotRequired["str"],
    'name': "str",
    'hidden': "bool",
    'internal': "bool",
    'original_category_group_id': NotRequired["str | None"],
    'note': NotRequired["str | None"],
    'budgeted': "int",
    'activity': "int",
    'balance': "int",
    'goal_type': NotRequired["CategoryBaseGoalType | None"],
    'goal_needs_whole_amount': NotRequired["bool | None"],
    'goal_day': NotRequired["int | None"],
    'goal_cadence': NotRequired["int | None"],
    'goal_cadence_frequency': NotRequired["int | None"],
    'goal_creation_month': NotRequired["str | None"],
    'goal_target': NotRequired["int | None"],
    'goal_target_month': NotRequired["str | None"],
    'goal_target_date': NotRequired["str | None"],
    'goal_percentage_complete': NotRequired["int | None"],
    'goal_months_to_budget': NotRequired["int | None"],
    'goal_under_funded': NotRequired["int | None"],
    'goal_overall_funded': NotRequired["int | None"],
    'goal_overall_left': NotRequired["int | None"],
    'goal_snoozed_at': NotRequired["str | None"],
    'deleted': "bool",
    },
)

type CategoryBaseGoalType = Literal['TB', 'TBD', 'MF', 'NEED', 'DEBT']
"""The type of goal, if the category has a goal (TB='Target Category Balance', TBD='Target Category Balance by Date', MF='Monthly Funding', NEED='Plan Your Spending')"""

CategoryGroup = TypedDict(
    'CategoryGroup',
    {
    'id': "str",
    'name': "str",
    'hidden': "bool",
    'internal': "bool",
    'deleted': "bool",
    },
)

CategoryGroupWithCategories = TypedDict(
    'CategoryGroupWithCategories',
    {
    'id': "str",
    'name': "str",
    'hidden': "bool",
    'internal': "bool",
    'deleted': "bool",
    'categories': "list[Category]",
    },
)

CategoryResponse = TypedDict(
    'CategoryResponse',
    {
    'data': "CategoryResponseData",
    },
)

CategoryResponseData = TypedDict(
    'CategoryResponseData',
    {
    'category': "Category",
    },
)

CurrencyFormat = TypedDict(
    'CurrencyFormat',
    {
    'iso_code': "str",
    'example_format': "str",
    'decimal_digits': "int",
    'decimal_separator': "str",
    'symbol_first': "bool",
    'group_separator': "str",
    'currency_symbol': "str",
    'display_symbol': "bool",
    },
)
"""The currency format setting for the plan.  In some cases the format will not be available and will be specified as null."""

DateFormat = TypedDict(
    'DateFormat',
    {
    'format': "str",
    },
)
"""The date format setting for the plan.  In some cases the format will not be available and will be specified as null."""

ErrorDetail = TypedDict(
    'ErrorDetail',
    {
    'id': "str",
    'name': "str",
    'detail': "str",
    },
)

ErrorResponse = TypedDict(
    'ErrorResponse',
    {
    'error': "ErrorDetail",
    },
)

ExistingCategory = TypedDict(
    'ExistingCategory',
    {
    'name': NotRequired["str | None"],
    'note': NotRequired["str | None"],
    'category_group_id': NotRequired["str"],
    'goal_target': NotRequired["int | None"],
    'goal_target_date': NotRequired["str | None"],
    'goal_needs_whole_amount': NotRequired["bool | None"],
    'goal_frequency': NotRequired["SaveCategoryGoalFrequency"],
    },
)

ExistingTransaction = TypedDict(
    'ExistingTransaction',
    {
    'account_id': NotRequired["str"],
    'date': NotRequired["str"],
    'amount': NotRequired["int"],
    'payee_id': NotRequired["str | None"],
    'payee_name': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'memo': NotRequired["str | None"],
    'cleared': NotRequired["TransactionClearedStatus"],
    'approved': NotRequired["bool"],
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'subtransactions': NotRequired["list[SaveSubTransaction]"],
    },
)

type GetTransactionsByAccountType = Literal['uncategorized', 'unapproved']

type GetTransactionsByCategoryType = Literal['uncategorized', 'unapproved']

type GetTransactionsByMonthType = Literal['uncategorized', 'unapproved']

type GetTransactionsByPayeeType = Literal['uncategorized', 'unapproved']

type GetTransactionsType = Literal['uncategorized', 'unapproved']

HybridTransaction = TypedDict(
    'HybridTransaction',
    {
    'id': "str",
    'date': "str",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'cleared': "TransactionClearedStatus",
    'approved': "bool",
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'flag_name': NotRequired["TransactionFlagName | None"],
    'account_id': "str",
    'payee_id': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'transfer_transaction_id': NotRequired["str | None"],
    'matched_transaction_id': NotRequired["str | None"],
    'import_id': NotRequired["str | None"],
    'import_payee_name': NotRequired["str | None"],
    'import_payee_name_original': NotRequired["str | None"],
    'debt_transaction_type': NotRequired["TransactionSummaryBaseDebtTransactionType | None"],
    'deleted': "bool",
    'amount_formatted': NotRequired["str"],
    'amount_currency': NotRequired["float"],
    'type': "HybridTransactionType",
    'parent_transaction_id': NotRequired["str | None"],
    'account_name': "str",
    'payee_name': NotRequired["str | None"],
    'category_name': NotRequired["str"],
    },
)

type HybridTransactionType = Literal['transaction', 'subtransaction']
"""Whether the hybrid transaction represents a regular transaction or a subtransaction"""

HybridTransactionsResponse = TypedDict(
    'HybridTransactionsResponse',
    {
    'data': "HybridTransactionsResponseData",
    },
)

HybridTransactionsResponseData = TypedDict(
    'HybridTransactionsResponseData',
    {
    'transactions': "list[HybridTransaction]",
    'server_knowledge': NotRequired["int"],
    },
)

type LoanAccountPeriodicValue = dict[str, int] | None

MoneyMovement = TypedDict(
    'MoneyMovement',
    {
    'id': "str",
    'month': NotRequired["str | None"],
    'moved_at': NotRequired["str | None"],
    'note': NotRequired["str | None"],
    'money_movement_group_id': NotRequired["str | None"],
    'performed_by_user_id': NotRequired["str | None"],
    'from_category_id': NotRequired["str | None"],
    'to_category_id': NotRequired["str | None"],
    'amount': "int",
    'amount_formatted': NotRequired["str"],
    'amount_currency': NotRequired["float"],
    },
)

MoneyMovementBase = TypedDict(
    'MoneyMovementBase',
    {
    'id': "str",
    'month': NotRequired["str | None"],
    'moved_at': NotRequired["str | None"],
    'note': NotRequired["str | None"],
    'money_movement_group_id': NotRequired["str | None"],
    'performed_by_user_id': NotRequired["str | None"],
    'from_category_id': NotRequired["str | None"],
    'to_category_id': NotRequired["str | None"],
    'amount': "int",
    },
)

MoneyMovementGroup = TypedDict(
    'MoneyMovementGroup',
    {
    'id': "str",
    'group_created_at': "str",
    'month': "str",
    'note': NotRequired["str | None"],
    'performed_by_user_id': NotRequired["str | None"],
    },
)

MoneyMovementGroupsResponse = TypedDict(
    'MoneyMovementGroupsResponse',
    {
    'data': "MoneyMovementGroupsResponseData",
    },
)

MoneyMovementGroupsResponseData = TypedDict(
    'MoneyMovementGroupsResponseData',
    {
    'money_movement_groups': "list[MoneyMovementGroup]",
    'server_knowledge': "int",
    },
)

MoneyMovementsResponse = TypedDict(
    'MoneyMovementsResponse',
    {
    'data': "MoneyMovementsResponseData",
    },
)

MoneyMovementsResponseData = TypedDict(
    'MoneyMovementsResponseData',
    {
    'money_movements': "list[MoneyMovement]",
    'server_knowledge': "int",
    },
)

MonthDetail = TypedDict(
    'MonthDetail',
    {
    'month': "str",
    'note': NotRequired["str | None"],
    'income': "int",
    'budgeted': "int",
    'activity': "int",
    'to_be_budgeted': "int",
    'age_of_money': NotRequired["int | None"],
    'deleted': "bool",
    'income_formatted': NotRequired["str"],
    'income_currency': NotRequired["float"],
    'budgeted_formatted': NotRequired["str"],
    'budgeted_currency': NotRequired["float"],
    'activity_formatted': NotRequired["str"],
    'activity_currency': NotRequired["float"],
    'to_be_budgeted_formatted': NotRequired["str"],
    'to_be_budgeted_currency': NotRequired["float"],
    'categories': "list[Category]",
    },
)

MonthDetailBase = TypedDict(
    'MonthDetailBase',
    {
    'month': "str",
    'note': NotRequired["str | None"],
    'income': "int",
    'budgeted': "int",
    'activity': "int",
    'to_be_budgeted': "int",
    'age_of_money': NotRequired["int | None"],
    'deleted': "bool",
    'categories': "list[CategoryBase]",
    },
)

MonthDetailResponse = TypedDict(
    'MonthDetailResponse',
    {
    'data': "MonthDetailResponseData",
    },
)

MonthDetailResponseData = TypedDict(
    'MonthDetailResponseData',
    {
    'month': "MonthDetail",
    },
)

MonthSummariesResponse = TypedDict(
    'MonthSummariesResponse',
    {
    'data': "MonthSummariesResponseData",
    },
)

MonthSummariesResponseData = TypedDict(
    'MonthSummariesResponseData',
    {
    'months': "list[MonthSummary]",
    'server_knowledge': "int",
    },
)

MonthSummary = TypedDict(
    'MonthSummary',
    {
    'month': "str",
    'note': NotRequired["str | None"],
    'income': "int",
    'budgeted': "int",
    'activity': "int",
    'to_be_budgeted': "int",
    'age_of_money': NotRequired["int | None"],
    'deleted': "bool",
    'income_formatted': NotRequired["str"],
    'income_currency': NotRequired["float"],
    'budgeted_formatted': NotRequired["str"],
    'budgeted_currency': NotRequired["float"],
    'activity_formatted': NotRequired["str"],
    'activity_currency': NotRequired["float"],
    'to_be_budgeted_formatted': NotRequired["str"],
    'to_be_budgeted_currency': NotRequired["float"],
    },
)

MonthSummaryBase = TypedDict(
    'MonthSummaryBase',
    {
    'month': "str",
    'note': NotRequired["str | None"],
    'income': "int",
    'budgeted': "int",
    'activity': "int",
    'to_be_budgeted': "int",
    'age_of_money': NotRequired["int | None"],
    'deleted': "bool",
    },
)

NewCategory = TypedDict(
    'NewCategory',
    {
    'name': "str | None",
    'note': NotRequired["str | None"],
    'category_group_id': "str",
    'goal_target': NotRequired["int | None"],
    'goal_target_date': NotRequired["str | None"],
    'goal_needs_whole_amount': NotRequired["bool | None"],
    'goal_frequency': NotRequired["SaveCategoryGoalFrequency"],
    },
)

NewTransaction = TypedDict(
    'NewTransaction',
    {
    'account_id': NotRequired["str"],
    'date': NotRequired["str"],
    'amount': NotRequired["int"],
    'payee_id': NotRequired["str | None"],
    'payee_name': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'memo': NotRequired["str | None"],
    'cleared': NotRequired["TransactionClearedStatus"],
    'approved': NotRequired["bool"],
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'subtransactions': NotRequired["list[SaveSubTransaction]"],
    'import_id': NotRequired["str | None"],
    },
)

PatchCategoryGroupWrapper = TypedDict(
    'PatchCategoryGroupWrapper',
    {
    'category_group': "SaveCategoryGroup",
    },
)

PatchCategoryWrapper = TypedDict(
    'PatchCategoryWrapper',
    {
    'category': "ExistingCategory",
    },
)

PatchMonthCategoryWrapper = TypedDict(
    'PatchMonthCategoryWrapper',
    {
    'category': "SaveMonthCategory",
    },
)

PatchPayeeWrapper = TypedDict(
    'PatchPayeeWrapper',
    {
    'payee': "SavePayee",
    },
)

PatchTransactionsWrapper = TypedDict(
    'PatchTransactionsWrapper',
    {
    'transactions': "list[SaveTransactionWithIdOrImportId]",
    },
)

Payee = TypedDict(
    'Payee',
    {
    'id': "str",
    'name': "str",
    'transfer_account_id': NotRequired["str | None"],
    'deleted': "bool",
    },
)

PayeeLocation = TypedDict(
    'PayeeLocation',
    {
    'id': "str",
    'payee_id': "str",
    'latitude': "str",
    'longitude': "str",
    'deleted': "bool",
    },
)

PayeeLocationResponse = TypedDict(
    'PayeeLocationResponse',
    {
    'data': "PayeeLocationResponseData",
    },
)

PayeeLocationResponseData = TypedDict(
    'PayeeLocationResponseData',
    {
    'payee_location': "PayeeLocation",
    },
)

PayeeLocationsResponse = TypedDict(
    'PayeeLocationsResponse',
    {
    'data': "PayeeLocationsResponseData",
    },
)

PayeeLocationsResponseData = TypedDict(
    'PayeeLocationsResponseData',
    {
    'payee_locations': "list[PayeeLocation]",
    },
)

PayeeResponse = TypedDict(
    'PayeeResponse',
    {
    'data': "PayeeResponseData",
    },
)

PayeeResponseData = TypedDict(
    'PayeeResponseData',
    {
    'payee': "Payee",
    },
)

PayeesResponse = TypedDict(
    'PayeesResponse',
    {
    'data': "PayeesResponseData",
    },
)

PayeesResponseData = TypedDict(
    'PayeesResponseData',
    {
    'payees': "list[Payee]",
    'server_knowledge': "int",
    },
)

PlanDetail = TypedDict(
    'PlanDetail',
    {
    'id': "str",
    'name': "str",
    'last_modified_on': NotRequired["str"],
    'first_month': NotRequired["str"],
    'last_month': NotRequired["str"],
    'date_format': NotRequired["DateFormat | None"],
    'currency_format': NotRequired["CurrencyFormat | None"],
    'accounts': NotRequired["list[Account]"],
    'payees': NotRequired["list[Payee]"],
    'payee_locations': NotRequired["list[PayeeLocation]"],
    'category_groups': NotRequired["list[CategoryGroup]"],
    'categories': NotRequired["list[CategoryBase]"],
    'months': NotRequired["list[MonthDetailBase]"],
    'transactions': NotRequired["list[TransactionSummaryBase]"],
    'subtransactions': NotRequired["list[SubTransactionBase]"],
    'scheduled_transactions': NotRequired["list[ScheduledTransactionDetail]"],
    'scheduled_subtransactions': NotRequired["list[ScheduledSubTransaction]"],
    },
)

PlanDetailResponse = TypedDict(
    'PlanDetailResponse',
    {
    'data': "PlanDetailResponseData",
    },
)

PlanDetailResponseData = TypedDict(
    'PlanDetailResponseData',
    {
    'plan': "PlanDetail",
    'server_knowledge': "int",
    },
)

PlanSettings = TypedDict(
    'PlanSettings',
    {
    'date_format': "DateFormat | None",
    'currency_format': "CurrencyFormat | None",
    },
)

PlanSettingsResponse = TypedDict(
    'PlanSettingsResponse',
    {
    'data': "PlanSettingsResponseData",
    },
)

PlanSettingsResponseData = TypedDict(
    'PlanSettingsResponseData',
    {
    'settings': "PlanSettings",
    },
)

PlanSummary = TypedDict(
    'PlanSummary',
    {
    'id': "str",
    'name': "str",
    'last_modified_on': NotRequired["str"],
    'first_month': NotRequired["str"],
    'last_month': NotRequired["str"],
    'date_format': NotRequired["DateFormat | None"],
    'currency_format': NotRequired["CurrencyFormat | None"],
    'accounts': NotRequired["list[Account]"],
    },
)

PlanSummaryResponse = TypedDict(
    'PlanSummaryResponse',
    {
    'data': "PlanSummaryResponseData",
    },
)

PlanSummaryResponseData = TypedDict(
    'PlanSummaryResponseData',
    {
    'plans': "list[PlanSummary]",
    'default_plan': NotRequired["PlanSummary | None"],
    },
)

PostAccountWrapper = TypedDict(
    'PostAccountWrapper',
    {
    'account': "SaveAccount",
    },
)

PostCategoryGroupWrapper = TypedDict(
    'PostCategoryGroupWrapper',
    {
    'category_group': "SaveCategoryGroup",
    },
)

PostCategoryWrapper = TypedDict(
    'PostCategoryWrapper',
    {
    'category': "NewCategory",
    },
)

PostPayee = TypedDict(
    'PostPayee',
    {
    'name': "str",
    },
)

PostPayeeWrapper = TypedDict(
    'PostPayeeWrapper',
    {
    'payee': "PostPayee",
    },
)

PostScheduledTransactionWrapper = TypedDict(
    'PostScheduledTransactionWrapper',
    {
    'scheduled_transaction': "SaveScheduledTransaction",
    },
)

PostTransactionsWrapper = TypedDict(
    'PostTransactionsWrapper',
    {
    'transaction': NotRequired["NewTransaction"],
    'transactions': NotRequired["list[NewTransaction]"],
    },
)

PutScheduledTransactionWrapper = TypedDict(
    'PutScheduledTransactionWrapper',
    {
    'scheduled_transaction': "SaveScheduledTransaction",
    },
)

PutTransactionWrapper = TypedDict(
    'PutTransactionWrapper',
    {
    'transaction': "ExistingTransaction",
    },
)

SaveAccount = TypedDict(
    'SaveAccount',
    {
    'name': "str",
    'type': "SaveAccountType",
    'balance': "int",
    },
)

type SaveAccountType = Literal['checking', 'savings', 'cash', 'creditCard', 'otherAsset', 'otherLiability']
"""The type of account to create or update"""

SaveCategory = TypedDict(
    'SaveCategory',
    {
    'name': NotRequired["str | None"],
    'note': NotRequired["str | None"],
    'category_group_id': NotRequired["str"],
    'goal_target': NotRequired["int | None"],
    'goal_target_date': NotRequired["str | None"],
    'goal_needs_whole_amount': NotRequired["bool | None"],
    'goal_frequency': NotRequired["SaveCategoryGoalFrequency"],
    },
)

type SaveCategoryGoalFrequency = Literal['monthly', 'weekly', 'yearly']
"""When specified, configures a recurring 'NEED' target of goal_target that repeats at this frequency, replacing any existing target. Requires goal_target. 'yearly' also requires goal_target_date, the date the target is next due. 'monthly' accepts an optional goal_target_date, and 'weekly' cannot be combined with goal_target_date. Not supported for Credit Card Payment categories or categories paired to a loan account. Omit to leave an existing target's cadence unchanged."""

SaveCategoryGroup = TypedDict(
    'SaveCategoryGroup',
    {
    'name': "str",
    },
)

SaveCategoryGroupResponse = TypedDict(
    'SaveCategoryGroupResponse',
    {
    'data': "SaveCategoryGroupResponseData",
    },
)

SaveCategoryGroupResponseData = TypedDict(
    'SaveCategoryGroupResponseData',
    {
    'category_group': "CategoryGroup",
    'server_knowledge': "int",
    },
)

SaveCategoryResponse = TypedDict(
    'SaveCategoryResponse',
    {
    'data': "SaveCategoryResponseData",
    },
)

SaveCategoryResponseData = TypedDict(
    'SaveCategoryResponseData',
    {
    'category': "Category",
    'server_knowledge': "int",
    },
)

SaveMonthCategory = TypedDict(
    'SaveMonthCategory',
    {
    'budgeted': "int",
    },
)

SavePayee = TypedDict(
    'SavePayee',
    {
    'name': NotRequired["str"],
    },
)

SavePayeeResponse = TypedDict(
    'SavePayeeResponse',
    {
    'data': "SavePayeeResponseData",
    },
)

SavePayeeResponseData = TypedDict(
    'SavePayeeResponseData',
    {
    'payee': "Payee",
    'server_knowledge': "int",
    },
)

SaveScheduledTransaction = TypedDict(
    'SaveScheduledTransaction',
    {
    'account_id': "str",
    'date': "str",
    'amount': NotRequired["int"],
    'payee_id': NotRequired["str | None"],
    'payee_name': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'memo': NotRequired["str | None"],
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'frequency': NotRequired["ScheduledTransactionFrequency"],
    },
)

SaveSubTransaction = TypedDict(
    'SaveSubTransaction',
    {
    'amount': "int",
    'payee_id': NotRequired["str | None"],
    'payee_name': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'memo': NotRequired["str | None"],
    },
)

SaveTransactionWithIdOrImportId = TypedDict(
    'SaveTransactionWithIdOrImportId',
    {
    'id': NotRequired["str | None"],
    'import_id': NotRequired["str | None"],
    'account_id': NotRequired["str"],
    'date': NotRequired["str"],
    'amount': NotRequired["int"],
    'payee_id': NotRequired["str | None"],
    'payee_name': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'memo': NotRequired["str | None"],
    'cleared': NotRequired["TransactionClearedStatus"],
    'approved': NotRequired["bool"],
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'subtransactions': NotRequired["list[SaveSubTransaction]"],
    },
)

SaveTransactionWithOptionalFields = TypedDict(
    'SaveTransactionWithOptionalFields',
    {
    'account_id': NotRequired["str"],
    'date': NotRequired["str"],
    'amount': NotRequired["int"],
    'payee_id': NotRequired["str | None"],
    'payee_name': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'memo': NotRequired["str | None"],
    'cleared': NotRequired["TransactionClearedStatus"],
    'approved': NotRequired["bool"],
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'subtransactions': NotRequired["list[SaveSubTransaction]"],
    },
)

SaveTransactionsResponse = TypedDict(
    'SaveTransactionsResponse',
    {
    'data': "SaveTransactionsResponseData",
    },
)

SaveTransactionsResponseData = TypedDict(
    'SaveTransactionsResponseData',
    {
    'transaction_ids': "list[str]",
    'transaction': NotRequired["TransactionDetail"],
    'transactions': NotRequired["list[TransactionDetail]"],
    'duplicate_import_ids': NotRequired["list[str]"],
    'server_knowledge': "int",
    },
)

ScheduledSubTransaction = TypedDict(
    'ScheduledSubTransaction',
    {
    'id': "str",
    'scheduled_transaction_id': "str",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'payee_id': NotRequired["str | None"],
    'payee_name': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'category_name': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'deleted': "bool",
    'amount_formatted': NotRequired["str"],
    'amount_currency': NotRequired["float"],
    },
)

ScheduledSubTransactionBase = TypedDict(
    'ScheduledSubTransactionBase',
    {
    'id': "str",
    'scheduled_transaction_id': "str",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'payee_id': NotRequired["str | None"],
    'payee_name': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'category_name': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'deleted': "bool",
    },
)

ScheduledTransactionDetail = TypedDict(
    'ScheduledTransactionDetail',
    {
    'id': "str",
    'date_first': "str",
    'date_next': "str",
    'frequency': "ScheduledTransactionSummaryBaseFrequency",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'flag_name': NotRequired["TransactionFlagName | None"],
    'account_id': "str",
    'payee_id': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'deleted': "bool",
    'amount_formatted': NotRequired["str"],
    'amount_currency': NotRequired["float"],
    'account_name': "str",
    'payee_name': NotRequired["str | None"],
    'category_name': NotRequired["str | None"],
    'subtransactions': "list[ScheduledSubTransaction]",
    },
)

type ScheduledTransactionFrequency = Literal['never', 'daily', 'weekly', 'everyOtherWeek', 'twiceAMonth', 'every4Weeks', 'monthly', 'everyOtherMonth', 'every3Months', 'every4Months', 'twiceAYear', 'yearly', 'everyOtherYear']
"""The scheduled transaction frequency"""

ScheduledTransactionResponse = TypedDict(
    'ScheduledTransactionResponse',
    {
    'data': "ScheduledTransactionResponseData",
    },
)

ScheduledTransactionResponseData = TypedDict(
    'ScheduledTransactionResponseData',
    {
    'scheduled_transaction': "ScheduledTransactionDetail",
    },
)

ScheduledTransactionSummary = TypedDict(
    'ScheduledTransactionSummary',
    {
    'id': "str",
    'date_first': "str",
    'date_next': "str",
    'frequency': "ScheduledTransactionSummaryBaseFrequency",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'flag_name': NotRequired["TransactionFlagName | None"],
    'account_id': "str",
    'payee_id': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'deleted': "bool",
    'amount_formatted': NotRequired["str"],
    'amount_currency': NotRequired["float"],
    },
)

ScheduledTransactionSummaryBase = TypedDict(
    'ScheduledTransactionSummaryBase',
    {
    'id': "str",
    'date_first': "str",
    'date_next': "str",
    'frequency': "ScheduledTransactionSummaryBaseFrequency",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'flag_name': NotRequired["TransactionFlagName | None"],
    'account_id': "str",
    'payee_id': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'deleted': "bool",
    },
)

type ScheduledTransactionSummaryBaseFrequency = Literal['never', 'daily', 'weekly', 'everyOtherWeek', 'twiceAMonth', 'every4Weeks', 'monthly', 'everyOtherMonth', 'every3Months', 'every4Months', 'twiceAYear', 'yearly', 'everyOtherYear']

ScheduledTransactionsResponse = TypedDict(
    'ScheduledTransactionsResponse',
    {
    'data': "ScheduledTransactionsResponseData",
    },
)

ScheduledTransactionsResponseData = TypedDict(
    'ScheduledTransactionsResponseData',
    {
    'scheduled_transactions': "list[ScheduledTransactionDetail]",
    'server_knowledge': "int",
    },
)

SubTransaction = TypedDict(
    'SubTransaction',
    {
    'id': "str",
    'transaction_id': "str",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'payee_id': NotRequired["str | None"],
    'payee_name': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'category_name': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'transfer_transaction_id': NotRequired["str | None"],
    'deleted': "bool",
    'amount_formatted': NotRequired["str"],
    'amount_currency': NotRequired["float"],
    },
)

SubTransactionBase = TypedDict(
    'SubTransactionBase',
    {
    'id': "str",
    'transaction_id': "str",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'payee_id': NotRequired["str | None"],
    'payee_name': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'category_name': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'transfer_transaction_id': NotRequired["str | None"],
    'deleted': "bool",
    },
)

type TransactionClearedStatus = Literal['cleared', 'uncleared', 'reconciled']
"""The cleared status of the transaction"""

TransactionDetail = TypedDict(
    'TransactionDetail',
    {
    'id': "str",
    'date': "str",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'cleared': "TransactionClearedStatus",
    'approved': "bool",
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'flag_name': NotRequired["TransactionFlagName | None"],
    'account_id': "str",
    'payee_id': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'transfer_transaction_id': NotRequired["str | None"],
    'matched_transaction_id': NotRequired["str | None"],
    'import_id': NotRequired["str | None"],
    'import_payee_name': NotRequired["str | None"],
    'import_payee_name_original': NotRequired["str | None"],
    'debt_transaction_type': NotRequired["TransactionSummaryBaseDebtTransactionType | None"],
    'deleted': "bool",
    'amount_formatted': NotRequired["str"],
    'amount_currency': NotRequired["float"],
    'account_name': "str",
    'payee_name': NotRequired["str | None"],
    'category_name': NotRequired["str | None"],
    'subtransactions': "list[SubTransaction]",
    },
)

type TransactionFlagColor = Literal['red', 'orange', 'yellow', 'green', 'blue', 'purple', '']
"""The transaction flag"""

type TransactionFlagName = str | None
"""The customized name of a transaction flag"""

TransactionResponse = TypedDict(
    'TransactionResponse',
    {
    'data': "TransactionResponseData",
    },
)

TransactionResponseData = TypedDict(
    'TransactionResponseData',
    {
    'transaction': "TransactionDetail",
    'server_knowledge': "int",
    },
)

TransactionSummary = TypedDict(
    'TransactionSummary',
    {
    'id': "str",
    'date': "str",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'cleared': "TransactionClearedStatus",
    'approved': "bool",
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'flag_name': NotRequired["TransactionFlagName | None"],
    'account_id': "str",
    'payee_id': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'transfer_transaction_id': NotRequired["str | None"],
    'matched_transaction_id': NotRequired["str | None"],
    'import_id': NotRequired["str | None"],
    'import_payee_name': NotRequired["str | None"],
    'import_payee_name_original': NotRequired["str | None"],
    'debt_transaction_type': NotRequired["TransactionSummaryBaseDebtTransactionType | None"],
    'deleted': "bool",
    'amount_formatted': NotRequired["str"],
    'amount_currency': NotRequired["float"],
    },
)

TransactionSummaryBase = TypedDict(
    'TransactionSummaryBase',
    {
    'id': "str",
    'date': "str",
    'amount': "int",
    'memo': NotRequired["str | None"],
    'cleared': "TransactionClearedStatus",
    'approved': "bool",
    'flag_color': NotRequired["TransactionFlagColor | None"],
    'flag_name': NotRequired["TransactionFlagName | None"],
    'account_id': "str",
    'payee_id': NotRequired["str | None"],
    'category_id': NotRequired["str | None"],
    'transfer_account_id': NotRequired["str | None"],
    'transfer_transaction_id': NotRequired["str | None"],
    'matched_transaction_id': NotRequired["str | None"],
    'import_id': NotRequired["str | None"],
    'import_payee_name': NotRequired["str | None"],
    'import_payee_name_original': NotRequired["str | None"],
    'debt_transaction_type': NotRequired["TransactionSummaryBaseDebtTransactionType | None"],
    'deleted': "bool",
    },
)

type TransactionSummaryBaseDebtTransactionType = Literal['payment', 'refund', 'fee', 'interest', 'escrow', 'balanceAdjustment', 'credit', 'charge']
"""If the transaction is a debt/loan account transaction, the type of transaction"""

TransactionsImportResponse = TypedDict(
    'TransactionsImportResponse',
    {
    'data': "TransactionsImportResponseData",
    },
)

TransactionsImportResponseData = TypedDict(
    'TransactionsImportResponseData',
    {
    'transaction_ids': "list[str]",
    },
)

TransactionsResponse = TypedDict(
    'TransactionsResponse',
    {
    'data': "TransactionsResponseData",
    },
)

TransactionsResponseData = TypedDict(
    'TransactionsResponseData',
    {
    'transactions': "list[TransactionDetail]",
    'server_knowledge': "int",
    },
)

User = TypedDict(
    'User',
    {
    'id': "str",
    },
)

UserResponse = TypedDict(
    'UserResponse',
    {
    'data': "UserResponseData",
    },
)

UserResponseData = TypedDict(
    'UserResponseData',
    {
    'user': "User",
    },
)
