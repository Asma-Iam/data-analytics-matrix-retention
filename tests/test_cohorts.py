from nbresult import ChallengeResultTestCase
import pandas as pd


class TestCohorts(ChallengeResultTestCase):
    def test_df_required_columns(self):
        required_columns = [
            'date_date',
            'orders_id',
            'customers_id',
            'member_at',
            'cohort',
            'nb_months',
            'total_turnover']
        self.assertTrue(
            all(col in self.result.columns for col in required_columns),
            f"DataFrame must contain required cohort columns: {required_columns}. Extra columns are fine!"
        )

    def test_df_shape(self):
        self.assertGreater(
            self.result.shape[0], 150000,
            "Cohort DataFrame has too few rows. Did you join/merge correctly?"
        )
        self.assertGreaterEqual(
            self.result.shape[1],
            10,
            "DataFrame should have at least 10 columns")

    def test_cohort_data_not_empty(self):
        self.assertGreater(
            self.result.shape[0],
            0,
            "Cohort DataFrame is empty. Did you create the cohort analysis correctly?")

    def test_df_index(self):
        self.assertNotEqual(type(self.result.df_index), pd.DatetimeIndex)
