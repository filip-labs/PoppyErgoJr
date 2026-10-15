# Contributing

Open an issue describing the problem or proposal before making a large change. Small documentation fixes are welcome directly as pull requests.

1. Fork the repository and create a branch.
2. Keep changes focused and explain their effect on the sorting workflow.
3. Follow [offline development](docs/development.md): run unit tests, syntax validation, Ruff lint and format checks. Test launcher help without hardware.
4. For motion or vision changes, record the exact environment and calibration used. Distinguish offline checks from supervised hardware testing.
5. Include results and remaining limitations in your pull request.

Never run robot motion in CI. Avoid publishing credentials, local IP details, OS images, or unlicensed third-party material. Be respectful and give constructive feedback. Licensing is pending; discuss substantial code contributions with the maintainer before submission.
