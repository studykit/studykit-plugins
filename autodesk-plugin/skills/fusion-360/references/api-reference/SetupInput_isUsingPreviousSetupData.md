# SetupInput.isUsingPreviousSetupData Property

Parent Object: [SetupInput](SetupInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupInput.h>

## Description

Get and set if data from the previous setup should be used when creating another setup. The data applied from the previous setup is machine information and the stock from the preceeding setup. By default this value is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupInput\_var" is a variable referencing a SetupInput object. |

"setupInput\_var" is a variable referencing a SetupInput object. ```` ``` #include <Cam/CAM/SetupInput.h>  // Get the value of the property. boolean propertyValue = setupInput_var->isUsingPreviousSetupData();  // Set the value of the property, where value_var is a boolean. bool returnValue = setupInput_var->isUsingPreviousSetupData(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |