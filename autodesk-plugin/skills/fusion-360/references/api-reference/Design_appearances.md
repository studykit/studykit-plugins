# Design.appearances Property

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Returns the appearances contained in this document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a Design object. |

"design\_var" is a variable referencing a Design object. ```` ``` #include <Fusion/Fusion/Design.h>  // Get the value of the property. Ptr<Appearances> propertyValue = design_var->appearances(); ``` ```` |

## Property Value

This is a read only property whose value is an [Appearances](Appearances.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Material API Sample](MaterialSample_Sample.htm) | Demonstrates using materials and appearance using the API.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. The sample also used an external appearance library which you can get [here](../ExtraFiles/APISampleMaterialLibrary2.adsklib). Copy that to any location on your computer and edit the path in the script. When running the script, have a design open that contains a body in the root component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |