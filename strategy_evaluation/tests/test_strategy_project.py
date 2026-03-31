import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

"""Run strategy evaluation experiments for in/out-of-sample and impact sensitivity."""

import datetime as dt
from ManualStrategy import ManualStrategy
from StrategyLearner import StrategyLearner
from experiment1 import compute_benchmark, plot_portfolio_values, print_stats
from experiment2 import compute_benchmark2, plot_portfolio_values2, print_stats2
from marketsimcode import compute_portvals


def author():
    return "ndaponte3"


def study_group():
    return "ndaponte3"


def run_experiment_1(symbol="JPM", sv=100000):
    manual = ManualStrategy()
    learner = StrategyLearner(verbose=False, impact=0.005, commission=9.95)

    # In-sample evaluation.
    sd_in, ed_in = dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31)
    learner.add_evidence(symbol=symbol, sd=sd_in, ed=ed_in, sv=sv)

    trades_manual_in = manual.testPolicy(symbol=symbol, sd=sd_in, ed=ed_in, sv=sv)
    trades_learner_in = learner.testPolicy(symbol=symbol, sd=sd_in, ed=ed_in, sv=sv)

    vals_manual_in = compute_portvals(trades_manual_in, start_val=sv, commission=9.95, impact=0.005)
    vals_learner_in = compute_portvals(trades_learner_in, start_val=sv, commission=9.95, impact=0.005)
    vals_bench_in = compute_benchmark(sd_in, ed_in, sv, symbol=symbol, impact=0.005)

    vals_manual_in = vals_manual_in / vals_manual_in.iloc[0]
    vals_learner_in = vals_learner_in / vals_learner_in.iloc[0]

    plot_portfolio_values(vals_manual_in, vals_learner_in, vals_bench_in, sample="IN_SAMPLE", save_filename="IN_1.png")
    print_stats(vals_bench_in, vals_manual_in, "in_sample_stats.txt")

    # Out-of-sample evaluation using learned policy.
    sd_out, ed_out = dt.datetime(2010, 1, 1), dt.datetime(2011, 12, 31)
    trades_manual_out = manual.testPolicy(symbol=symbol, sd=sd_out, ed=ed_out, sv=sv)
    trades_learner_out = learner.testPolicy(symbol=symbol, sd=sd_out, ed=ed_out, sv=sv)

    vals_manual_out = compute_portvals(trades_manual_out, start_val=sv, commission=9.95, impact=0.005)
    vals_learner_out = compute_portvals(trades_learner_out, start_val=sv, commission=9.95, impact=0.005)
    vals_bench_out = compute_benchmark(sd_out, ed_out, sv, symbol=symbol, impact=0.005)

    vals_manual_out = vals_manual_out / vals_manual_out.iloc[0]
    vals_learner_out = vals_learner_out / vals_learner_out.iloc[0]

    plot_portfolio_values(vals_manual_out, vals_learner_out, vals_bench_out, sample="OUT_SAMPLE", save_filename="OUT_1.png")
    print_stats(vals_bench_out, vals_manual_out, "out_sample_stats.txt")


def run_experiment_2(symbol="JPM", sv=100000):
    sd, ed = dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31)
    for impact in [0.000, 0.005, 0.010]:
        learner = StrategyLearner(verbose=False, impact=impact, commission=9.95)
        learner.add_evidence(symbol=symbol, sd=sd, ed=ed, sv=sv)
        trades = learner.testPolicy(symbol=symbol, sd=sd, ed=ed, sv=sv)

        vals_learner = compute_portvals(trades, start_val=sv, commission=9.95, impact=impact)
        vals_learner = vals_learner / vals_learner.iloc[0]
        vals_bench = compute_benchmark2(sd, ed, sv, symbol=symbol, impact=impact)

        plot_portfolio_values2(vals_learner, vals_bench, sample="IN_SAMPLE", save_filename=f"IN_{impact}.png")
        print_stats2(vals_bench, vals_learner, f"{impact}_impact.txt")


if __name__ == "__main__":
    run_experiment_1()
    run_experiment_2()

