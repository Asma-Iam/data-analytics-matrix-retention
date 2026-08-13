from nbresult import ChallengeResultTestCase
import pandas as pd


class TestMatrix(ChallengeResultTestCase):
    def test_df_columns(self):
        self.assertGreater(
            len(self.result.columns), 10,
            "Retention matrix has too few columns. Did you pivot the data correctly?"
        )

    def test_df_shape(self):
        self.assertGreater(
            self.result.shape[0], 10,
            "Retention matrix has too few cohorts. Did you create all cohorts?"
        )
        self.assertGreater(
            self.result.shape[1],
            10,
            "Retention matrix has too few month columns. Check your pivot operation.")

    def test_matrix_not_empty(self):
        self.assertGreater(
            self.result.shape[0], 0,
            "Retention matrix is empty. Did you create the pivot table?"
        )

    def test_df_index(self):
        self.assertEqual(type(self.result.df_index), pd.DatetimeIndex)
