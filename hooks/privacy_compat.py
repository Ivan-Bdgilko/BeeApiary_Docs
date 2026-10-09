"""Keep Material's Google Fonts cache usable without Windows symlink privileges."""

import os
from mkdocs.plugins import event_priority


@event_priority(-200)
def on_config(config):
    if os.name != "nt":
        return config
    plugin = config.plugins.get("material/privacy") or config.plugins.get("privacy")
    if plugin is None:
        raise RuntimeError("Google Fonts privacy plugin is required")
    original = getattr(plugin, "_beeapiary_path_to_file", plugin._path_to_file)
    plugin._beeapiary_path_to_file = original

    def path_to_file(path, config):
        file = original(path, config)
        # Google Fonts returns CSS from the extensionless /css endpoint.
        # Give only this known CSS response its real cache extension upfront.
        # Material then performs its normal download, rewriting and validation
        # without trying to create a privileged extensionless symbolic link.
        if path.startswith("fonts.googleapis.com/css."):
            file.abs_src_path += ".css"
        return file

    plugin._path_to_file = path_to_file
    return config
