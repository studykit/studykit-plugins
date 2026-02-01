# GeneralPreferences.isHangDetectionEnabled Property

Parent Object: [GeneralPreferences](GeneralPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GeneralPreferences.h>

## Description

Gets and sets whether hang detection is enabled. This is a Windows only setting. If True, Fusion will detect when a task processes for longer than a specific time. A dialog is displayed if a hang is detected, allowing the user to continue processing or stop Fusion and send an error report.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. |

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. ```` ``` #include <Core/Application/GeneralPreferences.h>  // Get the value of the property. boolean propertyValue = generalPreferences_var->isHangDetectionEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = generalPreferences_var->isHangDetectionEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |