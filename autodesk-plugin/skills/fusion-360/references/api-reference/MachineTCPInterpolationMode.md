# MachineTCPInterpolationMode Enumerator

## Description

Interpolation modes available for TCP motions.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| MachineTCPInterpolationMode\_IndependentAxes | 1 | Moves the axes together, completing the motion simultaneously, although the tool's tip may deviate from the direct line between the start and finish points. |
| MachineTCPInterpolationMode\_SynchronizedAxes | 0 | Moves the axes independently at maximum speed, potentially resulting in different completion times for each axis |
| MachineTCPInterpolationMode\_ToolTip | 2 | Adjusts the linear axes to keep the tool's tip positioned along the direct line between the start and finish points. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |