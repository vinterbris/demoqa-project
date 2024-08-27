def relative_from_root(path: str):
    import demoqa_tests
    from pathlib import Path

    return Path(demoqa_tests.__file__).parent.parent.joinpath(path).absolute().__str__()
