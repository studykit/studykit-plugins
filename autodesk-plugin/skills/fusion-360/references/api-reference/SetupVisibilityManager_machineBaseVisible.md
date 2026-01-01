# SetupVisibilityManager.machineBaseVisible Property

Parent Object: [SetupVisibilityManager](SetupVisibilityManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Visibility/SetupVisibilityManager.h>

## Description

Controls the visibility of the setup's machine base where it exists. This is always disabled for additive setups.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupVisibilityManager\_var" is a variable referencing a SetupVisibilityManager object. |

"setupVisibilityManager\_var" is a variable referencing a SetupVisibilityManager object. ```` ``` #include <Cam/Visibility/SetupVisibilityManager.h>  // Get the value of the property. boolean propertyValue = setupVisibilityManager_var->machineBaseVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = setupVisibilityManager_var->machineBaseVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |