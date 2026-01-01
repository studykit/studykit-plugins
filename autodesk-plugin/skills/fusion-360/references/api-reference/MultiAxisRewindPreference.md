# MultiAxisRewindPreference Enumerator

## Description

Enumeration of the multi-axis rewind preferences that can be used in MultiAxisRetractAndReconfigureSettings.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| MultiAxisRewindPreference\_RewindAtLinear | 0 | It can retract at any point, including cutting moves. |
| MultiAxisRewindPreference\_RewindAtRapid | 1 | Allows the retract and rewind to occur at a rapid (non-cutting) move instead of at the limits of the rotary axis when possible. It may not be possible in all cases to retract and rewind at a rapid move, in this case the rewind occurs at a cutting move. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |