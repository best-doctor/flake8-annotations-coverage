

def has_type_annotations(func_def) -> bool:
    has_return_annotation = func_def.returns is not None
    has_args_annotations = any(a for a in func_def.args.args if a.annotation is not None)
    has_kwonly_args_annotations = any(a for a in func_def.args.kwonlyargs if a.annotation is not None)
    return has_return_annotation or has_args_annotations or has_kwonly_args_annotations
