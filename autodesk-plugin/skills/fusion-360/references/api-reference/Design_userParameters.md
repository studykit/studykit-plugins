# Design.userParameters Property

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Returns the collection of User Parameters in a design

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a Design object. |

"design\_var" is a variable referencing a Design object. ```` ``` #include <Fusion/Fusion/Design.h>  // Get the value of the property. Ptr<UserParameters> propertyValue = design_var->userParameters(); ``` ```` |

## Property Value

This is a read only property whose value is a [UserParameters](UserParameters.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Set parameters from a csv file and export to STEP](SetParametersFromACsvFileAndExportToSTEP_Sample.htm) | Reads data from a .csv file and sets user parameters in the model and then exports the model to STEP. When setting parameters be aware that this sample is setting user parameters. It's also possible to set model parameters but that's not demonstrated here. Also when accessing parameters, it is case sensitive so the names you use in your program much exactly match the names in the model. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |