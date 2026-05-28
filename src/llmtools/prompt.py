def render(template: str, **kwargs) -> str:
    try:
        return template.format(**kwargs)
    except KeyError as e:
        missing = e.args[0]
        raise ValueError(f"Missing variable in prompt: {missing}")


def with_system(prompt: str, system: str) -> str:
    return f"SYSTEM:\n{system}\n\nUSER:\n{prompt}"