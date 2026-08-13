from nbresult import ChallengeResultTestCase
import pandas as pd


class TestCustomers(ChallengeResultTestCase):
    def test_df_columns(self):
        required_columns = ['customers_id']
        self.assertTrue(
            all(col in self.result.columns for col in required_columns),
            f"DataFrame must contain required column: {required_columns}. Extra columns are fine!"
        )

    def test_df_shape(self):
        self.assertGreater(
            self.result.shape[0],
            20,
            "Customer cohort has too few rows. Did you aggregate by month correctly?")
        self.assertGreaterEqual(
            self.result.shape[1],
            1,
            "DataFrame should have at least 1 column")

    def test_cohort_not_empty(self):
        self.assertGreater(
            self.result.shape[0], 0,
            "Customer cohort DataFrame is empty. Did you aggregate the data?"
        )

    def test_df_index(self):
        self.assertEqual(type(self.result.df_index), pd.DatetimeIndex)

    def test_df_index_gap_monthly(self):
        self.assertIsNotNone(
            self.result.df_index.freq,
            "Index should have a frequency set")
        self.assertIn(str(self.result.df_index.freq), ['<MonthEnd>', 'M', 'ME'],
                      "Frequency should be monthly (month-end)")
