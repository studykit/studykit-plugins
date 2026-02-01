# MachineAxisRange.create Method

Parent Object: [MachineAxisRange](MachineAxisRange.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineAxisRange.h>

## Description

Creates a new range object with limited extents. Requires min to be less than or equal to max. Types of the fields depend on where this range is being used. Centimeters are used for distances and radians for angles.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachineAxisRange](MachineAxisRange.htm) | A new range object. Returns null if validation fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| min | double | New minimum value for range. |
| max | double | New maximum value for range. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |