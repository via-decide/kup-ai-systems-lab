Branch: simba/build-the-tensorrt-optimizer-in-srcoptimizationt
Title: Build the 'TensorRT Optimizer' in src/optimization/trt-quantizer.py. ...

## Summary
- Repo orchestration task for via-decide/kup-ai-systems-lab
- Goal: Build the 'TensorRT Optimizer' in src/optimization/trt-quantizer.py. Develop a script that automatically converts PyTorch/ONNX models to TensorRT engines with INT8 quantization, specifically tuned for the Jetson Orin NX architecture.

## Testing Checklist
- [ ] Run unit/integration tests
- [ ] Validate command flow
- [ ] Validate generated artifact files

## Risks
- Prompt quality depends on repository metadata completeness.
- GitHub API limits/token scope can block deep inspection.

## Rollback
- Revert branch and remove generated artifact files if workflow output is invalid.