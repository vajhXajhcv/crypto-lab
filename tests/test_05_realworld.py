import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "05_realworld"))

from inspect_tls import inspect_tls


def test_inspect_tls_runs():
    """TLS 检查依赖网络，只验证函数能正常执行不报错"""
    inspect_tls("wumingmp.me")
