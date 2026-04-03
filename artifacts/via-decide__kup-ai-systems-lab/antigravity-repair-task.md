Repair mode for repository via-decide/kup-ai-systems-lab.

TARGET
Validate and repair only the files touched by the previous implementation.

TASK
Build the 'TensorRT Optimizer' in src/optimization/trt-quantizer.py. Develop a script that automatically converts PyTorch/ONNX models to TensorRT engines with INT8 quantization, specifically tuned for the Jetson Orin NX architecture.

RULES
1. Audit touched files first and identify regressions.
2. Preserve architecture and naming conventions.
3. Make minimal repairs only; do not expand scope.
4. Re-run checks and provide concise root-cause notes.
5. Return complete contents for changed files only.

SOP: REPAIR PROTOCOL (MANDATORY)
1. Strict Fix Only: Do not use repair mode to expand scope or add features.
2. Regression Check: Audit why previous attempt failed before proposing a fix.
3. Minimal Footprint: Only return contents for the actual repaired files.

REPO CONTEXT
- README snippet:
# kup-ai-systems-lab
- AGENTS snippet:
not found
- package.json snippet:
not found