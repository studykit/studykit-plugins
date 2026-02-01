# WorkingModel.allParameters Property

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

Returns a read only list of all parameters in the design. This includes the user parameters and model parameters from all components in this design. The parameters from Externally Referenced components are NOT included because they are in actuality, separate designs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a WorkingModel object. |

"workingModel\_var" is a variable referencing a WorkingModel object. ```` ``` #include <Fusion/Fusion/WorkingModel.h>  // Get the value of the property. Ptr<ParameterList> propertyValue = workingModel_var->allParameters(); ``` ```` |

## Property Value

This is a read only property whose value is a [ParameterList](ParameterList.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |