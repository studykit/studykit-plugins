# WorkingModel.isContactAnalysisEnabled Property

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

Gets and sets whether contact analysis is enabled for all components. This is the equivalent of the "Disable Contact / Enable Contact" command. If this if True then any contact analysis defined (either all or contact sets) is enabled. if False, then no contact analysis is performed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a WorkingModel object. |

"workingModel\_var" is a variable referencing a WorkingModel object. ```` ``` #include <Fusion/Fusion/WorkingModel.h>  // Get the value of the property. boolean propertyValue = workingModel_var->isContactAnalysisEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = workingModel_var->isContactAnalysisEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |