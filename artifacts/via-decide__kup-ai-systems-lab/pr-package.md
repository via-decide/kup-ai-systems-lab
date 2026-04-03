Branch: simba/build-the-vision-translator-in-srcvisionmetadata
Title: Build the 'Vision Translator' in src/vision/metadata-bridge.js. Extra...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Build the 'Vision Translator' in src/vision/metadata-bridge.js. Extract the JSON metadata from the DeepStream inference (e.g., bounding box confidence, thermal heat-map delta) and inject it as a "Vision Context" into the Vora LLM prompt.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.