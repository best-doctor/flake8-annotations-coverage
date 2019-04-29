

def has_type_annotations(func_def) -> bool:
    has_return_annotation = func_def.returns is not None
    has_args_annotations = any(a for a in func_def.args.args if a.annotation is not None)
    has_kwargs_annotations = func_def.args and func_def.args.kwarg and func_def.args.kwarg.annotation is not None
    has_kwonly_args_annotations = any(a for a in func_def.args.kwonlyargs if a.annotation is not None)
    return any(
        (has_return_annotation, has_kwargs_annotations, has_args_annotations, has_kwonly_args_annotations),
    )
