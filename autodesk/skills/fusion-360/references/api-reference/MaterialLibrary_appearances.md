# MaterialLibrary.appearances Property

Parent Object: [MaterialLibrary](MaterialLibrary.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/MaterialLibrary.h>

## Description

Returns the appearances defined within this library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialLibrary\_var" is a variable referencing a MaterialLibrary object. |

"materialLibrary\_var" is a variable referencing a MaterialLibrary object. ```` ``` #include <Core/Materials/MaterialLibrary.h>  // Get the value of the property. Ptr<Appearances> propertyValue = materialLibrary_var->appearances(); ``` ```` |

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