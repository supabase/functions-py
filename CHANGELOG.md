# CHANGELOG



## v0.3.3 (2024-01-03)

### Fix

* fix: update job to publish legacy package if current is released (#36) ([`2565c37`](https://github.com/supabase-community/functions-py/commit/2565c372124c08bc2a0bd8fd4b3005cf427062e3))


## v0.3.2 (2024-01-03)

### Chore

* chore(release): bump version to v0.3.2 ([`403418c`](https://github.com/supabase-community/functions-py/commit/403418cc3a801be12e73f84e53daddd517cd5de0))

* chore(deps-dev): bump isort from 5.12.0 to 5.13.0 (#24) ([`e7443ee`](https://github.com/supabase-community/functions-py/commit/e7443eeaad029a19a4276bae8ebfb899d042be3a))

* chore(deps-dev): bump isort from 5.12.0 to 5.13.0

Bumps [isort](https://github.com/pycqa/isort) from 5.12.0 to 5.13.0.
- [Release notes](https://github.com/pycqa/isort/releases)
- [Changelog](https://github.com/PyCQA/isort/blob/main/CHANGELOG.md)
- [Commits](https://github.com/pycqa/isort/compare/5.12.0...5.13.0)

---
updated-dependencies:
- dependency-name: isort
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`89a31c9`](https://github.com/supabase-community/functions-py/commit/89a31c9afb987063f18dd853bc826e4d7e815be3))

* chore(deps-dev): bump pytest-asyncio from 0.21.1 to 0.23.2 (#22) ([`ab767f5`](https://github.com/supabase-community/functions-py/commit/ab767f5cf591679f38404cf609a42d853620c96f))

* chore(deps-dev): bump pytest-asyncio from 0.21.1 to 0.23.2

Bumps [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio) from 0.21.1 to 0.23.2.
- [Release notes](https://github.com/pytest-dev/pytest-asyncio/releases)
- [Commits](https://github.com/pytest-dev/pytest-asyncio/compare/v0.21.1...v0.23.2)

---
updated-dependencies:
- dependency-name: pytest-asyncio
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f6fb590`](https://github.com/supabase-community/functions-py/commit/f6fb5906e99e5194413ef8b7f819ba82ae47355e))

* chore: allow manual workflow trigger for releases (#19) ([`07d1ffa`](https://github.com/supabase-community/functions-py/commit/07d1ffa6faa89219f7c73cbd4699436763d9d8bc))

* chore: allow manual workflow trigger for releases ([`2a01399`](https://github.com/supabase-community/functions-py/commit/2a013997215f417fb0efe2badfc9b8a2d3686c48))

### Ci

* ci: update workflow with new pypi project name (#34) ([`7564e2b`](https://github.com/supabase-community/functions-py/commit/7564e2bc1d157a279175a3c8ad6fb2708e1700f4))

### Fix

* fix: update httpx and other dev dependencies (#35) ([`1f8897f`](https://github.com/supabase-community/functions-py/commit/1f8897f88acc4449cd697bd0e122bd4ee3bf0417))


## v0.3.1 (2023-10-30)

### Chore

* chore(release): bump version to v0.3.1 ([`b787f01`](https://github.com/supabase-community/functions-py/commit/b787f0187c1a5312ea368919afd24863ff2f40f0))

### Fix

* fix: exceptions now has message in dictionary (#16) ([`7273927`](https://github.com/supabase-community/functions-py/commit/7273927aa9d0e6eb9d9c9985a7ba5b42f9b6296d))

* fix: exceptions now has message in dictionary

Added tests to check for the messages. ([`07a813a`](https://github.com/supabase-community/functions-py/commit/07a813a02ffcf8999802cece27ee5278c140760d))


## v0.3.0 (2023-10-29)

### Chore

* chore(release): bump version to v0.3.0 ([`4e18712`](https://github.com/supabase-community/functions-py/commit/4e1871215e72efed058d5adf619ae2be0bb27b56))

### Feature

* feat: downgrade httpx dep to 0.24.0 (#15) ([`1f37216`](https://github.com/supabase-community/functions-py/commit/1f37216326c26b65a3c9ccd1c29bea0a184c7624))

### Fix

* fix: update lockfile ([`d4856ec`](https://github.com/supabase-community/functions-py/commit/d4856ec8c6bbbde7efe7ca67c5137ba75e8e7bdb))

### Unknown

* Update pyproject.toml ([`dd43949`](https://github.com/supabase-community/functions-py/commit/dd4394994ae995dd6f953093da73cbd9c1344483))

* Restoring order to the CI/CD pipeline ([`4f28dc6`](https://github.com/supabase-community/functions-py/commit/4f28dc628c9a9aac27a153121c90960bddb5c8bf))


## v0.2.4 (2023-10-25)

### Chore

* chore(release): bump version to v0.2.4 ([`f618547`](https://github.com/supabase-community/functions-py/commit/f61854760d2d90d1352962e427d099da6dac50c1))

* chore: update readme with correct function call ([`88fc1a7`](https://github.com/supabase-community/functions-py/commit/88fc1a797ef7d848bd2e870ddadcf8d51d405989))

* chore(release): bump version to v0.2.4 ([`e958722`](https://github.com/supabase-community/functions-py/commit/e95872200a7470da0e92bd95431eea1e20c66df3))

* chore: bump autoflake version ([`fc3a7bb`](https://github.com/supabase-community/functions-py/commit/fc3a7bb5788feca7acbdf4662feee7cce87f2cda))

### Fix

* fix: correct return type from invoke ([`9a15026`](https://github.com/supabase-community/functions-py/commit/9a15026bbbc63cd4b6d960f8a48db40a06770381))

* fix: add single instance of client instantiation ([`4b8a134`](https://github.com/supabase-community/functions-py/commit/4b8a134ac675bdcc0387cb1d1d55068e1b6be253))

### Unknown

* Temporary CI change to allow publishing of package ([`2d66f21`](https://github.com/supabase-community/functions-py/commit/2d66f21c01efcfd3ba34ab458c11977009580118))

* Merge pull request #11 from supabase-community/silentworks/update-readme

chore: update readme with correct function call ([`1dfe72e`](https://github.com/supabase-community/functions-py/commit/1dfe72eb28c35b0452e8f65d6e9612f9d4e80eb3))

* Merge pull request #9 from supabase-community/silentworks/sync_functions

Add sync functions ([`e2db242`](https://github.com/supabase-community/functions-py/commit/e2db242994c66ce3beec399416512342a2266f85))

* update file formatting with black ([`b1c64f5`](https://github.com/supabase-community/functions-py/commit/b1c64f51a487e9782c45324d0903a5e18c7bd31e))

* Apply suggestions from code review

Co-authored-by: Anand &lt;40204976+anand2312@users.noreply.github.com&gt; ([`e2a59aa`](https://github.com/supabase-community/functions-py/commit/e2a59aaff604a8c0ff1e3d648a1d2ae3aff44ea7))

* Add github workflow ([`14c8db9`](https://github.com/supabase-community/functions-py/commit/14c8db932527056343e5e7af012db87af6242006))

* Update errors and function signature of invoke ([`575da96`](https://github.com/supabase-community/functions-py/commit/575da968238a494de0996226df0bf54a48bf4e2b))

* Apply suggestions from code review

Co-authored-by: Anand &lt;40204976+anand2312@users.noreply.github.com&gt; ([`b60615d`](https://github.com/supabase-community/functions-py/commit/b60615d2c70c5a2e32e87f850d5fe1d68e492f59))

* Update supafunc/errors.py

Co-authored-by: Anand &lt;40204976+anand2312@users.noreply.github.com&gt; ([`2971673`](https://github.com/supabase-community/functions-py/commit/2971673451c4775c3f5e400983972bebefff4dfe))

* Add sync functions
Add pytests
Throw errors instead of returning them ([`692022f`](https://github.com/supabase-community/functions-py/commit/692022fa4816de5ec3e4cd929352535af719bb87))


## v0.2.3 (2023-08-04)

### Chore

* chore: bump version ([`d5f32ba`](https://github.com/supabase-community/functions-py/commit/d5f32ba75368cc1ba337e1cda0e6d89d426160b1))

* chore: bump httpx to 0.24 ([`6152992`](https://github.com/supabase-community/functions-py/commit/615299278b1d810c1113546938b81eabf075987f))

* chore(deps): bump httpx from 0.23.0 to 0.24.1

Bumps [httpx](https://github.com/encode/httpx) from 0.23.0 to 0.24.1.
- [Release notes](https://github.com/encode/httpx/releases)
- [Changelog](https://github.com/encode/httpx/blob/master/CHANGELOG.md)
- [Commits](https://github.com/encode/httpx/compare/0.23.0...0.24.1)

---
updated-dependencies:
- dependency-name: httpx
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f5c5ca4`](https://github.com/supabase-community/functions-py/commit/f5c5ca44de7d130be5ba2da0671ae8a845ad4d0d))

### Fix

* fix: small typo in authorization

for consistent naming ([`3f0bba8`](https://github.com/supabase-community/functions-py/commit/3f0bba80100f86886f4e8132862fc1e96868e479))

### Unknown

* Merge pull request #4 from anand2312/annad/bump-httpx

chore: bump httpx to 0.24 ([`f9d1c3c`](https://github.com/supabase-community/functions-py/commit/f9d1c3c6f3611f322d336bbd86f080c0d65f6d28))

* Merge pull request #3 from supabase-community/dependabot/pip/main/httpx-0.24.1

chore(deps): bump httpx from 0.23.0 to 0.24.1 ([`67ada27`](https://github.com/supabase-community/functions-py/commit/67ada272a6ea645b9b51041e6dedd829d3410113))

* Create dependabot.yml ([`c7394d7`](https://github.com/supabase-community/functions-py/commit/c7394d7691b6ed35997f6222fe8f37748e132242))

* Merge pull request #2 from 0xflotus/patch-1

fix: small typo in authorization ([`7c60eda`](https://github.com/supabase-community/functions-py/commit/7c60eda605337784a63a99a1405a6cb2c5f407f1))


## v0.2.2 (2022-10-10)

### Chore

* chore: update version ([`a6584a7`](https://github.com/supabase-community/functions-py/commit/a6584a783ed9fea347f89c87f420ba4d56e0383a))

### Feature

* feat: version 0.1.4 ([`7ffeec5`](https://github.com/supabase-community/functions-py/commit/7ffeec5465ce86f7ee077dbf18c21f332f31b1a5))

### Fix

* fix: update dependencies ([`91bc97b`](https://github.com/supabase-community/functions-py/commit/91bc97b66ef609618bb953a6557a2eb904b35d00))

* fix: add default for optional headers ([`02c838c`](https://github.com/supabase-community/functions-py/commit/02c838c73b692ea16912192278dd8550570553a1))

* fix: pass down body ([`d3f9f61`](https://github.com/supabase-community/functions-py/commit/d3f9f6187b7bd7206f89eb3331fa6ea6f13dd58e))


## v0.1.4 (2022-03-31)

### Chore

* chore: update version ([`883661f`](https://github.com/supabase-community/functions-py/commit/883661f3c50d8d5fabcbf9639daaf7e6b8fa2499))

* chore: update version ([`61f78b4`](https://github.com/supabase-community/functions-py/commit/61f78b4986917a234e631a233d72f65b28b414a4))

* chore: cleanup and add LICENSE ([`c9d035e`](https://github.com/supabase-community/functions-py/commit/c9d035eb4005ef9b595206395513abaca8325953))

* chore: rename and update README ([`0e26f92`](https://github.com/supabase-community/functions-py/commit/0e26f92f27079d6ab63da6860f6a26d229be2374))

### Unknown

* initial commit ([`5c93da6`](https://github.com/supabase-community/functions-py/commit/5c93da6948288c3312c0065e22ab968d25b9801b))
