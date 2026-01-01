# SetupInput.parameters Property

Parent Object: [SetupInput](SetupInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupInput.h>

## Description

Get all parameters for the setup to be created. Parameters are initialized by user defaults. Configure operation parameters before creation for a better performance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupInput\_var" is a variable referencing a SetupInput object. |

"setupInput\_var" is a variable referencing a SetupInput object. ```` ``` #include <Cam/CAM/SetupInput.h>  // Get the value of the property. Ptr<CAMParameters> propertyValue = setupInput_var->parameters(); ``` ```` |

## Property Value

This is a read only property whose value is a [CAMParameters](CAMParameters.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |