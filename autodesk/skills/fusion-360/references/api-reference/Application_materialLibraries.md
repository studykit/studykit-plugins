# Application.materialLibraries Property

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Returns the collection of material libraries currently available.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an Application object. |

"application\_var" is a variable referencing an Application object. ```` ``` #include <Core/Application/Application.h>  // Get the value of the property. Ptr<MaterialLibraries> propertyValue = application_var->materialLibraries(); ``` ```` |

## Property Value

This is a read only property whose value is a [MaterialLibraries](MaterialLibraries.htm).

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