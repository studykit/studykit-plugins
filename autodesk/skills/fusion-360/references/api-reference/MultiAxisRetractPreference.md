# MultiAxisRetractPreference Enumerator

## Description

Enumeration of the multi-axis retract preferences that can be used in MultiAxisRetractAndReconfigureSettings.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| MultiAxisRetractPreference\_RetractAtApex | 0 | Always retract when repositioning rotary axes. |
| MultiAxisRetractPreference\_StayAtApex | 1 | Allows the tool to stay down without retracting when the rotary axes are repositioned. The tool must be perpendicular to the rotary axis rotational vector (so that only one rotary axis will move) and TCP must be enabled for this axis. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |