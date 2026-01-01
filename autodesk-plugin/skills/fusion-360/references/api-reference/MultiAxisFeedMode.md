# MultiAxisFeedMode Enumerator

## Description

Enumeration of the multi-axis feed modes that can be used in MultiAxisFeedrateSettings and its specializations.
Defined in namespace "adsk::cam" and the header file is <Cam\CamTypeDefs.h>

## Methods

|  |  |  |
| --- | --- | --- |
| Name | Value | Description |
| MultiAxisFeedMode\_DegreesPerMinute | 1 | Sets the feedrate based on the diameter of the cutting operation and calculates the degrees of the move. Used for most rotary axes. |
| MultiAxisFeedMode\_InverseTime | 0 | Sets the time for completing a move as an inverse of the feedrate. The smaller the value, the faster the move. |
| MultiAxisFeedMode\_ProgrammerdFeedrate | 2 | Applies the programmed feedrates without adjustments. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |