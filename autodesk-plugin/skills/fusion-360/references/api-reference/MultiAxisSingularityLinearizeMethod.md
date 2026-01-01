# MultiAxisSingularityLinearizeMethod Enumerator

## Description

The linearization method the MultiAxisSingularitySettings should use. Different values will be used in different MultiAxisSingularitySettings specializations.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| MultiAxisSingularityLinearize\_Linear | 0 | Moves the tool end point along the straight line by adding points to the toolpath. It keeps the tool within the specified Linearization Tolerance. |
| MultiAxisSingularityLinearize\_Rotary | 1 | Applies a linear shape to the moves around the singularity by adding points to the toolpath. It keeps the tool within the specified Linearization Tolerance. The rotary linearization optimizes the tool for revolved movement as if the tool were moving around a cylinder or other object created by revolution. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |