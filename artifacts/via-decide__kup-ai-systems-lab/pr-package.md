Branch: simba/build-the-deepstream-vision-core-in-srcvisiondee
Title: Build the 'DeepStream Vision Core' in src/vision/deepstream-pipeline....

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Build the 'DeepStream Vision Core' in src/vision/deepstream-pipeline.c. Integrate NVIDIA DeepStream SDK to process live camera feeds from the highway sensors. The pipeline must perform real-time tire segmentation and thermal anomaly detection.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.