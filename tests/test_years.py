from nbresult import ChallengeResultTestCase
import pandas as pd


class TestYears(ChallengeResultTestCase):
    def test_df_columns(self):
        required_columns = ['total_turnover']
        self.assertTrue(
            all(col in self.result.columns for col in required_columns),
            f"DataFrame must contain required column: {required_columns}. Extra columns are fine!"
        )

    def test_df_shape(self):
        self.assertGreaterEqual(
            self.result.shape[0],
            3,
            "Should have at least 3 years of data")
        self.assertGreaterEqual(
            self.result.shape[1],
            1,
            "DataFrame should have at least 1 column")

    def test_yearly_aggregation_not_empty(self):
        self.assertGreater(
            self.result.shape[0], 0,
            "Yearly aggregation is empty. Did you aggregate by year correctly?"
        )

    def test_df_values(self):
        self.assertEqual(
            self.result.values, [
                [20990674.51], [30413594.84], [25917818.28]])

    def test_df_index(self):
        self.assertEqual(type(self.result.df_index), pd.DatetimeIndex)

    def test_df_index_gap_yearly(self):
        self.assertIsNotNone(
            self.result.df_index.freq,
            "Index should have a frequency set")
        self.assertIn(str(self.result.df_index.freq),
                      ['<YearEnd: month=12>',
                       'YE-DEC',
                       'A-DEC',
                       'Y'],
                      "Frequency should be yearly (year-end)")
