# ⚠️⚠️⚠️ Deprecation notice ⚠️⚠️⚠️ 

The `supafunc` package name is deprecated and is not going to receive any more updates. Please, use `supabase_functions` instead.

## How to switch

1. Use `uv add supabase_functions` instead of `uv add supafunc`.
2. Replace `supafunc` with `supabase_functions` in your `requirements.txt`, `pyproject.toml`, `setup.py`, etc.
3. Replace all imports `from supafunc import ...` to `from supabase_functions import ...`
4. If `supafunc` is still used by one of your dependencies, consider reporting it in their issue tracker.

## Reasoning

The `supafunc` package has been replaced by the `supabase_functions` since December 14th, 2024, following the JavaScript implementation name switch. Changes and fixes were maintained for a couple of months by pushing them in both packages at the same time, using a patching script.

In order to simplify maintenance and development of new features, the `supafunc` package is going to cease receiving updates as of 7th of August 2025, and going forward everyone should use `supabase_functions` instead.
