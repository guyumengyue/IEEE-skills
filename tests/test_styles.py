from pathlib import Path

import matplotlib.pyplot as plt

from ieee_skills import audit_figure, save_figure
from ieee_skills.styles import IEEEFigureSpec


def test_figure_spec_one_column():
    spec = IEEEFigureSpec(columns=1)
    assert abs(spec.width - 3.5) < 1e-9


def test_save_figure_creates_outputs(tmp_path: Path):
    fig, ax = plt.subplots(figsize=(3.5, 2.2))
    ax.plot([0, 1], [0, 1])
    outputs = save_figure(fig, tmp_path / "demo", formats=("pdf", "png"))
    assert all(path.exists() for path in outputs)
    assert audit_figure(fig, intended_columns=1) == []
