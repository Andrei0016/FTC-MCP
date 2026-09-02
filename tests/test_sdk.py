import pytest

from ftc_mcp.tools import sdk


def test_libs_present():
    txt = sdk.list_libs()
    for lib in ("ftc-sdk", "pedro-pathing", "panels"):
        assert lib in txt


def test_lib_index_lists_packages():
    idx = sdk.lib_index("pedro-pathing")
    assert "com.pedropathing.follower" in idx


def test_package_digest_exact_signatures():
    d = sdk.package_digest("pedro-pathing", "com.pedropathing.follower")
    assert "class Follower" in d
    assert "void followPath(" in d
    assert "boolean isBusy();" in d


def test_search_method_across_libs():
    out = sdk.search("followPath")
    assert "[pedro-pathing]" in out and "Follower" in out


def test_search_lib_filter():
    out = sdk.search("setVelocity", "ftc-sdk")
    assert "DcMotorEx" in out
    assert "[pedro-pathing]" not in out


def test_class_block_by_simple_name():
    b = sdk.class_block("DcMotorEx")
    assert "interface DcMotorEx" in b
    assert "setVelocity(double" in b
    assert "ftc://sdk/ftc-sdk/com.qualcomm.robotcore.hardware" in b


def test_class_block_unknown():
    assert "not found" in sdk.class_block("NoSuchClassXYZ")


def test_unknown_lib_raises():
    with pytest.raises(ValueError):
        sdk.package_digest("bogus", "x")
