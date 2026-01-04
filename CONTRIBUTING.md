# Contributing to FarmYield Predictor

Thank you for your interest in improving FarmYield Predictor! This document provides guidelines for contributing.

## How to Contribute

### Report Bugs
1. Check existing issues first
2. Create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable

### Suggest Enhancements
1. Use GitHub Issues
2. Describe the feature and why it's useful
3. Include examples if possible

### Code Contributions
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and test thoroughly
4. Commit with clear messages: `git commit -m "Add feature: description"`
5. Push to your fork: `git push origin feature/your-feature`
6. Create a Pull Request

## Code Standards

### Python
- Follow PEP 8 style guide
- Use meaningful variable names
- Add comments for complex logic
- Test with `python -m pytest`

### C++
- Use clear, readable code
- Add input validation
- Include error handling

## Testing

Before submitting a PR:
1. Test with sample data
2. Check for edge cases
3. Verify output formatting

## Documentation

- Update README.md for major changes
- Add docstrings to new functions
- Update USAGE.md if user workflow changes

## Development Setup

```bash
git clone https://github.com/itsowanga/FarmYield-Predictor.git
cd FarmYield-Predictor
pip install -r requirements.txt
python src/train.py
python src/predict.py
```

## Commit Message Format

```
[type]: Brief description (50 chars max)

Longer explanation if needed (72 chars per line)

Fixes #123
```

Types: feat, fix, docs, style, refactor, test, chore

## Questions?

Open a GitHub Discussion or contact the maintainer.

---

**Together we build better farming tools! 🌾**
