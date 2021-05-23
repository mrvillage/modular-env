def _get_envs():
    from pathlib import Path
    from json import loads
    path = Path(__file__).parent
    envs = [i for i in path.glob(".env*")]
    for env in envs:
        with open(env, "r") as f:
            lines = [i.strip() for i in f.readlines()]
        for line in lines:
            arg = line.split("=")
            arg[0] = arg[0].upper()
            if arg[0].startswith("INT"):
                globals()[f"{env.suffix[1:].upper()}{arg[0].replace('INT', '')}"] = int(
                    arg[1])
            elif arg[0].startswith("JSON"):
                globals()[f"{env.suffix[1:].upper()}{arg[0].replace('JSON', '')}"] = loads(
                    arg[1])
            else:
                globals()[f"{env.suffix[1:].upper()}{arg[0]}"] = arg[1]


_get_envs()
