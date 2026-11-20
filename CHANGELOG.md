# Changelog

## [0.4.0](https://github.com/mikejhill/codapact-ynab/compare/v0.3.0...v0.4.0) (2026-11-20)


### Features

* generate the README with Codapact 0.11.0 ([#9](https://github.com/mikejhill/codapact-ynab/issues/9)) ([bff4a42](https://github.com/mikejhill/codapact-ynab/commit/bff4a428ebeaa161d25f17e8d7def2fc58c97b7c))

## [0.3.0](https://github.com/mikejhill/codapact-ynab/compare/v0.2.0...v0.3.0) (2026-11-15)


### ⚠ BREAKING CHANGES

* the `ynab` command is now `codapact-ynab`.

### Features

* rename the command to codapact-ynab ([#7](https://github.com/mikejhill/codapact-ynab/issues/7)) ([b9cfb58](https://github.com/mikejhill/codapact-ynab/commit/b9cfb5830f5fe72c30239936fd2424fe11378338))

## [0.2.0](https://github.com/mikejhill/codapact-ynab/compare/v0.1.0...v0.2.0) (2026-11-14)


### ⚠ BREAKING CHANGES

* the package, import, and command are now codapact-ynab, codapact_ynab, and ynab.

### Features

* add protected live CI and UTF-8 CLI output ([#1](https://github.com/mikejhill/codapact-ynab/issues/1)) ([4c88810](https://github.com/mikejhill/codapact-ynab/commit/4c8881037ce5c219a07e0f1b9c33b9128aa06f73))
* replace ynab-api-cli with the Codapact-generated YNAB coda ([#5](https://github.com/mikejhill/codapact-ynab/issues/5)) ([142f982](https://github.com/mikejhill/codapact-ynab/commit/142f982116f6b17c457bb32e2acf27c190954677))

## 0.1.0

- Provide a standalone YNAB REST API CLI with typed generated endpoints and request validation.
- Include XDG connection configuration, diagnostics, discovery, mutation previews, and explicit execution guards.
- Bundle the supplementary `ynab-api-cli` Codex skill and isolated live-test runner.
- Verify reviewed operations, schema features, deterministic generation, and clean installation.
